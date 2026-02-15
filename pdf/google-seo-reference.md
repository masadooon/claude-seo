<!-- Updated: 2026-02-07 -->
# Google SEO クイックリファレンス (2026年2月)

サブエージェント向けの簡潔なリファレンスガイド。Google Search の主要な概念、
要件、ベストプラクティスをまとめたもの。Google の公式ドキュメントの複製ではなく、
詳細については末尾の公式ドキュメントリンクを参照してください。

---

## Google Search の仕組み

Google Search は3つの段階で動作します: **Crawling**(Googlebot がリンクをたどり、sitemap を読み取ることでページを発見する)、**Indexing**(Google がページのコンテンツ、メタデータ、シグナルを処理し、検索インデックスに保存する)、**Serving**(ユーザーが検索すると、Google のアルゴリズムがインデックスされたページを関連性、品質、ユーザビリティに基づいてランク付けし、最も有用な結果を返す)。検索結果に表示されるためには、ページがクロール可能かつインデックス可能である必要があります。

---

## Google Search Essentials

旧称「Webmaster Guidelines」。主な要件:

### 技術的要件
- ページが Googlebot からアクセス可能であること(robots.txt や noindex でブロックされていないこと)
- インデックス対象のコンテンツは HTTP 200 ステータスを返すこと
- コンテンツは Google が処理可能な形式であること(HTML 推奨、JS レンダリングコンテンツもサポートされるが処理が遅い)
- ページは HTTPS で配信されること

### Spam Policies
- Cloaking の禁止(Googlebot とユーザーに異なるコンテンツを表示すること)
- Doorway pages の禁止(特定のクエリでランク付けするためだけに作成されたページ)
- 隠しテキストや隠しリンクの禁止
- Keyword stuffing の禁止
- Link spam の禁止(リンクの購入、過度なリンク交換)
- 付加価値のないスクレイピングコンテンツや自動生成コンテンツの禁止
- 不正なリダイレクトの禁止
- 内容の薄いアフィリエイトページの禁止

### 主なベストプラクティス
- 検索エンジンではなく、ユーザーのためにコンテンツを作成する
- 明確な階層構造でサイトをナビゲートしやすくする
- ページごとに説明的でユニークなタイトルと meta description を使用する
- 見出しタグ(H1-H6)を使用してコンテンツを論理的に構造化する
- alt テキストと適切なファイルサイズで画像を最適化する
- モバイルフレンドリーなレスポンシブデザインを確保する
- ページの読み込み速度を改善する(Core Web Vitals)
- XML sitemap を Google Search Console に送信する
- Structured Data(JSON-LD)を使用して Google がコンテンツを理解できるようにする

---

## コンテンツ品質シグナル

Google は E-E-A-T フレームワークを通じてコンテンツの品質を評価します:

- **Experience(経験)**: コンテンツ作成者はそのトピックについて実体験を持っているか?(オリジナル写真、個人的な体験談、実際の使用実績)
- **Expertise(専門性)**: 作成者は関連する知識や資格を持っているか?(専門的な経歴、技術的な深さ、正確な情報源)
- **Authoritativeness(権威性)**: 作成者やサイトはその分野の信頼できる情報源として認められているか?(業界での引用、ブランドへの言及、専門家としての評価)
- **Trustworthiness(信頼性)**: コンテンツとサイトは信頼でき、透明性があるか?(連絡先情報、安全なサイト、編集基準、正確な主張)

> **YMYL に関する注記**: 「Your Money or Your Life」トピック(健康、金融、安全、法律)には、最も高い E-E-A-T 基準が適用されます。不正確な YMYL コンテンツは現実世界に害を及ぼす可能性があるため、Google はより厳格な品質基準を適用します。

> **2025年12月アップデート**: E-E-A-T の評価が YMYL トピックだけでなく、すべての競合クエリに拡大されました。ランキングを競うすべてのページがこれらのシグナルで評価されます。

---

## Core Web Vitals

実際のユーザーデータ(フィールドデータ)の75パーセンタイルで測定されます。

| 指標 | 良好 | 改善が必要 | 不良 |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5s – 4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200ms – 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1 – 0.25 | > 0.25 |

