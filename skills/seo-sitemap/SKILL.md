---
name: seo-sitemap
description: >
  既存のXML sitemapを分析、または業界テンプレートを使用して新規sitemapを生成します。
  フォーマット、URL、構造を検証します。ユーザーが「sitemap」「sitemapを生成」
  「sitemapの問題」「XML sitemap」と言った場合に使用してください。
---

# Sitemap 分析・生成

## モード1: 既存のSitemapを分析

### 検証チェック項目
- 有効なXMLフォーマット
- 1ファイルあたりのURL数が50,000件未満（プロトコル上の制限）
- すべてのURLがHTTP 200を返す
- `<lastmod>` の日付が正確である（すべて同一でない）
- 非推奨タグがない: `<priority>` と `<changefreq>` はGoogleに無視される
- robots.txtでsitemapが参照されている
- クロール済みページとsitemapを比較 — 欠落ページをフラグ付け

### 品質シグナル
- 50k超のURLがある場合はsitemap indexファイルを使用
- コンテンツタイプ別に分割（ページ、投稿、画像、動画）
- sitemapにcanonicalでないURLが含まれていない
- sitemapにnoindexのURLが含まれていない
- sitemapにリダイレクトされるURLが含まれていない
- HTTPSのURLのみ（HTTPは不可）

### よくある問題
| 問題 | 重大度 | 修正方法 |
|------|--------|----------|
| 1ファイルに50k超のURL | Critical | sitemap indexで分割する |
| 200以外のステータスのURL | High | 壊れたURLを削除または修正する |
| noindexのURLが含まれている | High | sitemapから削除する |
| リダイレクトされるURLが含まれている | Medium | 最終URLに更新する |
| lastmodがすべて同一 | Low | 実際の更新日を使用する |
| priority/changefreqが使用されている | Info | 削除可能（Googleに無視される） |

## モード2: 新規Sitemapを生成

### プロセス
1. ビジネスの種類を確認（または既存サイトから自動検出）
2. `assets/` ディレクトリから業界テンプレートを読み込む
3. ユーザーとインタラクティブに構造を計画
4. 品質ゲートを適用:
   - ⚠️ 警告: 30件以上のロケーションページ（60%以上のユニークコンテンツが必要）
   - 🛑 強制停止: 50件以上のロケーションページ（正当な理由が必要）
5. 有効なXML出力を生成
6. 50k URLでsitemap indexに分割
7. STRUCTURE.md ドキュメントを生成

### 大規模展開が安全なプログラマティックページ
✅ インテグレーションページ（実際のセットアップドキュメント付き）
✅ テンプレート/ツールページ（ダウンロード可能なコンテンツ付き）
✅ 用語集ページ（200語以上の定義）
✅ 商品ページ（固有のスペック、レビュー付き）
✅ ユーザープロフィールページ（ユーザー生成コンテンツ）

### ペナルティリスク（大規模展開は避ける）
❌ 都市名のみを入れ替えたロケーションページ
❌ 業界固有の価値がない「[業界]向けベスト[ツール]」ページ
❌ 実際の比較データがない「[競合]の代替」ページ
❌ 人間のレビューと固有の価値がないAI生成ページ

## Sitemapフォーマット

### 標準Sitemap
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/page</loc>
    <lastmod>2026-02-07</lastmod>
  </url>
</urlset>
```

### Sitemap Index（50k超のURL向け）
```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap-pages.xml</loc>
    <lastmod>2026-02-07</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-posts.xml</loc>
    <lastmod>2026-02-07</lastmod>
  </sitemap>
</sitemapindex>
```

## 出力

### 分析の場合
- `VALIDATION-REPORT.md` — 分析結果
- 重大度付きの問題リスト
- 改善提案

### 生成の場合
- `sitemap.xml`（または分割ファイルとindex）
- `STRUCTURE.md` — サイト構造ドキュメント
- URL数と構成のサマリー
