# FigCraft (ACowork)

Open-source interface design and prototyping — frames, auto layout, components,
variants, vectors, styles, variables and prototypes — adapted so ACowork can
install it as a **hosted app** and show the UI in a Desktop iframe.

| | |
|---|---|
| **ACowork package repo** | [acowork/figcraft-app](https://github.com/acowork/figcraft-app) |
| **Upstream** | [storytold/figcraft](https://github.com/storytold/figcraft) |
| **License** | MIT OR Apache-2.0 |
| **Package** | [v0.18.1-acowork](https://github.com/acowork/figcraft-app/releases/tag/v0.18.1-acowork) (windows-x86_64) |

## Status

A thin ACowork host (`figcraft-acowork`) is packaged for Windows. It serves
`/health` + `/ui/` for the Gateway supervisor. The current Release ships a
**placeholder UI**; the full Trunk `figcraft-web` surface is not bundled yet.

Install requires a Gateway that accepts this package (unsigned packages need
`apps.allow_unsigned = true` or `dev_mode` until a signed Release is published).

## Privacy

Your design files stay on disk; nothing is sent unless you share a file. See
upstream docs for sharing behaviour.
