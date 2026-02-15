# 変更履歴

このプロジェクトに対するすべての重要な変更はこのファイルに記録されます。

このフォーマットは [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) に基づいており、
このプロジェクトは [Semantic Versioning](https://semver.org/spec/v2.0.0.html) に準拠しています。

## [1.1.0] - 2026-02-07

### セキュリティ (重大)
- **urllib3 ≥2.6.3**: CVE-2026-21441 (CVSS 8.9) を修正 - 解凍バイパスの脆弱性
- **lxml ≥6.0.2**: 追加の libxml2 セキュリティパッチのため 5.3.2 から更新
- **Pillow ≥12.1.0**: CVE-2025-48379 を修正
- **playwright ≥1.55.1**: CVE-2025-59288 (macOS) を修正
- **requests ≥2.32.4**: CVE-2024-47081、CVE-2024-35195 を修正

### 追加
- **GEO (Generative Engine Optimization) の大幅な機能強化**:
  - ブランド言及分析（AI の可視性においてバックリンクの3倍重要）
  - AI クローラー検出（GPTBot、OAI-SearchBot、ClaudeBot、PerplexityBot など）
  - llms.txt 標準の検出と推奨事項
  - RSL 1.0 (Really Simple Licensing) の検出
  - パッセージレベルの引用可能性スコアリング（最適範囲: 134〜167語）
  - プラットフォーム別の最適化（Google AI Overviews vs ChatGPT vs Perplexity）
  - AI クローラーのアクセシビリティに対するサーバーサイドレンダリングチェック
- **LCP Subparts 分析**: TTFB、リソース読み込み遅延、リソース読み込み時間、レンダリング遅延
- **Soft Navigations API の検出** - SPA における CWV 測定の制限事項の把握
- **Schema.org v29.4 の追加**: ConferenceEvent、PerformingArtsEvent、LoyaltyProgram
- **E-commerce schema の更新**: returnPolicyCountry が必須に変更、組織レベルのポリシー追加

### 変更
- **E-E-A-T フレームワーク**: 2025年12月コアアップデートに対応 - YMYL だけでなく、すべての競合性の高いクエリに適用されるように変更
- **SKILL.md の説明**: 新しい1024文字制限を活用するため拡充
- **Schema の非推奨項目を拡張**: ClaimReview、VehicleListing を追加（2025年6月）
- **WebApplication schema**: ブラウザベースの SaaS 向けの正しいタイプとして追加（SoftwareApplication との区別）

### 修正
- Schema-types.md にて SoftwareApplication（アプリ）と WebApplication（SaaS）の区別を正しく記載

---

## [1.0.0] - 2026-02-07

### 追加
- Claude SEO の初回リリース
- 9つの専門スキル: audit、page、sitemap、schema、images、technical、content、geo、plan
- 並列分析のための6つのサブエージェント: seo-technical、seo-content、seo-schema、seo-sitemap、seo-performance、seo-visual
- 業種別テンプレート: SaaS、ローカルサービス、E-commerce、パブリッシャー、エージェンシー、汎用
- 非推奨トラッキング付きの Schema ライブラリ:
  - HowTo schema を非推奨に指定（2023年9月）
  - FAQ schema を政府・医療サイトのみに制限（2023年8月）
  - SpecialAnnouncement schema を非推奨に指定（2025年7月31日）
- AI Overviews / GEO 最適化スキル (seo-geo) - 2026年の新機能
- 現行指標を使用した Core Web Vitals 分析:
  - LCP (Largest Contentful Paint): <2.5s
  - INP (Interaction to Next Paint): <200ms - 2024年3月12日に FID を置換
  - CLS (Cumulative Layout Shift): <0.1
- E-E-A-T フレームワークを2025年9月の品質評価ガイドラインに更新
- 低品質コンテンツおよびドアウェイページ防止のための品質ゲート:
  - 30以上のロケーションページで警告
  - 50以上のロケーションページで強制停止
- pre-commit および post-edit の自動化フック
- ワンコマンドによるインストール・アンインストールスクリプト（Unix および Windows）
- CVE を考慮した最小バージョン指定による Python 依存関係のピンニング（lxml >= 5.3.2）

### アーキテクチャ
- Anthropic 公式の Claude Code スキル仕様に準拠（2026年2月）
- 標準ディレクトリ構成: `scripts/`、`references/`、`assets/`
- 有効なフックマッチャー（ツール名のみ、引数パターンなし）
- 正しいサブエージェントのフロントマターフィールド（name、description、tools）
- CLI コマンドは `claude`（`claude-code` ではない）
