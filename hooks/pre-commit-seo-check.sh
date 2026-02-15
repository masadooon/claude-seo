#!/usr/bin/env bash
set -euo pipefail

# Claude Code 用の pre-commit SEO バリデーションフック。
#
# ~/.claude/settings.json でのフック設定:
# {
#   "hooks": {
#     "PreToolUse": [
#       {
#         "matcher": "Bash",
#         "hooks": [
#           {
#             "type": "command",
#             "command": "~/.claude/skills/seo/hooks/pre-commit-seo-check.sh",
#             "exitCodes": { "2": "block" }
#           }
#         ]
#       }
#     ]
#   }
# }
#
# 注意: matcher は "Bash"（ツール名のみ）です。このスクリプトはすべての
# Bash ツール使用時に実行されます。処理を続行する前にステージされたファイルが
# あるかどうかを確認します。ステージされた変更がない場合、即座に exit 0 します。

ERRORS=0
WARNINGS=0

# ステージされた変更があるか確認 — なければ早期終了
if ! git diff --cached --quiet 2>/dev/null; then
    : # ステージされた変更あり、チェックを続行
else
    exit 0  # ステージされた変更なし、チェック不要
fi

echo "🔍 pre-commit SEO チェックを実行中..."

# ステージされた HTML 系ファイルを確認
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null | grep -E '\.(html|htm|php|jsx|tsx|vue|svelte)$' || true)

if [ -z "${STAGED_FILES}" ]; then
    echo "✓ HTML ファイルがステージされていません — SEO チェックをスキップします"
    exit 0
fi

for file in ${STAGED_FILES}; do
    if [ ! -f "${file}" ]; then
        continue
    fi

    # schema 内のプレースホルダーテキストを確認
    if grep -qiE '\[(Business Name|City|State|Phone|Address|Your|INSERT|REPLACE)\]' "${file}" 2>/dev/null; then
        echo "🛑 ${file}: schema マークアップにプレースホルダーテキストが含まれています"
        ERRORS=$((ERRORS + 1))
    fi

    # title タグの文字数を確認
    TITLE=$(grep -oP '(?<=<title>).*?(?=</title>)' "${file}" 2>/dev/null | head -1 || true)
    if [ -n "${TITLE}" ]; then
        TITLE_LEN=${#TITLE}
        if [ "${TITLE_LEN}" -lt 30 ] || [ "${TITLE_LEN}" -gt 70 ]; then
            echo "⚠️  ${file}: title タグの文字数 ${TITLE_LEN} 文字（推奨: 30〜60）"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi

    # alt テキストのない画像を確認
    if grep -qP '<img(?![^>]*alt=)' "${file}" 2>/dev/null; then
        echo "⚠️  ${file}: alt テキストのない画像が見つかりました"
        WARNINGS=$((WARNINGS + 1))
    fi

    # 非推奨の schema タイプを確認
    if grep -qE '"@type"\s*:\s*"(HowTo|SpecialAnnouncement)"' "${file}" 2>/dev/null; then
        echo "🛑 ${file}: 非推奨の schema タイプが含まれています"
        ERRORS=$((ERRORS + 1))
    fi

    # FID の参照を確認（INP を使用すべき）
    if grep -qi 'First Input Delay\|"FID"' "${file}" 2>/dev/null; then
        echo "⚠️  ${file}: FID を参照しています — INP (Interaction to Next Paint) を使用してください"
        WARNINGS=$((WARNINGS + 1))
    fi

    # meta description の文字数を確認
    META_DESC=$(grep -oP '(?<=<meta name="description" content=").*?(?=")' "${file}" 2>/dev/null | head -1 || true)
    if [ -n "${META_DESC}" ]; then
        META_LEN=${#META_DESC}
        if [ "${META_LEN}" -lt 120 ] || [ "${META_LEN}" -gt 160 ]; then
            echo "⚠️  ${file}: meta description の文字数 ${META_LEN} 文字（推奨: 120〜160）"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
done

echo ""
if [ "${ERRORS}" -gt 0 ]; then
    echo "🛑 重大なエラーが ${ERRORS} 件見つかりました — コミットをブロックしました"
    echo "上記のエラーを修正してから再度お試しください。"
    exit 2
elif [ "${WARNINGS}" -gt 0 ]; then
    echo "⚠️  警告が ${WARNINGS} 件見つかりました — コミットは許可されました"
    exit 0
else
    echo "✓ すべての SEO チェックに合格しました"
    exit 0
fi
