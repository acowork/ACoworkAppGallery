const INDEX_URL = new URL("./data/index.json", import.meta.url);

function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

/** Minimal Markdown → HTML for gallery READMEs (headings, lists, code, links, tables). */
function renderMarkdown(md) {
  const lines = String(md || "").replace(/\r\n/g, "\n").split("\n");
  const out = [];
  let i = 0;
  let inCode = false;
  let codeLang = "";
  let codeBuf = [];
  let inUl = false;
  let inTable = false;

  const flushList = () => {
    if (inUl) {
      out.push("</ul>");
      inUl = false;
    }
  };
  const flushTable = () => {
    if (inTable) {
      out.push("</tbody></table>");
      inTable = false;
    }
  };
  const inline = (text) =>
    esc(text)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");

  while (i < lines.length) {
    const line = lines[i];
    if (line.startsWith("```")) {
      flushList();
      flushTable();
      if (!inCode) {
        inCode = true;
        codeLang = line.slice(3).trim();
        codeBuf = [];
      } else {
        out.push(`<pre><code class="lang-${esc(codeLang)}">${esc(codeBuf.join("\n"))}</code></pre>`);
        inCode = false;
      }
      i += 1;
      continue;
    }
    if (inCode) {
      codeBuf.push(line);
      i += 1;
      continue;
    }
    if (/^\|/.test(line) && lines[i + 1] && /^\|?\s*-/.test(lines[i + 1])) {
      flushList();
      const headers = line.split("|").slice(1, -1).map((c) => c.trim());
      i += 2;
      out.push("<table><thead><tr>" + headers.map((h) => `<th>${inline(h)}</th>`).join("") + "</tr></thead><tbody>");
      inTable = true;
      while (i < lines.length && /^\|/.test(lines[i])) {
        const cells = lines[i].split("|").slice(1, -1).map((c) => c.trim());
        out.push("<tr>" + cells.map((c) => `<td>${inline(c)}</td>`).join("") + "</tr>");
        i += 1;
      }
      flushTable();
      continue;
    }
    if (/^###\s+/.test(line)) {
      flushList();
      flushTable();
      out.push(`<h3>${inline(line.replace(/^###\s+/, ""))}</h3>`);
    } else if (/^##\s+/.test(line)) {
      flushList();
      flushTable();
      out.push(`<h2>${inline(line.replace(/^##\s+/, ""))}</h2>`);
    } else if (/^#\s+/.test(line)) {
      flushList();
      flushTable();
      out.push(`<h1>${inline(line.replace(/^#\s+/, ""))}</h1>`);
    } else if (/^[-*]\s+/.test(line)) {
      flushTable();
      if (!inUl) {
        out.push("<ul>");
        inUl = true;
      }
      out.push(`<li>${inline(line.replace(/^[-*]\s+/, ""))}</li>`);
    } else if (line.trim() === "") {
      flushList();
      flushTable();
    } else {
      flushList();
      flushTable();
      out.push(`<p>${inline(line)}</p>`);
    }
    i += 1;
  }
  flushList();
  flushTable();
  if (inCode) {
    out.push(`<pre><code>${esc(codeBuf.join("\n"))}</code></pre>`);
  }
  return out.join("\n");
}

function cardHtml(app, selected) {
  const icon = app.icon
    ? `<img class="card__icon" src="${esc(app.icon)}" alt="" />`
    : `<div class="card__icon card__icon--ph">${esc((app.name || "?").slice(0, 1).toUpperCase())}</div>`;
  const pkg = app.package?.url ? "Installable" : "Catalog";
  const pillClass = app.package?.url ? "pill pill--ok" : "pill";
  return `<button type="button" class="card" role="option" data-id="${esc(app.id)}" aria-selected="${selected ? "true" : "false"}">
    ${icon}
    <div>
      <div class="card__name">${esc(app.name)}</div>
      <div class="card__meta">${esc(app.publisher?.display_name || "")}${app.latest_version ? " · " + esc(app.latest_version) : ""}</div>
      <div class="card__sum">${esc(app.summary || "")}</div>
      <span class="${pillClass}">${pkg}</span>
    </div>
  </button>`;
}

function showDetail(app) {
  const empty = document.getElementById("detail-empty");
  const detail = document.getElementById("detail");
  empty.hidden = true;
  detail.hidden = false;
  document.getElementById("d-name").textContent = app.name;
  document.getElementById("d-sub").textContent = [
    app.publisher?.display_name,
    app.license,
    app.latest_version && `v${app.latest_version}`,
  ]
    .filter(Boolean)
    .join(" · ");
  document.getElementById("d-summary").textContent = app.summary || "";
  const icon = document.getElementById("d-icon");
  if (app.icon) {
    icon.src = app.icon;
    icon.hidden = false;
  } else {
    icon.hidden = true;
  }
  const repo = document.getElementById("d-repo");
  repo.href = app.repository || "#";
  const home = document.getElementById("d-home");
  if (app.homepage) {
    home.href = app.homepage;
    home.hidden = false;
  } else {
    home.hidden = true;
  }
  const pkg = document.getElementById("d-pkg");
  if (app.package?.url) {
    pkg.textContent = "Desktop can install via package URL";
    pkg.className = "pill pill--ok";
    pkg.hidden = false;
  } else {
    pkg.textContent = "Packaging in progress — open the repository";
    pkg.className = "pill pill--warn";
    pkg.hidden = false;
  }
  document.getElementById("d-readme").innerHTML = renderMarkdown(app.readme_md || "_No README._");
}

async function main() {
  const res = await fetch(INDEX_URL);
  if (!res.ok) throw new Error(`index HTTP ${res.status}`);
  const index = await res.json();
  const apps = Array.isArray(index.apps) ? index.apps : [];
  document.getElementById("count").textContent = String(apps.length);

  let selectedId = apps[0]?.id || null;
  const cardsEl = document.getElementById("cards");
  const emptyEl = document.getElementById("empty");
  const qEl = document.getElementById("q");

  const render = () => {
    const q = (qEl.value || "").trim().toLowerCase();
    const visible = apps.filter((a) =>
      `${a.name} ${a.id} ${a.summary} ${a.publisher?.display_name || ""}`.toLowerCase().includes(q),
    );
    emptyEl.hidden = visible.length > 0;
    cardsEl.innerHTML = visible.map((a) => cardHtml(a, a.id === selectedId)).join("");
    const sel = apps.find((a) => a.id === selectedId);
    if (sel) showDetail(sel);
  };

  cardsEl.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-id]");
    if (!btn) return;
    selectedId = btn.getAttribute("data-id");
    render();
  });
  qEl.addEventListener("input", render);
  render();
}

main().catch((err) => {
  document.getElementById("count").textContent = "0";
  document.getElementById("detail-empty").textContent = `Failed to load catalog: ${err.message}`;
  console.error(err);
});
