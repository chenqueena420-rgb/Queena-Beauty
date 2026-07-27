import json
import pathlib

# Paths
ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "products-data.json"

if not DB_PATH.exists():
    print(f"Error: {DB_PATH} not found")
    exit(1)

data = json.loads(DB_PATH.read_text(encoding="utf-8"))
existing_names = {d.get("name") for d in data if isinstance(d, dict)}

new_items = [
    # 面膜
    {"name": "TERAECO 蘆薈舒緩超水嫩面膜", "features": "蘆薈葉萃取、玻尿酸、甜菜鹼。", "pain": "曬後紅腫、乾燥缺水、肌膚躁動。", "skin": "所有膚質、曬後修復肌。", "category": "面膜"},
    {"name": "Dr. Satin 頂級魚子膠原面膜", "features": "魚子精華、海洋膠原蛋白、四胜肽。", "pain": "鬆弛無彈性、缺水細紋、醫美術後。", "skin": "熟齡肌、乾性肌。", "category": "面膜"},
    {"name": "森田藥粧 多重玻尿酸複合精華高保濕面膜", "features": "大小分子玻尿酸、神經醯胺。", "pain": "長效補水需求、皮膚粗糙、乾燥脫屑。", "skin": "一般肌、乾性肌。", "category": "面膜"},
    {"name": "MEDI-PEEL 美蒂菲植萃積雪草B5精華面膜", "features": "積雪草、維他命B5、煙醯胺。", "pain": "敏弱泛紅、毛孔粗大、屏障受損。", "skin": "敏感肌、油痘肌。", "category": "面膜"},
    {"name": "未來美 EX8分鐘逆時空膠囊亮白面膜", "features": "膠囊精華技術、速效亮白配方。", "pain": "暗沉無光、熬夜蠟黃、急救提亮。", "skin": "所有膚質、熬夜肌。", "category": "面膜"},
    {"name": "BEYOND YOUTH 極藻保濕精華面膜", "features": "6大深海藻類萃取、微量元素。", "pain": "缺水乾紋、肌膚疲憊、吸收力下降。", "skin": "輕熟肌、缺水肌。", "category": "面膜"},
    {"name": "我的心機 玻尿酸保濕鎖水黑面膜", "features": "備長炭黑膜布、雙重玻尿酸。", "pain": "毛孔髒污、深層缺水、妝前不貼。", "skin": "混合肌、油性肌。", "category": "面膜"},
    {"name": "肌研 光透潤白金修護保濕面膜", "features": "白金微粒、4重玻尿酸、神經醯胺。", "pain": "極度乾燥、屏障受損、換季敏感。", "skin": "敏弱肌、乾性肌。", "category": "面膜"},
    {"name": "LuLuLun Pure 基礎保濕面膜 (粉色)", "features": "天天敷設計、乳酸菌發酵精華。", "pain": "基礎保養不足、皮膚不穩定、懶人保養。", "skin": "所有膚質、學生族。", "category": "面膜"},
    {"name": "Neogence 霓淨思 N3 神經醯胺潤澤保濕面膜", "features": "神經醯胺、高效保濕因子。", "pain": "脫皮、緊繃感、屏障功能弱。", "skin": "乾性肌、敏感肌。", "category": "面膜"},
    {"name": "寵愛之名 乙基維他命C生物纖維面膜", "features": "生物纖維材質、乙基維他命C。", "pain": "頑固斑點、膚色不均、深層美白。", "skin": "追求高階美白者。", "category": "面膜"},
    {"name": "我的心機 縮毛孔控油安瓶面膜", "features": "控油安瓶精華、金縷梅萃取。", "pain": "T字出油、毛孔粗大、黑頭困擾。", "skin": "油性肌、混合肌。", "category": "面膜"},
    {"name": "Dr.Wu 玻尿酸保濕微導面膜 (3入)", "features": "專利玻尿酸、微導棉科技。", "pain": "醫美術後急救、極度缺水、皮膚緊繃。", "skin": "術後肌、敏弱肌。", "category": "面膜"},
    {"name": "提提研 實驗室系列 01角鯊烷修護面膜", "features": "植物性角鯊烷、高純度精華。", "pain": "乾燥脫屑、肌膚粗糙、油水失衡。", "skin": "所有膚質、乾肌。", "category": "面膜"},
    {"name": "SexyLook 酵素亮白面膜", "features": "蔬果酵素萃取、黑面膜布。", "pain": "老廢角質堆積、膚色暗沉、粉刺問題。", "skin": "混合肌、暗沉肌。", "category": "面膜"},

    # 精華
    {"name": "OLAY 專業科研淡斑精華 (第3代)", "features": "高純度B3、SDL、甘草酸二鉀。", "pain": "頑固痘印、色斑、膚色不均。", "skin": "所有膚質、有淡斑需求者。", "category": "精華"},
    {"name": "巴黎萊雅 玻尿酸瞬效保濕水光精華", "features": "1.5%玻尿酸、無添加香料。", "pain": "乾紋細紋、皮膚乾癟、妝前打底。", "skin": "所有膚質、乾性肌。", "category": "精華"},
    {"name": "NIVEA 妮維雅 630淡斑亮白精華 (升級版)", "features": "專利成分Luminous 630。", "pain": "孕斑、曬斑、長期色素沉澱。", "skin": "所有膚質、熟齡肌。", "category": "精華"},
    {"name": "肌研 H.A. Supreme 激亮淡斑精華", "features": "高濃度煙醯胺、維他命C。", "pain": "暗沉無光、膚色蠟黃、局部斑點。", "skin": "所有膚質。", "category": "精華"},
    {"name": "露得清 10% 煙醯胺細緻毛孔精華", "features": "10%煙醯胺、玻尿酸。", "pain": "毛孔粗大、油光滿面、膚質粗糙。", "skin": "油性肌、混合肌。", "category": "精華"},
    {"name": "Neogence 霓淨思 15% C+極透光亮白精華", "features": "15%維他命C衍生物。", "pain": "膚色暗黃、追求極致透亮。", "skin": "一般肌、混合肌。", "category": "精華"},
    {"name": "Dr.Wu 10% 菸鹼醯胺B5舒緩精華", "features": "10%菸鹼醯胺、B5、舒緩成分。", "pain": "肌膚泛紅、屏障受損、燥動不安。", "skin": "敏感肌、所有膚質。", "category": "精華"},
    {"name": "PUR%CENT 璞珥森 10% 煙醯胺煥白精華", "features": "高濃度煙醯胺、極光藻萃取。", "pain": "預算有限的美白需求、暗沉、油水不均。", "skin": "小資族、油性肌。", "category": "精華"},
    {"name": "巴黎萊雅 青春密碼酵素肌底調理精華", "features": "98%高純度酵素萃取。", "pain": "保養吸收停滯、皮膚粗糙、缺乏彈性。", "skin": "所有膚質、追求穩定者。", "category": "精華"},
    {"name": "CeraVe 適樂膚 全效超級修護乳 (含精華)", "features": "三重神經醯胺、煙醯胺。", "pain": "臉部乾癢、紅腫、屏障脆弱。", "skin": "乾敏肌、受損肌。", "category": "精華"},
    {"name": "AHC 醫美級玻尿酸保濕精華", "features": "高純度玻尿酸、多種植萃。", "pain": "韓系水光需求、深層缺水、緊繃。", "skin": "所有膚質、韓系保養愛好者。", "category": "精華"},
    {"name": "Melano CC 高純度維他命C亮白精華", "features": "活性維他命C、E衍生物。", "pain": "痘疤修復、預防斑點、毛孔管理。", "skin": "混合肌、油痘肌。", "category": "精華"},
    {"name": "Tunemakers 神經醯胺前導原液", "features": "高純度神經醯胺、無添加。", "pain": "角質層薄、易敏感、水分易流失。", "skin": "乾敏肌、所有膚質。", "category": "精華"},
    {"name": "Bioderma 貝膚黛瑪 水潤擴散保濕精華", "features": "專利水通道科技、玻尿酸。", "pain": "皮膚缺水暗沈、化妝容易脫屑。", "skin": "所有膚質、缺水肌。", "category": "精華"},
    {"name": "Avene 雅漾 舒敏倍護長效精華露", "features": "雅漾活泉水、舒緩因子。", "pain": "極度敏感、發紅、刺痛。", "skin": "敏弱肌、醫美術後。", "category": "精華"},

    # 洗面乳
    {"name": "雪芙蘭 胺基酸保濕洗面乳", "features": "100%胺基酸洗淨、保濕因子。", "pain": "洗後緊繃、清潔力過強、乾澀。", "skin": "乾性肌、一般肌、敏弱肌。", "category": "洗面乳"},
    {"name": "Biore 蜜妮 淨爽控油洗面乳", "features": "皮脂吸收粉末、清爽控油。", "pain": "洗完沒多久就出油、悶黏感。", "skin": "油性肌、混合肌。", "category": "洗面乳"},
    {"name": "肌研 極潤保濕洗面乳", "features": "雙重玻尿酸、溫和配方。", "pain": "保濕力不足、洗後皮膚乾癢。", "skin": "所有膚質、乾性肌。", "category": "洗面乳"},
    {"name": "專科 超微米潔顏乳 (經典藍)", "features": "濃密泡泡、蠶絲蛋白精華。", "pain": "洗不乾淨、追求綿密泡泡感。", "skin": "所有膚質、大眾首選。", "category": "洗面乳"},
    {"name": "CeraVe 適樂膚 溫和泡沫潔膚露", "features": "神經醯胺、玻尿酸、煙醯胺。", "pain": "洗臉會痛、屏障受損、乾癢發紅。", "skin": "敏弱肌、乾性肌。", "category": "洗面乳"},
    {"name": "Divinia 蒂芬妮亞 胺基酸洗顏霜", "features": "高純度胺基酸、親膚弱酸性。", "pain": "平價好用洗面乳需求、溫和洗淨。", "skin": "所有膚質、小資族。", "category": "洗面乳"},
    {"name": "Neutrogena 露得清 深層淨化洗面乳", "features": "深層清潔技術、控油配方。", "pain": "黑頭粉刺、毛孔髒污殘留。", "skin": "油性肌、混合肌。", "category": "洗面乳"},
    {"name": "Senka 專科 淨荳潔顏泥", "features": "白泥、水楊酸、防荳成分。", "pain": "青春痘、粉刺、油脂過剩。", "skin": "油痘肌。", "category": "洗面乳"},
    {"name": "Hada Labo 肌研 極潤健康深層清潔洗面乳", "features": "薏仁萃取、甘草酸、玻尿酸。", "pain": "肌膚不穩定、粗糙感、暗沉。", "skin": "所有膚質、穩定膚況需求。", "category": "洗面乳"},
    {"name": "La Roche-Posay 理膚寶水 多容安舒緩保濕潔乳", "features": "極簡配方、溫和不刺激。", "pain": "極度敏感、醫美術後、不耐受。", "skin": "敏弱肌、受損肌。", "category": "洗面乳"},

    # 乳霜
    {"name": "雪芙蘭 積雪草水潤凝霜", "features": "積雪草萃取、清爽凝霜質地。", "pain": "乳霜太油膩、曬後泛紅、水分流失。", "skin": "油性肌、混合肌、敏弱肌。", "category": "乳霜"},
    {"name": "OLAY 新生高效緊緻護膚霜 (大紅瓶)", "features": "胜肽、煙醯胺、橄欖油衍生物。", "pain": "細紋鬆弛、缺乏光澤、熟齡乾燥。", "skin": "熟齡肌、中乾性肌。", "category": "乳霜"},
    {"name": "CeraVe 適樂膚 長效潤澤修護霜", "features": "MVE技術、三重神經醯胺。", "pain": "極度乾燥脫屑、冬季癢、屏障受損。", "skin": "乾性肌、敏弱肌、全家人。", "category": "乳霜"},
    {"name": "SKINTIFIC 5X神經醯胺修護保濕霜", "features": "5種神經醯胺、積雪草。", "pain": "換季敏感、外油內乾、屏障薄弱。", "skin": "所有膚質、特別是屏障受損肌。", "category": "乳霜"},
    {"name": "巴黎萊雅 活力緊緻抗皺修護晚霜", "features": "積雪草修護、普拉斯鏈。", "pain": "夜間修復不足、早起臉部暗沉、細紋。", "skin": "熟齡肌、抗老需求者。", "category": "乳霜"},
    {"name": "Curél 潤浸保濕深層乳霜", "features": "潤浸保濕Ceramide成分。", "pain": "乾敏肌專用、洗臉後緊繃脫皮。", "skin": "乾燥敏感肌。", "category": "乳霜"},
    {"name": "肌研 極潤多效精華水感凝露", "features": "一瓶多效 (水、乳、精華、霜)。", "pain": "保養步驟繁瑣、趕時間出門。", "skin": "所有膚質、懶人保養。", "category": "乳霜"},
    {"name": "Aveeno 艾惟諾 燕麥保濕乳霜", "features": "益生菌燕麥、長效保濕。", "pain": "皮膚乾癢發紅、不喜歡香料。", "skin": "敏弱肌、乾性肌。", "category": "乳霜"},
    {"name": "Dr.Wu 玻尿酸保濕精華乳", "features": "第五代玻尿酸配方、清爽乳液。", "pain": "怕油膩但需要保濕、醫美後鎖水。", "skin": "所有膚質、術後肌。", "category": "乳霜"},
    {"name": "NIVEA 妮維雅 霜 (小藍罐)", "features": "經典綿羊油、維他命E。", "pain": "手肘膝蓋乾燥、極乾裂痕、萬用保濕。", "skin": "極乾性肌、身體局部。", "category": "乳霜"},

    # 防曬
    {"name": "Anessa 安耐曬 金鑽高效防曬露NA", "features": "自動修復技術、耐水耐汗。", "pain": "海邊曬傷、戶外運動流汗、防曬脫落。", "skin": "所有膚質、戶外活動肌。", "category": "防曬"},
    {"name": "Biore 蜜妮 含水防曬水凝乳", "features": "超微米防禦技術、清爽如水。", "pain": "防曬黏膩、厚重不透氣、泛白。", "skin": "所有膚質、日常通勤。", "category": "防曬"},
    {"name": "Allie 持采UV高效防曬水凝乳EX", "features": "抗摩擦、海洋友友善配方。", "pain": "口罩摩擦掉防曬、去海邊擔心環境。", "skin": "所有膚質、戶外族。", "category": "防曬"},
    {"name": "La Roche-Posay 理膚寶水 全護清爽防曬液", "features": "專利濾鏡、高防護力。", "pain": "曬老曬黑、皮膚敏感、預防色斑。", "skin": "敏弱肌、所有膚質。", "category": "防曬"},
    {"name": "Suncut 曬可艾 強效防曬噴霧", "features": "大容量、倒著也能噴。", "pain": "身體大面積補擦困難、髮際線曬傷。", "skin": "所有膚質、戶外補擦。", "category": "防曬"},
    {"name": "曼秀雷敦 水潤肌柔光透亮防曬隔離乳", "features": "薰衣草紫校色、光澤微粒。", "pain": "膚色蠟黃、暗沈、妝前飾底需求。", "skin": "蠟黃肌、追求偽素顏者。", "category": "防曬"},
    {"name": "雪芙蘭 海洋友善極效防水防曬乳", "features": "海洋友善、高效防水。", "pain": "水上活動、預算有限、環保考量。", "skin": "所有膚質、水上運動。", "category": "防曬"},
    {"name": "專科 全效防曬水凝乳", "features": "蠶絲蛋白、無香料。", "pain": "防曬後皮膚乾澀、日常防護。", "skin": "混合肌、乾性肌。", "category": "防曬"},
    {"name": "DHC 金靚白水感防曬乳", "features": "輔酶Q10、橄欖精華。", "pain": "高係數但想保有水感、抗氧化。", "skin": "所有膚質、乾性肌。", "category": "防曬"},
    {"name": "Biore 蜜妮 控油隔離乳液", "features": "皮脂吸收粉末、長效持妝。", "pain": "化妝後易出油脫妝、毛孔明顯。", "skin": "極油肌、需妝前者。", "category": "防曬"},

    # 化妝水
    {"name": "肌研 極潤保濕化妝水 (清爽型)", "features": "4重玻尿酸、溫和配方。", "pain": "洗臉後瞬間乾燥、需要基礎補水。", "skin": "所有膚質、油性肌。", "category": "化妝水"},
    {"name": "Imju 薏仁清潤化妝水", "features": "薏仁萃取、大容量高CP。", "pain": "濕敷不心疼、曬後鎮靜、二次清潔。", "skin": "所有膚質、小資族。", "category": "化妝水"},
    {"name": "Avene 雅漾 舒護活泉水", "features": "100%天然活泉水、舒緩鎮靜。", "pain": "肌膚燥熱、泛紅不適、定妝需求。", "skin": "敏感肌、所有膚質。", "category": "化妝水"},
    {"name": "Hada Labo 肌研 白潤美白化妝水", "features": "傳明酸、維他命C。", "pain": "膚色不均、想在第一步就美白。", "skin": "所有膚質、追求美白者。", "category": "化妝水"},
    {"name": "Neogence 霓淨思 玻尿酸保濕化妝水", "features": "高純度玻尿酸、雙分子補水。", "pain": "深度缺水、後續保養吸收差。", "skin": "乾性肌、敏弱肌。", "category": "化妝水"},
    {"name": "Dr.Wu 玻尿酸保濕精華露", "features": "精華液質地、類精華化妝水。", "pain": "極度乾荒、想簡化步驟、醫美後。", "skin": "乾性肌、術後肌。", "category": "化妝水"},
    {"name": "廣源良 絲瓜水", "features": "天然絲瓜萃取、台灣老字號。", "pain": "追求天然成分、控油舒緩、平價。", "skin": "所有膚質、油性肌。", "category": "化妝水"},
    {"name": "Labo Labo 毛孔緊膚化妝水", "features": "乳酸、蘋果酸、毛孔護理。", "pain": "黑頭粉刺、毛孔粗大、角質肥厚。", "skin": "油性肌、混合肌。", "category": "化妝水"},
    {"name": "專科 完美保濕化妝水", "features": "玄米油、蜂蜜、蠶絲蛋白。", "pain": "乾澀緊繃、追求潤澤感。", "skin": "乾性肌、混合偏乾。", "category": "化妝水"},
    {"name": "Minon 氨基酸滋潤保濕化妝水", "features": "11種氨基酸、低刺激。", "pain": "屏障功能低下、換季發癢。", "skin": "敏感肌、乾性肌。", "category": "化妝水"},

    # 卸妝
    {"name": "Bioderma 貝膚黛瑪 舒敏高效潔膚液 (粉紅瓶)", "features": "膠束科技、不需水洗。", "pain": "卸妝刺痛、沒時間洗臉、敏感肌。", "skin": "敏感肌、所有膚質。", "category": "卸妝"},
    {"name": "Biore 蜜妮 深層卸妝油", "features": "高效溶解防水彩妝、手濕可卸。", "pain": "防水睫毛膏難卸、殘留彩妝、粉刺。", "skin": "所有膚質、有濃妝需求者。", "category": "卸妝"},
    {"name": "Divinia 蒂芬妮亞 輕快眼唇卸妝液", "features": "油水分離、溫和不熏眼。", "pain": "眼妝難卸、眼睛刺痛、卸不乾淨。", "skin": "所有膚質、小資族。", "category": "卸妝"},
    {"name": "L`Oreal Paris 巴黎萊雅 溫和眼唇卸妝液", "features": "經典配方、不油膩。", "pain": "眼妝殘留、追求極致乾淨。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "Banila Co Zero 零感肌瞬卸凝霜", "features": "膏狀轉油、深層清潔。", "pain": "卸妝油流滿手、卸妝水卸不淨。", "skin": "所有膚質、韓系控。", "category": "卸妝"},
    {"name": "Hada Labo 肌研 極潤保濕內外兼顧卸妝水", "features": "5重玻尿酸、溫和卸除。", "pain": "卸後皮膚乾澀、日常淡妝卸除。", "skin": "乾性肌、敏弱肌。", "category": "卸妝"},
    {"name": "Senka 專科 超微米眼唇卸妝液", "features": "蠶絲蛋白、無添加。", "pain": "眼周乾燥、追求溫和卸妝。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "Neutrogena 露得清 深層淨化卸妝棉", "features": "便攜設計、一張即卸。", "pain": "旅遊卸妝麻煩、懶得拿化妝棉。", "skin": "所有膚質、旅遊族。", "category": "卸妝"},
    {"name": "Curél 潤浸保濕深層卸妝凝露", "features": "凝露質地、保護Ceramide。", "pain": "卸妝造成泛紅、乾燥感。", "skin": "敏感肌、乾性肌。", "category": "卸妝"},
    {"name": "Softymo 絲芙蒂 乾濕兩用瞬淨卸妝油", "features": "洗澡順便卸妝、高CP值。", "pain": "手濕不能卸妝的困擾。", "skin": "所有膚質。", "category": "卸妝"},

    # 唇部/其他
    {"name": "DHC 橄欖護唇膏", "features": "橄欖精華、親膚性佳。", "pain": "嘴唇脫皮、乾裂、死皮多。", "skin": "乾唇、所有膚質。", "category": "唇部"},
    {"name": "Mentholatum 曼秀雷敦 頂級濃潤柔霜潤唇膏", "features": "遇體溫即化、高保濕。", "pain": "一般護唇膏不夠力、追求極潤。", "skin": "極乾唇。", "category": "唇部"},
    {"name": "Vaseline 凡士林 經典護唇膏 (玫瑰/原味)", "features": "高純度凡士林、鎖水。", "pain": "睡前厚敷、唇紋明顯。", "skin": "所有膚質。", "category": "唇部"},
    {"name": "Nivea 妮維雅 水漾護唇膏", "features": "乳油木果、長效鎖水。", "pain": "日常護唇、口紅打底。", "skin": "所有膚質。", "category": "唇部"},
    {"name": "雪芙蘭 經典滋養霜 (身體用)", "features": "台灣經典配方、維他命E。", "pain": "身體乾燥、預算極低、懷舊感。", "skin": "所有膚質、乾性肌。", "category": "身體保養"},
    {"name": "Vaseline 凡士林 蘆薈舒緩潤膚露", "features": "蘆薈萃取、清爽不黏。", "pain": "夏天身體黏膩、曬後發燙。", "skin": "所有膚質。", "category": "身體保養"},
    {"name": "Nivea 妮維雅 美白潤膚乳液", "features": "維他命C、5天有感。", "pain": "身體膚色暗沈、曬痕明顯。", "skin": "想提亮身體膚色者。", "category": "身體保養"},
    {"name": "Sebamed 施巴 5.5 潔膚露", "features": "pH5.5、溫和不含皂鹼。", "pain": "背部痘痘、皮膚易癢、醫美後。", "skin": "敏感肌、問題肌。", "category": "身體保養"},
    {"name": "Johnson's 強生 嬰兒潤膚油", "features": "純淨礦物油、鎖水力強。", "pain": "洗完澡皮膚極乾、按摩需求。", "skin": "乾性肌、嬰幼兒。", "category": "身體保養"},
    {"name": "Cetaphil 舒特膚 溫和乳霜 (身體/臉兩用)", "features": "低刺激、長效潤澤。", "pain": "全家人共用、換季乾癢。", "skin": "敏弱肌、乾性肌。", "category": "身體保養"},
    {"name": "Dr.Wu 杏仁酸亮白煥膚身體乳", "features": "2%杏仁酸、代謝角質。", "pain": "背部粉刺、毛囊角化 (雞皮)。", "skin": "問題肌、粗糙肌。", "category": "身體保養"},
    {"name": "曼秀雷敦 AD 高效抗乾草本修復乳液", "features": "止癢成分、薄荷感。", "pain": "冬季癢、抓到破皮、極度乾燥。", "skin": "乾癢肌。", "category": "身體保養"},
    {"name": "Sabon 經典身體磨砂膏 (小包裝/體驗)", "features": "死海鹽、天然植物油。", "pain": "身體粗糙、角質厚、追求香氛感。", "skin": "所有膚質。", "category": "身體保養"},
    {"name": "Bioderma 貝膚黛瑪 沐浴油", "features": "專利皮膚防禦、洗護合一。", "pain": "洗澡後皮膚乾澀、屏障受損。", "skin": "極乾肌、敏弱肌。", "category": "身體保養"},
    {"name": "Palmer's 帕瑪氏 可可脂潤膚乳液", "features": "純可可脂、維他命E。", "pain": "孕期肚皮緊繃、乾紋、深層修復。", "skin": "乾性肌、孕婦。", "category": "身體保養"},
]

added_count = 0
for item in new_items:
    if item["name"] not in existing_names:
        data.append(item)
        existing_names.add(item["name"])
        added_count += 1
    if added_count >= 100:
        break

DB_PATH.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Added {added_count} items. Total: {len(data)}")
