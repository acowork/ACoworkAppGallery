# GridCraft (ACowork)

Spreadsheets in ACowork: cells, a real formula engine, charts, formatting and sorting. Opens and saves Excel (`.xlsx`) in a hosted grid agents can compute on over MCP.

## Features

- Formula engine with the common Excel function set and live recalculation.
- Range formatting, number formats, sort and filter; charts from ranges.
- Multiple sheets, cell pictures and floating objects.
- Excel round-trip (`.xlsx` default save).

## Working with agents in ACowork

Installing the app adds it to the Desktop nav and registers its MCP tools with
the Gateway. Every agent session gets a headless document session **confined to
the workspace it is acting on**: open, inspect and edit files through tools, and
render a page or slide back as an image the agent can look at and attach to chat.
Edits land in the same workspace file the hosted UI shows, and the app's Save
writes back to it — so you and the agent edit one document, not two copies.

Typical loop: drop a file into the workspace (or attach it in chat), ask the agent
to change it, watch the result in the hosted UI, keep or refine it by hand.
- `get_cell` / `set_cell`, `evaluate_formula`, `format_range`, `sort_range`,
  `insert_chart`, plus `commands` for everything else.
- The agent reads and writes the same workbook the UI shows; formulas are
  evaluated by the engine, not guessed by the model.

Ask e.g. *"read sales.xlsx, add monthly totals and a column chart"* or *"clean the
date column and sort by revenue"*. Workspace `.xlsx` files open in the hosted UI;
Save writes back to the same file.

## License

Hosted adaptation of upstream GridCraft, used under its MIT OR Apache-2.0 license. Links: [package repo](https://github.com/acowork/gridcraft-app) ·
[upstream](https://github.com/storytold/gridcraft) · [release](https://github.com/acowork/gridcraft-app/releases).

Files stay on this machine; nothing leaves it unless you share a file. Unsigned
packages need `apps.allow_unsigned = true` or `dev_mode` until a signed Release exists.
