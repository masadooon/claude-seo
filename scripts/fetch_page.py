#!/usr/bin/env python3
"""
適切なヘッダーとエラーハンドリングを使用してWebページを取得します。

使い方:
    python fetch_page.py https://example.com
    python fetch_page.py https://example.com --output page.html
"""

import argparse
import sys
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("エラー: requests ライブラリが必要です。次のコマンドでインストールしてください: pip install requests")
    sys.exit(1)


DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ClaudeSEO/1.0; +https://github.com/AgriciDaniel/claude-seo)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}


def fetch_page(
    url: str,
    timeout: int = 30,
    follow_redirects: bool = True,
    max_redirects: int = 5,
) -> dict:
    """
    Webページを取得し、レスポンスの詳細を返します。

    引数:
        url: 取得対象のURL
        timeout: リクエストのタイムアウト（秒）
        follow_redirects: リダイレクトに追従するかどうか
        max_redirects: 追従するリダイレクトの最大数

    戻り値:
        以下を含む辞書:
            - url: リダイレクト後の最終URL
            - status_code: HTTPステータスコード
            - content: レスポンスの本文
            - headers: レスポンスヘッダー
            - redirect_chain: リダイレクトURLのリスト
            - error: 失敗した場合のエラーメッセージ
    """
    result = {
        "url": url,
        "status_code": None,
        "content": None,
        "headers": {},
        "redirect_chain": [],
        "error": None,
    }

    # URLを検証する
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        result["error"] = f"無効なURLスキーム: {parsed.scheme}"
        return result

    try:
        session = requests.Session()
        session.max_redirects = max_redirects

        response = session.get(
            url,
            headers=DEFAULT_HEADERS,
            timeout=timeout,
            allow_redirects=follow_redirects,
        )

        result["url"] = response.url
        result["status_code"] = response.status_code
        result["content"] = response.text
        result["headers"] = dict(response.headers)

        # リダイレクトチェーンを記録する
        if response.history:
            result["redirect_chain"] = [r.url for r in response.history]

    except requests.exceptions.Timeout:
        result["error"] = f"リクエストが{timeout}秒後にタイムアウトしました"
    except requests.exceptions.TooManyRedirects:
        result["error"] = f"リダイレクトが多すぎます（最大{max_redirects}回）"
    except requests.exceptions.SSLError as e:
        result["error"] = f"SSLエラー: {e}"
    except requests.exceptions.ConnectionError as e:
        result["error"] = f"接続エラー: {e}"
    except requests.exceptions.RequestException as e:
        result["error"] = f"リクエストに失敗しました: {e}"

    return result


def main():
    parser = argparse.ArgumentParser(description="SEO分析のためにWebページを取得します")
    parser.add_argument("url", help="取得するURL")
    parser.add_argument("--output", "-o", help="出力ファイルのパス")
    parser.add_argument("--timeout", "-t", type=int, default=30, help="タイムアウト（秒）")
    parser.add_argument("--no-redirects", action="store_true", help="リダイレクトに追従しない")

    args = parser.parse_args()

    result = fetch_page(
        args.url,
        timeout=args.timeout,
        follow_redirects=not args.no_redirects,
    )

    if result["error"]:
        print(f"エラー: {result['error']}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result["content"])
        print(f"{args.output} に保存しました")
    else:
        print(result["content"])

    # メタデータを標準エラー出力に表示する
    print(f"\nURL: {result['url']}", file=sys.stderr)
    print(f"ステータス: {result['status_code']}", file=sys.stderr)
    if result["redirect_chain"]:
        print(f"リダイレクト: {' -> '.join(result['redirect_chain'])}", file=sys.stderr)


if __name__ == "__main__":
    main()
