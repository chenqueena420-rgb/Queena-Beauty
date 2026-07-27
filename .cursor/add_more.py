import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "products-data.json"

data = json.loads(DB_PATH.read_text(encoding="utf-8"))
existing_names = {d.get("name") for d in data if isinstance(d, dict)}

extra_items = [
    {"name": "Biodance 膠原蛋白實感深層全效面膜", "features": "低分子膠原蛋白、玻尿酸。", "pain": "毛孔鬆弛、保養品吸收不佳、肌膚無光。", "skin": "熟齡肌、所有膚質。", "category": "面膜"},
    {"name": "LuLuLun 晚安舒緩面膜 (薰衣草)", "features": "植物萃取、療癒薰衣草香氛。", "pain": "壓力肌、睡前放鬆、夜間修護不足。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "提提研 浸潤補水黑面膜", "features": "補水因子、長效保濕。", "pain": "換季脫皮、乾燥緊繃。", "skin": "乾性肌、混合肌。", "category": "面膜"},
    {"name": "AHC 瞬效保濕B5微導洗面乳", "features": "高濃度維他命B5、玻尿酸。", "pain": "洗臉後發紅、乾澀、清潔不夠。", "skin": "敏感肌、乾性肌。", "category": "洗面乳"},
    {"name": "Biore 蜜妮 深層卸妝乳", "features": "瞬效卸妝成分、質地溫和。", "pain": "不喜歡卸妝油的油膩感、日常淡妝。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "肌研 白潤美白精華液", "features": "高純度傳明酸、維他命C。", "pain": "曬後變黑、局部暗沈、想提升白皙度。", "skin": "追求美白者。", "category": "精華"},
    {"name": "專科 完美保濕水凝露", "features": "水感凝露、不黏膩鎖水。", "pain": "夏天用乳霜太悶、水分散失快。", "skin": "油性肌、混合肌。", "category": "乳霜"},
    {"name": "雪芙蘭 防曬水凝乳 (SPF50+)", "features": "超水感質地、高效防曬。", "pain": "防曬乳的厚重感、預算有限。", "skin": "所有膚質。", "category": "防曬"},
    {"name": "廣源良 蘆薈敷臉凝露", "features": "天然蘆薈、鎮靜舒緩。", "pain": "曬後發燙、皮膚躁動、清涼補水。", "skin": "所有膚質、曬後肌。", "category": "面膜"},
    {"name": "提提研 保濕金箔黑面膜 (新版)", "features": "添加金箔、備長炭纖維。", "pain": "精華液吸收慢、皮膚疲憊感。", "skin": "混合肌、所有膚質。", "category": "面膜"},
]

added_count = 0
for item in extra_items:
    if item["name"] not in existing_names:
        data.append(item)
        existing_names.add(item["name"])
        added_count += 1

DB_PATH.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Added {added_count} more items. Total: {len(data)}")
