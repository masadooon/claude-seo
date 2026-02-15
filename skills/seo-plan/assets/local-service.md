<!-- Updated: 2026-02-07 -->
# 地域密着型サービス業向けSEO戦略テンプレート

## 業界の特徴

- 地域に特化した検索が中心
- 高い検索意図、迅速な意思決定
- レビューが意思決定に大きく影響
- 電話がメインのコンバージョン経路
- モバイルファーストのユーザー行動
- 緊急対応のサービスニーズ

## 推奨サイト構造

```
/
├── Home
├── /services
│   ├── /service-1
│   ├── /service-2
│   └── ...
├── /locations
│   ├── /city-1
│   │   ├── /service-1-city-1
│   │   └── ...
│   ├── /city-2
│   └── ...
├── /about
├── /reviews
├── /gallery (or /portfolio)
├── /blog
├── /contact
├── /emergency (if applicable)
└── /faq
```

## 品質基準

### ロケーションページの上限

- ⚠️ ロケーションページが30件以上で**警告**
- 🛑 ロケーションページが50件以上で**強制停止**

### ユニークコンテンツの要件
| ページ種別 | 最低語数 | ユニーク率 |
|-----------|-----------|----------|
| 主要ロケーション | 600 | 60%以上 |
| サービスエリア | 500 | 40%以上 |
| サービスページ | 800 | 100% |

### ロケーションページをユニークにする要素
- 地域のランドマークや近隣エリア
- そのロケーションで提供される具体的なサービス
- 地域のチームメンバー
- ロケーション固有のお客様の声
- 地域コミュニティへの参加
- 地域特有の規制や考慮事項

## Schema の推奨設定

| ページ種別 | Schema タイプ |
|-----------|-------------|
| トップページ | LocalBusiness, Organization |
| サービスページ | Service, LocalBusiness |
| ロケーションページ | LocalBusiness (geo付き) |
| お問い合わせ | ContactPage, LocalBusiness |
| レビュー | LocalBusiness (AggregateRating付き) |

### LocalBusiness Schema の例
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "openingHours": "Mo-Fr 08:00-18:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.7128",
    "longitude": "-74.0060"
  },
  "areaServed": ["City 1", "City 2"],
  "priceRange": "$$"
}
```

## Google Business Profile の統合

- NAP（Name, Address, Phone）の一貫性を確保する
- サービスカテゴリを同期する
- 定期的に投稿を更新する
- 写真をアップロードする
- レビュー返信の戦略を策定する

### Google Business Profile の最新情報（2025-2026）

- **動画認証**が標準となり、ハガキ認証はほぼ廃止されました。ビジネスの所在地やサービスエリアを映す短い動画認証プロセスに備えてください。
- **WhatsApp連携**がGoogle Business Chat（廃止済み）に代わりました。WhatsAppをメインのメッセージングチャネルとして接続できます。
- **Q&AがGoogle Mapsから削除**され、AIが生成する回答に置き換わりました。Google AIがクエリに回答する際に使用するため、GBPの説明文、サービス内容、ウェブサイトのFAQを充実させてください。
- **営業時間がランキング要因トップ5に**——「検索時にビジネスが営業中」が初めてトップの個別要因にランクインしました（Whitespark 2026 Local Search Ranking Factors Report）。営業時間を正確に保ち、可能であれば営業時間の延長を検討してください。
- **レビューの「ストーリーズ」形式**——Google Mapsのモバイル版では、レビューの抜粋がスワイプ可能なストーリーズ形式で表示されるようになりました。写真付きの詳細で具体的なレビューを促してください。

### Service Area Business（SAB）の更新（2025年6月）

GoogleがSABのガイドラインを更新し、**州全体や国全体をサービスエリアとして設定することを禁止**しました。SABでは、市区町村、郵便番号、または地域名を指定する必要があります。都市圏全体にサービスを提供している場合は、州名ではなく、圏内の主要都市を個別にリストしてください。

### 地域ビジネスのAI検索における可視性

AI Overviewsはローカルキーワードの約0.14%にしか表示されません（2025年3月時点のデータ）。ローカルSEOは他の分野と比べてAIによる影響が大幅に少ない状況です。ただし、ChatGPTやPerplexityが地域のおすすめ情報として利用されるケースは増加しています。

AI検索でのローカル可視性を最適化するには：
- 専門家が選ぶ「ベスト〇〇」リストへの掲載を確保する（Whitespark 2026レポートでAI可視性要因の第1位）
- すべてのプラットフォームでNAP（Name, Address, Phone）の一貫性を維持する
- 真正なレビューの量と質を構築する
- LocalBusiness schemaを完全なプロパティ（geo, openingHours, priceRange, areaServed）で実装する

## コンテンツの優先順位

### 高優先度
1. サービスエリアを明確にしたトップページ
2. 主要サービスページ
3. 主要都市ページ
4. 全ロケーション情報を含むお問い合わせページ

### 中優先度
1. サービス×ロケーションの組み合わせページ
2. FAQページ
3. 会社概要・チーム紹介ページ
4. レビュー・お客様の声ページ

### ブログのトピック
- 季節ごとのメンテナンスのコツ
- ［サービス提供者］の選び方
- ［問題］の警告サイン
- DIYとプロへの依頼の比較
- 地域の規制や許認可について

## 追跡すべき主要指標

- ローカルパックの順位
- オーガニック経由の電話件数
- 経路案内リクエスト数
- Google Business Profile のインサイト
- レビュー数と評価

## ローカルビジネス向け Generative Engine Optimization（GEO）

- [ ] 明確で引用しやすいサービス説明と料金の目安を記載する
- [ ] LocalBusiness schemaにgeo、openingHours、areaServedを完全に設定する
- [ ] 厳選された「ベスト〇〇」リストやローカルディレクトリへの掲載を進める
- [ ] すべてのプラットフォーム（Google、Yelp、Apple Maps）でNAPの一貫性を維持する
- [ ] 施工実績、チーム、ロケーションのオリジナル写真を掲載する
- [ ] 地域サービスに関するよくある質問をFAQ形式で構造化する
- [ ] ChatGPTやPerplexityの地域おすすめ情報でのAI引用状況を監視する
