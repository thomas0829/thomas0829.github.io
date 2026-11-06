"""Regression checks for citation freshness and preservation during outages."""

from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, quote_plus, urlsplit

import sync_scholar as sync


PROFILE = f"""
<div id="gsc_prf_in">Ying-Chun Lee</div>
<table id="gsc_rsb_st">
  <tr><td class="gsc_rsb_sc1">Citations</td><td class="gsc_rsb_std">171</td></tr>
  <tr><td class="gsc_rsb_sc1">h-index</td><td class="gsc_rsb_std">4</td></tr>
  <tr><td class="gsc_rsb_sc1">i10-index</td><td class="gsc_rsb_std">4</td></tr>
</table>
<button id="gsc_bpf_more" disabled></button>
<tr class="gsc_a_tr">
  <td><a class="gsc_a_at" href="/citations?user={sync.USER}&amp;citation_for_view={sync.USER}:paper-id">Paper</a></td>
  <td><a class="gsc_a_ac">91</a><span class="gsc_a_m">*</span></td>
</tr>
"""


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        root = Path(self.temporary.name)
        self.output, self.cache = root / "site.json", root / "cache.json"
        self.summary = root / "summary.md"
        self.fixture = root / "profile.html"
        for target, value in (("OUTPUT", self.output), ("CACHE", self.cache)):
            patcher = patch.object(sync, target, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        patcher = patch.dict("os.environ", {"GITHUB_STEP_SUMMARY": str(self.summary),
                                            "SERPAPI_API_KEY": ""})
        patcher.start()
        self.addCleanup(patcher.stop)

    def snapshot(self, path, date, citations):
        data = sync.parse_profile(PROFILE)
        data["updated_at"], data["metrics"]["citations"] = date, citations
        sync.write_snapshot(path, data)
        return data

    def run_sync(self, *arguments, html=PROFILE, error=None):
        response = io.BytesIO(html.encode("utf-8"))
        stdout, stderr = io.StringIO(), io.StringIO()
        with (patch("sys.argv", ["sync_scholar.py", *arguments]),
              patch.object(sync.urllib.request, "urlopen", return_value=response,
                           side_effect=error) as fetch,
              redirect_stdout(stdout), redirect_stderr(stderr)):
            status = sync.main()
        self.logs = stdout.getvalue() + stderr.getvalue()
        return status, fetch

    def test_success_publishes_fresh_metrics_and_paper_estimate(self):
        status, fetch = self.run_sync("--require-fresh")
        self.assertEqual(status, 0)
        fetch.assert_called_once_with(sync.PROFILE_URL + "&pagesize=100", timeout=30)
        data = json.loads(self.output.read_text(encoding="utf-8"))
        self.assertEqual(data["metrics"], {"citations": 171, "h_index": 4, "i10_index": 4})
        self.assertEqual(data["papers"]["paper-id"]["citations"], 91)
        self.assertTrue(data["papers"]["paper-id"]["estimated"])
        self.assertEqual(data, json.loads(self.cache.read_text(encoding="utf-8")))
        self.assertIn("Fresh data fetched", self.summary.read_text(encoding="utf-8"))

    def test_403_returns_failure_and_retains_newest_saved_data(self):
        self.snapshot(self.output, "2026-11-04T00:00:00+00:00", 160)
        newest = self.snapshot(self.cache, "2026-11-05T00:00:00+00:00", 165)
        cache_bytes = self.cache.read_bytes()
        error = HTTPError(sync.PROFILE_URL, 403, "Forbidden", None, None)
        status, _ = self.run_sync("--require-fresh", error=error)
        self.assertEqual(status, 1)
        self.assertEqual(json.loads(self.output.read_text(encoding="utf-8")), newest)
        self.assertEqual(self.cache.read_bytes(), cache_bytes)
        summary = self.summary.read_text(encoding="utf-8")
        self.assertIn("Fetch failed", summary)
        self.assertIn("403", summary)
        self.assertIn(newest["updated_at"], summary)

    def test_repository_snapshot_wins_over_older_cache(self):
        newest = self.snapshot(self.output, "2026-11-06T00:00:00+00:00", 171)
        self.snapshot(self.cache, "2026-11-05T00:00:00+00:00", 160)
        status, _ = self.run_sync("--require-fresh", error=TimeoutError("timed out"))
        self.assertEqual(status, 1)
        self.assertEqual(json.loads(self.output.read_text(encoding="utf-8")), newest)

    def test_non_strict_local_use_can_retain_saved_data_without_failure(self):
        self.snapshot(self.output, "2026-11-05T00:00:00+00:00", 160)
        status, _ = self.run_sync(error=TimeoutError("timed out"))
        self.assertEqual(status, 0)
        self.assertFalse(self.cache.exists())

    def test_failure_without_any_valid_snapshot_does_not_create_data(self):
        self.cache.write_text("{}", encoding="utf-8")
        status, _ = self.run_sync(error=TimeoutError("timed out"))
        self.assertEqual(status, 1)
        self.assertFalse(self.output.exists())
        self.assertEqual(self.cache.read_text(encoding="utf-8"), "{}")
        self.assertIn("No valid saved data", self.summary.read_text(encoding="utf-8"))

    def test_captcha_or_incomplete_profile_cannot_replace_saved_metrics(self):
        for html in ("<html>CAPTCHA</html>", PROFILE.replace("Citations", "Other"),
                     PROFILE.replace(" disabled", ""), PROFILE.replace(sync.USER, "wrong-user")):
            with self.subTest(html=html[:60]):
                saved = self.snapshot(self.output, "2026-11-05T00:00:00+00:00", 160)
                status, _ = self.run_sync("--require-fresh", html=html)
                self.assertEqual(status, 1)
                self.assertEqual(json.loads(self.output.read_text(encoding="utf-8")), saved)
                self.assertFalse(self.cache.exists())

    def test_offline_html_does_not_make_a_network_request(self):
        self.fixture.write_text(PROFILE, encoding="utf-8")
        status, fetch = self.run_sync("--require-fresh", "--html", str(self.fixture))
        self.assertEqual(status, 0)
        fetch.assert_not_called()

    def test_serpapi_fetch_uses_author_api_and_preserves_estimate(self):
        with patch.dict("os.environ", {"SERPAPI_API_KEY": "test-only-key"}):
            status, fetch = self.run_sync("--source", "serpapi", "--require-fresh")
        self.assertEqual(status, 0)
        fetch.assert_called_once()
        url = urlsplit(fetch.call_args.args[0])
        self.assertEqual((url.scheme, url.netloc, url.path), ("https", "serpapi.com", "/search"))
        self.assertEqual(parse_qs(url.query), {
            "engine": ["google_scholar_author"], "author_id": [sync.USER],
            "hl": ["en"], "num": ["100"], "output": ["html"],
            "api_key": ["test-only-key"],
        })
        self.assertEqual(fetch.call_args.kwargs["timeout"], 90)
        data = json.loads(self.output.read_text(encoding="utf-8"))
        self.assertEqual(data["source"], "serpapi")
        self.assertTrue(data["papers"]["paper-id"]["estimated"])
        for path in (self.output, self.cache, self.summary):
            self.assertNotIn("test-only-key", path.read_text(encoding="utf-8"))
        self.assertNotIn("test-only-key", self.logs)

    def test_missing_api_key_fails_without_direct_access_or_changing_timestamp(self):
        saved = self.snapshot(self.output, "2026-11-05T00:00:00+00:00", 160)
        status, fetch = self.run_sync("--source", "serpapi", "--require-fresh")
        self.assertEqual(status, 1)
        fetch.assert_not_called()
        self.assertEqual(json.loads(self.output.read_text(encoding="utf-8")), saved)
        self.assertIn("SERPAPI_API_KEY is not configured", self.logs)

    def test_api_auth_or_quota_errors_fail_once_and_preserve_metrics(self):
        with patch.dict("os.environ", {"SERPAPI_API_KEY": "test-only-key"}):
            for code in (401, 429):
                with self.subTest(code=code):
                    saved = self.snapshot(self.output, "2026-11-05T00:00:00+00:00", 160)
                    error = HTTPError("https://serpapi.com/search", code, "API failure", None, None)
                    status, fetch = self.run_sync("--source", "serpapi", "--require-fresh", error=error)
                    self.assertEqual(status, 1)
                    fetch.assert_called_once()
                    self.assertEqual(json.loads(self.output.read_text(encoding="utf-8")), saved)
                    self.assertFalse(self.cache.exists())

    def test_api_json_error_cannot_replace_metrics_or_leak_response(self):
        saved = self.snapshot(self.output, "2026-11-05T00:00:00+00:00", 160)
        with patch.dict("os.environ", {"SERPAPI_API_KEY": "test-only-key"}):
            status, _ = self.run_sync("--source", "serpapi", "--require-fresh",
                                      html='{"error": "test-only-key"}')
        self.assertEqual(status, 1)
        self.assertEqual(json.loads(self.output.read_text(encoding="utf-8")), saved)
        self.assertNotIn("test-only-key", self.logs + self.summary.read_text(encoding="utf-8"))

    def test_api_key_is_redacted_from_exception_logs_and_summary(self):
        key = "test-only/key+with=punctuation"
        self.snapshot(self.output, "2026-11-05T00:00:00+00:00", 160)
        with patch.dict("os.environ", {"SERPAPI_API_KEY": key}):
            status, _ = self.run_sync("--source", "serpapi", "--require-fresh",
                                      error=RuntimeError(key + " " + quote_plus(key)))
        self.assertEqual(status, 1)
        text = self.logs + self.summary.read_text(encoding="utf-8")
        self.assertNotIn(key, text)
        self.assertNotIn(quote_plus(key), text)
        self.assertIn("[redacted]", text)


if __name__ == "__main__":
    unittest.main()
