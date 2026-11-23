# Figcraft (ACowork)

Interface design and prototyping in ACowork: frames, auto layout, components and variants, vectors, styles, variables and interactive prototypes — edited in a hosted canvas and drivable by agents over MCP.

## Features

- Frames and auto layout for responsive screens; components with variants and overrides.
- Vector editing, fills/strokes/effects, shared styles and design variables.
- Prototypes with interactions; export PNG / JPEG / WebP / SVG / PDF.
- Inspect and drive the live UI: `ui.inspect`, `ui.pointer`, `ui.key`, `ui.type`.

## Working with agents in ACowork

Installing the app adds it to the Desktop nav and registers its MCP tools with
the Gateway. Every agent session gets a headless document session **confined to
the workspace it is acting on**: open, inspect and edit files through tools, and
render a page or slide back as an image the agent can look at and attach to chat.
Edits land in the same workspace file the hosted UI shows, and the app's Save
writes back to it — so you and the agent edit one document, not two copies.

Typical loop: drop a file into the workspace (or attach it in chat), ask the agent
to change it, watch the result in the hosted UI, keep or refine it by hand.
- `document.inspect`, `node.create` / `node.get` / `node.set`, `select.set`,
  `text.edit.begin` / `text.edit.end` for structural edits.
- `file.open` / `file.save` / `file.export`, `run_command` / `command.batch`,
  `screenshot` and `wait_for_changes` for look-and-verify loops.

Ask e.g. *"rebuild this screenshot as a login frame with auto layout"* or *"rename
every component variant to the new token names and export a PNG"*. Workspace
`.figcraft` files open in the hosted UI; renders write a sibling `.preview.png`
for chat and editor cards.

## License

Hosted adaptation of upstream FigCraft (MIT OR Apache-2.0); ACowork is not affiliated with or
endorsed by the upstream authors. Links: [package repo](https://github.com/acowork/figcraft-app) ·
[upstream](https://github.com/storytold/figcraft) · [release](https://github.com/acowork/figcraft-app/releases).

Files stay on this machine; nothing leaves it unless you share a file. Unsigned
packages need `apps.allow_unsigned = true` or `dev_mode` until a signed Release exists.
