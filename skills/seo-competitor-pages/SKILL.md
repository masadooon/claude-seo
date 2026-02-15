---
name: seo-competitor-pages
description: >
  SEO最適化された競合比較ページおよび代替製品ページを生成します。「X vs Y」レイアウト、
  「Xの代替」ページ、機能比較マトリクス、schema markup、コンバージョン最適化を網羅します。
  ユーザーが「comparison page」「vs page」「alternatives page」「competitor comparison」
  「X vs Y」と言った場合に使用してください。
---

# 競合比較ページ & 代替製品ページ

競合意図キーワードをターゲットにした、正確で構造化されたコンテンツによる
高コンバージョンの比較ページおよび代替製品ページを作成します。

## ページタイプ

### 1. 「X vs Y」比較ページ
- 2つの製品・サービスの直接比較
- バランスの取れた機能ごとの分析
- 根拠を伴った明確な結論または推奨
- ターゲットキーワード: `[Product A] vs [Product B]`

### 2. 「Xの代替」ページ
- 特定の製品・サービスの代替リスト
- 各代替製品について概要、長所/短所、最適なユースケースを記載
- ターゲットキーワード: `[Product] alternatives`、`best alternatives to [Product]`

### 3. 「ベスト[カテゴリ]ツール」まとめページ
- カテゴリ内のトップツール・サービスの厳選リスト
- ランキング基準を明確に記載
- ターゲットキーワード: `best [category] tools [year]`、`top [category] software`

### 4. 比較表ページ
- 列に複数の製品を配置した機能マトリクス
- インタラクティブな場合はソート・フィルタリング機能付き
- ターゲットキーワード: `[category] comparison`、`[category] comparison chart`

## 比較表の生成

### 機能マトリクスのレイアウト
```
| Feature          | Your Product | Competitor A | Competitor B |
|------------------|:------------:|:------------:|:------------:|
| Feature 1        | ✅           | ✅           | ❌           |
| Feature 2        | ✅           | ⚠️ Partial   | ✅           |
| Feature 3        | ✅           | ❌           | ❌           |
| Pricing (from)   | $X/mo        | $Y/mo        | $Z/mo        |
| Free Tier        | ✅           | ❌           | ✅           |
```

### データ正確性の要件
- すべての機能に関する記載は公開情報から検証可能であること
- 価格は最新であること（「[date]時点」の注記を含める）
- 更新頻度: 四半期ごと、または競合が大きな変更をリリースした際にレビュー
- 可能な限り、各競合データのソースへリンクすること

## Schema Markup の推奨事項

### Product Schema（AggregateRating付き）
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product Name]",
  "description": "[Product Description]",
  "brand": {
    "@type": "Brand",
    "name": "[Brand Name]"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[Rating]",
    "reviewCount": "[Count]",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

### SoftwareApplication（ソフトウェア比較向け）
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[Software Name]",
  "applicationCategory": "[Category]",
  "operatingSystem": "[OS]",
  "offers": {
    "@type": "Offer",
    "price": "[Price]",
    "priceCurrency": "USD"
  }
}
```

### ItemList（まとめページ向け）
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Best [Category] Tools [Year]",
  "itemListOrder": "https://schema.org/ItemListOrderDescending",
  "numberOfItems": "[Count]",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "[Product Name]",
      "url": "[Product URL]"
    }
  ]
}
```

## キーワードターゲティング

### 比較意図パターン
| パターン | 例 | 検索ボリュームシグナル |
|---------|---------|---------------------|
| `[A] vs [B]` | "Slack vs Teams" | 高 |
| `[A] alternative` | "Figma alternatives" | 高 |
| `[A] alternatives [year]` | "Notion alternatives 2026" | 高 |
| `best [category] tools` | "best project management tools" | 高 |
| `[A] vs [B] for [use case]` | "AWS vs Azure for startups" | 中 |
| `[A] review [year]` | "Monday.com review 2026" | 中 |
| `[A] vs [B] pricing` | "HubSpot vs Salesforce pricing" | 中 |
| `is [A] better than [B]` | "is Notion better than Confluence" | 中 |

### Title Tag の構成パターン
- X vs Y: `[A] vs [B]: [主な差別化ポイント] ([Year])`
- 代替製品: `[N] Best [A] Alternatives in [Year] (Free & Paid)`
- まとめ: `[N] Best [Category] Tools in [Year] — Compared & Ranked`

### H1 パターン
- Title Tag の意図と一致させる
- メインキーワードを自然に含める
- 70文字以内に収める

## コンバージョン最適化レイアウト

### CTA の配置
- **ファーストビュー**: 簡潔な比較サマリーとメインCTAを配置
- **比較表の後**: 「[Your Product]を無料で試す」CTAを配置
- **ページ下部**: 最終推奨とCTAを配置
- 競合の説明セクションでは過度なCTAを避ける（信頼性が低下するため）

### ソーシャルプルーフセクション
- 比較基準に関連する顧客の声
- G2/Capterra/TrustPilot の評価（ソースリンク付き）
- 競合からの移行を示すケーススタディ
- 「[Competitor]から乗り換えました」ストーリー

### 価格のハイライト
- 明確な価格比較表
- 価格の安さだけでなく、価値の優位性を強調
- 隠れたコストを含める（初期費用、ユーザー単価、超過料金）
- 詳細な料金ページへのリンク

### 信頼性シグナル
- 「最終更新日: [date]」のタイムスタンプ
- 関連分野の専門知識を持つ著者
- 方法論の開示（比較の実施方法）
- 自社製品との関係性の開示

## 公正性ガイドライン

- **正確性**: 競合に関するすべての情報は公開情報から検証可能であること
- **名誉毀損の禁止**: 競合について虚偽または誤解を招く記載をしないこと
- **出典の明記**: 競合のウェブサイト、レビューサイト、またはドキュメントへリンクすること
- **適時の更新**: 競合が大きな変更をリリースした際にレビュー・更新すること
- **所属の開示**: どの製品が自社のものかを明確に記載すること
- **バランスの取れた紹介**: 競合の強みを正直に認めること
- **価格の正確性**: すべての価格データに「[date]時点」の免責事項を含めること
- **機能の検証**: 可能な限り競合の機能を実際にテストし、それ以外はドキュメントを引用すること

## 内部リンク

- 比較セクションから自社の製品・サービスページへリンク
- 関連する比較ページ間で相互リンク（例: 「A vs B」から「A vs C」へリンク）
- 個々の機能について議論する際に機能別ページへリンク
- パンくずリスト: ホーム > 比較 > [このページ]
- ページ下部に関連比較セクションを配置
- 比較で言及したケーススタディや顧客の声へリンク

## 出力

### 比較ページテンプレート
- `COMPARISON-PAGE.md` — セクション付きのすぐに実装可能なページ構造
- 機能マトリクス表
- 目標文字数付きのコンテンツアウトライン（最低1,500ワード）

### Schema Markup
- `comparison-schema.json` — Product/SoftwareApplication/ItemList の JSON-LD

### キーワード戦略
- メインキーワードとサブキーワード
- 関連するロングテールキーワードの機会
- 既存の競合ページとのコンテンツギャップ

### 推奨事項
- 既存の比較ページに対するコンテンツ改善
- 新しい比較ページの機会
- Schema Markup の追加
- コンバージョン最適化の提案
