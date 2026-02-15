<!-- Updated: 2026-02-07 -->
---
name: seo-technical
description: >
  テクニカルSEO監査（8カテゴリ）：クローラビリティ、インデックス可能性、セキュリティ、
  URL構造、モバイル、Core Web Vitals、構造化データ、JavaScriptレンダリング。
  ユーザーが「テクニカルSEO」「クロールの問題」「robots.txt」「Core Web Vitals」
  「サイト速度」「セキュリティヘッダー」と言った場合に使用。
---

# テクニカルSEO監査

## カテゴリ

### 1. クローラビリティ
- robots.txt：存在するか、有効か、重要なリソースをブロックしていないか
- XML sitemap：存在するか、robots.txtで参照されているか、フォーマットが正しいか
- noindexタグ：意図的なものか、誤設定か
- クロール深度：重要なページがホームページから3クリック以内にあるか
- JavaScriptレンダリング：重要なコンテンツがJS実行を必要とするか確認
- クロールバジェット：大規模サイト（1万ページ超）では効率が重要

#### AIクローラー管理

2025〜2026年現在、AI企業はモデル学習やAI検索のためにウェブを積極的にクロールしています。robots.txtを通じたこれらのクローラーの管理は、テクニカルSEOにおける重要な考慮事項です。

**既知のAIクローラー：**

| クローラー | 企業 | robots.txtトークン | 目的 |
|---------|---------|-----------------|---------|
| GPTBot | OpenAI | `GPTBot` | モデル学習 |
| ChatGPT-User | OpenAI | `ChatGPT-User` | リアルタイムブラウジング |
| ClaudeBot | Anthropic | `ClaudeBot` | モデル学習 |
| PerplexityBot | Perplexity | `PerplexityBot` | 検索インデックス＋学習 |
| Bytespider | ByteDance | `Bytespider` | モデル学習 |
| Google-Extended | Google | `Google-Extended` | Gemini学習（検索には影響なし） |
| CCBot | Common Crawl | `CCBot` | オープンデータセット |

**重要な違い：**
- `Google-Extended`をブロックするとGeminiの学習利用は防げますが、Google検索のインデックスやAI Overviewsには影響しません（それらは`Googlebot`を使用）
- `GPTBot`をブロックするとOpenAIの学習は防げますが、ChatGPTがブラウジング機能（`ChatGPT-User`）であなたのコンテンツを引用することは防げません
- 現在、約3〜5%のウェブサイトがAI固有のrobots.txtルールを使用しています

**例 — AIクローラーの選択的ブロック：**
```
# Allow search indexing, block AI training crawlers
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Bytespider
Disallow: /

# Allow all other crawlers (including Googlebot for search)
User-agent: *
Allow: /
```

**推奨事項：** ブロックする前にAI可視性戦略を検討してください。AIシステムに引用されることは、ブランド認知やリファラルトラフィックの向上につながります。AI可視性の最適化については`seo-geo`スキルも参照してください。

### 2. インデックス可能性
- canonicalタグ：自己参照か、noindexとの競合がないか
- 重複コンテンツ：類似コンテンツ、パラメータURL、wwwありなし
- 低品質コンテンツ：ページタイプごとの最低文字数を下回るページ
- ページネーション：rel=next/prevまたはload-moreパターン
- hreflang：多言語・多地域サイトで正しく設定されているか
- インデックスの肥大化：クロールバジェットを消費する不要なページ

### 3. セキュリティ
- HTTPS：強制されているか、SSL証明書が有効か、混在コンテンツがないか
- セキュリティヘッダー：
  - Content-Security-Policy (CSP)
  - Strict-Transport-Security (HSTS)
  - X-Frame-Options
  - X-Content-Type-Options
  - Referrer-Policy
- HSTSプリロード：高セキュリティサイトではプリロードリストへの登録を確認

### 4. URL構造
- クリーンなURL：説明的、ハイフン区切り、コンテンツにクエリパラメータなし
- 階層構造：サイトアーキテクチャを反映した論理的なフォルダ構造
- リダイレクト：チェーンなし（最大1ホップ）、恒久的な移動には301を使用
- URLの長さ：100文字超を警告
- 末尾スラッシュ：一貫した使用

