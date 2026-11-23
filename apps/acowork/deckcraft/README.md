# DeckCraft (ACowork)

Presentations in ACowork: slides, masters and layouts, shapes, tables and charts, themes and text formatting. Opens and saves PowerPoint (`.pptx`, reads `.ppt` / `.potx`), exports PDF — in a hosted canvas agents can edit over MCP.

## Features

- Slide editor with masters/layouts, themes, guides and pasteboard overflow.
- Shapes, tables, charts and pictures; per-run text formatting and font fallback.
- PowerPoint round-trip (`.pptx` save is the default), PDF export, slide renders.
- Presenter view and slide sorter for review passes.

## Working with agents in ACowork

Installing the app adds it to the Desktop nav and registers its MCP tools with
the Gateway. Every agent session gets a headless document session **confined to
the workspace it is acting on**: open, inspect and edit files through tools, and
render a page or slide back as an image the agent can look at and attach to chat.
Edits land in the same workspace file the hosted UI shows, and the app's Save
writes back to it — so you and the agent edit one document, not two copies.

Typical loop: drop a file into the workspace (or attach it in chat), ask the agent
to change it, watch the result in the hosted UI, keep or refine it by hand.
- `document`, `go_to_slide`, `add_shape`, `set_text`, `insert_chart`, `export`.
- `render_slide` / `screenshot` return the slide as an image so the agent can see
  what it built; `run_command` / `commands` / `list_commands` expose the rest.

Ask e.g. *"turn page 3 into two columns with a chart"* or *"apply the brand theme
to every slide and export a PDF"*. Workspace `.pptx` / `.deckcraft` files open in
the hosted UI; Save writes back to the same file.

## License

Hosted adaptation of upstream DeckCraft, used under its MIT OR Apache-2.0 license. Links: [package repo](https://github.com/acowork/deckcraft-app) ·
[upstream](https://github.com/storytold/deckcraft) · [release](https://github.com/acowork/deckcraft-app/releases).

Files stay on this machine; nothing leaves it unless you share a file. Unsigned
packages need `apps.allow_unsigned = true` or `dev_mode` until a signed Release exists.
