# ACoworkAppGallery

Community / official **hosted-app registry** for ACowork Desktop, published at
**[gallery.acowork.ai](https://gallery.acowork.ai)**.

This repository registers applications — it does **not** hold app source trees
or binary `.app` packages. Each entry points at an external project
(repository + optional Release artifact with `sha256`) so the Desktop Apps
panel can browse cards, render a README, and call
`POST /api/apps/install-url` when a package is published.

Sister project: [ACoworkAgentHub](https://github.com/acowork/ACoworkAgentHub)
→ [hub.acowork.ai](https://hub.acowork.ai). Apps and Bots stay separate
surfaces in the Desktop.

## Layout

```
ACoworkAppGallery/
├── schema/                 # gallery.json + index.json contracts
├── apps/<owner>/<id>/      # registration only (gallery.json, README, icon)
├── tools/{validate,build-index}.py
├── dist/index.json         # machine catalog (also copied into site/)
├── site/                   # Cloudflare Pages output (gallery.acowork.ai)
│   ├── index.html          # public browse UI
│   ├── data/index.json
│   ├── apps/**/assets/     # icons synced by build-index
│   ├── CNAME               # gallery.acowork.ai
│   └── _headers
└── docs/deploy.md          # Cloudflare Pages ↔ GitHub setup
```

## Quick start

```bash
cp -r apps/_template apps/<owner>/<app-id>
# edit gallery.json + README.md (+ icon)
python tools/validate.py
python tools/build-index.py
# commit apps/** and the regenerated dist/ + site/data (+ synced icons)
```

## Deploy

Connect this repo to **Cloudflare Pages** (build → `site/`). Step-by-step:
[docs/deploy.md](docs/deploy.md). Homepage link copy:
[docs/homepage-link.md](docs/homepage-link.md).

## Desktop catalog URL

```
https://gallery.acowork.ai/data/index.json
```

Override with `VITE_ACOWORK_APP_GALLERY_URL` or
`localStorage.acowork.appGalleryUrl` while developing against a branch or
`python -m http.server`.

## First entry

[`apps/acowork/figcraft`](apps/acowork/figcraft) →
[acowork/figcraft-app](https://github.com/acowork/figcraft-app)
(public name **FigCraft (ACowork)**; upstream
[storytold/figcraft](https://github.com/storytold/figcraft)).
Latest Windows package: [v0.18.2-acowork](https://github.com/acowork/figcraft-app/releases/tag/v0.18.2-acowork).

## Trust

`package.sha256` is required for URL install (Gateway rejects empty digests).
Unsigned / missing packages are catalog-only until a Release lands.