### 5. モバイル最適化
- レスポンシブデザイン：viewportメタタグ、レスポンシブCSS
- タッチターゲット：最小48x48px、8pxの間隔
- フォントサイズ：基本16px以上
- 水平スクロールなし
- モバイルファーストインデックス：Googleはモバイル版をインデックスする。**モバイルファーストインデックスは2024年7月5日に100%完了。** Googleは現在、すべてのウェブサイトをモバイルGooglebotユーザーエージェントのみでクロール・インデックスしています。

### 6. Core Web Vitals
- **LCP** (Largest Contentful Paint)：目標 <2.5秒
- **INP** (Interaction to Next Paint)：目標 <200ms
  - INPは2024年3月12日にFIDを置き換えました。FIDは2024年9月9日にすべてのChromeツール（CrUX API、PageSpeed Insights、Lighthouse）から完全に削除されました。FIDへの言及は一切不要です。
- **CLS** (Cumulative Layout Shift)：目標 <0.1
- 評価には実ユーザーデータの75パーセンタイルを使用
- MCP利用可能な場合はPageSpeed Insights APIまたはCrUXデータを使用

### 7. 構造化データ
- 検出：JSON-LD（推奨）、Microdata、RDFa
- Googleがサポートするタイプに対するバリデーション
- 詳細な分析についてはseo-schemaスキルを参照

### 8. JavaScriptレンダリング
- コンテンツが初期HTMLで表示されるか、JSが必要かを確認
- クライアントサイドレンダリング（CSR）とサーバーサイドレンダリング（SSR）を特定
- インデックスの問題を引き起こす可能性のあるSPAフレームワーク（React、Vue、Angular）を警告
- 該当する場合はダイナミックレンダリングの設定を検証

#### JavaScript SEO — canonical＆インデックスに関するガイダンス（2025年12月）

Googleは2025年12月にJavaScript SEOドキュメントを更新し、重要な明確化を行いました：

1. **canonicalの競合：** 生HTMLのcanonicalタグとJavaScriptで挿入されたcanonicalタグが異なる場合、Googleはどちらを使用するか分かりません。サーバーレンダリングされたHTMLとJS出力の間でcanonicalタグが同一であることを確認してください。
2. **JavaScriptによるnoindex：** 生HTMLに`<meta name="robots" content="noindex">`が含まれていてJavaScriptがそれを削除した場合でも、Googleは生HTMLのnoindexを適用する可能性があります。正しいrobots指示は初期HTMLレスポンスで提供してください。
3. **非200ステータスコード：** Googleは非200 HTTPステータスコードを返すページではJavaScriptをレンダリングしません。エラーページでJSにより挿入されたコンテンツやメタタグはGooglebotには見えません。
4. **JavaScriptによる構造化データ：** Product、Articleなど、JSで挿入された構造化データは処理が遅延する場合があります。時間的制約のある構造化データ（特にEコマースのProductマークアップ）は、初期サーバーレンダリングHTMLに含めてください。

**ベストプラクティス：** 重要なSEO要素（canonical、meta robots、構造化データ、title、meta description）はJavaScript挿入に頼らず、初期サーバーレンダリングHTMLで提供してください。

### 9. IndexNowプロトコル
- サイトがBing、Yandex、Naver向けにIndexNowをサポートしているか確認
- Google以外の検索エンジンがサポート
- Google以外のエンジンでの高速インデックスのため、実装を推奨

## 出力

### テクニカルスコア：XX/100

### カテゴリ別内訳
| カテゴリ | ステータス | スコア |
|----------|--------|-------|
| クローラビリティ | ✅/⚠️/❌ | XX/100 |
| インデックス可能性 | ✅/⚠️/❌ | XX/100 |
| セキュリティ | ✅/⚠️/❌ | XX/100 |
| URL構造 | ✅/⚠️/❌ | XX/100 |
| モバイル | ✅/⚠️/❌ | XX/100 |
| Core Web Vitals | ✅/⚠️/❌ | XX/100 |
| 構造化データ | ✅/⚠️/❌ | XX/100 |
| JSレンダリング | ✅/⚠️/❌ | XX/100 |

### 重大な問題（直ちに修正）
### 高優先度（1週間以内に修正）
### 中優先度（1ヶ月以内に修正）
### 低優先度（バックログ）
