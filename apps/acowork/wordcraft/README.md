# WordCraft (ACowork)

Documents in ACowork: paginated writing with styles, tables, headers and footers, and Zotero-backed citations. Opens and saves Word (`.docx`) and Markdown, exports PDF — in a hosted canvas agents can edit over MCP.

## Features

- True pagination with styles, sections, headers/footers and page setup.
- Tables, images, comments and tracked changes; Markdown import/export.
- Zotero integration for citations and bibliographies.
- Word round-trip (`.docx` default save) and PDF export.

## Working with agents in ACowork

Installing the app adds it to the Desktop nav and registers its MCP tools with
the Gateway. Every agent session gets a headless document session **confined to
the workspace it is acting on**: open, inspect and edit files through tools, and
render a page or slide back as an image the agent can look at and attach to chat.
Edits land in the same workspace file the hosted UI shows, and the app's Save
writes back to it — so you and the agent edit one document, not two copies.

Typical loop: drop a file into the workspace (or attach it in chat), ask the agent
to change it, watch the result in the hosted UI, keep or refine it by hand.
- `document`, `execute` / `commands`, `insert_table`, `type_text`.
- `render_page` / `screenshot` return a page image so the agent can check layout,
  not just markup.

Ask e.g. *"turn these meeting notes into a docx with heading levels and a summary
table"* or *"insert the results table and re-flow page 2"*. Workspace `.docx` /
`.md` files open in the hosted UI; Save writes back to the same file.

## License

Hosted adaptation of upstream WordCraft, used under its MIT OR Apache-2.0 license. Links: [package repo](https://github.com/acowork/wordcraft-app) ·
[upstream](https://github.com/storytold/wordcraft) · [release](https://github.com/acowork/wordcraft-app/releases).

Files stay on this machine; nothing leaves it unless you share a file. Unsigned
packages need `apps.allow_unsigned = true` or `dev_mode` until a signed Release exists.
