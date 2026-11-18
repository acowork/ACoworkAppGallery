# ACoworkAppGallery

Community / official **hosted-app registry** for ACowork Desktop.

This repository registers applications — it does **not** hold app source trees
or binary `.app` packages. Each entry points at an external project
(repository + optional Release artifact with `sha256`) so the Desktop Apps
panel can browse cards, render a README, and call
`POST /api/apps/install-url` when a package is published.

Sister project: [ACoworkAgentHub](https://github.com/acowork/ACoworkAgentHub)
(agents). Apps and Agents stay separate surfaces in the Desktop.

## Layout

```
ACoworkAppGallery/
├── schema/
│   ├── gallery.schema.json   # one apps/<owner>/<id>/gallery.json
│   └── index.schema.json     # published dist/index.json
├── apps/
│   ├── _template/            # copy me
│   └── <owner>/<id>/
│       ├── gallery.json
│       ├── README.md         # rendered in the Desktop detail pane
│       └── assets/icon.png
├── tools/
│   ├── validate.py
│   └── build-index.py        # → dist/index.json (embeds README text)
└── dist/index.json           # what Desktop fetches
```

## Quick start

```bash
# 1. copy the template
cp -r apps/_template apps/<owner>/<app-id>

# 2. edit gallery.json + README.md (+ icon)

# 3. validate + rebuild the catalog
python tools/validate.py
python tools/build-index.py

# 4. commit gallery.json, README, assets, and dist/index.json
```

## First entry

[`apps/acowork/figcraft`](apps/acowork/figcraft) registers
[acowork/figcraft-app](https://github.com/acowork/figcraft-app) — a fork of
FigCraft adapted for ACowork hosted packaging (iframe UI). Until that fork
publishes a signed `.app`, `package` stays `null` and Desktop shows
repository / “packaging in progress” instead of Install.

## Desktop catalog URL

Default (raw GitHub):

```
https://raw.githubusercontent.com/acowork/ACoworkAppGallery/main/dist/index.json
```

Override with env `ACOWORK_APP_GALLERY_URL` (Desktop) when pointing at a
branch or local static server.

## Trust

`package.sha256` is required for URL install (Gateway rejects empty digests).
Unsigned / missing packages are catalog-only until a Release lands.
