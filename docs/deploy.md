# Deploy App Gallery (Cloudflare Pages)

Target: **https://gallery.acowork.ai** — sister of `hub.acowork.ai`.

## One-time: Cloudflare ↔ GitHub

1. Cloudflare Dashboard → **Workers & Pages** → **Create** → **Pages** →
   **Connect to Git**.
2. Authorize the `acowork` org and select **ACoworkAppGallery**.
3. Build settings:

   | Field | Value |
   |---|---|
   | Production branch | `main` |
   | Build command | `python3 tools/build-index.py` |
   | Build output directory | `site` |
   | Root directory | `/` (repo root) |

4. Environment: Python is available on Pages build images; if the image
   lacks `python3`, change the build command to
   `pip install --user nothing 2>/dev/null; python tools/build-index.py`
   or commit a prebuilt `site/data/index.json` (this repo does both).
5. After the first deploy succeeds, **Custom domains** → add
   `gallery.acowork.ai` (CNAME already in [`site/CNAME`](../site/CNAME)).
6. Point DNS for `gallery.acowork.ai` at Cloudflare Pages (usually automatic
   when the zone for `acowork.ai` is on Cloudflare).

Every push to `main` rebuilds and republishes. Desktop fetches:

```
https://gallery.acowork.ai/data/index.json
```

## Local preview

```bash
python tools/build-index.py
python -m http.server 8787 --directory site
# open http://127.0.0.1:8787
```

## Homepage link (acowork.ai)

Add an App Gallery entry next to Agent Hub, for example:

```html
<a href="https://gallery.acowork.ai">App Gallery</a>
```

Suggested copy: **App Gallery** — hosted apps for ACowork Desktop.
See [`homepage-link.md`](homepage-link.md).
