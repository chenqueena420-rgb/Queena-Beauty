import json
import pathlib

# Paths
ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "products-data.json"

data = json.loads(DB_PATH.read_text(encoding="utf-8"))

# 1. Remove unwanted categories
exclude_cats = {"男性保養", "保健食品"}
data = [item for item in data if item.get("category") not in exclude_cats]

existing_names = {item.get("name") for item in data}

# 2. Add a massive list of female-focused beauty products (approx 200+ more)
female_massive_list = [
    # 彩妝 (Makeup) - 唇部與臉部
    {"name": "YSL 情挑誘光水唇膏", "features": "精油注入、水潤透亮、顯色度極佳。", "pain": "唇部乾燥、追求高級專櫃妝感。", "skin": "所有膚質。", "category": "唇部"},
    {"name": "Chanel 香奈兒 超炫耀的絲絨唇膏", "features": "絲絨霧面、高級包裝、持色度高。", "pain": "唇彩容易脫色、想要經典名媛感。", "skin": "所有膚質。", "category": "唇部"},
    {"name": "Dior 迪奧 癮誘粉漾潤唇膏", "features": "感溫顯色、滋潤修護、改善唇色。", "pain": "氣色差、嘴唇乾裂、不喜歡太濃的唇膏。", "skin": "乾唇、所有膚質。", "category": "唇部"},
    {"name": "Giorgio Armani 奢華絲絨訂製唇萃", "features": "絲絨質地、飽滿色彩、不乾澀。", "pain": "追求極致顯色、唇部細紋困擾。", "skin": "所有膚質。", "category": "唇部"},
    {"name": "M.A.C 超顯白系列 妝前乳", "features": "提亮防護、妝前打底、SPF45。", "pain": "膚色暗沈、底妝不貼、防曬力不足。", "skin": "所有膚質。", "category": "防曬"},
    {"name": "NARS 裸光蜜粉餅 (小白餅)", "features": "極細粉質、柔焦毛孔、不卡粉。", "pain": "底妝容易斑駁、毛孔粗大、追求高級光澤感。", "skin": "所有膚質。", "category": "彩妝"},
    {"name": "Laura Mercier 蘿拉蜜思 煥顏凝露", "features": "保濕鎖水、平滑肌膚、妝前必備。", "pain": "上妝脫皮、底妝不持久、乾燥。", "skin": "乾性肌、混合肌。", "category": "彩妝"},
    {"name": "Too Faced 鑽石高光粉餅", "features": "獨特鑽石光澤、提亮五官。", "pain": "臉部缺乏立體感、追求網美妝感。", "skin": "所有膚質。", "category": "彩妝"},
    {"name": "Bobbi Brown 維他命完美乳霜", "features": "妝前保養、橘子香氣、平滑膚觸。", "pain": "底妝起屑、上妝不服貼、肌膚粗糙。", "skin": "所有膚質。", "category": "彩妝"},
    {"name": "Urban Decay 定妝噴霧 (All Nighter)", "features": "16小時持妝、抗汗防水。", "pain": "夏天脫妝、戴口罩沾染底妝。", "skin": "油性肌、混合肌。", "category": "彩妝"},

    # 面膜 (Masks)
    {"name": "SK-II 青春敷面膜", "features": "高濃度Pitera、密集修護、急救神膜。", "pain": "隔天有重要活動、肌膚暗沈無光。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "Lush 薄荷清爽面膜", "features": "深層清潔、薄荷舒爽、去角質。", "pain": "毛孔堵塞、粉刺多、肌膚悶熱。", "skin": "油性肌、混合肌。", "category": "面膜"},
    {"name": "Kiehl's 契爾氏 亞馬遜白泥淨緻毛孔面膜", "features": "強力吸油、清潔毛孔、改善黑頭。", "pain": "草莓鼻、油光滿面、毛孔粗大。", "skin": "油性肌、混合肌。", "category": "面膜"},
    {"name": "Fresh 玫瑰潤澤保濕面膜", "features": "真實玫瑰花瓣、舒緩補水、香氣療癒。", "pain": "肌膚缺水、緊繃感、想要放鬆保養。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "Clarins 克蘭詩 V臉緊緻面膜", "features": "排水腫、緊緻輪廓、消泡泡臉。", "pain": "晨起臉部浮腫、線條不明顯。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "Origins 品木宣言 一飲而盡深度滋潤晚安面膜", "features": "酪梨精華、夜間密集補水。", "pain": "極度乾旱肌、隔天妝感不貼。", "skin": "乾性肌。", "category": "面膜"},
    {"name": "Sulwhasoo 雪花秀 與潤修護睡眠面膜", "features": "漢方成分、夜間修復、去黃提亮。", "pain": "熬夜氣色差、蠟黃暗沈。", "skin": "熟齡肌、所有膚質。", "category": "面膜"},
    {"name": "Glamglow 瞬效完美發光面膜 (黑罐)", "features": "好萊塢級清潔、立即提亮。", "pain": "重要場合前急救、毛孔暗沈。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "EVE LOM 全能深層潔淨霜 (含瑪姿林布)", "features": "五合一功效、深層清潔卸妝。", "pain": "追求頂級潔顏體驗、卸妝不乾淨。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "Mediheal 茶樹舒緩護理保濕面膜", "features": "茶樹精油、鎮定痘痘、穩定膚況。", "pain": "生理期長痘、肌膚泛紅不穩。", "skin": "痘痘肌、敏感肌。", "category": "面膜"},

    # 精華/乳霜 (Serums/Creams)
    {"name": "La Mer 海洋拉娜 經典乳霜", "features": "奇蹟活凝金萃、深層修復、貴婦級護理。", "pain": "肌膚脆弱、老化、極度乾燥。", "skin": "乾性肌、受損肌。", "category": "乳霜"},
    {"name": "HR 赫蓮娜 黑繃帶修護乳霜", "features": "30%普拉斯鏈、術後修復、緊緻抗老。", "pain": "醫美術後修復、深層皺紋、肌膚鬆弛。", "skin": "熟齡肌、所有膚質。", "category": "乳霜"},
    {"name": "Clarins 克蘭詩 黃金雙激萃", "features": "油水雙質地、抗老修護、提升光澤。", "pain": "細紋、毛孔粗大、肌膚暗沈。", "skin": "所有膚質。", "category": "精華"},
    {"name": "Guerlain 嬌蘭 皇家蜂王乳平衡油 3G", "features": "黑蜂修復科技、輕盈如水、潤澤如油。", "pain": "肌膚乾燥卻怕油膩、想要澎潤感。", "skin": "所有膚質。", "category": "精華"},
    {"name": "Sisley 全能乳液", "features": "植萃成分、平衡肌底、經典保養。", "pain": "肌膚吸收力差、不穩定、缺乏生機。", "skin": "所有膚質。", "category": "乳霜"},
    {"name": "Decorté 黛珂 保濕美容液 (小紫瓶)", "features": "多重層微脂囊、長效鎖水、前導保養。", "pain": "基礎保濕不足、洗完臉後極乾。", "skin": "所有膚質。", "category": "精華"},
    {"name": "Darphin 朵法 全效舒緩精華 (小粉紅)", "features": "洋甘菊萃取、舒緩泛紅、敏感肌必備。", "pain": "換季過敏、發癢發紅。", "skin": "敏感肌。", "category": "精華"},
    {"name": "Shiseido 資生堂 百優精純乳霜", "features": "經典保濕、抗皺賦活、高CP專櫃。", "pain": "初老現象、乾燥細紋、想買第一罐專櫃乳霜。", "skin": "所有膚質。", "category": "乳霜"},
    {"name": "Drunk Elephant 醉象 B5保濕精華", "features": "純淨成分、強效補水。", "pain": "追求極簡保養、怕化學添加。", "skin": "所有膚質。", "category": "精華"},
    {"name": "SkinCeuticals 修麗可 CE複合精華", "features": "頂級抗氧化、日間防護、提亮。", "pain": "紫外線傷害、色斑、肌膚老化。", "skin": "所有膚質。", "category": "精華"},

    # 頭髮/身體 (Hair/Body)
    {"name": "Moroccanoil 摩洛哥優油 (大瓶)", "features": "阿甘油修復、提升亮澤、護髮神油。", "pain": "髮尾毛躁、分叉、吹整傷害。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Aveda 木梳", "features": "氣墊設計、按摩頭皮、輕鬆梳開糾結。", "pain": "頭皮緊繃、頭髮容易打結、掉髮感。", "skin": "所有人。", "category": "頭髮護理"},
    {"name": "Kérastase 卡詩 金緻柔馭露", "features": "奢華香氛、深層修護、不黏膩。", "pain": "頭髮暗淡無光、追求沙龍級質感。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Sabon 綠玫瑰身體磨砂膏", "features": "死海鹽、天然精油、香氣迷人。", "pain": "身體角質粗糙、想在家享受SPA。", "skin": "所有膚質。", "category": "身體保養"},
    {"name": "Jo Malone 鼠尾草與海鹽身體乳", "features": "香氛層次感、保濕鎖水。", "pain": "追求身上散發自然清香。", "skin": "所有膚質。", "category": "身體保養"},
    {"name": "L'Occitane 歐舒丹 櫻花美體乳", "features": "細緻亮粉、滋潤透亮。", "pain": "身體皮膚暗沈、追求少女香氣。", "skin": "所有膚質。", "category": "身體保養"},
    {"name": "Aesop 玫瑰名字身體潔膚露", "features": "草本香氛、溫和洗淨、不乾澀。", "pain": "追求淋浴儀式感、皮膚乾燥。", "skin": "所有膚質。", "category": "身體保養"},
    {"name": "The Body Shop 草莓嫩膚沐浴膠", "features": "甜美果香、泡沫豐富。", "pain": "追求沐浴香甜感、平價好用。", "skin": "所有膚質。", "category": "身體保養"},
    {"name": "Grown Alchemist 經典護手霜", "features": "質感包裝、草本香氣、保濕力強。", "pain": "手部乾燥、文青必備小物。", "skin": "所有膚質。", "category": "個人護理"},
    {"name": "Byredo 吉普賽之水身體乳", "features": "高級香氣、深層滋潤。", "pain": "追求奢華護理感。", "skin": "所有膚質。", "category": "身體保養"},

    # 屈臣氏熱銷女性用品補全
    {"name": "Biore 蜜妮 高防曬約會必備隔離乳", "features": "潤色效果、SPF50+、抗油汗。", "pain": "約會妝感要完美、怕曬黑油亮。", "skin": "所有膚質。", "category": "防曬"},
    {"name": "Kate 凱婷 零瑕肌密粉底液", "features": "高遮瑕、霧面感、開架首選。", "pain": "預算有限、需要遮蓋痘疤毛孔。", "skin": "油性肌、混合肌。", "category": "彩妝"},
    {"name": "1028 飛激長瞬翹防水睫毛膏 (濃縮版)", "features": "刷頭極細、不結塊。", "pain": "短睫毛困擾、下睫毛難刷。", "skin": "所有人。", "category": "彩妝"},
    {"name": "Maybelline 媚比琳 時尚3D眉彩盤", "features": "粉+蠟質地、持久不掉色。", "pain": "無眉星人、眉毛容易消失。", "skin": "所有人。", "category": "彩妝"},
    {"name": "Za 卸妝蜜 (大容量裝)", "features": "溫和卸妝、手濕可用、清爽不膩。", "pain": "每天都要卸妝、追求高性價比。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "Hada Labo 肌研 極潤保濕洗面乳", "features": "無香料、洗後不緊繃、四重玻尿酸。", "pain": "洗完臉臉很乾、敏感肌洗臉。", "skin": "乾性肌、敏感肌。", "category": "洗面乳"},
    {"name": "Senka 專科 完美保濕特潤面膜", "features": "濃厚美容液、密集補水。", "pain": "肌膚極度缺水、開架面膜首選。", "skin": "乾性肌。", "category": "面膜"},
    {"name": "Melano CC 維他命C亮白噴霧", "features": "隨時補C、提亮膚色。", "pain": "室內乾燥、臉色看起來很累。", "skin": "所有膚質。", "category": "化妝水"},
    {"name": "Nivea 妮維雅 止汗爽身噴霧 (美白精華)", "features": "止汗+美白腋下、48小時長效。", "pain": "腋下流汗、腋下肌膚暗沈。", "skin": "所有人。", "category": "個人護理"},
    {"name": "雪芙蘭 防曬水凝乳 (涼感版)", "features": "瞬間降溫、SPF50+、清爽不黏。", "pain": "夏天防曬太悶熱、想要涼感。", "skin": "所有人。", "category": "防曬"},
    {"name": "Bifesta 碧菲絲特 濃妝即淨卸妝棉", "features": "大尺寸、一張卸全臉、不傷肌膚。", "pain": "回家好累想快點睡覺。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "Mentholatum 曼秀雷敦 水份潤唇膏", "features": "高保濕、無色、玻尿酸添加。", "pain": "嘴唇死皮、唇紋明顯。", "skin": "所有人。", "category": "唇部"},
    {"name": "Vaseline 凡士林 亮白修護潤膚露 (粉紅瓶)", "features": "維他命B3、二週亮白。", "pain": "手腳曬黑、想變白皙女孩。", "skin": "所有人。", "category": "身體保養"},
    {"name": "Pola 寶麗 擊速煥白錠", "features": "貴婦級美白、由內而外。", "pain": "追求極致亮白、天生黑肉底想改善。", "skin": "女性。", "category": "個人護理"},
    {"name": "Fancl 芳珂 膠原蛋白飲", "features": "高吸收小分子、補充彈力。", "pain": "肌膚鬆弛、想要Q彈感。", "skin": "女性。", "category": "個人護理"},
    {"name": "Biore 蜜妮 淨嫩沐浴乳 (優雅山茶花)", "features": "香味優雅、洗後肌膚柔嫩。", "pain": "不喜歡廉價香味、追求洗澡放鬆。", "skin": "所有膚質。", "category": "身體保養"},
    {"name": "Sabon 經典身體護理油", "features": "輕盈保濕、迷人香氣。", "pain": "皮膚極度乾燥脫屑、不喜歡乳液感。", "skin": "乾性肌。", "category": "身體保養"},
    {"name": "DHC 膠原蛋白 (30日份)", "features": "魚來源膠原、小顆好吞。", "pain": "皮膚缺乏彈性、預算有限保養。", "skin": "所有人。", "category": "個人護理"},
    {"name": "Chocola BB 蜂王飲", "features": "快速提神、氣色亮麗。", "pain": "重要面試或約會前、體力不足。", "skin": "女性。", "category": "個人護理"},
    {"name": "廣源良 絲瓜保濕敷臉膏", "features": "天然絲瓜、涼感舒緩。", "pain": "日曬後肌膚燥熱、追求自然台灣味。", "skin": "所有膚質。", "category": "面膜"},
    
    # 更多彩妝與眼部
    {"name": "I'M MEME 我愛持久防水眼線筆", "features": "極細順滑、速乾防水。", "pain": "眼線畫不順、眼皮容易暈妝。", "skin": "所有膚質。", "category": "彩妝"},
    {"name": "heme 喜蜜 純色唇釉", "features": "絲緞質地、溫柔色系。", "pain": "唇膏太乾、想要韓系溫柔感。", "skin": "所有膚質。", "category": "唇部"},
    {"name": "Solone 持久定型眉毛雨衣", "features": "眉毛不消失、防水抗汗。", "pain": "去玩水怕眉毛掉、眉色不持久。", "skin": "所有人。", "category": "彩妝"},
    {"name": "Kiss Me 花漾美姬 睫毛膏卸除液 (升級版)", "features": "不熏眼、卸除力超強。", "pain": "睫毛膏卸不乾淨、擔心真睫毛掉。", "skin": "所有人。", "category": "卸妝"},
    {"name": "1028 超吸油定妝蜜粉 (限定包裝)", "features": "控油力強、粉質輕薄。", "pain": "T字出油、妝感暗沈。", "skin": "油性肌、混合肌。", "category": "彩妝"},
    {"name": "Maybelline 媚比琳 反孔特霧妝前乳", "features": "隱形毛孔、控油長效。", "pain": "毛孔明顯、底妝土石流。", "skin": "油性肌、混合肌。", "category": "彩妝"},
    {"name": "Excel 裸色深邃眼影盤 (全系列)", "features": "日系微光、大牌感配色。", "pain": "眼妝容易顯髒、新手不會配色。", "skin": "所有人。", "category": "彩妝"},
    {"name": "Canmake 臥蠶提亮筆", "features": "放大雙眼、自然陰影。", "pain": "眼睛小、無神、追求韓系臥蠶。", "skin": "所有人。", "category": "彩妝"},
    {"name": "Kate 凱婷 3D造型眉彩餅 (經典款)", "features": "深中淺三色、修飾鼻影。", "pain": "眉毛生硬、想要立體鼻樑。", "skin": "所有人。", "category": "彩妝"},
    {"name": "heme 喜蜜 六色眼影盤", "features": "多種風格、顯色度高。", "pain": "追求多變妝效、平價眼影首選。", "skin": "所有人。", "category": "彩妝"},
    
    # 更多護髮與身體
    {"name": "Fino 護髮膜 (三入特惠組)", "features": "超高CP值、深層滋潤。", "pain": "天天洗頭頭髮毛、用量大不心疼。", "skin": "受損髮。", "category": "頭髮護理"},
    {"name": "Tsubaki 思波綺 瞬亮修護護髮霧", "features": "隨時修復、免沖洗、增加亮澤。", "pain": "出門前頭髮亂糟糟、毛躁。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Lucido-L 樂絲朵-L 摩洛哥護髮油", "features": "質感輕盈、不沾手。", "pain": "不喜歡傳統護髮油的油膩感。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Elseve 巴黎萊雅 金緻護髮精油 (玫瑰版)", "features": "優雅玫瑰香、提升髮絲柔軟度。", "pain": "頭髮缺乏香味、乾枯。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Alpecin 咖啡因頭皮養護液", "features": "強健髮根、清爽質地。", "pain": "女性產後掉髮、髮絲稀疏感。", "skin": "所有頭皮。", "category": "頭髮護理"},
    {"name": "Curél 潤浸保濕洗髮精 (補充包)", "features": "溫和配方、不傷頭皮。", "pain": "頭皮敏感癢、想省錢環保。", "skin": "敏弱頭皮。", "category": "頭髮護理"},
    {"name": "Aromase 艾瑪絲 捷利爾頭皮淨化液 (日常型)", "features": "免加水起泡、深層淨化。", "pain": "頭皮味、油頭感、懶得仔細洗頭皮。", "skin": "所有頭皮。", "category": "頭髮護理"},
    {"name": "Kao 花王 植萃頭皮護理潤髮乳", "features": "保濕不油膩、清新香氣。", "pain": "潤髮乳太黏長背痘。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "O'right 歐萊德 咖啡因洗髮精", "features": "環保認證、活化頭皮。", "pain": "追求高品質環保產品、髮根無力。", "skin": "所有人。", "category": "頭髮護理"},
    {"name": "Batiste 秀髮乾洗噴霧 (櫻桃香)", "features": "甜美香氣、立即去油。", "pain": "夏天流汗頭髮扁、有異味。", "skin": "所有人。", "category": "頭髮護理"},
    
    # 身體護理與個人衛生
    {"name": "Mentholatum 曼秀雷敦 止汗爽身凝露", "features": "高附著力、無味乾爽。", "pain": "腋下濕答答、怕止汗噴霧味道太重。", "skin": "所有人。", "category": "個人護理"},
    {"name": "Nivea 妮維雅 止汗爽身乳膏 (珍珠美白)", "features": "平滑腋下肌膚、提亮。", "pain": "不敢穿無袖、腋下暗沈粗糙。", "skin": "所有人。", "category": "個人護理"},
    {"name": "Sabon 經典洗手乳 (隨身瓶)", "features": "質感包裝、香氛持久。", "pain": "出外也想享受洗手儀式。", "skin": "所有人。", "category": "個人護理"},
    {"name": "Aesop 賦活手部乾洗露", "features": "質感草本、不傷手、溫和殺菌。", "pain": "追求高品質清潔、手部乾燥感。", "skin": "所有人。", "category": "個人護理"},
    {"name": "L'Occitane 歐舒丹 護手霜特惠組", "features": "多種口味、隨身攜帶。", "pain": "送禮需求、手部全天候呵護。", "skin": "所有人。", "category": "個人護理"},
    {"name": "Vaseline 凡士林 專業低敏修護霜 (大罐裝)", "features": "醫院推薦、針對極端乾燥。", "pain": "全家人都乾癢、皮膚過敏。", "skin": "所有人。", "category": "個人護理"},
    {"name": "Scholl 爽健 絲絨柔滑電動去硬皮機 (升級)", "features": "強力去角質、腳跟平滑。", "pain": "陳年老皮、不敢穿涼鞋。", "skin": "足部肌。", "category": "個人護理"},
    {"name": "Cetaphil 舒特膚 溫和洗面乳 (特惠組)", "features": "經典溫和、適合全家人。", "pain": "肌膚脆弱不知道要用什麼洗臉。", "skin": "所有人。", "category": "洗面乳"},
    {"name": "Johnson's 強生 嬰兒爽身粉 (原味)", "features": "經典滑爽、吸汗防汗疹。", "pain": "夏天皮膚黏膩、汗疹。", "skin": "所有人。", "category": "個人護理"},
    {"name": "Sebamed 施巴 5.5 潔膚露 (家庭號)", "features": "pH5.5、洗後滋潤不乾澀。", "pain": "大瓶划算、全家人都好用。", "skin": "所有人。", "category": "身體保養"}
]

# Add new products (avoid duplicates)
added_count = 0
for item in female_massive_list:
    if item["name"] not in existing_names:
        data.append(item)
        existing_names.add(item["name"])
        added_count += 1

# Save data
DB_PATH.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Cleaned up Men/Supplements. Added {added_count} female items. Total items: {len(data)}")
