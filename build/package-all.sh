#!/bin/bash
# Stage + pack the six craft apps into unsigned .app / .app.zip (Windows x86_64).
# Web UI sources: dist/web for the trunk apps, target/web-site for lightcraft (its own xtask pipeline).
set -u
PLATFORM=windows-x86_64
PACK=/e/projects/tranxon/ACowork/target/release/acowork-pack-app.exe
[ -x "$PACK" ] || PACK=/e/projects/tranxon/ACowork/target/debug/acowork-pack-app.exe
OUT=/e/projects/tranxon/ACowork/build/packages
mkdir -p "$OUT"
: > /tmp/pack-all.log

for app in wordcraft gridcraft deckcraft pdfcraft vectorcraft lightcraft; do
  root=/e/projects/tranxon/$app-app
  web=$root/dist/web
  [ "$app" = lightcraft ] && web=$root/target/web-site
  # The package version is the manifest's, not the crate's: `app.toml` is what the
  # Gateway reads a package by, and installing an already-present version is a
  # no-op, so a rebuild that must land has to bump it.
  ver=$(grep -m1 '^version' "$root/packaging/acowork/app.toml" | sed 's/.*"\(.*\)".*/\1/')
  zip=/tmp/$app-web.zip
  rm -f "$zip"
  # python's zipfile: Expand-Archive in package.ps1 rejects bsdtar's zip, and the
  # `*.br` / `*.gz` copies are precompressed variants for a static host that asks for
  # them (lightcraft's xtask makes them) — the app's own ServeDir never does, and in
  # the package they were ~40 MB of dead weight on lightcraft alone.
  python - "$(cygpath -w "$web")" "$(cygpath -w "$zip")" >> /tmp/pack-all.log 2>&1 <<'PYEOF'
import pathlib, sys, zipfile
src, dst = pathlib.Path(sys.argv[1]), sys.argv[2]
with zipfile.ZipFile(dst, "w", zipfile.ZIP_STORED) as z:
    for p in sorted(src.rglob("*")):
        if p.is_file() and p.suffix not in (".br", ".gz"):
            z.write(p, p.relative_to(src))
PYEOF
  [ -s "$zip" ] || { echo "$app ZIP FAIL" >> /tmp/pack-all.log; continue; }

  ( cd "$root" && powershell -NoProfile -ExecutionPolicy Bypass -File packaging/acowork/package.ps1 -WebArchive "$zip" ) >> /tmp/pack-all.log 2>&1 \
    || { echo "$app STAGE FAIL" >> /tmp/pack-all.log; continue; }

  stage=$root/dist/acowork/$app-$PLATFORM
  appfile=$OUT/$app-$ver-$PLATFORM.app
  rm -f "$appfile" "$appfile.zip"
  "$PACK" --app-dir "$stage" --output "$appfile" >> /tmp/pack-all.log 2>&1 || { echo "$app PACK FAIL" >> /tmp/pack-all.log; continue; }
  ( cd "$OUT" && cp -f "$(basename "$appfile")" "$appfile.zip" ) >> /tmp/pack-all.log 2>&1
  echo "=== $app $ver DONE app=$(stat -c%s "$appfile" 2>/dev/null) zip=$(stat -c%s "$appfile.zip" 2>/dev/null)" >> /tmp/pack-all.log
done
echo ALLPACKED >> /tmp/pack-all.log