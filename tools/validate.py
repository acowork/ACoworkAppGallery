#!/usr/bin/env python3
"""Validate every apps/<owner>/<id>/gallery.json against the schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "apps"
SCHEMA_PATH = ROOT / "schema" / "gallery.schema.json"


def main() -> int:
    try:
        import jsonschema
    except ImportError:
        print("jsonschema is optional; doing structural checks only", file=sys.stderr)
        jsonschema = None  # type: ignore

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = None
    if jsonschema is not None:
        validator = jsonschema.Draft202012Validator(schema)

    errors: list[str] = []
    entries = sorted(
        p
        for p in APPS.glob("*/*/gallery.json")
        if "_template" not in p.parts
    )
    if not entries:
        print("no gallery entries found under apps/", file=sys.stderr)
        return 1

    for path in entries:
        owner, app_id = path.parent.parent.name, path.parent.name
        data = json.loads(path.read_text(encoding="utf-8"))
        if validator is not None:
            for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
                errors.append(f"{path.relative_to(ROOT)}: {err.message}")
        if data.get("id") != app_id:
            errors.append(
                f"{path.relative_to(ROOT)}: id {data.get('id')!r} must match directory {app_id!r}"
            )
        if owner not in str(data.get("publisher", {}).get("id", "")) and owner != "acowork":
            # Soft hint only for community paths; official may use acowork publisher.
            pass
        readme = path.parent / "README.md"
        if not readme.is_file():
            errors.append(f"{path.parent.relative_to(ROOT)}: missing README.md")
        icon = data.get("icon")
        if isinstance(icon, str) and not icon.startswith(("http://", "https://")):
            icon_path = path.parent / icon
            if not icon_path.is_file():
                errors.append(f"{path.relative_to(ROOT)}: icon not found: {icon}")

    if errors:
        print("FAIL")
        for e in errors:
            print(" ", e)
        return 1
    print(f"OK: {len(entries)} entr{'y' if len(entries) == 1 else 'ies'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
