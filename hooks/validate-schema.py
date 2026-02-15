#!/usr/bin/env python3
"""Claude Code 用の編集後 Schema バリデーションフック。

ファイル編集後に JSON-LD Schema を検証します。重大なバリデーションエラーが
見つかった場合、終了コード 2 を返してブロックします。

~/.claude/settings.json でのフック設定:
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

注意: matcher はツール名（Edit、Write）のみでフィルタリングします。
スクリプト自体が、バリデーション前にファイルに Schema マークアップが
含まれているかどうかを確認します。
"""

import json
import re
import sys
import os
from typing import List


def validate_jsonld(content: str) -> List[str]:
    """HTML コンテンツ内の JSON-LD ブロックを検証します。"""
    errors = []
    pattern = r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>'
    blocks = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)

    if not blocks:
        return []  # Schema が見つかりません — エラーではありません

    for i, block in enumerate(blocks, 1):
        block = block.strip()
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"ブロック {i}: 無効な JSON — {e}")
            continue

        if isinstance(data, list):
            for item in data:
                errors.extend(_validate_schema_object(item, i))
        elif isinstance(data, dict):
            errors.extend(_validate_schema_object(data, i))

    return errors


def _validate_schema_object(obj: dict, block_num: int) -> List[str]:
    """単一の Schema オブジェクトを検証します。"""
    errors = []
    prefix = f"ブロック {block_num}"

    # @context の確認
    if "@context" not in obj:
        errors.append(f"{prefix}: @context がありません")
    elif obj["@context"] not in ("https://schema.org", "http://schema.org"):
        errors.append(f"{prefix}: @context は 'https://schema.org' であるべきです")

    # @type の確認
    if "@type" not in obj:
        errors.append(f"{prefix}: @type がありません")

    # プレースホルダーテキストの確認
    placeholders = [
        "[Business Name]",
        "[City]",
        "[State]",
        "[Phone]",
        "[Address]",
        "[Your",
        "[INSERT",
        "REPLACE",
        "[URL]",
        "[Email]",
    ]
    text = json.dumps(obj)
    for p in placeholders:
        if p.lower() in text.lower():
            errors.append(f"{prefix}: プレースホルダーテキストが含まれています: {p}")

    # 非推奨タイプの確認
    schema_type = obj.get("@type", "")
    deprecated = {
        "HowTo": "2023年9月に非推奨",
        "SpecialAnnouncement": "2025年7月31日に非推奨",
        "CourseInfo": "2025年6月に廃止",
        "EstimatedSalary": "2025年6月に廃止",
        "LearningVideo": "2025年6月に廃止",
        "ClaimReview": "2025年6月に廃止 — ファクトチェックのリッチリザルトは終了",
        "VehicleListing": "2025年6月に廃止 — 車両リスティングの構造化データは終了",
    }
    if schema_type in deprecated:
        errors.append(f"{prefix}: @type '{schema_type}' は{deprecated[schema_type]}です")

    # 制限付きタイプの不正使用の確認
    restricted = {"FAQPage": "政府および医療サイトのみに制限されています（2023年8月）"}
    if schema_type in restricted:
        errors.append(f"{prefix}: @type '{schema_type}' は{restricted[schema_type]} — サイトが対象かご確認ください")

    return errors


def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        sys.exit(0)

    # HTML 系ファイルのみを検証
    valid_extensions = (".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".php", ".ejs")
    if not filepath.endswith(valid_extensions):
        sys.exit(0)

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except (OSError, IOError):
        sys.exit(0)

    errors = validate_jsonld(content)

    if not errors:
        sys.exit(0)

    # エラーの分類
    critical_keywords = ["プレースホルダー", "非推奨", "廃止"]
    critical = [e for e in errors if any(kw in e.lower() for kw in critical_keywords)]
    warnings = [e for e in errors if e not in critical]

    if warnings:
        print("⚠️  Schema バリデーション警告:")
        for w in warnings:
            print(f"  - {w}")

    if critical:
        print("🛑 Schema バリデーションエラー（ブロック）:")
        for e in critical:
            print(f"  - {e}")
        sys.exit(2)  # 編集をブロック

    sys.exit(1)  # 警告のみ — 続行


if __name__ == "__main__":
    main()