**重要事項:**
- INP は2024年3月12日に FID (First Input Delay) を置き換えました。FID は2024年9月9日にすべての Chrome ツール(CrUX API、PageSpeed Insights、Lighthouse)から完全に削除されました。FID を参照しないでください。
- Core Web Vitals は確定的なランキングシグナルです(2021年6月以降)
- 評価にはラボデータ(Lighthouse)よりもフィールドデータ(CrUX)が優先されます
- 3つの指標すべてで「良好」を達成することが目標です

**測定ツール:**
- Google PageSpeed Insights (フィールドデータ + ラボデータ)
- Chrome User Experience Report (CrUX) — フィールドデータ
- Lighthouse (ラボデータのみ)
- Google Search Console Core Web Vitals レポート

---

## Structured Data のベストプラクティス

- **JSON-LD が Google の推奨形式です**(Microdata や RDFa よりも優先)
- JSON-LD は `<script type="application/ld+json">` タグ内に `<head>` または `<body>` に配置する
- 常に `@context` と `@type` プロパティを含める
- **必須プロパティ**は Rich Results の対象となるために存在する必要がある
- **推奨プロパティ**は Rich Results の品質を向上させるが、必須ではない
- ページ上に表示されているコンテンツのみをマークアップする
- デプロイ前に Google の Rich Results Test で検証する
- ユーザーに対して誤解を招くコンテンツや非表示のコンテンツをマークアップしない
- Schema を最新の状態に保つ — ページコンテンツの変更時に更新する

### 廃止・制限された型 (2026年2月時点)
- **HowTo**: Rich Results が削除されました(2023年9月)
- **FAQ**: 政府機関および医療機関のサイトに制限されました(2023年8月)
- **SpecialAnnouncement**: 廃止されました(2025年7月31日)
- **CourseInfo, EstimatedSalary, LearningVideo**: 廃止されました(2025年6月)
- **ClaimReview**: 廃止されました(2025年6月)
- **VehicleListing**: 廃止されました(2025年6月)

---

## 一般的なペナルティと回避方法

### Manual Actions
Google Search Console での違反通知。一般的な原因:
- **不自然なリンク**(リンクの売買): 不正なリンクを Disavow し、再審査リクエストを送信する
- **内容の薄いコンテンツ**: 影響を受けたページに実質的な独自の価値を追加する
- **Cloaking/不正なリダイレクト**: 欺瞞的な配信を削除し、再審査リクエストを送信する
- **ユーザー生成スパム**: コメント/フォーラムをモデレートし、ユーザーリンクに nofollow を追加する
- **Structured Data の問題**: 誤解を招くマークアップやスパムマークアップを修正する

### アルゴリズムによる降格
手動通知なし — ランキングの低下によって検出されます。一般的な原因:
- **Helpful Content System**: 2024年3月に Google の Core Ranking に統合され、独立したシステムではなくなりました。有用性シグナルは、すべての Core Update 内で評価されるようになりました。大量の低品質な AI 生成コンテンツや有用でないコンテンツは、Core Update を通じて依然として降格の対象となります。
- **Core Updates**: すべてのシグナルにわたる包括的な品質再評価
- **Spam Updates**: スパムパターンの自動検出
- **Link Spam Updates**: 操作的なリンクパターンの価値低下

### 回復手順
1. 問題を特定する(Search Console、ランキングのタイムライン分析)
2. 根本原因を修正する(スパムの除去、コンテンツの改善、リンクのクリーンアップ)
3. Manual Actions の場合: Search Console から再審査リクエストを送信する
4. アルゴリズムの場合: 品質を改善し、次の Core Update での再評価を待つ
5. Search Console のパフォーマンスレポートで回復を監視する

---

## 公式ドキュメントリンク

- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [How Google Search Works](https://developers.google.com/search/docs/fundamentals/how-search-works)
- [Structured Data Overview](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Rich Results Test](https://search.google.com/test/rich-results)
- [Core Web Vitals Report](https://support.google.com/webmasters/answer/9205520)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Search Console Help](https://support.google.com/webmasters)
- [Manual Actions Report](https://support.google.com/webmasters/answer/9044175)
- [Google Search Status Dashboard](https://status.search.google.com/)
- [Google Search Central Blog](https://developers.google.com/search/blog)
- [Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [E-E-A-T and Quality Rater Guidelines](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

> **Mobile-first indexing** は2024年7月5日に100%完了しました。Google は現在、すべてのウェブサイトをモバイル版の Googlebot ユーザーエージェントのみでクロールおよびインデックスしています。
