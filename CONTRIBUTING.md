# Contributing to ACoworkAppGallery

1. Copy `apps/_template` to `apps/<owner>/<app-id>`.
2. Fill `gallery.json` (schema: `schema/gallery.schema.json`) and `README.md`.
3. Add `assets/icon.png` (or set `icon` to an https URL).
4. Run `python tools/validate.py` and `python tools/build-index.py`.
5. Open a PR that includes the regenerated `dist/index.json`.

Do **not** commit `.app` binaries here. Publish packages from the app's own
repository Releases and reference them with `package.url` + `package.sha256`.
