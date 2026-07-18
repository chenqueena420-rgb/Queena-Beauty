import html
import json
import pathlib
import re
import urllib.parse
import urllib.request
from collections import OrderedDict

ROOT = pathlib.Path(__file__).resolve().parent
DB_PATH = ROOT / "products-data.json"
AUDIT_PATH = ROOT / "watsons_added_100_audit.json"

data = json.loads(DB_PATH.read_text(encoding="utf-8"))


def norm(s: str) -> str:
    s = s.lower()
    return re.sub(r"[\s\-_/()（）+.,，。'\"`~!@#$%^&*:;？?！!、｜|]", "", s)


existing_names = [d.get("name", "") for d in data if isinstance(d, dict)]
existing_norm = {norm(n) for n in existing_names if n}

HEADERS = {"User-Agent": "Mozilla/5.0"}


def get(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "ignore")


link_re = re.compile(r"uddg=([^&\"]+)")
title_re = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)

queries = {
    "面膜": [
        "site:watsons.com.tw 面膜 p/BP_ 屈臣氏",
        "site:watsons.com.tw 臉部保養 面膜 屈臣氏",
        "site:watsons.com.tw sheet mask 屈臣氏",
        "site:watsons.com.tw 保濕 面膜 屈臣氏",
        "site:watsons.com.tw 積雪草 面膜 屈臣氏",
    ],
    "洗面乳": [
        "site:watsons.com.tw 洗面乳 p/BP_ 屈臣氏",
        "site:watsons.com.tw 潔面 凝膠 屈臣氏",
        "site:watsons.com.tw 洗顏 屈臣氏",
        "site:watsons.com.tw cleanser watsons.com.tw",
        "site:watsons.com.tw 胺基酸 洗面乳 屈臣氏",
    ],
    "乳霜": [
        "site:watsons.com.tw 乳霜 p/BP_ 屈臣氏",
        "site:watsons.com.tw 保濕霜 屈臣氏",
        "site:watsons.com.tw 修護霜 屈臣氏",
        "site:watsons.com.tw cream watsons.com.tw",
        "site:watsons.com.tw 神經醯胺 乳霜 屈臣氏",
    ],
    "防曬": [
        "site:watsons.com.tw 防曬 p/BP_ 屈臣氏",
        "site:watsons.com.tw 防曬乳 屈臣氏",
        "site:watsons.com.tw sunscreen watsons.com.tw",
        "site:watsons.com.tw UV 屈臣氏",
        "site:watsons.com.tw SPF50 屈臣氏",
    ],
}
cat_targets = {"面膜": 25, "洗面乳": 25, "乳霜": 25, "防曬": 25}

cand = OrderedDict()
for cat, q_list in queries.items():
    for q in q_list:
        try:
            search_url = "https://duckduckgo.com/html/?q=" + urllib.parse.quote(q)
            html_doc = get(search_url, timeout=25)
        except Exception:
            continue
        for match in link_re.finditer(html_doc):
            u = urllib.parse.unquote(match.group(1))
            if "watsons.com.tw" not in u:
                continue
            if "/p/" not in u:
                continue
            u = u.split("&rut=")[0]
            key = (cat, u)
            if key not in cand:
                cand[key] = None

cat_items = {k: [] for k in queries}
for cat, u in list(cand.keys()):
    if len(cat_items[cat]) >= cat_targets[cat] * 4:
        continue
    try:
        doc = get(u, timeout=20)
    except Exception:
        continue
    t_match = title_re.search(doc)
    if not t_match:
        continue
    title = html.unescape(t_match.group(1))
    title = re.sub(r"\s+", " ", title).strip()
    title = re.sub(r"\|\s*屈臣氏.*$", "", title).strip()
    title = re.sub(r"\|\s*Watsons.*$", "", title).strip()
    title = re.sub(r"\s*-\s*屈臣氏.*$", "", title).strip()
    if not title or len(title) < 4:
        continue
    if any(x in title for x in ["台灣屈臣氏網路商店", "全部商品", "首頁", "搜尋結果", "Access Denied"]):
        continue
    cat_items[cat].append((title, u))


def infer_category(name: str, fallback: str) -> str:
    if any(k in name for k in ["防曬", "UV", "SPF", "隔離"]):
        return "防曬"
    if any(k in name for k in ["洗面", "潔面", "洗顏", "慕斯", "潔顏"]):
        return "洗面乳"
    if any(k in name for k in ["面膜", "凍膜", "泥膜"]):
        return "面膜"
    if any(k in name for k in ["乳霜", "面霜", "凝霜", "修護霜", "保濕霜", "晚霜"]):
        return "乳霜"
    return fallback


picked = []
seen_norm = set(existing_norm)
seen_url = set()

for cat in ["面膜", "洗面乳", "乳霜", "防曬"]:
    for name, url in cat_items[cat]:
        n = norm(name)
        if n in seen_norm or url in seen_url:
            continue
        picked.append((cat, name, url))
        seen_norm.add(n)
        seen_url.add(url)
        if sum(1 for x in picked if x[0] == cat) >= cat_targets[cat]:
            break

if len(picked) < 100:
    pool = []
    for cat, lst in cat_items.items():
        for name, url in lst:
            pool.append((cat, name, url))
    for cat, name, url in pool:
        n = norm(name)
        if n in seen_norm or url in seen_url:
            continue
        picked.append((infer_category(name, cat), name, url))
        seen_norm.add(n)
        seen_url.add(url)
        if len(picked) >= 100:
            break

picked = picked[:100]

templates = {
    "面膜": ("高效保濕精華、修護舒緩配方。", "缺水乾燥、膚況粗糙、上妝不服貼。", "一般肌、混合肌、缺水肌。"),
    "洗面乳": ("溫和潔淨系統、保濕配方。", "毛孔髒污、出油悶黏、洗後緊繃。", "混合肌、油性肌、一般肌。"),
    "乳霜": ("保濕修護複方、鎖水屏障科技。", "乾燥脫屑、細紋粗糙、屏障不穩。", "乾性肌、混合偏乾肌、敏感肌。"),
    "防曬": ("廣譜UVA/UVB防護、清爽防曬科技。", "曬黑暗沉、光老化、戶外曝曬。", "一般肌、混合肌、戶外活動肌。"),
}

new_rows = []
for cat, name, url in picked:
    f, pain, skin = templates[cat]
    new_rows.append({"name": name, "features": f, "pain": pain, "skin": skin, "category": cat, "_source_url": url})

existing = {d.get("name") for d in data if isinstance(d, dict)}
added_count = 0
for row in new_rows:
    source_url = row.pop("_source_url", None)
    if row["name"] in existing:
        continue
    data.append(row)
    existing.add(row["name"])
    added_count += 1

DB_PATH.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

AUDIT_PATH.write_text(
    json.dumps(
        {
            "picked_count": len(new_rows),
            "added_count": added_count,
            "new_total": len(data),
            "items": [{"name": r["name"], "category": r["category"]} for r in new_rows],
        },
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)

print(f"picked={len(new_rows)} added={added_count} total={len(data)}")
