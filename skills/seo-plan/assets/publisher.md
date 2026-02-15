<!-- Updated: 2026-02-07 -->
# パブリッシャー/メディア SEO戦略テンプレート

## 業界の特徴

- コンテンツ量が多い
- 速報性の高いコンテンツ（ニュース）
- 広告収益がトラフィックに依存
- 権威性と信頼性が重要
- ソーシャルプラットフォームとの競合
- AI Overviewsによるトラフィックへの影響

## 推奨サイト構造

```
/
├── Home
├── /news (or /latest)
├── /topics
│   ├── /topic-1
│   ├── /topic-2
│   └── ...
├── /authors
│   ├── /author-1
│   └── ...
├── /opinion
├── /reviews
├── /guides
├── /videos
├── /podcasts
├── /newsletter
├── /about
│   ├── /editorial-policy
│   ├── /corrections
│   └── /contact
└── /[year]/[month]/[slug] (記事URL)
```

## schema推奨設定

| ページタイプ | schema タイプ |
|-----------|-------------|
| 記事 | NewsArticle or Article, Person (著者), Organization (発行者) |
| 著者ページ | Person, ProfilePage |
| トピックページ | CollectionPage, ItemList |
| ホームページ | WebSite, Organization |
| 動画 | VideoObject |
| ポッドキャスト | PodcastEpisode, PodcastSeries |

### NewsArticle schema の例
```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Article Headline",
  "datePublished": "2026-02-07T10:00:00Z",
  "dateModified": "2026-02-07T14:30:00Z",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/authors/author-name"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Publication Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "image": ["https://example.com/article-image.jpg"],
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/article-url"
  }
}
```

## E-E-A-T 要件

パブリッシャーは最も厳しい E-E-A-T の審査を受けます。

### 著者ページに必須の情報
- フルネームと写真
- 経歴と資格
- 専門分野
- 連絡先情報
- ソーシャルプロフィール（sameAs）
- その著者による過去の記事

### 編集基準
- 明確な訂正ポリシー
- 透明性のある編集プロセス
- ファクトチェックの手順
- 利益相反の開示

## コンテンツの優先順位

### 高優先度
1. 速報ニュース（速度が重要）
2. コアトピックに関するエバーグリーンガイド
3. 資格情報を含む著者ページ
4. トピックハブ/ピラーページ

### 中優先度
1. 意見・分析記事
2. 動画コンテンツ
3. インタラクティブコンテンツ
4. ニュースレターのランディングページ

### GEO に関する考慮事項
- 記事内に明確で引用しやすい事実を記載する
- データが多いコンテンツにはテーブルを使用する
- 出典付きの専門家の引用を含める
- 更新日を目立つ位置に表示する
- 構造化された見出し（H2/H3）を使用する
- ファーストパーティデータとオリジナルリサーチはAIシステムに頻繁に引用される
- Person schema + sameAs リンクで著者エンティティを明確に定義する
- Google AI Overviews、AI Mode、ChatGPT、Perplexity におけるAI引用頻度を監視する
- AI引用をオーガニックトラフィックと並ぶ独立したKPIとして扱う

### パブリッシャーSEOの最新情報（2025-2026）

- **Google News の自動掲載:** Google News はもはや手動申請を受け付けていません（2025年3月以降）。掲載は Google のコンテンツ品質基準に基づき完全に自動化されています。Google News sitemap マークアップと、一貫した高品質な公開頻度に注力してください。
- **KPIの変化:** トラフィックベースのKPI（セッション数、ページビュー数）は、AI Overviewsによるクリック率の低下に伴い、重要性が低下しています。先進的なパブリッシャーは以下に移行しています：購読者コンバージョン、ページ滞在時間、スクロール深度、ニュースレター登録数、AI引用頻度、訪問者あたりの収益。
- **サイトレピュテーション悪用のリスク:** 自社ドメイン配下にサードパーティコンテンツ（クーポン、製品レビュー、アフィリエイトコンテンツ）をホスティングしているパブリッシャーは高リスクです。Google は2024年後半にForbes、WSJ、Time、CNNをこの理由でペナルティを課しました。サードパーティコンテンツをホスティングする場合は、強力な編集監督と明確なファーストパーティの関与を確保してください。

## 技術的な考慮事項

### Core Web Vitals
- 広告配置がCLSに影響する
- ファーストビュー以下の広告と画像を遅延読み込みする
- ヒーロー画像をLCP向けに最適化する
- レンダリングブロッキングリソースを最小化する

### AMP（使用している場合）
- AMPの廃止を検討する（トップストーリーへの掲載に不要になった）
- canonical の設定が正しいことを確認する
- 非AMPとのパフォーマンスを比較監視する

### ページネーション
- 複数ページ記事には適切なページネーションを実装する
- または適切なインデックス設定を行った無限スクロールを使用する
- canonical は1ページ目または全文記事に設定する

## 追跡すべき主要指標

- オーガニック経由のページビュー数
- ページ滞在時間
- セッションあたりのページ数
- オーガニック経由のニュースレター登録数
- Google News/Discover からのトラフィック
- AI Overviewsへの表示回数
