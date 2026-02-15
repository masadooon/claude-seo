# トラブルシューティング

## よくある問題

### Skill が読み込まれない

**症状:** `/seo` コマンドが認識されない

**解決方法:**

1. インストールを確認する:
```bash
ls ~/.claude/skills/seo/SKILL.md
```

2. SKILL.md に正しい frontmatter があるか確認する:
```bash
head -5 ~/.claude/skills/seo/SKILL.md
```
`---` で始まり、その後に YAML が続いている必要があります。

3. Claude Code を再起動する:
```bash
claude
```

4. インストーラーを再実行する:
```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

---

### Python 依存関係のエラー

**症状:** `ModuleNotFoundError: No module named 'requests'`

**解決方法:**
```bash
pip install -r ~/.claude/skills/seo/requirements.txt
```

または個別にインストールする:
```bash
pip install beautifulsoup4 requests lxml playwright Pillow urllib3 validators
```

---

### Playwright スクリーンショットのエラー

**症状:** `playwright._impl._errors.Error: Executable doesn't exist`

**解決方法:**
```bash
playwright install chromium
```

上記が失敗する場合:
```bash
pip install playwright
python -m playwright install chromium
```

---

### Permission Denied エラー

**症状:** スクリプト実行時に `Permission denied` が発生する

**解決方法:**
```bash
chmod +x ~/.claude/skills/seo/scripts/*.py
chmod +x ~/.claude/skills/seo/hooks/*.py
chmod +x ~/.claude/skills/seo/hooks/*.sh
```

---

### Hook がトリガーされない

**症状:** Schema バリデーション Hook が実行されない

**確認方法:**

1. Hook が設定に含まれているか確認する:
```bash
cat ~/.claude/settings.json
```

2. パスが正しいことを確認する:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/seo/hooks/validate-schema.py \"$FILE_PATH\"",
            "exitCodes": { "2": "block" }
          }
        ]
      }
    ]
  }
}
```

3. Hook を直接テストする:
```bash
python3 ~/.claude/skills/seo/hooks/validate-schema.py test.html
```

---

### Subagent が見つからない

**症状:** `Agent 'seo-technical' not found`

**解決方法:**

1. Agent ファイルが存在するか確認する:
```bash
ls ~/.claude/agents/seo-*.md
```

2. Agent の frontmatter を確認する:
```bash
head -5 ~/.claude/agents/seo-technical.md
```

3. Agent を再インストールする:
```bash
cp /path/to/claude-seo/agents/*.md ~/.claude/agents/
```

---

### タイムアウトエラー

**症状:** `Request timed out after 30 seconds`

**解決方法:**

1. 対象サイトの応答が遅い可能性があります。再度試してください
2. スクリプト呼び出しのタイムアウト値を増やしてください
3. ネットワーク接続を確認してください
4. 一部のサイトは自動リクエストをブロックしています

---

### Schema バリデーションの誤検知

**症状:** Hook が有効な Schema をブロックする

**確認方法:**

1. プレースホルダーが置き換えられていることを確認する
2. @context が `https://schema.org` であることを確認する
3. 非推奨のタイプ (HowTo, SpecialAnnouncement) がないか確認する
4. [Google's Rich Results Test](https://search.google.com/test/rich-results) で検証する

---

### 監査パフォーマンスが遅い

**症状:** フル監査に時間がかかりすぎる

**解決方法:**

1. 監査は最大 500 ページをクロールするため、大規模サイトでは時間がかかります
2. Subagent は並列で実行され、分析を高速化します
3. より迅速な確認には、特定の URL に対して `/seo page` を使用してください
4. サイトの応答時間が遅くないか確認してください

---

## ヘルプを得る

1. **ドキュメントを確認する:** [COMMANDS.md](COMMANDS.md) と [ARCHITECTURE.md](ARCHITECTURE.md) を参照してください

2. **GitHub Issues:** リポジトリでバグを報告してください

3. **ログ:** Claude Code の出力でエラーの詳細を確認してください

## デバッグモード

詳細な出力を確認するには、Claude Code の内部ログを確認するか、スクリプトを直接実行してください:

```bash
# fetch のテスト
python3 ~/.claude/skills/seo/scripts/fetch_page.py https://example.com

# parse のテスト
python3 ~/.claude/skills/seo/scripts/parse_html.py page.html --json

# スクリーンショットのテスト
python3 ~/.claude/skills/seo/scripts/capture_screenshot.py https://example.com
```
