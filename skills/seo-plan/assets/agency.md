<!-- Updated: 2026-02-07 -->
# エージェンシー/コンサルティング会社向けSEO戦略テンプレート

## 業界の特徴

- サービスベースの高額取引
- 専門性と信頼が最も重要
- 検討期間が長い
- ポートフォリオ/ケーススタディに基づく意思決定
- リレーションシップベースの営業
- ニッチな専門分野への特化が有利

## 推奨サイト構成

```
/
├── Home
├── /services
│   ├── /service-1
│   │   ├── /sub-service-1
│   │   └── ...
│   └── /service-2
├── /industries
│   ├── /industry-1
│   ├── /industry-2
│   └── ...
├── /work (or /case-studies)
│   ├── /case-study-1
│   ├── /case-study-2
│   └── ...
├── /about
│   ├── /team
│   │   ├── /team-member-1
│   │   └── ...
│   ├── /culture
│   └── /careers
├── /insights (or /blog)
│   ├── /articles
│   ├── /guides
│   ├── /webinars
│   └── /podcasts
├── /contact
├── /process
└── /faq
```

## schema の推奨設定

| ページ種別 | schema タイプ |
|-----------|-------------|
| トップページ | Organization, ProfessionalService |
| サービスページ | Service, ProfessionalService |
| ケーススタディ | Article, Organization（クライアント） |
| チームメンバー | Person, ProfilePage |
| ブログ | Article, BlogPosting |

### ProfessionalService schema の例
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Agency Name",
  "description": "What the agency does",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Agency St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "areaServed": "National",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Service 1"
        }
      }
    ]
  }
}
```

## E-E-A-T の要件

### チームページに必要な要素
- プロフェッショナルな顔写真
- 資格・経歴を含む詳細なプロフィール
- 業界での経験
- 登壇実績
- 出版・執筆実績
- ソーシャルプロフィール

### ケーススタディに必要な要素
- クライアント名（許可がある場合）または業種
- 課題・問題の説明
- アプローチ・方法論
- 具体的な数値を含む成果
- タイムライン
- 推薦コメント

## コンテンツの優先順位

### 高優先度
1. サービスページ（詳細かつ具体的）
2. 業種別ページ（業界ごとの専門性）
3. 3〜5件の詳細なケーススタディ
4. チーム/リーダーシップページ

### 中優先度
1. 方法論/プロセスページ
2. ソートリーダーシップを含むブログ
3. 比較コンテンツ（代替手段との比較）
4. FAQページ

### ソートリーダーシップのトピック
- 業界トレンド分析
- ハウツーガイド（競合しない領域）
- 独自のリサーチ/アンケート調査
- イベントレポートとインサイト
- 専門家インタビュー
- ツール/テクノロジーレビュー

## コンテンツ戦略

### サービスページ（最低800語）
- 明確なバリュープロポジション
- 方法論の概要
- 成果物一覧
- 関連するケーススタディ
- このサービスを担当するチームメンバー
- 相談予約へのCTA

### 業種別ページ（最低800語）
- 業種固有の課題
- 自社ならではの解決方法
- 関連するケーススタディ
- 業界の資格・実績
- クライアントのロゴ（許可がある場合）

### ケーススタディ（最低1,000語）
- エグゼクティブサマリー
- クライアントの背景
- 課題の詳細
- ソリューションのアプローチ
- 実施プロセス
- 測定可能な成果
- クライアントの推薦コメント
- 関連サービス/CTA

## 追跡すべき主要指標

- サービスページへのオーガニックトラフィック
- ケーススタディページのページビュー
- オーガニック経由のお問い合わせフォーム送信数
- 主要コンテンツの滞在時間
- ブログからサービスページへのコンバージョン

## エージェンシー向け Generative Engine Optimization (GEO)

- [ ] 具体的で引用可能な数値や成果を含む独自のケーススタディを公開する
- [ ] 全チームメンバーに sameAs リンク付きの Person schema を使用する（エンティティの権威性を構築）
- [ ] チームメンバーページに ProfilePage schema を使用する
- [ ] サービスページの説明に、明確で引用しやすい専門性の記述を含める
- [ ] AIシステムが引用できる独自の業界リサーチやアンケート調査を制作する
- [ ] ソートリーダーシップコンテンツを明確な見出しと抽出しやすいインサイトで構成する
- [ ] ディレクトリ、ソーシャルプロフィール、業界サイト全体でエージェンシーのエンティティ情報の一貫性を維持する
- [ ] ChatGPT、Perplexity、Google AI Overviews でのブランドおよび主要サービス用語のAI引用を監視する
