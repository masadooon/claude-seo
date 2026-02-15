#!/usr/bin/env bash
set -euo pipefail

# Claude SEO インストーラー
# ネットワーク障害による部分的な実行を防ぐため、すべてを main() で囲んでいます

main() {
    SKILL_DIR="${HOME}/.claude/skills/seo"
    AGENT_DIR="${HOME}/.claude/agents"
    REPO_URL="https://github.com/AgriciDaniel/claude-seo"

    echo "════════════════════════════════════════"
    echo "║   Claude SEO - インストーラー          ║"
    echo "║   Claude Code SEO スキル              ║"
    echo "════════════════════════════════════════"
    echo ""

    # 前提条件の確認
    command -v python3 >/dev/null 2>&1 || { echo "✗ Python 3 が必要ですが、インストールされていません。"; exit 1; }
    command -v git >/dev/null 2>&1 || { echo "✗ Git が必要ですが、インストールされていません。"; exit 1; }

    # Python バージョンの確認
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    echo "✓ Python ${PYTHON_VERSION} を検出しました"

    # ディレクトリの作成
    mkdir -p "${SKILL_DIR}"
    mkdir -p "${AGENT_DIR}"

    # クローンまたは更新
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf ${TEMP_DIR}" EXIT

    echo "↓ Claude SEO をダウンロード中..."
    git clone --depth 1 "${REPO_URL}" "${TEMP_DIR}/claude-seo" 2>/dev/null

    # スキルファイルのコピー
    echo "→ スキルファイルをインストール中..."
    cp -r "${TEMP_DIR}/claude-seo/seo/"* "${SKILL_DIR}/"

    # サブスキルのコピー
    if [ -d "${TEMP_DIR}/claude-seo/skills" ]; then
        for skill_dir in "${TEMP_DIR}/claude-seo/skills"/*/; do
            skill_name=$(basename "${skill_dir}")
            target="${HOME}/.claude/skills/${skill_name}"
            mkdir -p "${target}"
            cp -r "${skill_dir}"* "${target}/"
        done
    fi

    # スキーマテンプレートのコピー
    if [ -d "${TEMP_DIR}/claude-seo/schema" ]; then
        mkdir -p "${SKILL_DIR}/schema"
        cp -r "${TEMP_DIR}/claude-seo/schema/"* "${SKILL_DIR}/schema/"
    fi

    # リファレンスドキュメントのコピー
    if [ -d "${TEMP_DIR}/claude-seo/pdf" ]; then
        mkdir -p "${SKILL_DIR}/pdf"
        cp -r "${TEMP_DIR}/claude-seo/pdf/"* "${SKILL_DIR}/pdf/"
    fi

    # エージェントのコピー
    echo "→ サブエージェントをインストール中..."
    cp -r "${TEMP_DIR}/claude-seo/agents/"*.md "${AGENT_DIR}/" 2>/dev/null || true

    # 共有スクリプトのコピー
    if [ -d "${TEMP_DIR}/claude-seo/scripts" ]; then
        mkdir -p "${SKILL_DIR}/scripts"
        cp -r "${TEMP_DIR}/claude-seo/scripts/"* "${SKILL_DIR}/scripts/"
    fi

    # フックのコピー
    if [ -d "${TEMP_DIR}/claude-seo/hooks" ]; then
        mkdir -p "${SKILL_DIR}/hooks"
        cp -r "${TEMP_DIR}/claude-seo/hooks/"* "${SKILL_DIR}/hooks/"
        chmod +x "${SKILL_DIR}/hooks/"*.sh 2>/dev/null || true
        chmod +x "${SKILL_DIR}/hooks/"*.py 2>/dev/null || true
    fi

    # Python 依存パッケージのインストール
    echo "→ Python 依存パッケージをインストール中..."
    pip install --quiet --break-system-packages -r "${TEMP_DIR}/claude-seo/requirements.txt" 2>/dev/null || \
    pip install --quiet -r "${TEMP_DIR}/claude-seo/requirements.txt" 2>/dev/null || \
    echo "⚠  Python パッケージの自動インストールに失敗しました。次のコマンドを実行してください: pip install -r requirements.txt"

    # オプション: Playwright ブラウザのインストール
    echo "→ Playwright ブラウザをインストール中（オプション）..."
    python3 -m playwright install chromium 2>/dev/null || \
    echo "⚠  Playwright ブラウザのインストールに失敗しました。スクリーンショット機能は使用できません。次のコマンドを実行してください: playwright install chromium"

    echo ""
    echo "✓ Claude SEO のインストールが完了しました！"
    echo ""
    echo "使い方:"
    echo "  1. Claude Code を起動:  claude"
    echo "  2. コマンドを実行:       /seo audit https://example.com"
    echo ""
    echo "アンインストールするには: curl -fsSL ${REPO_URL}/raw/main/uninstall.sh | bash"
}

main "$@"
