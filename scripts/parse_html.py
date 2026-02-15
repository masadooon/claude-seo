#!/usr/bin/env python3
"""
HTMLを解析してSEO関連の要素を抽出する。

使い方:
    python parse_html.py page.html
    python parse_html.py --url https://example.com
"""

import argparse
import json
import re
import sys
from typing import Optional
from urllib.parse import urljoin, urlparse

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("エラー: beautifulsoup4 が必要です。次のコマンドでインストールしてください: pip install beautifulsoup4")
    sys.exit(1)


def parse_html(html: str, base_url: Optional[str] = None) -> dict:
    """
    HTMLを解析してSEO関連の要素を抽出する。

    Args:
        html: 解析対象のHTMLコンテンツ
        base_url: 相対リンクを解決するためのベースURL

    Returns:
        抽出されたSEOデータを含む辞書
    """
    soup = BeautifulSoup(html, "lxml" if "lxml" in sys.modules else "html.parser")

    result = {
        "title": None,
        "meta_description": None,
        "meta_robots": None,
        "canonical": None,
        "h1": [],
        "h2": [],
        "h3": [],
        "images": [],
        "links": {
            "internal": [],
            "external": [],
        },
        "schema": [],
        "open_graph": {},
        "twitter_card": {},
        "word_count": 0,
        "hreflang": [],
    }

    # タイトル
    title_tag = soup.find("title")
    if title_tag:
        result["title"] = title_tag.get_text(strip=True)

    # メタタグ
    for meta in soup.find_all("meta"):
        name = meta.get("name", "").lower()
        property_attr = meta.get("property", "").lower()
        content = meta.get("content", "")

        if name == "description":
            result["meta_description"] = content
        elif name == "robots":
            result["meta_robots"] = content

        # Open Graph
        if property_attr.startswith("og:"):
            result["open_graph"][property_attr] = content

        # Twitter Card
        if name.startswith("twitter:"):
            result["twitter_card"][name] = content

    # Canonical
    canonical = soup.find("link", rel="canonical")
    if canonical:
        result["canonical"] = canonical.get("href")

    # Hreflang
    for link in soup.find_all("link", rel="alternate"):
        hreflang = link.get("hreflang")
        if hreflang:
            result["hreflang"].append({
                "lang": hreflang,
                "href": link.get("href"),
            })

    # 見出し
    for tag in ["h1", "h2", "h3"]:
        for heading in soup.find_all(tag):
            text = heading.get_text(strip=True)
            if text:
                result[tag].append(text)

    # 画像
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if base_url and src:
            src = urljoin(base_url, src)

        result["images"].append({
            "src": src,
            "alt": img.get("alt"),
            "width": img.get("width"),
            "height": img.get("height"),
            "loading": img.get("loading"),
        })

    # リンク
    if base_url:
        base_domain = urlparse(base_url).netloc

        for a in soup.find_all("a", href=True):
            href = a.get("href", "")
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue

            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)

            link_data = {
                "href": full_url,
                "text": a.get_text(strip=True)[:100],
                "rel": a.get("rel", []),
            }

            if parsed.netloc == base_domain:
                result["links"]["internal"].append(link_data)
            else:
                result["links"]["external"].append(link_data)

    # Schema (JSON-LD)
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            schema_data = json.loads(script.string)
            result["schema"].append(schema_data)
        except (json.JSONDecodeError, TypeError):
            pass

    # 単語数（表示テキストのみ）
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)
    words = re.findall(r"\b\w+\b", text)
    result["word_count"] = len(words)

    return result


def main():
    parser = argparse.ArgumentParser(description="SEO分析のためにHTMLを解析する")
    parser.add_argument("file", nargs="?", help="解析対象のHTMLファイル")
    parser.add_argument("--url", "-u", help="リンク解決用のベースURL")
    parser.add_argument("--json", "-j", action="store_true", help="JSON形式で出力する")

    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        html = sys.stdin.read()

    result = parse_html(html, args.url)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"タイトル: {result['title']}")
        print(f"メタディスクリプション: {result['meta_description']}")
        print(f"Canonical: {result['canonical']}")
        print(f"H1タグ数: {len(result['h1'])}")
        print(f"H2タグ数: {len(result['h2'])}")
        print(f"画像数: {len(result['images'])}")
        print(f"内部リンク数: {len(result['links']['internal'])}")
        print(f"外部リンク数: {len(result['links']['external'])}")
        print(f"Schemaブロック数: {len(result['schema'])}")
        print(f"単語数: {result['word_count']}")


if __name__ == "__main__":
    main()
