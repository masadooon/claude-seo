#!/usr/bin/env python3
"""
Playwrightを使用してWebページのビジュアル面を分析します。

使い方:
    python analyze_visual.py https://example.com
"""

import argparse
import json
import sys

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("エラー: playwrightが必要です。次のコマンドでインストールしてください: pip install playwright && playwright install chromium")
    sys.exit(1)


def analyze_visual(url: str, timeout: int = 30000) -> dict:
    """
    Webページのビジュアル面を分析します。

    Args:
        url: 分析対象のURL
        timeout: ページ読み込みのタイムアウト（ミリ秒）

    Returns:
        ビジュアル分析結果を含む辞書
    """
    result = {
        "url": url,
        "above_fold": {
            "h1_visible": False,
            "cta_visible": False,
            "hero_image": None,
        },
        "mobile": {
            "viewport_meta": False,
            "horizontal_scroll": False,
            "touch_targets_ok": True,
        },
        "layout": {
            "overlapping_elements": [],
            "text_overflow": [],
        },
        "fonts": {
            "base_size": None,
            "readable": True,
        },
        "error": None,
    }

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            # デスクトップ分析
            desktop = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = desktop.new_page()
            page.goto(url, wait_until="networkidle", timeout=timeout)

            # ファーストビューでのH1の表示を確認
            h1 = page.query_selector("h1")
            if h1:
                box = h1.bounding_box()
                if box and box["y"] < 1080:
                    result["above_fold"]["h1_visible"] = True

            # ファーストビューでのCTAボタンの存在を確認
            cta_selectors = [
                "a[href*='signup']",
                "a[href*='contact']",
                "a[href*='demo']",
                "button:has-text('Get Started')",
                "button:has-text('Sign Up')",
                "button:has-text('Contact')",
                ".cta",
                "[class*='cta']",
            ]
            for selector in cta_selectors:
                try:
                    cta = page.query_selector(selector)
                    if cta:
                        box = cta.bounding_box()
                        if box and box["y"] < 1080:
                            result["above_fold"]["cta_visible"] = True
                            break
                except Exception:
                    pass

            # ヒーロー画像を確認
            hero_selectors = [
                ".hero img",
                "[class*='hero'] img",
                "header img",
                "main img:first-of-type",
            ]
            for selector in hero_selectors:
                try:
                    hero = page.query_selector(selector)
                    if hero:
                        src = hero.get_attribute("src")
                        if src:
                            result["above_fold"]["hero_image"] = src
                            break
                except Exception:
                    pass

            desktop.close()

            # モバイル分析
            mobile = browser.new_context(viewport={"width": 375, "height": 812})
            page = mobile.new_page()
            page.goto(url, wait_until="networkidle", timeout=timeout)

            # viewport metaタグを確認
            viewport_meta = page.query_selector('meta[name="viewport"]')
            result["mobile"]["viewport_meta"] = viewport_meta is not None

            # 横スクロールの有無を確認
            scroll_width = page.evaluate("document.documentElement.scrollWidth")
            viewport_width = page.evaluate("window.innerWidth")
            result["mobile"]["horizontal_scroll"] = scroll_width > viewport_width

            # フォントサイズを確認
            base_font_size = page.evaluate("""
                () => {
                    const body = document.body;
                    const style = window.getComputedStyle(body);
                    return parseFloat(style.fontSize);
                }
            """)
            result["fonts"]["base_size"] = base_font_size
            result["fonts"]["readable"] = base_font_size >= 16

            mobile.close()
            browser.close()

    except PlaywrightTimeout:
        result["error"] = f"ページの読み込みが{timeout}ミリ秒後にタイムアウトしました"
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    parser = argparse.ArgumentParser(description="Webページのビジュアル面を分析します")
    parser.add_argument("url", help="分析対象のURL")
    parser.add_argument("--timeout", "-t", type=int, default=30000, help="タイムアウト（ミリ秒）")
    parser.add_argument("--json", "-j", action="store_true", help="JSON形式で出力")

    args = parser.parse_args()

    result = analyze_visual(args.url, timeout=args.timeout)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("ビジュアル分析結果")
        print("=" * 40)

        print("\nファーストビュー:")
        print(f"  H1の表示: {'✓' if result['above_fold']['h1_visible'] else '✗'}")
        print(f"  CTAの表示: {'✓' if result['above_fold']['cta_visible'] else '✗'}")
        print(f"  ヒーロー画像: {result['above_fold']['hero_image'] or '見つかりませんでした'}")

        print("\nモバイルレスポンシブ対応:")
        print(f"  Viewport Metaタグ: {'✓' if result['mobile']['viewport_meta'] else '✗'}")
        print(f"  横スクロール: {'✗（問題あり）' if result['mobile']['horizontal_scroll'] else '✓'}")

        print("\nタイポグラフィ:")
        print(f"  基本フォントサイズ: {result['fonts']['base_size']}px")
        print(f"  可読性（16px以上）: {'✓' if result['fonts']['readable'] else '✗'}")

        if result["error"]:
            print(f"\nエラー: {result['error']}")


if __name__ == "__main__":
    main()
