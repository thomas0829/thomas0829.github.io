# Google Scholar citations

Both Publications pages render `_data/scholar.json`. Paper badges use Scholar's
stable publication IDs, so capitalization and title changes do not affect matching.
Scholar's estimated counts keep their asterisk. Metrics are the profile's all-time
values, read directly from its metrics table (not a sum of individual papers).

`python scripts/sync_scholar.py` fetches the public profile once, validates it,
then atomically replaces the snapshot. No API key or third-party service is used.
For offline verification, pass `--html path/to/saved-profile.html`.

The Pages workflow refreshes and rebuilds daily at 07:23 UTC, and on a normal
push or manual run. GitHub schedules can be delayed and can be disabled after
60 days of inactivity on a public repository. A blocked or changed Scholar page
produces a workflow warning and retains the most recent valid snapshot from the
repository or Actions cache. Cache eviction falls back to the checked-in snapshot.
The displayed timestamp always belongs to the last successful fetch, so stale
data is visible. There are no retries, proxies, or CAPTCHA bypasses.

If the profile grows beyond 100 papers the sync preserves existing data and warns
until pagination support is added. New publication cards need their Scholar ID
passed to the `scholar-citation.html` include in both languages.

The schedule only becomes active after these local changes are published.
