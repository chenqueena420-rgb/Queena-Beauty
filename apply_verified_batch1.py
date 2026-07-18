import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DB = ROOT / "products-data.json"

data = json.loads(DB.read_text(encoding="utf-8"))

verified_items = [
    {"name": "New Angance玻尿酸保濕面膜10片", "features": "玻尿酸、保濕修護精華。", "pain": "乾燥缺水、粗糙緊繃、妝前不服貼。", "skin": "乾性肌、混合肌、缺水肌。", "category": "面膜"},
    {"name": "寵愛之名維B舒緩保濕面膜4片/盒", "features": "維他命B群、舒緩保濕配方。", "pain": "泛紅不適、乾燥脫屑、屏障不穩。", "skin": "敏感肌、乾性肌、受損肌。", "category": "面膜"},
    {"name": "Target Pro 肌膚專研全效益活面膜 單片", "features": "高機能精華、修護保濕科技。", "pain": "肌膚疲憊、乾燥暗沉、膚況不穩。", "skin": "一般肌、混合肌、乾性肌。", "category": "面膜"},
    {"name": "NEOGENCE 霓淨思超爆水潤澤保濕面膜5入", "features": "高保濕因子、潤澤精華膜布。", "pain": "極度缺水、脫屑乾紋、妝感卡粉。", "skin": "乾性肌、混合偏乾肌。", "category": "面膜"},
    {"name": "碧歐斯BIO 水感舒緩B5極效保濕面膜20mlx7入", "features": "維他命B5、舒緩保濕精華。", "pain": "敏弱乾燥、泛紅緊繃、保濕不足。", "skin": "敏感肌、乾性肌、一般肌。", "category": "面膜"},
    {"name": "我的心機 濃潤黑珍珠絲光潤白黑面膜(8入)", "features": "黑珍珠萃取、亮白保濕精華。", "pain": "暗沉無光、膚色不均、乾燥粗糙。", "skin": "一般肌、混合肌、暗沉肌。", "category": "面膜"},
    {"name": "New Angance玫瑰胺基酸潔面乳100ml", "features": "玫瑰植萃、胺基酸潔淨系統。", "pain": "洗後乾澀、敏感不適、清潔不均。", "skin": "乾性肌、敏感肌、一般肌。", "category": "洗面乳"},
    {"name": "Skin Advanced 卓沿白金胺基酸紓潤保濕潔面乳100ml", "features": "胺基酸泡沫、保濕舒緩成分。", "pain": "毛孔髒污、清潔後緊繃、乾燥粗糙。", "skin": "混合肌、一般肌、乾性肌。", "category": "洗面乳"},
    {"name": "舒特膚BHR淨白無瑕潔面乳100g", "features": "溫和潔淨、亮白修護複方。", "pain": "暗沉膚色不均、清潔後不適。", "skin": "一般肌、混合肌、暗沉肌。", "category": "洗面乳"},
    {"name": "曼秀雷敦 保濕活力潔面乳150ml", "features": "保濕潔淨因子、綿密泡沫。", "pain": "出油髒污、洗後乾澀、膚觸粗糙。", "skin": "混合肌、油性肌、一般肌。", "category": "洗面乳"},
    {"name": "SKIN advanced 卓沿白金水耀肌光感煥亮潔面乳100g", "features": "亮白淨膚配方、溫和潔淨科技。", "pain": "暗沉粗糙、洗後蠟黃、毛孔髒污。", "skin": "一般肌、混合肌、暗沉肌。", "category": "洗面乳"},
    {"name": "薇佳速效抗痘調理潔面乳1+1超值組", "features": "抗痘調理成分、控油潔淨配方。", "pain": "粉刺痘痘、油光、毛孔堵塞。", "skin": "油性肌、痘痘肌、混合偏油肌。", "category": "洗面乳"},
    {"name": "SK-II 全效活膚潔面乳(20G)", "features": "細緻潔淨配方、保濕洗感。", "pain": "殘妝油脂殘留、洗後緊繃、膚觸粗糙。", "skin": "一般肌、混合肌、乾性肌。", "category": "洗面乳"},
    {"name": "碧歐斯BIO超能煥白極光潔面乳100G", "features": "亮白精華複方、溫和潔淨系統。", "pain": "暗沉蠟黃、膚色不均、毛孔粗糙。", "skin": "一般肌、混合肌、暗沉肌。", "category": "洗面乳"},
    {"name": "露得清極致呵護系列溫和修護洗顏露200ml", "features": "溫和低敏潔淨、舒緩保濕成分。", "pain": "敏感刺癢、洗臉不耐受、乾燥緊繃。", "skin": "敏感肌、乾性肌、一般肌。", "category": "洗面乳"},
    {"name": "CeraVe適樂膚水楊酸煥膚淨嫩潔膚露473ml", "features": "水楊酸、神經醯胺、溫和潔淨。", "pain": "角質堆積、粗糙顆粒、毛孔阻塞。", "skin": "油性肌、混合肌、粗糙肌。", "category": "洗面乳"},
    {"name": "CeraVe適樂膚輕柔保濕潔膚露473ml", "features": "神經醯胺、玻尿酸、溫和清潔。", "pain": "洗後緊繃、乾燥脫屑、屏障不穩。", "skin": "乾性肌、敏感肌、一般肌。", "category": "洗面乳"},
    {"name": "舒特膚溫和潔膚乳500ml", "features": "低刺激潔淨、保濕修護配方。", "pain": "敏感泛紅、清潔刺激、乾癢不適。", "skin": "敏感肌、乾性肌、一般肌。", "category": "洗面乳"},
    {"name": "舒特膚三酸煥膚嫩亮潔膚露473ml", "features": "三酸煥膚複方、溫和淨膚科技。", "pain": "粗糙暗沉、毛孔堵塞、痘印不均。", "skin": "混合肌、油性肌、暗沉肌。", "category": "洗面乳"},
    {"name": "CeraVe適樂膚長效潤澤修護霜177ml", "features": "3重神經醯胺、玻尿酸、長效鎖水。", "pain": "乾裂脫屑、屏障受損、反覆乾癢。", "skin": "乾性肌、敏感肌、受損肌。", "category": "乳霜"},
    {"name": "舒特膚長效潤膚霜250g", "features": "長效保濕修護、溫和低刺激。", "pain": "慢性乾燥、粗糙脫皮、屏障脆弱。", "skin": "乾性肌、敏感肌。", "category": "乳霜"},
    {"name": "Skin Advanced 卓沿白金紓潤保濕水感乳霜45g", "features": "保濕修護複方、水感鎖水科技。", "pain": "缺水緊繃、膚況不穩、粗糙細紋。", "skin": "乾性肌、混合偏乾肌。", "category": "乳霜"},
    {"name": "Target Pro 低敏長效保濕潤膚霜300g", "features": "低敏配方、長效保濕修護。", "pain": "敏弱乾癢、屏障不穩、反覆泛紅。", "skin": "敏感肌、乾性肌。", "category": "乳霜"},
    {"name": "OLAY 胜肽專研緊緻乳霜50g-輕潤", "features": "胜肽、保濕緊緻科技。", "pain": "鬆弛細紋、乾燥失彈、暗沉疲態。", "skin": "一般肌、混合肌、輕熟齡肌。", "category": "乳霜"},
    {"name": "Target Pro 低敏亮白防曬乳(防水型)SPF50+PA++++ 60ml", "features": "高係數防曬、低敏防水配方。", "pain": "曝曬曬黑、敏肌不耐受、戶外流汗脫落。", "skin": "敏感肌、一般肌、戶外活動肌。", "category": "防曬"},
    {"name": "AHC 極致防禦長效水潤防曬乳50ML", "features": "高係數UV防護、長效水潤科技。", "pain": "曬黑暗沉、乾燥緊繃、防曬厚重。", "skin": "一般肌、混合肌、乾性肌。", "category": "防曬"},
    {"name": "SOFINA 蘇菲娜iP 輕瑩高效美容防曬乳03光透亮30g", "features": "高防曬係數、提亮校色、防護配方。", "pain": "蠟黃暗沉、曬後老化、妝前氣色差。", "skin": "一般肌、混合肌、暗沉肌。", "category": "防曬"},
    {"name": "韓國BEAUSTA自然完美屏障防曬霜15ML", "features": "屏障防護配方、廣譜UV防護。", "pain": "曬後不適、屏障脆弱、外出曝曬。", "skin": "一般肌、敏感肌、混合肌。", "category": "防曬"},
    {"name": "妮維雅專業級防曬乳光敏感測試SPF50 200ml", "features": "高係數防曬、耐汗防護科技。", "pain": "戶外曬傷、曬黑暗沉、長時間曝曬。", "skin": "一般肌、戶外活動肌。", "category": "防曬"},
    {"name": "妮維雅三重防護水感防曬凝乳(涼感舒緩)180ml", "features": "三重防護系統、涼感舒緩配方。", "pain": "炎夏悶熱、補擦不便、易曬黑。", "skin": "一般肌、混合肌、油性肌。", "category": "防曬"}
]

# remove known non-TW item
data = [d for d in data if d.get("name") != "Dr.Jart+ 積雪草修護霜"]

existing = {d.get("name") for d in data if isinstance(d, dict)}
added = 0
for item in verified_items:
    if item["name"] in existing:
        continue
    data.append(item)
    existing.add(item["name"])
    added += 1

DB.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("added", added, "total", len(data))
