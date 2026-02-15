<!-- Updated: 2026-02-08 -->

![Claude SEO](screenshots/cover-image.jpeg)

# Claude SEO

Claude Code 向けの包括的なSEO分析スキル。技術的SEO、ページ内分析、コンテンツ品質（E-E-A-T）、schema マークアップ、画像最適化、sitemap アーキテクチャ、AI検索最適化（GEO）、戦略的プランニングをカバーします。

![SEO Command Demo](screenshots/seo-command-demo.gif)

[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## インストール

### ワンコマンドインストール (Unix/macOS/Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

### 手動インストール

```bash
git clone https://github.com/AgriciDaniel/claude-seo.git
cd claude-seo
./install.sh
```

### Windows

```powershell
irm https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.ps1 | iex
```

## クイックスタート

```bash
# Claude Code を起動
claude

# サイト全体の監査を実行
/seo audit https://example.com

# 単一ページを分析
/seo page https://example.com/about

# schema マークアップを確認
/seo schema https://example.com

# sitemap を生成
/seo sitemap generate

# AI検索向けに最適化
/seo geo https://example.com
```
### デモ:
[YouTube でフルデモを視聴](https://www.youtube.com/watch?v=COMnNlUakQk)

**`/seo audit` — 並列サブエージェントによるサイト全体監査:**

![SEO Audit Demo](screenshots/seo-audit-demo.gif)

## コマンド一覧

| コマンド | 説明 |
|---------|-------------|
| `/seo audit <url>` | 並列サブエージェント委任によるウェブサイト全体監査 |
| `/seo page <url>` | 単一ページの詳細分析 |
| `/seo sitemap <url>` | 既存のXML sitemap を分析 |
| `/seo sitemap generate` | 業種テンプレートを使用して新しい sitemap を生成 |
| `/seo schema <url>` | Schema.org マークアップの検出、検証、生成 |
| `/seo images <url>` | 画像最適化分析 |
| `/seo technical <url>` | 技術的SEO監査（8カテゴリ） |
| `/seo content <url>` | E-E-A-T およびコンテンツ品質分析 |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo plan <type>` | 戦略的SEOプランニング (saas, local, ecommerce, publisher, agency) |
| `/seo programmatic <url>` | プログラマティックSEO分析とプランニング |
| `/seo competitor-pages <url>` | 競合比較ページの生成 |
| `/seo hreflang <url>` | hreflang/i18n SEO監査と生成 |

### `/seo programmatic [url|plan]`
**プログラマティックSEO分析＆プランニング**

データソースから品質管理付きでSEOページを大規模に構築します。

**機能:**
- 既存のプログラマティックページの薄いコンテンツやカニバリゼーションを分析
- データ駆動型ページのURLパターンとテンプレート構造を計画
- 生成されたページ間の内部リンク自動化
- canonical 戦略とインデックス肥大化の防止
- 品質ゲート: 100ページ以上で警告、500ページ以上で監査なしの場合は強制停止

### `/seo competitor-pages [url|generate]`
**競合比較ページジェネレーター**

コンバージョン率の高い「X vs Y」や「Xの代替」ページを作成します。

**機能:**
- 機能マトリクス付きの構造化された比較テーブル
- AggregateRating 付きの Product schema マークアップ
- CTA配置を最適化したコンバージョン重視のレイアウト
- 比較意図クエリに対するキーワードターゲティング
- 正確な競合表現のための公正性ガイドライン

### `/seo hreflang [url]`
**hreflang / i18n SEO監査＆生成**

多言語サイトのhreflangタグを検証・生成します。

**機能:**
- hreflangタグの生成（HTML、HTTPヘッダー、またはXML sitemap）
- 自己参照タグ、リターンタグ、x-default の検証
- よくあるミスの検出（リターンタグの欠落、無効なコード、HTTP/HTTPSの不一致）
- クロスドメイン hreflang サポート
- 言語/地域コードの検証（ISO 639-1 + ISO 3166-1）

## 機能

### Core Web Vitals（現行指標）
- **LCP** (Largest Contentful Paint): 目標 < 2.5秒
- **INP** (Interaction to Next Paint): 目標 < 200ms
- **CLS** (Cumulative Layout Shift): 目標 < 0.1

> 注: INP は2024年3月12日にFIDに代わって導入されました。FIDは2024年9月9日にすべてのChromeツールから完全に削除されました。

### E-E-A-T 分析
2025年9月の品質評価ガイドラインに基づく更新:
- **Experience（経験）**: 実体験に基づく知識のシグナル
- **Expertise（専門性）**: 著者の資格と知識の深さ
- **Authoritativeness（権威性）**: 業界での認知度
- **Trustworthiness（信頼性）**: 連絡先情報、セキュリティ、透明性

### Schema マークアップ
- 検出: JSON-LD（推奨）、Microdata、RDFa
- Google がサポートするタイプに対する検証
- テンプレートによる生成
- 非推奨の認識:
  - HowTo: 非推奨（2023年9月）
  - FAQ: 政府/医療サイトに制限（2023年8月）
  - SpecialAnnouncement: 非推奨（2025年7月）

### AI検索最適化 (GEO)
2026年の新機能 - 以下に対する最適化:
- Google AI Overviews
- ChatGPT ウェブ検索
- Perplexity
- その他のAI搭載検索

### 品質ゲート
- 30以上のロケーションページで警告
- 50以上のロケーションページで強制停止
- ページタイプ別の薄いコンテンツ検出
- ドアウェイページの防止

## アーキテクチャ

```
~/.claude/skills/seo/         # メインスキル
~/.claude/skills/seo-*/       # サブスキル（全12個）
~/.claude/agents/seo-*.md     # サブエージェント（全6個）
```

### Video & Live Schema（新機能）
動画コンテンツ、ライブ配信、キーモーメント用の追加schemaタイプ:
- VideoObject — サムネイル、再生時間、アップロード日付を含む動画ページマークアップ
- BroadcastEvent — ライブ配信コンテンツ用のLIVEバッジサポート
- Clip — 動画内のキーモーメント/チャプター
- SeekToAction — 動画リッチリザルトでのシーク機能の有効化
- SoftwareSourceCode — オープンソースおよびコードリポジトリページ

すぐに使えるJSON-LDスニペットは `schema/templates.json` を参照してください。

### 最近の追加機能
- プログラマティックSEOスキル (`/seo programmatic`)
- 競合比較ページスキル (`/seo competitor-pages`)
- 多言語 hreflang 検証 (`/seo hreflang`)
- Video & Live schema タイプ (VideoObject, BroadcastEvent, Clip, SeekToAction)
- Google SEO クイックリファレンスガイド

## 要件

- Python 3.8+
- Claude Code CLI
- オプション: スクリーンショット用の Playwright

## アンインストール

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash
```

### MCP連携

MCPサーバーと連携してライブSEOデータを取得します。**Ahrefs** (`@ahrefs/mcp`) や **Semrush** の公式サーバー、および Google Search Console、PageSpeed Insights、DataForSEO のコミュニティサーバーに対応しています。セットアップについては [MCP連携ガイド](docs/MCP-INTEGRATION.md) を参照してください。

## ドキュメント

- [インストールガイド](docs/INSTALLATION.md)
- [コマンドリファレンス](docs/COMMANDS.md)
- [アーキテクチャ](docs/ARCHITECTURE.md)
- [MCP連携](docs/MCP-INTEGRATION.md)
- [トラブルシューティング](docs/TROUBLESHOOTING.md)

## ライセンス

MIT License - 詳細は [LICENSE](LICENSE) を参照してください。

## コントリビューション

コントリビューション歓迎！PRを提出する前に `docs/` 内のガイドラインをお読みください。

---

Claude Code 向けに [@AgriciDaniel](https://github.com/AgriciDaniel) が開発
