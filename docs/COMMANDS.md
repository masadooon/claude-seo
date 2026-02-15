# コマンドリファレンス

## 概要

Claude SEO のすべてのコマンドは `/seo` に続けてサブコマンドを指定します。

## コマンド一覧

### `/seo audit <url>`

並列分析によるウェブサイトの総合 SEO 監査。

**例:**
```
/seo audit https://example.com
```

**実行内容:**
1. 最大500ページをクロール
2. ビジネスタイプを検出
3. 6つの専門サブエージェントに並列で委任
4. SEO Health Score (0-100) を生成
5. 優先順位付きアクションプランを作成

**出力:**
- `FULL-AUDIT-REPORT.md`
- `ACTION-PLAN.md`
- `screenshots/` (Playwright が利用可能な場合)

---

### `/seo page <url>`

単一ページの詳細分析。

**例:**
```
/seo page https://example.com/about
```

**分析内容:**
- On-page SEO (title、meta、headings、URLs)
- コンテンツ品質 (文字数、可読性、E-E-A-T)
- 技術要素 (canonical、robots、Open Graph)
- Schema markup
- 画像 (alt text、サイズ、フォーマット)
- Core Web Vitals の潜在的な問題

---

### `/seo technical <url>`

8カテゴリにわたる Technical SEO 監査。

**例:**
```
/seo technical https://example.com
```

**カテゴリ:**
1. Crawlability
2. Indexability
3. Security
4. URL Structure
5. Mobile Optimization
6. Core Web Vitals (LCP, INP, CLS)
7. Structured Data
8. JavaScript Rendering

---

### `/seo content <url>`

E-E-A-T およびコンテンツ品質の分析。

**例:**
```
/seo content https://example.com/blog/post
```

**評価内容:**
- Experience シグナル (一次体験に基づく知識)
- Expertise (著者の資格・専門性)
- Authoritativeness (外部からの評価)
- Trustworthiness (透明性、セキュリティ)
- AI 引用への対応度
- コンテンツの鮮度

---

### `/seo schema <url>`

Schema markup の検出、検証、および生成。

**例:**
```
/seo schema https://example.com
```

**実行内容:**
- 既存の schema を検出 (JSON-LD, Microdata, RDFa)
- Google の要件に照らして検証
- 不足している機会を特定
- すぐに使える JSON-LD を生成

---

### `/seo geo <url>`

AI Overviews / Generative Engine Optimization。

**例:**
```
/seo geo https://example.com/blog/guide
```

**分析内容:**
- Citability score (引用可能な事実、統計データ)
- 構造的な可読性 (見出し、リスト、テーブル)
- Entity の明確性 (定義、コンテキスト)
- Authority シグナル (資格、出典)
- Structured Data のサポート状況

---

### `/seo images <url>`

画像最適化の分析。

**例:**
```
/seo images https://example.com
```

**チェック内容:**
- Alt text の有無と品質
- ファイルサイズ (200KB超をフラグ)
- フォーマット (WebP/AVIF の推奨)
- レスポンシブ画像 (srcset, sizes)
- Lazy loading
- CLS の防止 (dimensions)

---

### `/seo sitemap <url>`

既存の XML sitemap の分析。

**例:**
```
/seo sitemap https://example.com/sitemap.xml
```

**検証内容:**
- XML フォーマット
- URL 数 (ファイルあたり50,000件未満)
- URL のステータスコード
- lastmod の正確性
- 非推奨タグ (priority, changefreq)
- クロール済みページに対するカバレッジ

---

### `/seo sitemap generate`

業種テンプレートを使用した新規 sitemap の生成。

**例:**
```
/seo sitemap generate
```

**プロセス:**
1. ビジネスタイプを選択または自動検出
2. インタラクティブな構造設計
3. 品質ゲートの適用 (30/50 ロケーションページ制限)
4. 有効な XML を生成
5. ドキュメントを作成

---

### `/seo plan <type>`

戦略的 SEO プランニング。

**タイプ:** `saas`, `local`, `ecommerce`, `publisher`, `agency`

**例:**
```
/seo plan saas
```

**作成内容:**
- 包括的な SEO 戦略
- 競合分析
- コンテンツカレンダー
- 実装ロードマップ (4フェーズ)
- サイトアーキテクチャ設計

---

### `/seo competitor-pages [url|generate]`

競合比較ページの生成。

**例:**
```
/seo competitor-pages https://example.com/vs/competitor
/seo competitor-pages generate
```

**機能:**
- 「X vs Y」比較ページレイアウトの生成
- 「X の代替サービス」ページ構造の作成
- スコアリング付き機能比較マトリクスの構築
- Product + AggregateRating の schema markup 生成
- コンバージョン最適化された CTA 配置の適用
- 公平性ガイドラインの遵守 (正確なデータ、出典の明記)

---

### `/seo hreflang [url]`

Hreflang および国際 SEO の監査と生成。

**例:**
```
/seo hreflang https://example.com
```

**機能:**
- 自己参照 hreflang タグの検証
- リターンタグの相互参照チェック (A→B には B→A が必要)
- x-default タグの存在確認
- ISO 639-1 言語コードと ISO 3166-1 地域コードの検証
- canonical URL と hreflang の整合性チェック
- プロトコルの不一致検出 (HTTP vs HTTPS)
- 正しい hreflang link タグと sitemap XML の生成

---

### `/seo programmatic [url|plan]`

大規模生成ページ向けの Programmatic SEO 分析とプランニング。

**例:**
```
/seo programmatic https://example.com/tools/
/seo programmatic plan
```

**機能:**
- データソース品質の評価 (CSV, JSON, API, database)
- ページごとにユニークなコンテンツを持つテンプレートエンジンの設計
- URL パターン戦略の設計 (`/tools/[tool-name]`, `/[city]/[service]`)
- 内部リンクの自動化 (hub/spoke、関連アイテム、breadcrumbs)
- 低品質コンテンツ防止策の適用 (品質ゲート、文字数閾値)
- Index bloat の防止 (低価値ページの noindex、pagination、faceted nav)

---

## クイックリファレンス

| コマンド | 用途 |
|---------|----------|
| `/seo audit <url>` | ウェブサイト総合監査 |
| `/seo competitor-pages [url\|generate]` | 競合比較ページ |
| `/seo content <url>` | E-E-A-T 分析 |
| `/seo geo <url>` | AI 検索最適化 |
| `/seo hreflang [url]` | Hreflang/i18n SEO 監査 |
| `/seo images <url>` | 画像最適化 |
| `/seo page <url>` | 単一ページ分析 |
| `/seo plan <type>` | 戦略的プランニング |
| `/seo programmatic [url\|plan]` | Programmatic SEO 分析 |
| `/seo schema <url>` | Schema 検証 |
| `/seo sitemap <url>` | Sitemap 検証 |
| `/seo sitemap generate` | 新規 sitemap 作成 |
| `/seo technical <url>` | Technical SEO チェック |
