<!-- Updated: 2026-02-07 -->
# ECサイト SEO戦略テンプレート

## 業界の特徴

- 高いトランザクション意図
- 商品比較行動
- 価格感度の高さ
- ビジュアル重視の意思決定
- 季節的な需要パターン
- 競争の激しいマーケットプレイス掲載

## 推奨サイト構造

```
/
├── Home
├── /collections (or /categories)
│   ├── /category-1
│   │   ├── /subcategory-1
│   │   └── ...
│   ├── /category-2
│   └── ...
├── /products
│   ├── /product-1
│   ├── /product-2
│   └── ...
├── /brands
│   ├── /brand-1
│   └── ...
├── /sale (or /deals)
├── /new-arrivals
├── /best-sellers
├── /gift-guide
├── /blog
│   ├── /buying-guides
│   ├── /how-to
│   └── /trends
├── /about
├── /contact
├── /shipping
├── /returns
└── /faq
```

## schema の推奨事項

| ページ種別 | schema タイプ |
|-----------|-------------|
| 商品ページ | Product, Offer, AggregateRating, Review, BreadcrumbList |
| カテゴリページ | CollectionPage, ItemList, BreadcrumbList |
| ブランドページ | Brand, Organization |
| ブログ | Article, BlogPosting |

### ECサイト向け追加 schema（2025年）

- **ProductGroup**: バリエーション（サイズ、カラー）のある商品に使用。個別の Product エントリを `variesBy` と `hasVariant` プロパティでラップする。`schema/templates.json` を参照。
- **Certification**: 製品認証（Energy Star、安全性、オーガニック）向け。EnergyConsumptionDetails を置き換え（2025年4月）。Product に `hasCertification` を使用。
- **OfferShippingDetails**: 送料、処理時間、配送時間を含める。Google Merchant Center の掲載要件に不可欠。

> **Google Merchant Center 無料リスティング:** 商品は Google ショッピングに無料で表示可能。Product 構造化データが初回サーバーレンダリングされた HTML に含まれていること（JavaScript による注入ではない）。必須プロパティ: `name`, `image`, `price`, `priceCurrency`, `availability`。

> **JS レンダリングに関する注意:** Product 構造化データは初回サーバーレンダリングされた HTML に含める必要がある。JavaScript で動的に注入しないこと（2025年12月の Google JS SEO ガイダンスに基づく）。

### Product schema の例
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": ["https://example.com/product.jpg"],
  "description": "Product description",
  "sku": "SKU123",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://example.com/product"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "42"
  }
}
```

## コンテンツ要件

### 商品ページ（最低400語）
- ユニークな商品説明（メーカーのコピーをそのまま使わない）
- 特徴のハイライト
- ユースケース / 対象ユーザー
- スペック表
- サイズ・フィットガイド（アパレルの場合）
- お手入れ方法
- カスタマーレビュー

### カテゴリページ（最低400語）
- カテゴリの紹介文
- 購入ガイドの抜粋
- おすすめ商品
- サブカテゴリへのリンク
- フィルター・並び替えオプション

## 技術的考慮事項

### ページネーション
- rel="next"/rel="prev" またはもっと読み込むボタンを使用
- すべての商品がクロール可能であることを確認
- メインカテゴリページへの canonical 設定

### ファセットナビゲーション
- 重複コンテンツを生成するフィルターの組み合わせには noindex を設定
- canonical タグを適切に使用
- 人気のフィルターはインデックス可能にする

### 商品バリエーション
- バリエーションを持つ親商品に単一 URL を使用
- または個別 URL に親への canonical を設定
- すべてのバリエーションに構造化データを設定

## コンテンツの優先順位

### 高優先度
1. カテゴリページ（トップレベル）
2. 売れ筋商品ページ
3. ホームページ
4. 主要カテゴリの購入ガイド

### 中優先度
1. サブカテゴリページ
2. ブランドページ
3. 比較コンテンツ
4. 季節ごとのランディングページ

### ブログトピック
- 購入ガイド（「〜の選び方」）
- 商品比較
- トレンドレポート
- ユースケースとインスピレーション
- お手入れ・メンテナンスガイド

## 追跡すべき主要指標

- オーガニック検索からの収益
- 商品ページのランキング
- カテゴリページのランキング
- クリック率（リッチリザルト）
- オーガニック経由の平均注文額

## ECサイト向け Generative Engine Optimization（GEO）

AI 検索プラットフォームは商品クエリに直接回答するケースが増えている。AI による引用に最適化するために以下を実施:

- [ ] 商品スペック、寸法、素材を構造化フォーマットで明確に記載する
- [ ] バリエーション商品には ProductGroup schema を使用する
- [ ] オリジナルの商品写真に説明的な alt テキストを付ける
- [ ] 本物のカスタマーレビューコンテンツを含める（AggregateRating schema）
- [ ] すべてのプラットフォーム（自社サイト、Amazon、Google Merchant Center）で一貫した商品エンティティデータを維持する
- [ ] AI がパースできる明確な機能比較テーブルで比較コンテンツを構成する
- [ ] よくある商品の質問に対する詳細な FAQ コンテンツを追加する
