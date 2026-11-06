"""Fetch one public Scholar profile; retain the latest valid snapshot on failure."""

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import urllib.parse
import urllib.request

USER = "mTx-qU0AAAAJ"
PROFILE_URL = f"https://scholar.google.com/citations?user={USER}&hl=en"
OUTPUT = Path("_data/scholar.json")
CACHE = Path(".cache/scholar.json")


class Node:
    def __init__(self, tag="", attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def find(self, *, tag=None, id=None, cls=None):
        result = []
        for child in self.children:
            if isinstance(child, Node):
                if ((tag is None or child.tag == tag)
                        and (id is None or child.attrs.get("id") == id)
                        and (cls is None or cls in child.attrs.get("class", "").split())):
                    result.append(child)
                result.extend(child.find(tag=tag, id=id, cls=cls))
        return result

    def text(self):
        return "".join(c.text() if isinstance(c, Node) else c for c in self.children).strip()


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, attrs))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def number(value):
    value = value.strip().replace(",", "")
    if not re.fullmatch(r"\d+", value):
        raise ValueError(f"Unexpected citation metric: {value!r}")
    return int(value)


def parse_profile(html):
    root = Document(html).root
    name = root.find(id="gsc_prf_in")[0].text()
    rows = root.find(id="gsc_rsb_st")[0].find(tag="tr")
    metrics = {}
    keys = {"Citations": "citations", "h-index": "h_index", "i10-index": "i10_index"}
    for row in rows:
        labels, values = row.find(cls="gsc_rsb_sc1"), row.find(cls="gsc_rsb_std")
        if labels and labels[0].text() in keys:
            metrics[keys[labels[0].text()]] = number(values[0].text())
    if set(metrics) != set(keys.values()):
        raise ValueError("Scholar did not return all three metrics")
    more = root.find(id="gsc_bpf_more")
    if more and "disabled" not in more[0].attrs:
        raise ValueError("Profile exceeds 100 papers; pagination must be added before syncing")
    papers = {}
    for row in root.find(cls="gsc_a_tr"):
        title, count = row.find(cls="gsc_a_at")[0], row.find(cls="gsc_a_ac")[0]
        href = title.attrs["href"]
        if f"user={USER}" not in href:
            raise ValueError("Unexpected Scholar profile ID")
        # Use the stable citation ID rather than fuzzy title matching.
        match = re.search(r"citation_for_view=" + re.escape(USER) + r":([^&]+)", href)
        if not match:
            raise ValueError("Missing Scholar publication ID")
        papers[match[1]] = {
            "title": title.text(),
            "citations": number(count.text()) if count.text() else 0,
            "estimated": bool(row.find(cls="gsc_a_m") and row.find(cls="gsc_a_m")[0].text()),
            "url": "https://scholar.google.com" + href,
        }
    if not papers or not name:
        raise ValueError("Scholar returned an empty profile")
    return {
        "user": USER, "name": name, "url": PROFILE_URL,
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "metrics": metrics, "papers": papers,
    }


def read_snapshot(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if (data["user"] == USER and data["papers"]
                and all(type(data["metrics"][key]) is int and data["metrics"][key] >= 0
                        for key in ("citations", "h_index", "i10_index"))):
            datetime.fromisoformat(data["updated_at"])
            return data
    except (OSError, ValueError, KeyError, TypeError):
        pass
    return None


def write_snapshot(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def fetch_profile(source):
    url, timeout = PROFILE_URL + "&pagesize=100", 30
    if source == "serpapi":
        key = os.environ.get("SERPAPI_API_KEY", "").strip()
        if not key:
            raise ValueError("SERPAPI_API_KEY is not configured; add it as a GitHub Actions repository secret")
        # Raw Scholar HTML preserves estimated-count asterisks and stable paper IDs.
        query = urllib.parse.urlencode({
            "engine": "google_scholar_author", "author_id": USER,
            "hl": "en", "num": 100, "output": "html", "api_key": key,
        })
        url, timeout = "https://serpapi.com/search?" + query, 90
    with urllib.request.urlopen(url, timeout=timeout) as response:
        html = response.read().decode("utf-8")
    if source == "serpapi" and html.lstrip().startswith("{"):
        raise ValueError("SerpApi returned an API error; check the API key, quota, and service status")
    return html


def safe_error(error):
    message = str(error)
    key = os.environ.get("SERPAPI_API_KEY", "").strip()
    if key:
        for secret in (key, urllib.parse.quote_plus(key)):
            message = message.replace(secret, "[redacted]")
    return message


def report_sync(data, error=None):
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary:
        return
    status = "Fresh data fetched" if error is None else (
        "Fetch failed; saved data retained" if data else "Fetch failed")
    lines = ["### Google Scholar synchronization", "", status + "."]
    if data:
        lines += [f"Citations: **{data['metrics']['citations']}**.",
                  f"Last successful fetch: `{data['updated_at']}`.",
                  f"Snapshot source: `{data.get('source', 'direct')}`."]
    else:
        lines += ["No valid saved data is available."]
    if error is not None:
        lines += [f"Error: {error}"]
    with Path(summary).open("a", encoding="utf-8") as stream:
        stream.write("\n".join(lines) + "\n\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, help="Parse a saved public-profile response (offline verification)")
    parser.add_argument("--source", choices=("direct", "serpapi"), default="direct",
                        help="Use direct Scholar access locally, or SerpApi for the scheduled workflow")
    parser.add_argument("--require-fresh", action="store_true",
                        help="Return a failure status when a fetch fails, while preserving saved data")
    args = parser.parse_args()
    previous = [data for path in (OUTPUT, CACHE) if (data := read_snapshot(path))]
    previous = max(previous, key=lambda data: data["updated_at"], default=None)
    failure = None
    try:
        if args.html:
            html = args.html.read_text(encoding="utf-8")
        else:
            html = fetch_profile(args.source)
        data = parse_profile(html)
        data["source"] = "saved_html" if args.html else args.source
    except Exception as error:
        failure = safe_error(error)
        if previous is None:
            print(f"Scholar sync failed with no saved data: {failure}", file=sys.stderr)
            report_sync(None, failure)
            return 1
        data = previous
        warning = f"Scholar sync unavailable; keeping data from {data['updated_at']}: {failure}"
        print("::warning::" + warning.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A"))
    else:
        write_snapshot(CACHE, data)
        print(f"Synced {len(data['papers'])} papers; {data['metrics']['citations']} citations")
    write_snapshot(OUTPUT, data)
    report_sync(data, failure)
    return 1 if failure is not None and args.require_fresh else 0


if __name__ == "__main__":
    sys.exit(main())
