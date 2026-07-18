import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DB = ROOT / "products-data.json"

data = json.loads(DB.read_text(encoding="utf-8"))

items = [
    {"name": "NEOGENCE 霓淨思無針水光維他命B保濕面膜5入", "features": "維他命B、保濕修護精華。", "pain": "乾燥缺水、屏障不穩、膚況粗糙。", "skin": "乾性肌、敏感肌、混合肌。", "category": "面膜"},
    {"name": "Dr.Satin頂級魚子高效保濕面膜(30ml)-3片入", "features": "魚子精華、保濕修護複方。", "pain": "乾紋粗糙、膚況疲憊、彈性不足。", "skin": "乾性肌、輕熟齡肌、一般肌。", "category": "面膜"},
    {"name": "NEOGENCE 霓淨思高效亮白零觸感面膜5入", "features": "亮白修護精華、輕薄服貼膜布。", "pain": "暗沉無光、膚色不均、妝感不服貼。", "skin": "一般肌、混合肌、暗沉肌。", "category": "面膜"},
    {"name": "NEOGENCE 霓淨思0.5%穩膚煥采A醇修護乳10ML", "features": "0.5%A醇、穩膚修護科技。", "pain": "粗糙暗沉、細紋初老、膚況不穩。", "skin": "混合肌、油性肌、熟齡肌。", "category": "乳霜"},
    {"name": "DR.WU玻尿酸保濕精華乳50ML", "features": "玻尿酸、長效保濕修護配方。", "pain": "缺水緊繃、乾燥粗糙、妝後浮粉。", "skin": "乾性肌、混合肌、一般肌。", "category": "乳霜"},
    {"name": "DR.WU杏仁酸溫和煥膚精華8% 15mL", "features": "8%杏仁酸、溫和煥膚調理。", "pain": "毛孔粗大、粉刺堆積、膚色不均。", "skin": "油性肌、混合肌、粗糙肌。", "category": "乳霜"},
    {"name": "NEOGENCE 霓淨思玻尿酸保濕水平衡精華化妝水150ML", "features": "玻尿酸、水平衡保濕科技。", "pain": "缺水乾燥、膚觸粗糙、保養不吸收。", "skin": "乾性肌、混合肌、一般肌。", "category": "乳霜"},
    {"name": "CeraVe適樂膚全效超級修護乳52ML", "features": "神經醯胺、屏障修護保濕配方。", "pain": "屏障受損、乾癢脫屑、敏感泛紅。", "skin": "敏感肌、乾性肌、受損肌。", "category": "乳霜"},
    {"name": "妮維雅全護清爽防曬隔離乳-敏感肌專用SPF50+ 50ml", "features": "SPF50+高防護、溫和敏肌配方。", "pain": "曬後泛紅、敏感刺癢、光老化。", "skin": "敏感肌、一般肌、混合肌。", "category": "防曬"},
    {"name": "OLAY 新生高效緊緻護膚霜 50G", "features": "胜肽緊緻科技、滋潤修護成分。", "pain": "細紋鬆弛、暗沉疲態、乾燥失彈。", "skin": "一般肌、乾性肌、輕熟齡肌。", "category": "乳霜"},
    {"name": "露得清水活保濕凝露50g(New)", "features": "玻尿酸、清爽保濕凝露。", "pain": "缺水緊繃、悶黏不適、妝前卡粉。", "skin": "混合肌、油性肌、一般肌。", "category": "乳霜"},
    {"name": "露得清水活保濕凝露環保補充包50g", "features": "玻尿酸、保濕鎖水科技。", "pain": "乾燥缺水、保濕不持久、膚觸粗糙。", "skin": "一般肌、混合肌、乾性肌。", "category": "乳霜"},
    {"name": "露得清水活保濕菸鹼醯胺精華30ml*2【超值二入組】", "features": "菸鹼醯胺、保濕修護複方。", "pain": "暗沉毛孔、油水失衡、膚況不穩。", "skin": "混合肌、油性肌、暗沉肌。", "category": "乳霜"},
    {"name": "HEME 喜蜜 清透水感防曬凝膠 SPF50**** 40ml", "features": "高係數防曬、水感凝膠質地。", "pain": "曬黑暗沉、悶黏厚重、補擦困難。", "skin": "混合肌、油性肌、一般肌。", "category": "防曬"},
    {"name": "CeraVe全效清爽修護防曬乳SPF50 52ml", "features": "SPF50防護、神經醯胺修護。", "pain": "日曬老化、乾燥敏弱、防曬不持久。", "skin": "敏感肌、乾性肌、一般肌。", "category": "防曬"},
    {"name": "NEOGENCE 霓淨思全天候長效抗陽防曬乳50ml", "features": "廣譜UV防護、長效抗陽科技。", "pain": "長時間曝曬、曬黑曬老、防護不足。", "skin": "一般肌、混合肌、戶外活動肌。", "category": "防曬"},
    {"name": "Target Pro 肌膚專研低敏亮白防曬乳(防水型)SPF50+PA++++ 60ml", "features": "低敏防水、防曬亮白雙效。", "pain": "敏感不耐受、戶外流汗脫落、曬黑。", "skin": "敏感肌、混合肌、一般肌。", "category": "防曬"},
    {"name": "GATSBY 長效控油洗面乳130g", "features": "控油潔淨因子、深層清潔配方。", "pain": "油光滿面、毛孔堵塞、粉刺增生。", "skin": "油性肌、混合偏油肌。", "category": "洗面乳"},
    {"name": "碧菲絲特水嫩淨透洗面乳120g", "features": "綿密泡沫、保濕潔淨科技。", "pain": "髒污殘留、洗後乾澀、膚觸粗糙。", "skin": "一般肌、混合肌、乾性肌。", "category": "洗面乳"},
    {"name": "SHISEIDO 資生堂百優精純乳霜(7ml)X3-專櫃公司貨", "features": "保濕修護、彈潤滋養複方。", "pain": "乾紋細紋、彈力流失、膚觸粗糙。", "skin": "乾性肌、熟齡肌、一般肌。", "category": "乳霜"},
    {"name": "SHISEIDO資生堂百優精純乳霜(18ml) 3入組新版_公司貨", "features": "滋養修護科技、長效潤澤配方。", "pain": "乾燥緊繃、鬆弛暗沉、細紋增多。", "skin": "乾性肌、熟齡肌。", "category": "乳霜"},
    {"name": "【SHISEIDO 資生堂】百優精純乳霜75ml+18mlx3 公司貨", "features": "高滋潤修護、抗老彈潤配方。", "pain": "深層乾燥、細紋鬆弛、光澤不足。", "skin": "乾性肌、熟齡肌。", "category": "乳霜"},
    {"name": "【SHISEIDO 資生堂】百優精純乳霜75ml+50ml 公司貨", "features": "彈潤修護科技、長效保濕因子。", "pain": "乾紋粗糙、鬆弛失彈、膚況不穩。", "skin": "乾性肌、熟齡肌。", "category": "乳霜"},
    {"name": "SHISEIDO資生堂百優精純乳霜18mlX3【公司貨】", "features": "保濕修護複方、彈潤抗老科技。", "pain": "乾燥細紋、暗沉疲態、彈性下降。", "skin": "乾性肌、一般肌、熟齡肌。", "category": "乳霜"},
    {"name": "SHISEIDO資生堂百優精純乳霜75mlx2【公司貨】", "features": "高效保濕、抗老修護精華。", "pain": "乾燥脫屑、鬆弛細紋、膚觸粗糙。", "skin": "乾性肌、熟齡肌。", "category": "乳霜"},
    {"name": "GAMARDE 珂瑪德長效玻尿酸保濕乳霜-潤澤型40g", "features": "玻尿酸、潤澤鎖水配方。", "pain": "缺水緊繃、乾燥細紋、屏障不穩。", "skin": "乾性肌、敏感肌、混合偏乾肌。", "category": "乳霜"},
    {"name": "CeraVe適樂膚長效清爽保濕乳 473ml", "features": "神經醯胺、長效保濕修護。", "pain": "乾燥粗糙、屏障脆弱、保濕不持久。", "skin": "乾性肌、敏感肌、一般肌。", "category": "乳霜"},
    {"name": "Target Pro 低敏長效保濕潤膚乳500ml", "features": "低敏保濕科技、長效潤澤修護。", "pain": "乾燥敏感、換季泛紅、屏障受損。", "skin": "敏感肌、乾性肌。", "category": "乳霜"},
    {"name": "OLAY 新生高效緊緻精華乳100ml", "features": "胜肽緊緻複方、保濕修護精華。", "pain": "鬆弛細紋、乾燥暗沉、彈力下滑。", "skin": "一般肌、混合肌、熟齡肌。", "category": "乳霜"},
    {"name": "CHANEL 香奈兒山茶花保濕乳霜(50g)-國際航空版", "features": "山茶花保濕精華、潤澤修護配方。", "pain": "乾燥缺水、膚質粗糙、光澤不足。", "skin": "乾性肌、一般肌、混合偏乾肌。", "category": "乳霜"}
]

existing = {d.get("name") for d in data if isinstance(d, dict)}
added = 0
for item in items:
    if item["name"] in existing:
        continue
    data.append(item)
    existing.add(item["name"])
    added += 1

DB.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("added", added, "total", len(data))
