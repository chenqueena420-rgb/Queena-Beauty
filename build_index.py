# -*- coding: utf-8 -*-
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
data = json.loads(root.joinpath("products-data.json").read_text(encoding="utf-8"))
js_data = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

HTML = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8" />
<meta name="description" content="Queena Beauty 提供 AI 精準分析，專為敏弱肌與乾性肌篩選醫美修護乳霜，讓您輕鬆找到適合的保養產品。">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Queena Beauty - AI 精準化妝護膚品篩選平台</title>
<style>

.brand-logo {{
      font-family: "Georgia", "Times New Roman", "Noto Serif TC", serif;
      font-size: 2.8rem;
      font-weight: 700;
      color: #2d1b4d;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      padding: 2.5rem 0 1.5rem 0;
      display: block;
      text-align: left;
      line-height: 1.2;
    }}
html, body {{ margin: 0; min-height: 100%; font-family: "Segoe UI", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif; color: var(--ink); background: linear-gradient(160deg, var(--bg1) 0%, #fff 45%, var(--bg2) 100%); }}
body::before {{
  content: ""; position: fixed; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse 80% 50% at 10% -10%, rgba(167, 139, 250, .25), transparent 50%),
              radial-gradient(ellipse 60% 40% at 100% 100%, rgba(251, 113, 133, .2), transparent 45%);
  z-index: 0;
}}
.wrap {{ position: relative; z-index: 1; max-width: 72rem; margin: 0 auto; padding: 2rem 1.25rem 3rem; }}
header h1 {{ font-size: clamp(1.5rem, 4vw, 2.25rem); font-weight: 700; letter-spacing: -.02em; margin: .25rem 0 0; }}
header .sub {{ color: var(--muted); max-width: 40rem; line-height: 1.6; margin-top: .75rem; font-size: .95rem; }}
.tagline {{ font-size: .75rem; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: #7c3aed; margin: 0; }}
.search-row {{ display: flex; flex-wrap: wrap; gap: .75rem; margin-top: 1.75rem; align-items: flex-end; }}
.search-field {{ flex: 1; min-width: 200px; }}
.search-field label {{ display: block; font-size: .8rem; font-weight: 600; color: #475569; margin-bottom: .35rem; }}
.search-field input {{
  width: 100%; padding: .85rem 1rem .85rem 2.75rem; border-radius: 1rem; border: 1px solid #e2e8f0;
  background: rgba(255,255,255,.95); font-size: 1rem; outline: none;
  box-shadow: inset 0 1px 2px rgba(0,0,0,.04);
}}
.search-field input:focus {{ border-color: #c4b5fd; box-shadow: 0 0 0 4px var(--ring); }}
.search-ic {{ position: absolute; left: .85rem; top: 50%; transform: translateY(-50%); color: #94a3b8; pointer-events: none; }}
.search-wrap {{ position: relative; }}
.btn-clear {{
  padding: .85rem 1.25rem; border-radius: 1rem; border: 1px solid #e2e8f0; background: #fff;
  font-weight: 600; color: #475569; cursor: pointer; font-size: .9rem;
}}
.btn-clear:hover {{ background: #f8fafc; }}
.chips {{ display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1.25rem; align-items: center; }}
.chips > span {{ font-size: .65rem; font-weight: 700; letter-spacing: .08em; color: #94a3b8; text-transform: uppercase; margin-right: .25rem; }}
.chip {{
  border: none; cursor: pointer; padding: .4rem 1rem; border-radius: 999px; font-size: .875rem; font-weight: 600;
  background: rgba(255,255,255,.9); color: #475569; border: 1px solid #e2e8f0; transition: .15s;
}}
.chip:hover {{ background: #f5f3ff; color: #6d28d9; }}
.chip.on {{ background: #7c3aed; color: #fff; border-color: #7c3aed; box-shadow: 0 4px 14px rgba(124,58,237,.35); }}
.meta {{ display: flex; flex-wrap: wrap; justify-content: space-between; gap: .5rem; margin: 1.5rem 0 1rem; font-size: .85rem; color: var(--muted); }}
.meta strong {{ color: #4c1d95; }}
.grid {{ display: grid; gap: 1.25rem; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); }}
.card {{
  border-radius: 1.25rem; overflow: hidden; background: var(--card); border: 1px solid rgba(255,255,255,.8);
  box-shadow: 0 10px 40px -12px rgba(91, 33, 182, .2); display: flex; flex-direction: column; min-height: 100%;
  transition: transform .2s, box-shadow .2s;
}}
.card:hover {{ transform: translateY(-3px); box-shadow: 0 20px 50px -15px rgba(91, 33, 182, .28); }}
.card-visual {{
  height: 7.5rem; display: flex; align-items: center; justify-content: center; position: relative;
  font-size: 3rem; line-height: 1;
}}
.card-visual::after {{
  content: ""; position: absolute; inset: 0; opacity: .35;
  background: radial-gradient(circle at 30% 20%, rgba(255,255,255,.5), transparent 55%);
  pointer-events: none;
}}
.cat-精華 {{ background: linear-gradient(135deg, #3b82f6, #6366f1, #8b5cf6); }}
.cat-防曬 {{ background: linear-gradient(135deg, #fb923c, #f97316, #ea580c); }}
.cat-面膜 {{ background: linear-gradient(135deg, #f472b6, #ec4899, #db2777); }}
.cat-唇部 {{ background: linear-gradient(135deg, #f9a8d4, #f472b6, #e11d48); }}
.cat-其他 {{ background: linear-gradient(135deg, #94a3b8, #64748b, #475569); }}
.card-body {{ padding: 1.1rem 1.25rem 1.25rem; display: flex; flex-direction: column; flex: 1; gap: .65rem; }}
.badges {{ display: flex; flex-wrap: wrap; gap: .4rem; align-items: center; }}
.badge-cat {{ font-size: .7rem; font-weight: 700; padding: .2rem .55rem; border-radius: 999px; background: #f1f5f9; color: #475569; }}
.badge-score {{ font-size: .65rem; font-family: ui-monospace, monospace; padding: .15rem .4rem; border-radius: .35rem; background: #f1f5f9; color: #64748b; }}
.card h2 {{ font-size: 1.05rem; font-weight: 700; line-height: 1.35; margin: 0; }}
.price-note {{ font-size: .7rem; color: #94a3b8; margin: 0; }}
.dl {{ margin: 0; font-size: .82rem; line-height: 1.5; }}
.dl dt {{ font-size: .65rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: #94a3b8; margin-top: .5rem; }}
.dl dt:first-child {{ margin-top: 0; }}
.dl dd {{ margin: .2rem 0 0; color: #334155; }}
.dl dd.pain {{ color: #9f1239; font-weight: 500; }}
.match-hint {{ font-size: .7rem; color: #6d28d9; line-height: 1.45; margin: .25rem 0 0; }}
.buy-actions {{
  display: flex; flex-wrap: wrap; gap: .75rem; margin-top: auto;
}}
.btn-buy {{
  display: inline-flex; align-items: center; justify-content: center; gap: .5rem; text-decoration: none;
  font-weight: 700; font-size: .88rem; color: #fff !important; border-radius: .9rem; padding: .75rem 1rem;
  background: linear-gradient(135deg, var(--buy1), var(--buy2)); box-shadow: 0 6px 20px rgba(5,150,105,.35); transition: .15s;
  flex: 1 1 12rem; min-width: 120px;
}}
.btn-buy:hover {{ filter: brightness(1.06); box-shadow: 0 8px 24px rgba(5,150,105,.45); }}
.buy-foot {{ font-size: .62rem; color: #94a3b8; text-align: center; margin: .35rem 0 0; line-height: 1.4; }}
.empty {{
  text-align: center; padding: 3rem 1.5rem; border: 2px dashed #e2e8f0; border-radius: 1.25rem; background: rgba(255,255,255,.5); color: var(--muted);
}}
footer {{ text-align: center; padding: 2rem 1rem; font-size: .7rem; color: #94a3b8; }}
.logic {{ font-size: .7rem; max-width: 28rem; text-align: right; }}
@media (max-width: 640px) {{ .logic {{ text-align: left; width: 100%; }} }}
</style>
</head>
<body>
<div class="brand-logo">Queena Beauty</div>
<div class="wrap">
<header>
<p class="tagline">Single File · Offline Ready</p>
<h1>美妝選品搜尋</h1>
<p class="sub">加權搜尋：<strong>產品名稱</strong>與<strong>解決痛點</strong>權重最高；<strong>核心成分／特性</strong>與<strong>適合膚質</strong>次之。支援模糊比對（子字串，例如「乾」→「乾燥」「乾肌」）。資料以 <code>const productData</code> 內嵌，無 fetch、不需選檔；介面離線可用（屈臣氏按鈕需連線）。</p>
<div class="search-row">
<div class="search-field">
<label for="q">搜尋</label>
<div class="search-wrap">
<span class="search-ic" aria-hidden="true"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg></span>
<input id="q" type="search" autocomplete="off" placeholder="例如：乾、防曬、痘痘、唇紋…" />
</div>
</div>
<button type="button" class="btn-clear" id="btn-clear">清除</button>
</div>
<div class="chips"><span>分類</span><div id="cat-filters"></div></div>
</header>
<main>
<div class="meta"><p id="result-meta"></p><p class="logic" id="logic-hint"></p></div>
<div id="grid" class="grid"></div>
<div id="empty" class="empty" hidden><p style="font-weight:600;color:#334155;margin:0">找不到符合的產品</p><p style="margin:.5rem 0 0;font-size:.85rem">試試更短關鍵字或切換分類。</p></div>
</main>
</div>
<footer>
      <p>© 2026 Queena Beauty. All Rights Reserved. 著作權所有 · 轉載必究</p>
      <p style="margin-top: 0.25rem;">單一檔案封裝 · 屈臣氏連結需連線時開啟</p>
    </footer>
  </div>
<script>
const productData = {js_data};

const W_NAME = 12;
const W_PAIN = 12;
const W_FEAT = 5;
const W_SKIN = 5;
const W_PHRASE = 20;

const CAT_EMOJI = {{ 精華: "🧴", 防曬: "☀️", 面膜: "🧖", 唇部: "💄", 其他: "✨" }};

function normalize(s) {{
  return String(s || "").replace(/暗沈/g, "暗沉").toLowerCase();
}}

function tokenize(q) {{
  const t = String(q || "").trim();
  if (!t) return {{ phrase: "", tokens: [] }};
  const parts = t.split(/[\\s、，,]+/).filter(Boolean);
  const phrase = normalize(t.replace(/\\s+/g, ""));
  const tokens = [...new Set(parts.map((p) => normalize(p)).filter(Boolean))];
  if (tokens.length === 0 && t) tokens.push(phrase);
  return {{ phrase, tokens }};
}}

function scoreProduct(p, phrase, tokens) {{
  const name = normalize(p.name);
  const pain = normalize(p.pain);
  const feat = normalize(p.features);
  const skin = normalize(p.skin);
  let s = 0;
  const hits = [];
  if (phrase.length >= 2) {{
    const blobNP = name + pain;
    if (blobNP.includes(phrase)) {{ s += W_PHRASE; hits.push("片語·名稱/痛點"); }}
    else if (feat.includes(phrase) || skin.includes(phrase)) {{ s += W_PHRASE * 0.45; hits.push("片語·成分/膚質"); }}
  }}
  for (const tok of tokens) {{
    if (!tok) continue;
    if (name.includes(tok)) {{ s += W_NAME; hits.push("名稱:「" + tok + "」"); }}
    if (pain.includes(tok)) {{ s += W_PAIN; hits.push("痛點:「" + tok + "」"); }}
    if (feat.includes(tok)) {{ s += W_FEAT; hits.push("成分:「" + tok + "」"); }}
    if (skin.includes(tok)) {{ s += W_SKIN; hits.push("膚質:「" + tok + "」"); }}
  }}
  return {{ score: s, hits: [...new Set(hits)] }};
}}

function rank(list, q) {{
  const {{ phrase, tokens }} = tokenize(q);
  if (!phrase && tokens.length === 0) return list.map((p) => ({{ p, score: 0, hits: [] }}));
  return list
    .map((p) => {{
      const r = scoreProduct(p, phrase, tokens);
      return {{ p, score: r.score, hits: r.hits }};
    }})
    .filter((x) => x.score > 0)
    .sort((a, b) => b.score - a.score);
}}

function esc(s) {{
  const d = document.createElement("div");
  d.textContent = s;
  return d.innerHTML;
}}

function escAttr(s) {{
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}}

function renderBuyButtons(p) {{
    var links = p.links || {{}};
    var w = links["屈臣氏"] || "";
    var c = links["康是美"] || "";
    var b = links["寶雅"] || "";
    
    var activeButtons = "";
    var hiddenButtons = "";
    
    // 100% 複製你原本 227-229 行最完美的格式
    // 屈臣氏
    if (w !== "#" && w !== "") {{
        activeButtons += '<a class="btn-buy" href="' + w + '" target="_blank" style="color: #000000 !important; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-bottom: 8px; border: 1px solid #ccc; padding: 8px; border-radius: 4px; background: #fff;">前往 屈臣氏 購買</a>';
    }} else {{
        hiddenButtons += '<a class="btn-buy" style="color: #000000 !important; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-bottom: 8px; border: 1px solid transparent; padding: 8px; border-radius: 4px; background: transparent; opacity: 0; pointer-events: none; user-select: none;">前往 屈臣氏 購買</a>';
    }}
    
    // 康是美
    if (c !== "#" && c !== "") {{
        activeButtons += '<a class="btn-buy" href="' + c + '" target="_blank" style="color: #000000 !important; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-bottom: 8px; border: 1px solid #ccc; padding: 8px; border-radius: 4px; background: #fff;">前往 康是美 購買</a>';
    }} else {{
        hiddenButtons += '<a class="btn-buy" style="color: #000000 !important; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-bottom: 8px; border: 1px solid transparent; padding: 8px; border-radius: 4px; background: transparent; opacity: 0; pointer-events: none; user-select: none;">前往 康是美 購買</a>';
    }}
    
    // 寶雅
    if (b !== "#" && b !== "") {{
        activeButtons += '<a class="btn-buy" href="' + b + '" target="_blank" style="color: #000000 !important; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-bottom: 8px; border: 1px solid #ccc; padding: 8px; border-radius: 4px; background: #fff;">前往 寶雅 購買</a>';
    }} else {{
        hiddenButtons += '<a class="btn-buy" style="color: #000000 !important; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-bottom: 8px; border: 1px solid transparent; padding: 8px; border-radius: 4px; background: transparent; opacity: 0; pointer-events: none; user-select: none;">前往 寶雅 購買</a>';
    }}
    
    // 重點：把有網址的正常的按鈕全部放在最前面，透明的隱形按鈕全部塞到後面墊到底部！
    return activeButtons + hiddenButtons;
}}







function catClass(c) {{
  const k = ["精華", "防曬", "面膜", "唇部"].includes(c) ? c : "其他";
  return "cat-" + k;
}}

function renderCard(row) {{
  const p = row.p;
  if (!p.name) return "";
  const em = CAT_EMOJI[p.category] || CAT_EMOJI["其他"];
  const cc = catClass(p.category);
  const hint =
    row.score > 0 && row.hits.length
      ? '<p class="match-hint">匹配：' + esc(row.hits.slice(0, 5).join(" · ")) + (row.hits.length > 5 ? "…" : "") + "</p>"
      : "";
  const sc = row.score > 0 ? '<span class="badge-score">相關 ' + row.score.toFixed(1) + "</span>" : "";
  
  // 直接使用 p.level 欄位
  const levelDisplay = p.level || "💖 質感選品";
  
  const buyButtons = renderBuyButtons(p);
  const foot =
    buyButtons
      ? '<p class="buy-foot">依通路資料可直接前往購買</p>'
      : '<p class="buy-foot">實體店面販售</p>';
  return (
    '<article class="card">' +
    '<div class="card-visual ' +
    cc +
    '" aria-hidden="true"><span style="position:relative;z-index:1;text-shadow:0 2px 12px rgba(0,0,0,.15)">' +
    em +
    "</span></div>" +
    '<div class="card-body">' +
    '<div class="badges"><span class="badge-cat">' +
    esc(p.category) +
    "</span>" +
    sc +
    "</div>" +
    "<h2>" +
    esc(p.name) +
    "</h2>" +
    '<p class="price-note">分級：' + esc(levelDisplay) + '</p>' +
    '<dl class="dl">' +
    "<dt>核心成分與特性</dt><dd>" +
    esc(p.features) +
    "</dd>" +
    '<dt>解決痛點</dt><dd class="pain">' +
    esc(p.pain) +
    "</dd>" +
    "<dt>適合膚質</dt><dd>" +
    esc(p.skin) +
    "</dd></dl>" +
    hint +
   '<div class="buy-actions">' +
buyButtons +
'</div>' +

    "</div></article>"
  );
}}

let all = [];
let activeCat = "全部";

function validateRows(arr) {{
  if (!Array.isArray(arr)) return [];
  return arr.filter((x) => x && x.name && (x.pain != null || x.features != null));
}}

function apply() {{
  const q = document.getElementById("q").value;
  let base = all;
  if (activeCat !== "全部") base = base.filter((p) => p.category === activeCat);
  const {{ phrase, tokens }} = tokenize(q);
  const ranked = !phrase && tokens.length === 0 ? base.map((p) => ({{ p, score: 0, hits: [] }})) : rank(base, q);
  const grid = document.getElementById("grid");
  const empty = document.getElementById("empty");
  const meta = document.getElementById("result-meta");
  document.getElementById("logic-hint").textContent =
    "加權：名稱/痛點各 " + W_NAME + "，成分/膚質各 " + W_FEAT + "；子字串＝模糊比對。";

  if (!ranked.length) {{
    grid.innerHTML = "";
    empty.hidden = false;
    meta.textContent = "共 " + base.length + " 筆中，無符合條件的結果。";
    return;
  }}
  empty.hidden = true;
  grid.innerHTML = ranked.map(renderCard).join("");
  const n = ranked.length;
  const tot = base.length;
  meta.textContent =
    !phrase && tokens.length === 0
      ? "顯示全部 " + n + " 筆（分類：" + activeCat + "）"
      : "找到 " + n + " 筆相關產品（範圍 " + tot + " 筆）";
}}

function renderChips() {{
  const cats = ["全部", ...new Set(all.map((p) => p.category))];
  const el = document.getElementById("cat-filters");
  el.innerHTML = cats
    .map((c) => {{
      const on = c === activeCat;
      return '<button type="button" class="chip' + (on ? " on" : "") + '" data-cat="' + escAttr(c) + '">' + esc(c) + "</button>";
    }})
    .join("");
  el.querySelectorAll("button[data-cat]").forEach((btn) => {{
    btn.addEventListener("click", () => {{
      activeCat = btn.getAttribute("data-cat");
      renderChips();
      apply();
    }});
  }});
}}

all = validateRows(productData);
renderChips();
apply();

let deb;
document.getElementById("q").addEventListener("input", () => {{
  clearTimeout(deb);
  deb = setTimeout(apply, 100);
}});
document.getElementById("btn-clear").addEventListener("click", () => {{
  document.getElementById("q").value = "";
  activeCat = "全部";
  renderChips();
  apply();
}});
</script>
</body>
</html>
"""

out = root / "index.html"
out.write_text(HTML, encoding="utf-8")
print("wrote", out, "size", out.stat().st_size)
