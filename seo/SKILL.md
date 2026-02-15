---
name: seo
description: >
  あらゆるWebサイト・業種に対応する包括的なSEO分析スキル。サイト全体の監査、
  単一ページの詳細分析、技術的SEOチェック（クロール可能性、インデックス可能性、
  INPを含むCore Web Vitals）、schema マークアップの検出・検証・生成、コンテンツ
  品質評価（2025年12月アップデートにより全競合クエリに拡大されたE-E-A-Tフレーム
  ワーク）、画像最適化、sitemap分析、AI Overviews・ChatGPT・Perplexityの引用に
  向けた生成エンジン最適化（GEO）を実行。AIクローラーのアクセス可能性
  （GPTBot、ClaudeBot、PerplexityBot）、llms.txt準拠、ブランド言及シグナル、
  パッセージレベルの引用可能性を分析。SaaS、EC、ローカルビジネス、メディア、
  エージェンシーの業種検出に対応。トリガーワード: "SEO"、"audit"、"schema"、
  "Core Web Vitals"、"sitemap"、"E-E-A-T"、"AI Overviews"、"GEO"、
  "technical SEO"、"content quality"、"page speed"、"structured data"。
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
---

# SEO — 汎用SEO分析スキル

あらゆる業種（SaaS、ローカルサービス、EC、メディア、エージェンシー）に対応する
包括的なSEO分析。12の専門サブスキルと6つのサブエージェントを統合的に管理します。

## クイックリファレンス

| コマンド | 概要 |
|---------|-------------|
| `/seo audit <url>` | サブエージェントの並列委任によるサイト全体の監査 |
| `/seo page <url>` | 単一ページの詳細分析 |
| `/seo sitemap <url or generate>` | XML sitemapの分析または生成 |
| `/seo schema <url>` | Schema.orgマークアップの検出・検証・生成 |
| `/seo images <url>` | 画像最適化の分析 |
| `/seo technical <url>` | 技術的SEO監査（8カテゴリ） |
| `/seo content <url>` | E-E-A-Tおよびコンテンツ品質の分析 |
| `/seo geo <url>` | AI Overviews / 生成エンジン最適化 |
| `/seo plan <business-type>` | SEO戦略プランニング |
| `/seo programmatic [url\|plan]` | プログラマティックSEOの分析・計画 |
| `/seo competitor-pages [url\|generate]` | 競合比較ページの生成 |
| `/seo hreflang [url]` | hreflang/多言語SEOの監査・生成 |

## オーケストレーションロジック

ユーザーが `/seo audit` を実行した場合、サブエージェントに並列で委任します：
1. 業種を検出（SaaS、ローカル、EC、メディア、エージェンシー、その他）
2. サブエージェントを起動：seo-technical、seo-content、seo-schema、seo-sitemap、seo-performance、seo-visual
3. 結果を収集し、SEOヘルススコア（0〜100）を含む統合レポートを生成
4. 優先度付きアクションプランを作成（Critical → High → Medium → Low）

個別コマンドの場合は、該当するサブスキルを直接読み込みます。

## 業種検出

トップページのシグナルから業種を検出します：
- **SaaS**: 料金ページ、/features、/integrations、/docs、「free trial」、「sign up」
- **ローカルサービス**: 電話番号、住所、対応エリア、「serving [city]」、Google Maps埋め込み
- **EC**: /products、/collections、/cart、「add to cart」、product schema
- **メディア**: /blog、/articles、/topics、article schema、著者ページ、公開日
- **エージェンシー**: /case-studies、/portfolio、/industries、「our work」、クライアントロゴ

## 品質ゲート

ページ種別ごとの薄いコンテンツ閾値については `references/quality-gates.md` を参照してください。
絶対ルール：
- ⚠️ 警告：ロケーションページが30件以上（ユニークコンテンツ60%以上を必須とする）
- 🛑 強制停止：ロケーションページが50件以上（ユーザーによる正当性の説明が必要）
- HowTo schema は推奨しないこと（2023年9月に廃止済み）
- FAQ schema は政府系・医療系サイトのみに限定
- Core Web Vitalsへの言及はすべてINPを使用し、FIDは使用しないこと

## リファレンスファイル

必要に応じて都度読み込むこと。起動時にすべて読み込まないでください：
- `references/cwv-thresholds.md` — 現行のCore Web Vitals閾値と計測の詳細
- `references/schema-types.md` — 対応する全schemaタイプと廃止状況
- `references/eeat-framework.md` — E-E-A-T評価基準（2025年9月QRGアップデート）
- `references/quality-gates.md` — コンテンツの最低文字数、ユニーク率の閾値

## スコアリング方法

### SEOヘルススコア（0〜100）
全カテゴリの加重集計：

| カテゴリ | ウェイト |
|----------|--------|
| Technical SEO | 25% |
| コンテンツ品質 | 25% |
| On-Page SEO | 20% |
| Schema / 構造化データ | 10% |
| パフォーマンス (CWV) | 10% |
| 画像 | 5% |
| AI検索対応度 | 5% |

### 優先度レベル
- **Critical**: インデックスを阻害、またはペナルティの原因となる（即時対応が必要）
- **High**: 検索順位に大きな影響がある（1週間以内に対応）
- **Medium**: 最適化の余地がある（1ヶ月以内に対応）
- **Low**: あれば望ましい（バックログ）

## サブスキル

本スキルは12の専門サブスキルを統合管理します：

1. **seo-audit** — サブエージェント並列委任によるサイト全体の監査
2. **seo-page** — 単一ページの詳細分析
3. **seo-technical** — 技術的SEO（8カテゴリ）
4. **seo-content** — E-E-A-Tおよびコンテンツ品質
5. **seo-schema** — schemaマークアップの検出・生成
6. **seo-images** — 画像最適化
7. **seo-sitemap** — sitemap分析・生成
8. **seo-geo** — AI Overviews / GEO最適化
9. **seo-plan** — テンプレートを活用した戦略プランニング
10. **seo-programmatic** — プログラマティックSEOの分析・計画
11. **seo-competitor-pages** — 競合比較ページの生成
12. **seo-hreflang** — hreflang/多言語SEOの監査・生成

## サブエージェント

監査時の並列分析に使用：
- `seo-technical` — クロール可能性、インデックス可能性、セキュリティ、CWV
- `seo-content` — E-E-A-T、読みやすさ、薄いコンテンツ
- `seo-schema` — 検出、検証、生成
- `seo-sitemap` — 構造、カバレッジ、品質ゲート
- `seo-performance` — Core Web Vitalsの計測
- `seo-visual` — スクリーンショット、モバイルテスト、ファーストビュー
