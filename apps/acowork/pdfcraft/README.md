# PdfCraft (ACowork)

PDF in ACowork: read, annotate, fill and sign forms, redact, OCR, reorganize and export — a full PDF workbench in a hosted canvas agents can drive over MCP.

## Features

- Viewing, annotations and comments; form filling and signatures.
- Redaction, OCR for scanned pages, accessibility and preflight checks.
- Organize: split, combine, reorder, bookmarks, Bates numbering, optimize.
- Export text, images, data and Office formats from PDF content.

## Working with agents in ACowork

Installing the app adds it to the Desktop nav and registers its MCP tools with
the Gateway. Every agent session gets a headless document session **confined to
the workspace it is acting on**: open, inspect and edit files through tools, and
render a page or slide back as an image the agent can look at and attach to chat.
Edits land in the same workspace file the hosted UI shows, and the app's Save
writes back to it — so you and the agent edit one document, not two copies.

Typical loop: drop a file into the workspace (or attach it in chat), ask the agent
to change it, watch the result in the hosted UI, keep or refine it by hand.
- `doc_open` / `doc_inspect` / `doc_info` / `doc_save`, `doc_split` / `doc_combine` /
  `doc_optimize`, `doc_export_text` / `doc_export_images` / `doc_export_office`.
- `command_run` / `command_batch` / `command_list` for the long tail (annotations,
  forms, redaction, OCR), `edit_undo` to back out a bad batch.

Ask e.g. *"combine these two PDFs and add Bates numbers"* or *"redact every email
address and export the text"*. Workspace `.pdf` files open in the hosted UI; Save
writes back to the same file.

## License

Hosted adaptation of upstream PdfCraft, used under its MIT OR Apache-2.0 license. Links: [package repo](https://github.com/acowork/pdfcraft-app) ·
[upstream](https://github.com/storytold/pdfcraft) · [release](https://github.com/acowork/pdfcraft-app/releases).

Files stay on this machine; nothing leaves it unless you share a file. Unsigned
packages need `apps.allow_unsigned = true` or `dev_mode` until a signed Release exists.
