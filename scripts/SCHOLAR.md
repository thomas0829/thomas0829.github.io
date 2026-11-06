# Google Scholar citations

Both Publications pages render `_data/scholar.json`. Paper badges use Scholar's
stable publication IDs. Estimated counts keep their asterisks. Aggregate metrics
come from the profile's all-time metrics table, not a sum of individual papers.

## SerpApi setup

1. Get an API key from https://serpapi.com/manage-api-key.
2. In this repository's Settings > Secrets and variables > Actions, add a
   repository secret named `SERPAPI_API_KEY` containing that key.
3. Run **Deploy Jekyll site to Pages** from the Actions tab. Verify that the
   Scholar job summary reports a successful fetch with a new timestamp.

The scheduled workflow explicitly uses `--source serpapi --require-fresh`. It
makes one Google Scholar Author API request using `author_id=mTx-qU0AAAAJ`,
`hl=en`, `num=100`, and `output=html`. SerpApi's raw HTML response preserves the
estimated-citation flags that the existing parser reads. Data is still sourced
from Google Scholar; SerpApi supplies the server-side fetch.

API documentation: https://serpapi.com/google-scholar-author-api

The key is passed only through the sync step's environment. It is never written
to snapshots, artifacts, rendered pages, or logs. Exceptions redact the key and
its URL-encoded form. Raw API responses and request URLs are not logged or saved.

## Schedule and failure behavior

The Pages workflow attempts a refresh daily at 07:23 UTC and on pushes to master
or manual runs. There is one API lookup per run; regression tests mock all network
requests. SerpApi may serve a cached result for up to one hour. GitHub schedules
can be delayed or disabled after 60 days of inactivity on a public repository.

`--require-fresh` returns failure if the fetch or validation fails, after retaining
the newest valid snapshot from the repository or Actions cache. The Scholar job
and overall workflow are then marked failed, while the site can still deploy
content updates with the saved data. The job summary reports freshness, citation
count, timestamp, source, and any error. Only a successful fetch saves a new cache
entry. An artifact passes the selected snapshot to the site build. Cache eviction
falls back to the checked-in snapshot. The displayed timestamp always belongs to
the last successful fetch; failed requests never advance it.

For a local direct refresh, use `python scripts/sync_scholar.py`. For offline
verification, pass `--html path/to/saved-profile.html`. Run regression checks with
`python -m unittest discover -s scripts -p test_sync_scholar.py`.

Profiles with more than 100 papers retain existing data until pagination is
supported. New publication cards need their Scholar ID passed to the
`scholar-citation.html` include in both languages.
