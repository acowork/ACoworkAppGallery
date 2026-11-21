# FigCraft (ACowork)

ACowork hosted adaptation of FigCraft — frames, auto layout, components,
variants, vectors, styles, variables and prototypes — so Desktop can install
it as a **hosted app** and show the UI in an iframe.

This listing is published by **ACowork**. It is based on FigCraft by the
ArtCraft team. It is **not** an ArtCraft product and is not sponsored,
endorsed, certified or supported by the ArtCraft Team.

| | |
|---|---|
| **ACowork package repo** | [acowork/figcraft-app](https://github.com/acowork/figcraft-app) |
| **Upstream** | [storytold/figcraft](https://github.com/storytold/figcraft) |
| **License** | MIT OR Apache-2.0 |
| **Package** | [v0.18.2-acowork](https://github.com/acowork/figcraft-app/releases/tag/v0.18.2-acowork) (windows-x86_64) |

## Name and marks

- Public name: **FigCraft (ACowork)**. Package id remains `figcraft`.
- The gallery icon is the upstream **FigCraft app icon** (MIT OR Apache-2.0), not the ArtCraft mark.
- ArtCraft name, wordmark and logos are trademarks and are **not** used here.

## Status

A thin ACowork host (`figcraft-acowork`) is packaged for Windows. It serves
`/health` + `/ui/` for the Gateway supervisor and bundles the Trunk
`figcraft-web` surface. Desktop treats it as a **visual canvas** app
(`ui.canvas.kind = visual`): workspace `.figcraft` files open in the hosted
UI, and MCP tools write a sibling `.preview.png` for chat/editor cards.

Install requires a Gateway that accepts this package (unsigned packages need
`apps.allow_unsigned = true` or `dev_mode` until a signed Release is published).

## Privacy

Your design files stay on disk; nothing is sent unless you share a file. See
upstream docs for sharing behaviour.
