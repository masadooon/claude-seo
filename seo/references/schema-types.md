<!-- Updated: 2026-02-07 -->
# Schema.org タイプ — ステータスと推奨事項 (2026年2月)

**Schema.org バージョン:** 29.4 (2025年12月8日)

## フォーマットの推奨
常に **JSON-LD** (`<script type="application/ld+json">`) を使用してください。
Googleのドキュメントでは、MicrodataやRDFaよりもJSON-LDを明示的に推奨しています。

**AI検索に関する注記:** 適切なSchemaを持つコンテンツは、AI生成の回答に表示される可能性が約2.5倍高くなります（2025年3月にGoogleとMicrosoftが確認）。

---

## 有効 — 自由に推奨可能

| タイプ | ユースケース | 主要プロパティ |
|------|----------|----------------|
| Organization | 企業情報 | name, url, logo, contactPoint, sameAs |
| LocalBusiness | 実店舗ビジネス | name, address, telephone, openingHours, geo, priceRange |
| SoftwareApplication | デスクトップ/モバイルアプリ | name, operatingSystem, applicationCategory, offers, aggregateRating |
| WebApplication | ブラウザベースのSaaS | name, applicationCategory, offers, browserRequirements, featureList |
| Product | 物理的/デジタル製品 | name, image, description, sku, brand, offers, review |
| Offer | 価格設定 | price, priceCurrency, availability, url, validFrom |
| Service | サービスビジネス | name, provider, areaServed, description, offers |
| Article | ブログ記事、ニュース | headline, author, datePublished, dateModified, image, publisher |
| BlogPosting | ブログコンテンツ | Articleと同じ + ブログ固有のコンテキスト |
| NewsArticle | ニュースコンテンツ | Articleと同じ + ニュース固有のコンテキスト |
| Review | 個別レビュー | reviewRating, author, itemReviewed, reviewBody |
| AggregateRating | 評価の概要 | ratingValue, reviewCount, bestRating, worstRating |
| BreadcrumbList | ナビゲーション | itemListElement（position, name, itemを含む） |
| WebSite | サイトレベル | name, url, potentialAction（サイトリンク検索用のSearchAction） |
| WebPage | ページレベル | name, description, datePublished, dateModified |
| Person | 著者/チーム | name, jobTitle, url, sameAs, image, worksFor |
| ContactPage | お問い合わせページ | name, url |
| VideoObject | 動画コンテンツ | name, description, thumbnailUrl, uploadDate, duration, contentUrl |
| ImageObject | 画像コンテンツ | contentUrl, caption, creator, copyrightHolder |
| Event | イベント | name, startDate, endDate, location, organizer, offers |
| JobPosting | 求人情報 | title, description, datePosted, hiringOrganization, jobLocation |
| Course | 教育コンテンツ | name, description, provider, hasCourseInstance |
| DiscussionForumPosting | フォーラムスレッド | headline, author, datePublished, text, url |
| ProductGroup | バリエーション商品 | name, productGroupID, variesBy, hasVariant |
| ProfilePage | 著者/クリエイターのプロフィール | mainEntity (Person), name, url, description, sameAs |

---

## 制限付き — 特定のサイトタイプのみ対象

| タイプ | 制限事項 | 適用開始 |
|------|------------|-------|
| FAQPage | 政府および医療機関のサイトのみ | 2023年8月 |

> GoogleはFAQリッチリザルトを大幅に制限しました。現在、権威あるソース（政府、医療機関）のみがFAQリッチリザルトを受け取ります。商用サイトにはFAQPage Schemaを推奨しないでください。

---

## 非推奨 — 推奨しないこと

| タイプ | ステータス | 適用開始 | 備考 |
|------|--------|-------|-------|
| HowTo | リッチリザルト完全削除 | 2023年9月 | Googleがhow-toリッチリザルトの表示を停止 |
| SpecialAnnouncement | 非推奨 | 2025年7月31日 | COVID時代のSchema、処理されなくなった |
| CourseInfo | リッチリザルトから廃止 | 2025年6月 | Courseに統合 |
| EstimatedSalary | リッチリザルトから廃止 | 2025年6月 | 表示されなくなった |
| LearningVideo | リッチリザルトから廃止 | 2025年6月 | 代わりにVideoObjectを使用 |
| ClaimReview | リッチリザルトから廃止 | 2025年6月 | ファクトチェックマークアップはリッチリザルトを生成しなくなった |
| VehicleListing | リッチリザルトから廃止 | 2025年6月 | 車両リスティング構造化データの提供終了 |
| Book Actions | 非推奨後に撤回 | 2025年6月 | **2026年2月時点でも機能中** — 歴史的な記録のみ |
| Practice Problem | リッチリザルトから廃止 | 2025年後半 | 教育用練習問題が表示されなくなった |
| Dataset | リッチリザルトから廃止 | 2025年後半 | Dataset Search機能の提供終了 |

---

## 最近の追加 (2024-2026)

| タイプ/機能 | 追加時期 | 備考 |
|-------------|-------|-------|
| Product Certification マークアップ | 2025年4月 | エネルギー評価、安全認証。EnergyConsumptionDetailsの代替。 |
| ProductGroup | 2025年 | variesBy, hasVariantプロパティを持つECサイトの商品バリエーション |
| ProfilePage | 2025年 | E-E-A-TのためのmainEntity Personを持つ著者/クリエイターのプロフィールページ |
| DiscussionForumPosting | 2024年 | フォーラム/コミュニティコンテンツ向け |
| Speakable | 2024年更新 | 音声検索最適化向け |
| LoyaltyProgram | 2025年6月 | 会員価格、ロイヤルティカードの構造化データ |
| Organization レベルの配送/返品ポリシー | 2025年11月 | Merchant Centerなしで Search Console 経由で設定可能 |
| ConferenceEvent | 2025年12月 | Schema.org v29.4 で追加 |
| PerformingArtsEvent | 2025年12月 | Schema.org v29.4 で追加 |

## ECサイトの要件 (更新済み)

| 要件 | ステータス | 適用開始 |
|-------------|--------|-------|
| MerchantReturnPolicy の `returnPolicyCountry` | **必須** | 2025年3月 |
| Product バリエーション構造化データ | 拡張 | 2025年 — アパレル、化粧品、電子機器を含む |

> **注記:** Content API for Shoppingは2026年8月18日にサービス終了予定。Merchant APIへの移行が必要です。

---

## バリデーションチェックリスト

Schemaブロックについて、以下を確認してください:

1. `@context` が `"https://schema.org"` である（httpではない）
2. `@type` が有効かつ非推奨でないタイプである
3. すべての必須プロパティが存在する
4. プロパティの値が期待されるデータ型と一致する
5. プレースホルダーテキスト（例: "[Business Name]"）が含まれていない
6. URLが相対パスではなく絶対パスである
7. 日付がISO 8601形式である
8. 画像に有効なURLが設定されている

## テストツール

- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
