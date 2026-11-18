# FigCraft (ACowork)

Open-source interface design and prototyping — frames, auto layout, components,
variants, vectors, styles, variables and prototypes — adapted so ACowork can
install it as a **hosted app** and show the UI in a Desktop iframe.

| | |
|---|---|
| **ACowork package repo** | [acowork/figcraft-app](https://github.com/acowork/figcraft-app) |
| **Upstream** | [storytold/figcraft](https://github.com/storytold/figcraft) |
| **License** | MIT OR Apache-2.0 |

## Status

Packaging for ACowork (ADR-116 `.app` + loopback HTTP `/ui/`) is in progress on
the fork. Until a Release publishes `package.url` + `sha256` in this gallery
entry, Desktop will show this README and a link to the repository instead of
an Install button that downloads a package.

## What changes on the fork

Upstream FigCraft ships native egui windows and an optional `figcraft-web`
static build. The ACowork adaptation needs:

1. A supervised process that serves the web UI (or equivalent) on loopback
2. `app.toml` + signed `.app` per platform
3. Health endpoint for the Gateway supervisor

## Privacy

Your design files stay on disk; nothing is sent unless you share a file. See
upstream docs for sharing behaviour.
