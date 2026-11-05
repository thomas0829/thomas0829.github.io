"""Fetch one public Scholar profile; retain the latest valid snapshot on failure."""

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, help="Parse a saved public-profile response (offline verification)")
    args = parser.parse_args()
    previous = [data for path in (OUTPUT, CACHE) if (data := read_snapshot(path))]
    previous = max(previous, key=lambda data: data["updated_at"], default=None)
    try:
        if args.html:
            html = args.html.read_text(encoding="utf-8")
        else:
            with urllib.request.urlopen(PROFILE_URL + "&pagesize=100", timeout=30) as response:
                html = response.read().decode("utf-8")
        data = parse_profile(html)
    except Exception as error:
        if previous is None:
            print(f"Scholar sync failed with no saved data: {error}", file=sys.stderr)
            return 1
        data = previous
        print(f"::warning::Scholar sync unavailable; keeping data from {data['updated_at']}: {error}")
    else:
        write_snapshot(CACHE, data)
        print(f"Synced {len(data['papers'])} papers; {data['metrics']['citations']} citations")
    write_snapshot(OUTPUT, data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
