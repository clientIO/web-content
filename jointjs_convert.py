"""
JointJS — HTML to Markdown & Plaintext converter
=================================================
Usage:
  python3 jointjs_convert.py --url https://www.jointjs.com/blog/your-post
  python3 jointjs_convert.py --file path/to/article.html
  python3 jointjs_convert.py --sitemap https://www.jointjs.com/sitemap.xml

Output:
  ./[slug].md
  ./[slug].txt

Requirements:
  pip3 install requests beautifulsoup4 markdownify lxml
"""

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
except ImportError:
    print("Missing dependencies. Run: pip3 install requests beautifulsoup4 markdownify lxml")
    sys.exit(1)

OUTPUT_DIR = Path(".")
GITHUB_DEMOS_RAW = "https://raw.githubusercontent.com/clientIO/joint-demos/main"

# ── Helpers ──────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Turn a URL path or title into a clean filename slug."""
    text = text.strip("/").split("/")[-1]
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_]+", "-", text)
    return text or "index"


def fetch_html(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; JointJS-ContentBot/1.0)"}
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    return r.text


def clean_and_extract(html: str) -> BeautifulSoup:
    """Remove navigation, scripts, styles and return the main content node."""
    soup = BeautifulSoup(html, "html.parser")

    noise_selectors = [
        "script", "style", "noscript", "iframe",
        "nav", "header", "footer",
        ".w-nav", ".navbar", ".footer-section", ".footer",
        "[class*='cookie']", "[class*='banner']", "[class*='popup']",
        "[class*='newsletter']", "[class*='cta']", "[class*='sidebar']",
        ".breadcrumb", ".social-share", ".related-posts",
    ]
    for selector in noise_selectors:
        for tag in soup.select(selector):
            tag.decompose()

    candidates = [
        "article",
        ".blog-post-content",
        ".post-content",
        ".w-richtext",
        "[class*='blog_content']",
        "[class*='post_body']",
        "main",
    ]
    for selector in candidates:
        node = soup.select_one(selector)
        if node:
            return node

    return soup.find("body") or soup


def to_markdown(node) -> str:
    raw = md(
        str(node),
        heading_style="ATX",
        bullets="-",
        strip=["img", "button", "form"],
        convert_links=False,
    )
    cleaned = re.sub(r"\n{3,}", "\n\n", raw)
    return cleaned.strip()


def to_plaintext(markdown: str) -> str:
    """Strip markdown syntax from markdown → pure plaintext."""
    text = markdown
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`{1,3}(.+?)`{1,3}", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"^[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def add_frontmatter(markdown: str, slug: str, source_url: str = "") -> str:
    from datetime import date
    frontmatter = f"""---
source: {source_url or slug}
generated: {date.today().isoformat()}
format: markdown
---

"""
    return frontmatter + markdown


# ── Core processing ──────────────────────────────────────────────────────────

def process(html: str, slug: str, source_url: str = ""):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    node = clean_and_extract(html)
    markdown = to_markdown(node)
    markdown = add_frontmatter(markdown, slug, source_url)
    plaintext = to_plaintext(markdown)

    md_path = OUTPUT_DIR / f"{slug}.md"
    txt_path = OUTPUT_DIR / f"{slug}.txt"

    md_path.write_text(markdown, encoding="utf-8")
    txt_path.write_text(plaintext, encoding="utf-8")

    print(f"✓  {slug}")
    print(f"   → {md_path}  ({len(markdown):,} chars)")
    print(f"   → {txt_path}  ({len(plaintext):,} chars)")
    return md_path, txt_path


def process_demo(url: str):
    """For /demos/ pages, fetch README from GitHub instead of the web page."""
    slug = slugify(url)
    readme_url = f"{GITHUB_DEMOS_RAW}/{slug}/README.md"

    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; JointJS-ContentBot/1.0)"}
        r = requests.get(readme_url, headers=headers, timeout=15)
        r.raise_for_status()
        readme_markdown = r.text
    except Exception:
        print(f"  (no README found, falling back to web page)")
        return process_url(url)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    from datetime import date
    frontmatter = f"""---
source: {url}
github: {readme_url}
generated: {date.today().isoformat()}
format: markdown
---

"""
    markdown = frontmatter + readme_markdown
    plaintext = to_plaintext(markdown)

    md_path = OUTPUT_DIR / f"{slug}.md"
    txt_path = OUTPUT_DIR / f"{slug}.txt"

    md_path.write_text(markdown, encoding="utf-8")
    txt_path.write_text(plaintext, encoding="utf-8")

    print(f"✓  {slug}  (GitHub README)")
    print(f"   → {md_path}  ({len(markdown):,} chars)")
    print(f"   → {txt_path}  ({len(plaintext):,} chars)")
    return md_path, txt_path


def process_url(url: str):
    slug = slugify(url)
    html = fetch_html(url)
    return process(html, slug, source_url=url)


def process_file(path: str):
    p = Path(path)
    slug = slugify(p.stem)
    html = p.read_text(encoding="utf-8")
    return process(html, slug)


def process_sitemap(sitemap_url: str, limit: int = None):
    """Fetch all page URLs from a sitemap and convert each one."""
    print(f"Fetching sitemap: {sitemap_url}")
    html = fetch_html(sitemap_url)
    soup = BeautifulSoup(html, "xml")
    urls = [loc.text.strip() for loc in soup.find_all("loc")]

    excluded = [
        "/cdn-cgi/", "/.well-known/", "/wp-", "/feed",
        "pricing-copy-29-5-2022", "/dev-backup/",
        "/demo-features/", "/featured-tags/"
    ]
    relevant = [
        u for u in urls
        if not any(segment in u for segment in excluded)
    ]

    if limit:
        relevant = relevant[:limit]

    print(f"Found {len(relevant)} relevant URLs\n")

    # Always process homepage first
    base_url = sitemap_url.replace("/sitemap.xml", "")
    try:
        html = fetch_html(base_url)
        process(html, "index", source_url=base_url)
    except Exception as e:
        print(f"✗  homepage  ({e})")

    for url in relevant:
        try:
            if "/demos/" in url:
                process_demo(url)
            else:
                process_url(url)
        except Exception as e:
            print(f"✗  {url}  ({e})")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="JointJS HTML → MD/TXT converter")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="Single page URL to convert")
    group.add_argument("--file", help="Local HTML file to convert")
    group.add_argument("--sitemap", help="Sitemap URL — converts all pages")
    parser.add_argument("--limit", type=int, help="Max pages to process from sitemap")

    args = parser.parse_args()

    if args.url:
        process_url(args.url)
    elif args.file:
        process_file(args.file)
    elif args.sitemap:
        process_sitemap(args.sitemap, limit=args.limit)


if __name__ == "__main__":
    main()
