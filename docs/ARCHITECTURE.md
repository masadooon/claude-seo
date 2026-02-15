# アーキテクチャ

## 概要

Claude SEO は Anthropic 公式の Claude Code skill 仕様に準拠し、モジュール式のマルチスキルアーキテクチャを採用しています。

## ディレクトリ構造

```
~/.claude/
├── skills/
│   ├── seo/              # メインオーケストレータースキル
│   │   ├── SKILL.md          # ルーティングロジックを含むエントリーポイント
│   │   └── references/       # オンデマンドで読み込まれるリファレンスファイル
│   │       ├── cwv-thresholds.md
│   │       ├── schema-types.md
│   │       ├── eeat-framework.md
│   │       └── quality-gates.md
│   │
│   ├── seo-audit/            # サイト全体の監査
│   ├── seo-competitor-pages/ # 競合比較ページ
│   ├── seo-content/          # E-E-A-T 分析
│   ├── seo-geo/              # AI 検索最適化
│   ├── seo-hreflang/         # Hreflang/i18n SEO
│   ├── seo-images/           # 画像最適化
│   ├── seo-page/             # 単一ページ分析
│   ├── seo-plan/             # 戦略プランニング
│   │   └── assets/           # 業種別テンプレート
│   ├── seo-programmatic/     # Programmatic SEO
│   ├── seo-schema/           # Schema マークアップ
│   ├── seo-sitemap/          # Sitemap 分析・生成
│   └── seo-technical/        # Technical SEO
│
└── agents/
    ├── seo-technical.md      # Technical SEO スペシャリスト
    ├── seo-content.md        # コンテンツ品質レビュアー
    ├── seo-schema.md         # Schema マークアップエキスパート
    ├── seo-sitemap.md        # Sitemap アーキテクト
    ├── seo-performance.md    # パフォーマンスアナライザー
    └── seo-visual.md         # ビジュアルアナライザー
```

## コンポーネントの種類

### Skills

Skills は YAML frontmatter を持つ Markdown ファイルで、機能と手順を定義します。

**SKILL.md の形式:**
```yaml
---
name: skill-name
description: >
  When to use this skill. Include activation keywords
  and concrete use cases.
---

# Skill Title

Instructions and documentation...
```

### Subagents

Subagents はタスクを委任できる専門的なワーカーです。独自のコンテキストとツールを持ちます。

**Agent の形式:**
```yaml
---
name: agent-name
description: What this agent does.
tools: Read, Bash, Write, Glob, Grep
---

Instructions for the agent...
```

### リファレンスファイル

リファレンスファイルは、メインスキルの肥大化を防ぐためにオンデマンドで読み込まれる静的データを含みます。

## オーケストレーションフロー

### フル監査 (`/seo audit`)

```
User Request
    │
    ▼
┌─────────────────┐
│   seo       │  ← メインオーケストレーター
│   (SKILL.md)    │
└────────┬────────┘
         │
         │  ビジネスタイプを検出
         │  Subagents を並列で起動
         │
    ┌────┴────┬────────┬────────┬────────┬────────┐
    ▼         ▼        ▼        ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│tech   │ │content│ │schema │ │sitemap│ │perf   │ │visual │
│agent  │ │agent  │ │agent  │ │agent  │ │agent  │ │agent  │
└───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
    │         │        │        │        │        │
    └─────────┴────────┴────┬───┴────────┴────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  結果の       │
                    │  集約         │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  レポートの   │
                    │  生成         │
                    └───────────────┘
```

### 個別コマンド

```
User Request (e.g., /seo page)
    │
    ▼
┌─────────────────┐
│   seo       │  ← サブスキルへルーティング
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   seo-page      │  ← サブスキルが直接処理
│   (SKILL.md)    │
└─────────────────┘
```

## 設計原則

### 1. 段階的開示

- メインの SKILL.md は簡潔に保つ（200行未満）
- リファレンスファイルはオンデマンドで読み込み
- 詳細な手順はサブスキルに記載

### 2. 並列処理

- 監査時に Subagents が並行して実行される
- 独立した分析は互いをブロックしない
- すべて完了後に結果を集約

### 3. Quality Gates

- 不適切な推奨を防ぐ組み込みの閾値
- ロケーションページの制限（30件で警告、50件でハードストップ）
- Schema の非推奨への対応
- FID から INP への置き換えを強制

### 4. 業種対応

- さまざまなビジネスタイプ向けのテンプレート
- ホームページのシグナルからの自動検出
- 業種ごとにカスタマイズされた推奨事項

## ファイル命名規則

| 種類 | パターン | 例 |
|------|---------|---------|
| Skill | `seo-{name}/SKILL.md` | `seo-audit/SKILL.md` |
| Agent | `seo-{name}.md` | `seo-technical.md` |
| Reference | `{topic}.md` | `cwv-thresholds.md` |
| Script | `{action}_{target}.py` | `fetch_page.py` |
| Template | `{industry}.md` | `saas.md` |

## 拡張ポイント

### 新しいサブスキルの追加

1. `skills/seo-newskill/SKILL.md` を作成
2. name と description を含む YAML frontmatter を追加
3. スキルの手順を記述
4. メインの `seo/SKILL.md` に新しいスキルへのルーティングを追加

### 新しい Subagent の追加

1. `agents/seo-newagent.md` を作成
2. name、description、tools を含む YAML frontmatter を追加
3. エージェントの手順を記述
4. 関連するスキルから参照

### 新しいリファレンスファイルの追加

1. 適切な `references/` ディレクトリにファイルを作成
2. スキル内でオンデマンド読み込みの指示とともに参照
