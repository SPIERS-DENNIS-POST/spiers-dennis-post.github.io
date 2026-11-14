import argparse
import json
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urldefrag, urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attributes):
        if tag == "a":
            href = (dict(attributes).get("href") or "").strip()
            if href.startswith(("https://", "http://", "//")):
                self.links.append(href)
def page_path(root, file):
    path = "/" + file.relative_to(root).as_posix()
    return path[:-10] if path.endswith("index.html") else path
def collect_links(root, site_url):
    references = defaultdict(set)
    own_host = urlsplit(site_url).hostname
    pages = list(sorted(root.rglob("*.html")))
    for file in pages:
        parser = AnchorParser()
        parser.feed(file.read_text(encoding="utf-8", errors="replace"))
        for href in parser.links:
            url = urldefrag(urljoin(site_url, href)).url
            try:
                parts = urlsplit(url)
                external = parts.scheme in ("http", "https") and parts.hostname != own_host
            except ValueError:
                external = True
            if external:
                references[url].add(page_path(root, file))
    return references, len(pages)
def comparable_host(url):
    host = (urlsplit(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host
def surprising_redirect(original, final):
    a, b = urlsplit(original), urlsplit(final)
    return comparable_host(original) != comparable_host(final) or a.path.rstrip("/") != b.path.rstrip("/") or a.query != b.query or (a.scheme == "https" and b.scheme != "https")
def check_link(item):
    url, pages = item
    hops = []
    class RedirectRecorder(HTTPRedirectHandler):
        def redirect_request(self, request, response, status, message, headers, location):
            hops.append({"status": status, "url": location})
            return super().redirect_request(request, response, status, message, headers, location)
    status, final, error = None, url, None
    try:
        request = Request(url, headers={"User-Agent": "Spiers-Dennis-Post-Link-Checker/1.0", "Accept": "*/*"}, method="GET")
        with build_opener(RedirectRecorder()).open(request, timeout=15) as response:
            status, final = response.status, response.geturl()
    except HTTPError as failure:
        status, final = failure.code, failure.geturl()
        failure.close()
    except Exception as failure:
        error = f"{type(failure).__name__}: {failure}"
    if status is None:
        outcome = "Request failed"
    elif 200 <= status < 300:
        outcome = "OK"
    elif status in (401, 403, 407, 429, 451):
        outcome = "Access limited"
    elif status in (404, 410):
        outcome = "Not found"
    elif status >= 500:
        outcome = "Server error"
    else:
        outcome = "HTTP error"
    unexpected = bool(hops) and surprising_redirect(url, final)
    return {"url": url, "pages": sorted(pages), "status": status, "outcome": outcome, "final_url": final, "redirects": hops, "unexpected_redirect": unexpected, "error": error}
def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")
def row(record):
    flags = record["outcome"] + ("; redirect review" if record["unexpected_redirect"] else "")
    target = record["error"] or (record["final_url"] if record["redirects"] else "—")
    hops = " → ".join(str(hop["status"]) for hop in record["redirects"]) or "—"
    return "| " + " | ".join(map(cell, [flags, record["status"] or "—", hops, record["url"], target, ", ".join(record["pages"])])) + " |"
def report_markdown(records, page_count, timestamp):
    findings = [record for record in records if record["outcome"] != "OK" or record["unexpected_redirect"]]
    routine = [record for record in records if record["redirects"] and record["outcome"] == "OK" and not record["unexpected_redirect"]]
    counts = Counter(record["outcome"] for record in records)
    lines = ["# External-link verification", "", f"Checked: {timestamp}", f"Generated HTML pages scanned: {page_count}", f"Unique external HTTP(S) links checked: {len(records)}", f"References requiring review: {len(findings)}", f"Unexpected redirects: {sum(record['unexpected_redirect'] for record in records)}", "", "Automated errors are not evidence that a historical source has disappeared. Access restrictions, rate limits, bot blocking, and temporary server failures require human interpretation. No website references were changed. Normalization redirects are listed separately; redirects changing the host, path, or query are flagged for review.", "", "## Potentially broken or redirected references", "", "| Observation | HTTP | Redirect HTTP codes | Original URL | Final URL or error | Linked from |", "| --- | --- | --- | --- | --- | --- |"]
    lines.extend(map(row, findings))
    if not findings:
        lines.append("No findings requiring review.")
    lines.extend(["", "## Other redirects observed", "", "| Observation | HTTP | Redirect HTTP codes | Original URL | Final URL | Linked from |", "| --- | --- | --- | --- | --- | --- |"])
    lines.extend(map(row, routine))
    if not routine:
        lines.append("No other redirects observed.")
    lines.extend(["", "## Summary by response type", ""])
    lines.extend(f"- {key}: {value}" for key, value in sorted(counts.items()))
    lines.extend(["", "The accompanying JSON file contains every checked URL, its source pages, status, final URL, and redirect chain."])
    return "\n".join(lines) + "\n"
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("site_dir", type=Path)
    parser.add_argument("report_dir", type=Path)
    parser.add_argument("site_url")
    args = parser.parse_args()
    if not args.site_dir.is_dir():
        parser.error("The generated site directory does not exist")
    references, pages = collect_links(args.site_dir, args.site_url)
    if not pages or not references:
        parser.error("No generated HTML pages or external HTTP(S) links found")
    with ThreadPoolExecutor(max_workers=4) as pool:
        records = sorted(pool.map(check_link, references.items()), key=lambda record: record["url"])
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    args.report_dir.mkdir(parents=True, exist_ok=True)
    (args.report_dir / "report.md").write_text(report_markdown(records, pages, timestamp), encoding="utf-8")
    (args.report_dir / "report.json").write_text(json.dumps({"checked_at": timestamp, "pages_scanned": pages, "links": records}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Checked {len(records)} external URLs across {pages} pages; {sum(record['outcome'] != 'OK' or record['unexpected_redirect'] for record in records)} require review.")
if __name__ == "__main__":
    main()
