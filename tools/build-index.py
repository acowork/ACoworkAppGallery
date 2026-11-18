#!/usr/bin/env python3
"""Build dist/index.json from apps/*/gallery.json (embeds README markdown)."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "apps"
OUT = ROOT / "dist" / "index.json"
DEFAULT_BASE = "https://raw.githubusercontent.com/acowork/ACoworkAppGallery/main"


def git_commit() -> str | None:
    try:
        return (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"],
                cwd=ROOT,
                stderr=subprocess.DEVNULL,
                text=True,
            )
            .strip()
            or None
        )
    except (subprocess.SubprocessError, OSError):
        return None


def resolve_icon(entry_dir: Path, icon: str | None, source_path: str) -> str | None:
    if not icon:
        return None
    if icon.startswith(("http://", "https://")):
        return icon
    rel = f"{source_path}/{icon}".replace("\\", "/")
    return f"{DEFAULT_BASE}/{rel}"


def main() -> int:
    apps: list[dict] = []
    for path in sorted(APPS.glob("*/*/gallery.json")):
        if "_template" in path.parts:
            continue
        owner = path.parent.parent.name
        app_dir = path.parent.name
        source_path = f"apps/{owner}/{app_dir}"
        data = json.loads(path.read_text(encoding="utf-8"))
        readme_path = path.parent / "README.md"
        readme_md = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
        apps.append(
            {
                "id": data["id"],
                "name": data["name"],
                "summary": data["summary"],
                "publisher": data["publisher"],
                "license": data["license"],
                "repository": data["repository"],
                "homepage": data.get("homepage"),
                "upstream": data.get("upstream"),
                "categories": data.get("categories") or [],
                "icon": resolve_icon(path.parent, data.get("icon"), source_path),
                "latest_version": data.get("latest_version"),
                "package": data.get("package"),
                "readme_md": readme_md,
                "source_path": source_path,
            }
        )

    index = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": {
            "repository": "https://github.com/acowork/ACoworkAppGallery",
            "commit": git_commit(),
        },
        "apps": apps,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(apps)} apps)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
