<!-- Updated: 2026-02-07 -->
# MCP Integration

## 概要

Claude SEO は Model Context Protocol (MCP) サーバーと統合し、外部 API へのアクセスや分析機能の強化が可能です。

## 利用可能な統合

### PageSpeed Insights API

Google の PageSpeed Insights API を直接使用して、実際の Core Web Vitals データを取得できます。

**設定方法:**

1. [Google Cloud Console](https://console.cloud.google.com/) から API キーを取得する
2. PageSpeed Insights API を有効にする
3. 分析に使用する:

```bash
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=YOUR_API_KEY"
```

### Google Search Console

オーガニック検索データには、[ahonn](https://github.com/ahonn/mcp-server-gsc) による `mcp-server-gsc` MCP サーバーを使用します。検索パフォーマンスデータ、URL 検査、サイトマップ管理の機能を提供します。

**設定方法:**

```json
{
  "mcpServers": {
    "google-search-console": {
      "command": "npx",
      "args": ["-y", "mcp-server-gsc"],
      "env": {
        "GOOGLE_CREDENTIALS_PATH": "/path/to/credentials.json"
      }
    }
  }
}
```

### PageSpeed Insights MCP Server

[enemyrr](https://github.com/enemyrr/mcp-server-pagespeed) による `mcp-server-pagespeed` を使用して、MCP 経由で Lighthouse 監査、CWV メトリクス、パフォーマンススコアリングを行えます。

**設定方法:**

```json
{
  "mcpServers": {
    "pagespeed": {
      "command": "npx",
      "args": ["-y", "mcp-server-pagespeed"],
      "env": {
        "PAGESPEED_API_KEY": "your-api-key"
      }
    }
  }
}
```

### 公式 SEO MCP サーバー (2025-2026)

SEO 向けの MCP エコシステムは大きく成熟しました。以下は本番環境で利用可能な統合です:

| ツール | パッケージ / エンドポイント | 種類 | 備考 |
|------|-------------------|------|-------|
| **Ahrefs** | `@ahrefs/mcp` | 公式 | 2025年7月リリース。ローカルモードとリモートモードに対応。被リンク、キーワード、サイト監査データ。 |
| **Semrush** | `https://mcp.semrush.com/v1/mcp` | 公式 (リモート) | リモート MCP エンドポイント経由で API にフルアクセス可能。ドメイン分析、キーワード調査、被リンクデータ。 |
| **Google Search Console** | `mcp-server-gsc` | コミュニティ | ahonn 作。検索パフォーマンス、URL 検査、サイトマップ。 |
| **PageSpeed Insights** | `mcp-server-pagespeed` | コミュニティ | enemyrr 作。Lighthouse 監査、CWV メトリクス、パフォーマンススコアリング。 |
| **DataForSEO** | `dataforseo-mcp-server` | コミュニティ | Skobyn 作 (GitHub: Skobyn/dataforseo-mcp-server)。SERP データ、キーワードデータ、被リンク。 |
| **kwrds.ai** | kwrds MCP server | コミュニティ | キーワード調査、検索ボリューム、難易度スコアリング。 |
| **SEO Review Tools** | SEO Review Tools MCP | コミュニティ | サイト監査およびオンページ分析 API。 |

## API 使用例

### PageSpeed Insights

```python
import requests

def get_pagespeed_data(url: str, api_key: str) -> dict:
    """Fetch PageSpeed Insights data for a URL."""
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": url,
        "key": api_key,
        "strategy": "mobile",  # or "desktop"
        "category": ["performance", "accessibility", "best-practices", "seo"]
    }
    response = requests.get(endpoint, params=params)
    return response.json()
```

### CrUX からの Core Web Vitals

```python
def get_crux_data(url: str, api_key: str) -> dict:
    """Fetch Chrome UX Report data for a URL."""
    endpoint = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"
    payload = {
        "url": url,
        "formFactor": "PHONE"  # or "DESKTOP"
    }
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    response = requests.post(endpoint, json=payload, headers=headers, params=params)
    return response.json()
```

## 取得可能なメトリクス

### PageSpeed Insights から取得

| メトリクス | 説明 |
|--------|-------------|
| LCP | Largest Contentful Paint (ラボデータ) |
| INP | Interaction to Next Paint (推定値) |
| CLS | Cumulative Layout Shift (ラボデータ) |
| FCP | First Contentful Paint |
| TBT | Total Blocking Time |
| Speed Index | 視覚的な表示進行速度 |

### CrUX から取得 (フィールドデータ)

| メトリクス | 説明 |
|--------|-------------|
| LCP | 75パーセンタイル、実ユーザーデータ |
| INP | 75パーセンタイル、実ユーザーデータ |
| CLS | 75パーセンタイル、実ユーザーデータ |
| TTFB | Time to First Byte |

## ベストプラクティス

1. **レート制限**: API のクォータを遵守する (PageSpeed の場合、通常1日あたり25,000リクエスト)
2. **キャッシュ**: 不要な API 呼び出しを避けるために結果をキャッシュする
3. **フィールドデータ vs ラボデータ**: ランキングシグナルにはフィールドデータ (CrUX) を優先する
4. **エラーハンドリング**: API エラーを適切に処理する

## API キーなしでの利用

API キーがなくても、Claude SEO は以下のことが可能です:

1. HTML ソースを分析して潜在的な問題を特定する
2. 一般的なパフォーマンスの問題を特定する
3. レンダリングブロッキングリソースを確認する
4. 画像最適化の改善点を評価する
5. JavaScript に依存した実装を検出する

なお、実際の Core Web Vitals の測定には、実ユーザーによるフィールドデータが必要です。
