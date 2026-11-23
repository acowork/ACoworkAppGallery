#!/usr/bin/env python3
"""Fill each entry's `package` block from a built `.app` artifact.

Unsigned packages are fine (figcraft ships the same: `acowork-pack-app` output,
no signing block — install then needs `apps.allow_unsigned = true` or
`dev_mode`). What the entry must carry is the exact asset the release holds:

    <dir>/<app>-<version>-windows-x86_64.app
    → https://github.com/acowork/<app>-app/releases/download/v<version>-acowork/<app>-<version>-windows-x86_64.app.zip

Usage:
    python tools/set-package.py --dir ../build/packages [--dry-run]

Only apps whose artifact is actually present are touched, so it is safe to run
once per app as each one finishes.
"""

import argparse
import hashlib
import io
import json
import pathlib
import shutil
import sys

GALLERY = pathlib.Path(__file__).resolve().parent.parent / "apps" / "acowork"
PLATFORM = "windows-x86_64"
REPO_OWNER = "acowork"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="directory holding the built .app files")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    art_dir = pathlib.Path(args.dir)

    touched = 0
    for entry in sorted(GALLERY.iterdir()):
        manifest_path = entry / "gallery.json"
        if not manifest_path.is_file():
            continue
        manifest = json.load(io.open(manifest_path, encoding="utf-8"))
        app = manifest["id"]
        version = manifest["latest_version"]
        artifact = art_dir / f"{app}-{version}-{PLATFORM}.app"
        if not artifact.is_file():
            continue
        data = artifact.read_bytes()
        # The release asset is the `.app` renamed to `.app.zip` — no second compression:
        # install-url hashes the downloaded bytes, which are exactly the `.app` bytes.
        zip_path = pathlib.Path(str(artifact) + ".zip")
        shutil.copyfile(artifact, zip_path)
        manifest["package"] = {
            "url": (
                f"https://github.com/{REPO_OWNER}/{app}-app/releases/download/"
                f"v{version}-acowork/{app}-{version}-{PLATFORM}.app.zip"
            ),
            "sha256": hashlib.sha256(data).hexdigest(),
            "size_bytes": len(data),
            "platforms": [PLATFORM],
        }
        print(f"{app} {version}: {len(data)} bytes, sha256 {manifest['package']['sha256']}")
        if not args.dry_run:
            io.open(manifest_path, "w", encoding="utf-8", newline="\n").write(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
            )
        touched += 1

    if not touched:
        print(f"no artifacts found in {art_dir}", file=sys.stderr)
        return 1
    print(f"{touched} entr{'y' if touched == 1 else 'ies'} updated" + (" (dry run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())