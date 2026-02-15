# インストールガイド

## 前提条件

- **Python 3.8+** （pip を含む）
- **Git** （リポジトリのクローンに使用）
- **Claude Code CLI** がインストール・設定済みであること

任意:
- **Playwright** （スクリーンショット機能に使用）

## クイックインストール

### Unix/macOS/Linux

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.ps1 | iex
```

## 手動インストール

1. **リポジトリをクローンする**

```bash
git clone https://github.com/AgriciDaniel/claude-seo.git
cd claude-seo
```

2. **インストーラーを実行する**

```bash
./install.sh
```

3. **Python の依存パッケージをインストールする**（自動でインストールされなかった場合）

```bash
pip install -r requirements.txt
```

4. **Playwright のブラウザをインストールする**（任意、スクリーンショット機能に必要）

```bash
pip install playwright
playwright install chromium
```

## インストール先のパス

インストーラーは以下の場所にファイルをコピーします:

| コンポーネント | パス |
|-----------|------|
| メインスキル | `~/.claude/skills/seo/` |
| サブスキル | `~/.claude/skills/seo-*/` |
| サブエージェント | `~/.claude/agents/seo-*.md` |

## インストールの確認

1. Claude Code を起動します:

```bash
claude
```

2. スキルが読み込まれていることを確認します:

```
/seo
```

ヘルプメッセージまたは URL の入力を求めるプロンプトが表示されるはずです。

## アンインストール

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash
```

または手動で行う場合:

```bash
rm -rf ~/.claude/skills/seo
rm -rf ~/.claude/skills/seo-audit
rm -rf ~/.claude/skills/seo-competitor-pages
rm -rf ~/.claude/skills/seo-content
rm -rf ~/.claude/skills/seo-geo
rm -rf ~/.claude/skills/seo-hreflang
rm -rf ~/.claude/skills/seo-images
rm -rf ~/.claude/skills/seo-page
rm -rf ~/.claude/skills/seo-plan
rm -rf ~/.claude/skills/seo-programmatic
rm -rf ~/.claude/skills/seo-schema
rm -rf ~/.claude/skills/seo-sitemap
rm -rf ~/.claude/skills/seo-technical
rm -f ~/.claude/agents/seo-*.md
```

## アップグレード

最新バージョンにアップグレードするには:

```bash
# 現在のバージョンをアンインストール
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash

# 新しいバージョンをインストール
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

## トラブルシューティング

### 「Skill not found」エラー

スキルが正しい場所にインストールされていることを確認してください:

```bash
ls ~/.claude/skills/seo/SKILL.md
```

ファイルが存在しない場合は、インストーラーを再実行してください。

### Python の依存パッケージに関するエラー

依存パッケージを手動でインストールしてください:

```bash
pip install beautifulsoup4 requests lxml playwright Pillow urllib3 validators
```

### Playwright のスクリーンショットに関するエラー

Chromium ブラウザをインストールしてください:

```bash
playwright install chromium
```

### Unix でのパーミッションエラー

スクリプトに実行権限が付与されていることを確認してください:

```bash
chmod +x ~/.claude/skills/seo/scripts/*.py
chmod +x ~/.claude/skills/seo/hooks/*.py
chmod +x ~/.claude/skills/seo/hooks/*.sh
```
