# VectorCraft (ACowork)

Vector illustration in ACowork: paths, brushes and effects with SVG as the native format. Imports AI / EPS / CDR / PDF artwork, exports SVG / PDF / PNG — in a hosted canvas agents can edit over MCP.

## Features

- Bezier path editing, brushes, live effects and boolean path operations.
- SVG-native document model; imports AI, EPS, CDR, PDF and metafiles.
- Export SVG, PDF and raster (PNG) at chosen sizes; image tracing.
- Undo history and format-aware save options.

## Working with agents in ACowork

Installing the app adds it to the Desktop nav and registers its MCP tools with
the Gateway. Every agent session gets a headless document session **confined to
the workspace it is acting on**: open, inspect and edit files through tools, and
render a page or slide back as an image the agent can look at and attach to chat.
Edits land in the same workspace file the hosted UI shows, and the app's Save
writes back to it — so you and the agent edit one document, not two copies.

Typical loop: drop a file into the workspace (or attach it in chat), ask the agent
to change it, watch the result in the hosted UI, keep or refine it by hand.
- `document` / `doc_inspect`, `run_command` / `commands` / `list_commands`,
  `save_file`, `undo`, `formats`.
- The agent edits paths and styles structurally, then renders to check the result
  before saving.

Ask e.g. *"recolor logo.svg to the brand blue and export a 512px PNG"* or *"trace
this sketch into clean paths"*. Workspace `.svg` and imported artwork open in the
hosted UI; Save writes back to the same file.

## License

Hosted adaptation of upstream VectorCraft, used under its MIT OR Apache-2.0 license. Links: [package repo](https://github.com/acowork/vectorcraft-app) ·
[upstream](https://github.com/storytold/vectorcraft) · [release](https://github.com/acowork/vectorcraft-app/releases).

Files stay on this machine; nothing leaves it unless you share a file. Unsigned
packages need `apps.allow_unsigned = true` or `dev_mode` until a signed Release exists.
