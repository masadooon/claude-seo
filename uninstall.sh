#!/usr/bin/env bash
set -euo pipefail

main() {
    echo "→ Claude SEO をアンインストールしています..."

    # メインスキルを削除
    rm -rf "${HOME}/.claude/skills/seo"

    # サブスキルを削除
    for skill in seo-audit seo-competitor-pages seo-content seo-geo seo-hreflang seo-images seo-page seo-plan seo-programmatic seo-schema seo-sitemap seo-technical; do
        rm -rf "${HOME}/.claude/skills/${skill}"
    done

    # エージェントを削除
    for agent in seo-technical seo-content seo-schema seo-sitemap seo-performance seo-visual; do
        rm -f "${HOME}/.claude/agents/${agent}.md"
    done

    echo "✓ Claude SEO のアンインストールが完了しました。"
}

main "$@"
