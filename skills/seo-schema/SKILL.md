<!-- Updated: 2026-02-07 -->
---
name: seo-schema
description: >
  Schema.org 構造化データの検出、検証、生成を行う。JSON-LD 形式を推奨。
  ユーザーが「schema」「構造化データ」「リッチリザルト」「JSON-LD」「マークアップ」
  と言った場合に使用する。
---

# Schema マークアップの分析と生成

## 検出

1. ページソースから JSON-LD `<script type="application/ld+json">` をスキャンする
2. Microdata（`itemscope`、`itemprop`）の有無を確認する
3. RDFa（`typeof`、`property`）の有無を確認する
4. 常に JSON-LD を主要フォーマットとして推奨する（Google が公式に推奨）

## 検証

- schema タイプごとに必須プロパティを確認する
- Google がサポートするリッチリザルトタイプと照合して検証する
- よくあるエラーをチェックする：
  - @context の欠落
  - 無効な @type
  - 誤ったデータ型
  - プレースホルダーテキスト
  - 相対 URL（絶対 URL にすべき）
  - 無効な日付形式
- 非推奨のタイプにフラグを立てる（下記参照）

## Schema タイプのステータス（2026年2月時点）

完全なリストは `references/schema-types.md` を参照。主なルール：

### アクティブ — 自由に推奨可能：
Organization, LocalBusiness, SoftwareApplication, WebApplication, Product（2025年4月より Certification マークアップ対応）, ProductGroup, Offer, Service, Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting

### 動画・特殊用途 — 自由に推奨可能：
BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode

すぐに使える JSON-LD テンプレートについては `schema/templates.json` を参照。

> **JSON-LD と JavaScript レンダリング：** Google の2025年12月の JS SEO ガイダンスによると、JavaScript で挿入された構造化データは処理が遅延する可能性がある。時間的制約のあるマークアップ（特に Product、Offer）については、JSON-LD を最初のサーバーレンダリング HTML に含めること。

### 制限付き — 特定のサイトのみ：
- **FAQ**: 政府および医療機関の権威あるサイトのみ対象（2023年8月に制限）

### 非推奨 — 推奨しないこと：
- **HowTo**: リッチリザルトは2023年9月に廃止
- **SpecialAnnouncement**: 2025年7月31日に非推奨化
- **CourseInfo, EstimatedSalary, LearningVideo**: 2025年6月に廃止
- **ClaimReview**: 2025年6月にリッチリザルトから廃止
- **VehicleListing**: 2025年6月にリッチリザルトから廃止
- **Practice Problem**: 2025年後半にリッチリザルトから廃止
- **Dataset**: 2025年後半にリッチリザルトから廃止
- **Book Actions**: 一度非推奨化されたが撤回 — 2026年2月時点ではまだ機能している（参考情報）

## 生成

ページの schema を生成する際：
1. コンテンツ分析からページタイプを特定する
2. 適切な schema タイプを選択する
3. 必須プロパティと推奨プロパティをすべて含む有効な JSON-LD を生成する
4. 真実で検証可能なデータのみを含める — ユーザーが入力すべき箇所は明確にプレースホルダーとして表示する
5. 提示前に出力を検証する

## よく使う Schema テンプレート

### Organization
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "[Website URL]",
  "logo": "[Logo URL]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[Phone]",
    "contactType": "customer service"
  },
  "sameAs": [
    "[Facebook URL]",
    "[LinkedIn URL]",
    "[Twitter URL]"
  ]
}
```

### LocalBusiness
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "telephone": "[Phone]",
  "openingHours": "Mo-Fr 09:00-17:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[Lat]",
    "longitude": "[Long]"
  }
}
```

### Article/BlogPosting
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Title]",
  "author": {
    "@type": "Person",
    "name": "[Author Name]"
  },
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "image": "[Image URL]",
  "publisher": {
    "@type": "Organization",
    "name": "[Publisher]",
    "logo": {
      "@type": "ImageObject",
      "url": "[Logo URL]"
    }
  }
}
```

## 出力

- `SCHEMA-REPORT.md` — 検出および検証の結果
- `generated-schema.json` — すぐに使える JSON-LD スニペット

### 検証結果
| Schema | タイプ | ステータス | 問題点 |
|--------|--------|------------|--------|
| ... | ... | ✅/⚠️/❌ | ... |

### 推奨事項
- 不足している schema の機会
- 必要な検証の修正
- 実装用の生成コード
