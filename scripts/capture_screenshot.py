#!/usr/bin/env python3
"""
Playwrightを使用してWebページのスクリーンショットを撮影します。

使い方:
    python capture_screenshot.py https://example.com
    python capture_screenshot.py https://example.com --mobile
    python capture_screenshot.py https://example.com --output screenshots/
"""

import argparse
import os
import sys
from urllib.parse import urlparse

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("エラー: playwrightが必要です。次のコマンドでインストールしてください: pip install playwright && playwright install chromium")
    sys.exit(1)


VIEWPORTS = {
    "desktop": {"width": 1920, "height": 1080},
    "laptop": {"width": 1366, "height": 768},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 375, "height": 812},
}


def capture_screenshot(
    url: str,
    output_path: str,
    viewport: str = "desktop",
    full_page: bool = False,
    timeout: int = 30000,
) -> dict:
    """
    Webページのスクリーンショットを撮影します。

    Args:
        url: 撮影対象のURL
        output_path: 出力ファイルパス
        viewport: ビューポートのプリセット (desktop, laptop, tablet, mobile)
        full_page: ページ全体を撮影するか、ビューポートのみを撮影するか
        timeout: ページ読み込みのタイムアウト（ミリ秒）

    Returns:
        撮影結果を含む辞書
    """
    result = {
        "url": url,
        "output": output_path,
        "viewport": viewport,
        "success": False,
        "error": None,
    }

    if viewport not in VIEWPORTS:
        result["error"] = f"無効なビューポート: {viewport}。次の中から選択してください: {list(VIEWPORTS.keys())}"
        return result

    vp = VIEWPORTS[viewport]

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": vp["width"], "height": vp["height"]},
                device_scale_factor=2 if viewport == "mobile" else 1,
            )
            page = context.new_page()

            # ページに遷移し、ネットワークがアイドル状態になるまで待機
            page.goto(url, wait_until="networkidle", timeout=timeout)

            # 遅延読み込みコンテンツのためにさらに少し待機
            page.wait_for_timeout(1000)

            # スクリーンショットを撮影
            page.screenshot(path=output_path, full_page=full_page)

            result["success"] = True
            browser.close()

    except PlaywrightTimeout:
        result["error"] = f"ページの読み込みが{timeout}ミリ秒後にタイムアウトしました"
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    parser = argparse.ArgumentParser(description="Webページのスクリーンショットを撮影")
    parser.add_argument("url", help="撮影対象のURL")
    parser.add_argument("--output", "-o", default="screenshots", help="出力ディレクトリ")
    parser.add_argument("--viewport", "-v", default="desktop", choices=VIEWPORTS.keys())
    parser.add_argument("--all", "-a", action="store_true", help="すべてのビューポートで撮影")
    parser.add_argument("--full", "-f", action="store_true", help="ページ全体を撮影")
    parser.add_argument("--timeout", "-t", type=int, default=30000, help="タイムアウト（ミリ秒）")

    args = parser.parse_args()

    # 出力ディレクトリを作成
    os.makedirs(args.output, exist_ok=True)

    # URLからファイル名を生成
    parsed = urlparse(args.url)
    base_name = parsed.netloc.replace(".", "_")

    viewports = VIEWPORTS.keys() if args.all else [args.viewport]

    for viewport in viewports:
        filename = f"{base_name}_{viewport}.png"
        output_path = os.path.join(args.output, filename)

        print(f"{viewport}のスクリーンショットを撮影中...")
        result = capture_screenshot(
            args.url,
            output_path,
            viewport=viewport,
            full_page=args.full,
            timeout=args.timeout,
        )

        if result["success"]:
            print(f"  ✓ {output_path} に保存しました")
        else:
            print(f"  ✗ 失敗: {result['error']}")


if __name__ == "__main__":
    main()
