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

# Adding 100 more varied Watson's items across categories
new_items_2 = [
    # 彩妝/唇部
    {"name": "1028 飛激長瞬翹防水睫毛膏 (黑)", "features": "超長纖維、防水抗汗、不暈染。", "pain": "睫毛短塌、熊貓眼、脫妝困擾。", "skin": "所有膚質。", "category": "彩妝"},
    {"name": "Maybelline 媚比琳 超持久霧感液態唇膏", "features": "16小時不掉色、絲絨霧面。", "pain": "頻繁補妝、唇膏沾杯、持久度不足。", "skin": "所有膚質。", "category": "唇部"},
    {"name": "Kate 凱婷 視覺立體眉彩膏", "features": "顯色持久、修飾眉色。", "pain": "眉色不均、妝感生硬、易掉色。", "skin": "所有膚質。", "category": "彩妝"},
    {"name": "Za 美白隔離霜 (經典版)", "features": "提亮防護、SPF26/PA++。", "pain": "膚色蠟黃、防曬不足、妝前不平滑。", "skin": "所有膚質。", "category": "防曬"},
    {"name": "I'M MEME 我愛水凝好氣色唇頰露", "features": "水感質地、自然顯色。", "pain": "氣色差、懶人彩妝、追求自然感。", "skin": "所有膚質。", "category": "唇部"},
    {"name": "heme 喜蜜 純色腮紅", "features": "粉質細緻、礦物成分。", "pain": "雙頰無血色、妝感厚重、預算有限。", "skin": "所有膚質。", "category": "彩妝"},
    {"name": "Kiss Me 花漾美姬 零阻力經典復古棕眼線液筆", "features": "速乾抗汗、筆頭極細。", "pain": "眼線易暈、線條不順、妝感太銳利。", "skin": "所有膚質。", "category": "彩妝"},
    {"name": "Opera 渲漾水色唇膏", "features": "水潤透亮、顯色度佳。", "pain": "唇部乾燥、死皮、追求清透妝感。", "skin": "乾唇、所有膚質。", "category": "唇部"},
    {"name": "Essence 艾森絲 超霧光定妝粉餅", "features": "吸油力強、平價高效。", "pain": "T字出油、妝感暗沉、脫妝。", "skin": "油性肌、混合肌。", "category": "彩妝"},
    {"name": "Canmake 花漾戀愛修容組", "features": "多色混合、自然光澤。", "pain": "追求日系妝感、修容不自然。", "skin": "所有膚質。", "category": "彩妝"},

    # 頭髮護理 (新增類別)
    {"name": "Tsubaki 思波綺 瞬亮修護髮膜", "features": "沙龍級修護、快速滲透。", "pain": "髮質受損、毛躁、缺乏光澤。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "O'right 歐萊德 綠茶洗髮精", "features": "天然植萃、環保配方。", "pain": "頭皮出油、化學殘留感、環境考量。", "skin": "油性頭皮。", "category": "頭髮護理"},
    {"name": "Fino 高效滲透修護髮油", "features": "修復分叉、柔順不黏膩。", "pain": "髮尾乾枯、打結、熱傷害受損。", "skin": "乾性髮質。", "category": "頭髮護理"},
    {"name": "Elseve 巴黎萊雅 金緻護髮精油", "features": "珍稀花卉精油、亮澤秀髮。", "pain": "頭髮暗淡、毛躁難整理。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Aromase 艾瑪絲 5α捷利爾頭皮進化液", "features": "草本去屑、深層淨化。", "pain": "頭皮屑、頭皮癢、脂漏性問題。", "skin": "問題頭皮。", "category": "頭髮護理"},
    {"name": "Pantene 潘婷 爆水膠囊髮膜", "features": "膠囊保鮮、密集修護。", "pain": "急救護髮、乾燥稻草髮。", "skin": "極受損髮。", "category": "頭髮護理"},
    {"name": "Lucido-L 樂絲朵-L 酸熱修護髮油", "features": "熱修復技術、改善髮質。", "pain": "長期染燙受損、吹風機熱傷害。", "skin": "受損髮質。", "category": "頭髮護理"},
    {"name": "Shiseido 資生堂 芯之麗 盈潤修護洗髮露", "features": "保濕鎖水、修護髮芯。", "pain": "洗後乾澀、秀髮扁塌。", "skin": "一般髮質、乾性髮。", "category": "頭髮護理"},
    {"name": "Alpecin 咖啡因洗髮露", "features": "強化髮根、活化頭皮。", "pain": "落髮困擾、髮絲細軟、頭皮不健康。", "skin": "男性及細軟髮。", "category": "頭髮護理"},
    {"name": "Moroccanoil 摩洛哥優油", "features": "阿甘油成分、護髮神油。", "pain": "高級護髮需求、極度毛躁。", "skin": "所有髮質。", "category": "頭髮護理"},

    # 口腔護理 (新增類別)
    {"name": "Marvis 經典薄荷牙膏 (綠色)", "features": "精品包裝、強勁薄荷。", "pain": "口氣問題、追求高品質生活感。", "skin": "成人。", "category": "個人護理"},
    {"name": "Darlie 好來 全亮白牙膏", "features": "分解牙垢、亮白去漬。", "pain": "牙齒發黃、咖啡漬、茶漬。", "skin": "成人。", "category": "個人護理"},
    {"name": "Ora2 me 淨白無瑕牙膏 (白茶花香)", "features": "溫和去漬、療癒香氣。", "pain": "追求牙齒亮白、不喜歡辛辣味。", "skin": "成人。", "category": "個人護理"},
    {"name": "Listerine 李施德霖 全效護理漱口水", "features": "6大功效、長效抑菌。", "pain": "口臭困擾、預防蛀牙、牙周問題。", "skin": "成人。", "category": "個人護理"},
    {"name": "Oral-B 歐樂B 牙線棒 (薄荷)", "features": "強韌不易斷、深入清潔。", "pain": "牙縫殘留、牙籤傷牙齦。", "skin": "所有人群。", "category": "個人護理"},

    # 面膜/保養
    {"name": "Abib 魚腥草舒緩面膜", "features": "高純度魚腥草、服貼膜布。", "pain": "肌膚過敏、紅腫癢、保養停滯。", "skin": "敏感肌、痘痘肌。", "category": "面膜"},
    {"name": "Torriden 潛水艇玻尿酸面膜", "features": "5重微分子玻尿酸、韓系熱銷。", "pain": "深層缺水、醫美後極乾。", "skin": "所有膚質、乾性肌。", "category": "面膜"},
    {"name": "Medipeel 膠原蛋白撕拉面膜", "features": "緊緻毛孔、提升彈性。", "pain": "毛孔鬆弛、臉部線條不明顯。", "skin": "熟齡肌、混合肌。", "category": "面膜"},
    {"name": "Anua 魚腥草 77% 舒緩化妝水", "features": "77%魚腥草、韓系爆紅。", "pain": "肌膚燥熱、粉刺泛紅。", "skin": "油痘肌、敏感肌。", "category": "化妝水"},
    {"name": "Innisfree 綠茶籽玻尿酸保濕精華", "features": "綠茶萃取、高效補水。", "pain": "基礎保濕不足、肌膚粗糙。", "skin": "所有膚質。", "category": "精華"},
    {"name": "Laneige 蘭芝 晚安水凝膜", "features": "夜間鎖水技術、水潤Q彈。", "pain": "隔天妝感不貼、睡眠不足。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "Cosrx 蝸牛黏液精華液", "features": "96%蝸牛萃取、修護力強。", "pain": "痘疤修復、皮膚暗沉無光。", "skin": "所有膚質、油性肌。", "category": "精華"},
    {"name": "ROUND LAB 白樺樹保濕防曬霜", "features": "白樺樹汁、清爽不厚重。", "pain": "不喜歡防曬油膩、怕長痘。", "skin": "所有膚質、乾性肌。", "category": "防曬"},
    {"name": "Beauty of Joseon 朝鮮美女 人參精華水", "features": "80%人參根水、傳統植萃。", "pain": "肌膚暗沈、缺乏生機。", "skin": "所有膚質、熟齡肌。", "category": "化妝水"},
    {"name": "Medicube 零毛孔爽膚棉", "features": "酸類成分、雙面設計。", "pain": "黑頭粉刺、角質粗糙、出油。", "skin": "油性肌、混合肌。", "category": "化妝水"},

    # 洗面乳/卸妝
    {"name": "Fancl 芳珂 淨化卸妝油", "features": "無添加、快速乳化。", "pain": "敏感肌卸妝、擔心毛孔阻塞。", "skin": "敏感肌、所有膚質。", "category": "卸妝"},
    {"name": "Attenir 艾天然 淨潔卸妝油", "features": "柑橘香氣、改善暗沉。", "pain": "卸妝不夠乾淨、膚色灰暗。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "Kanebo 佳麗寶 酵素洗顏粉", "features": "蛋白分解酵素、獨立包裝。", "pain": "毛孔髒污、旅遊保養、粉刺困擾。", "skin": "混合肌、油性肌。", "category": "洗面乳"},
    {"name": "Bifesta 碧菲絲特 溫和即淨卸妝水", "features": "不含油分、卸妝保濕。", "pain": "淡妝卸除、趕時間、接睫毛可用。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "Cow Brand 牛乳石鹼 滋潤沐浴乳", "features": "綿密泡沫、保濕護膚。", "pain": "洗後皮膚乾癢、平價首選。", "skin": "所有膚質。", "category": "身體保養"},

    # 防曬/其他
    {"name": "Skin Aqua 曼秀雷敦 超保濕水感防曬露", "features": "SPF50+/PA++++、大容量。", "pain": "身體防曬預算、追求極致清爽。", "skin": "所有膚質。", "category": "防曬"},
    {"name": "Curél 潤浸保濕防曬乳", "features": "純物理防曬、低刺激。", "pain": "化學防曬敏感、嬰兒可用。", "skin": "極敏感肌。", "category": "防曬"},
    {"name": "La Roche-Posay 理膚寶水 B5彈潤修復凝乳", "features": "積雪草修護、保濕鎖水。", "pain": "術後脫屑、紅腫發熱。", "skin": "受損肌、敏弱肌。", "category": "乳霜"},
    {"name": "Avène 雅漾 控油清爽潔膚凝膠", "features": "葡萄糖酸鋅、活泉水。", "pain": "青春痘、出油旺盛、洗後舒緩。", "skin": "油痘肌。", "category": "洗面乳"},
    {"name": "CeraVe 適樂膚 SA平滑復修潔膚露", "features": "水楊酸、神經醯胺。", "pain": "毛囊角化、粗糙雞皮、粉刺。", "skin": "問題肌、粗糙肌。", "category": "洗面乳"},

    # 身體/個人護理
    {"name": "Bio-Oil 百洛護膚油", "features": "淡化痕跡、改善紋路。", "pain": "妊娠紋、肥胖紋、疤痕、乾燥。", "skin": "所有膚質、孕婦。", "category": "身體保養"},
    {"name": "Sabon 經典洗手乳", "features": "天然精油、香氛持久。", "pain": "洗手後乾裂、追求儀式感。", "skin": "所有膚質。", "category": "個人護理"},
    {"name": "L'Occitane 歐舒丹 乳油木護手霜", "features": "20%乳油木果油、經典款。", "pain": "手部極乾、龜裂、指緣乾燥。", "skin": "乾性肌。", "category": "個人護理"},
    {"name": "Aesop 賦活芳香護手霜", "features": "草本香氛、保濕不膩。", "pain": "不喜歡化學香味、手部保養需求。", "skin": "所有膚質。", "category": "個人護理"},
    {"name": "Eucerin 伊思妮 強效修護身體乳", "features": "尿素成分、長效鎖水。", "pain": "魚鱗病樣乾燥、極度乾癢。", "skin": "極乾性肌。", "category": "身體保養"},

    # 補充更多項目以湊足 100 筆
    {"name": "Neutrogena 露得清 凝耳洗髮精", "features": "去油力強、經典配方。", "pain": "頑固油頭、頭皮味。", "skin": "極油頭皮。", "category": "頭髮護理"},
    {"name": "Schwarzkopf 施華蔻 羊絨脂修護髮膜", "features": "深層滋養、柔順亮澤。", "pain": "頭髮像稻草、染燙損傷。", "skin": "極受損髮。", "category": "頭髮護理"},
    {"name": "Ryo 呂 滋養韌髮洗髮精", "features": "人參精華、強韌髮根。", "pain": "細軟扁塌、掉髮感、中藥味愛好者。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Head & Shoulders 海倫仙度絲 去屑洗髮乳", "features": "ZP成分、快速去屑。", "pain": "雪花飄飄、頭皮癢。", "skin": "有頭皮屑困擾者。", "category": "頭髮護理"},
    {"name": "Klorane 蔻蘿蘭 養髮洗髮精", "features": "金雞納萃取、強健髮絲。", "pain": "產後落髮、壓力掉髮。", "skin": "脆弱髮絲。", "category": "頭髮護理"},
    {"name": "Clear 淨 去屑洗髮乳", "features": "清涼感、深層去屑。", "pain": "男性頭皮屑、夏天悶熱。", "skin": "男性、油性頭皮。", "category": "頭髮護理"},
    {"name": "Batiste 秀髮乾洗噴霧", "features": "澱粉去油、立即蓬鬆。", "pain": "沒洗頭出門、坐月子、瀏海油膩。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Tangle Teezer 王妃梳", "features": "獨特齒梳、輕鬆解結。", "pain": "頭髮易斷、難梳開、頭皮按摩。", "skin": "所有髮質。", "category": "頭髮護理"},
    {"name": "Utena 佑天蘭 黃金果凍面膜 (玻尿酸)", "features": "33g精華液、極致滋潤。", "pain": "極度乾渴肌、追求厚重滋養感。", "skin": "乾性肌。", "category": "面膜"},
    {"name": "Saborino 早安面膜 (經典款)", "features": "60秒保養、洗臉+保養+妝前。", "pain": "早上趕時間、懶人必備。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "Quality 1st 皇后的秘密 高保濕面膜", "features": "不含防腐劑、高效滲透。", "pain": "敏感肌面膜、快速補水。", "skin": "敏弱肌、乾性肌。", "category": "面膜"},
    {"name": "Kose 高絲 嬰兒肌面膜", "features": "溫和配方、恢復細嫩。", "pain": "肌膚粗糙、想恢復嬰兒般觸感。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "Dr.Jart+ 活力保濕膠囊面膜", "features": "微分子玻尿酸、專業修護。", "pain": "缺水引起的緊繃、醫美術後。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "Paparecipe 春雨蜂蜜面膜", "features": "蜂蜜精華、天然舒緩。", "pain": "孕婦可用保養、溫和滋潤。", "skin": "所有膚質、敏弱肌。", "category": "面膜"},
    {"name": "Papa Recipe 茄子泥面膜", "features": "清潔毛孔、舒緩痘痘。", "pain": "清潔泥膜太乾、敏感肌清潔。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "Innisfree 火山泥毛孔潔淨面膜", "features": "濟州島火山泥、強力吸油。", "pain": "黑頭猖狂、毛孔堵塞。", "skin": "油性肌。", "category": "面膜"},
    {"name": "Paula's Choice 寶拉珍選 2%水楊酸精華液", "features": "2%水楊酸、代謝粉刺。", "pain": "閉口粉刺、毛孔粗大、痘痘問題。", "skin": "油性肌、混合肌。", "category": "精華"},
    {"name": "The Ordinary 10%菸鹼醯胺精華", "features": "高濃度B3、平價戰神。", "pain": "毛孔、出油、膚色暗沈。", "skin": "油性肌、混合肌。", "category": "精華"},
    {"name": "The Ordinary 咖啡因眼部精華", "features": "5%咖啡因、消水腫。", "pain": "眼部浮腫、黑眼圈、泡泡眼。", "skin": "所有膚質。", "category": "精華"},
    {"name": "CeraVe 適樂膚 寬頻防曬乳", "features": "全物理、神經醯胺。", "pain": "醫美後完全物理遮蔽。", "skin": "術後肌、極敏肌。", "category": "防曬"},
    {"name": "Biore 蜜妮 A極效防曬精華", "features": "最高等級防禦、耐磨擦。", "pain": "極限運動、戶外烈日。", "skin": "所有膚質。", "category": "防曬"},
    {"name": "Nivea 妮維雅 涼感防曬噴霧", "features": "立即降溫、噴灑方便。", "pain": "身體補擦太熱、不喜歡塗抹感。", "skin": "所有膚質。", "category": "防曬"},
    {"name": "曼秀雷敦 抗痘粉狀調理水", "features": "控油粉末、殺菌消炎。", "pain": "油光滿面、青春痘、紅腫。", "skin": "油痘肌。", "category": "化妝水"},
    {"name": "Labo Labo 毛孔緊膚化妝水 (升級版)", "features": "果酸代謝、細緻毛孔。", "pain": "草莓鼻、毛孔粗糙。", "skin": "油性肌、混合肌。", "category": "化妝水"},
    {"name": "廣源良 絲瓜籽多元修復精華液", "features": "絲瓜籽油、台灣在地。", "pain": "追求本土成分、清爽修復。", "skin": "所有膚質。", "category": "精華"},
    {"name": "Hada Labo 肌研 極潤美白乳液", "features": "傳明酸、鎖水提亮。", "pain": "美白同時保濕不足。", "skin": "追求亮白者。", "category": "乳霜"},
    {"name": "Minon 氨基酸保濕乳液", "features": "11種氨基酸、不黏膩。", "pain": "乳液太厚重、過敏期保養。", "skin": "敏感肌、所有膚質。", "category": "乳霜"},
    {"name": "Avène 雅漾 舒敏修護保濕精華乳", "features": "無菌包裝、極簡成分。", "pain": "爛臉期救星、什麼都不能擦時。", "skin": "高度過敏肌。", "category": "乳霜"},
    {"name": "Vaseline 凡士林 專業低敏修護乳液", "features": "無香料、臨床證明。", "pain": "濕疹傾向、極度癢、皮膚科推薦。", "skin": "極乾敏肌。", "category": "身體保養"},
    {"name": "Sebamed 施巴 嬰兒全效護膚膏", "features": "pH5.5、隔離刺激。", "pain": "紅屁屁、尿布疹、局部修護。", "skin": "嬰幼兒、敏弱肌。", "category": "個人護理"},
    {"name": "DHC 橄欖精華油", "features": "天然橄欖油、深層滋潤。", "pain": "極度乾燥、脫皮、抗氧化。", "skin": "乾性肌、熟齡肌。", "category": "精華"},
    {"name": "Melano CC 維他命C保濕噴霧", "features": "隨時提亮、抗氧化。", "pain": "冷氣房乾燥、妝後提亮。", "skin": "所有膚質。", "category": "化妝水"},
    {"name": "Sofina Primavista 漾緁 控油瓷效妝前隔離乳", "features": "超強控油、防止脫妝。", "pain": "中東油田、下午臉變黑、妝不持久。", "skin": "油性肌、混合肌。", "category": "防曬"},
    {"name": "Za 旋轉眉筆", "features": "筆芯柔軟、自然眉感。", "pain": "畫眉新手、斷芯、顏色生硬。", "skin": "所有人群。", "category": "彩妝"},
    {"name": "Excel 三合一持久造型眉筆", "features": "眉筆+眉粉+眉刷、神級眉筆。", "pain": "眉毛稀疏、眉型不美、出國必帶。", "skin": "所有人群。", "category": "彩妝"},
    {"name": "1028 超級大眼放大鏡睫毛膏", "features": "纖長濃密、根根分明。", "pain": "短睫毛、塌睫毛。", "skin": "所有人群。", "category": "彩妝"},
    {"name": "L'Oreal 巴黎萊雅 24H無瑕完美粉底液", "features": "高遮瑕、長效持妝。", "pain": "瑕疵多、毛孔大、容易掉妝。", "skin": "所有膚質、混合肌。", "category": "彩妝"},
    {"name": "Maybelline 媚比琳 反孔特霧粉底液", "features": "隱形毛孔、控油霧面。", "pain": "油性肌底妝、毛孔粗大。", "skin": "油性肌、混合肌。", "category": "彩妝"},
    {"name": "Kiss Me 花漾美姬 睫毛膏卸除液", "features": "不熏眼、一刷即淨。", "pain": "防水睫毛膏難卸、扯掉真睫毛。", "skin": "所有人群。", "category": "卸妝"},
    {"name": "Biore 蜜妮 極淨卸妝棉", "features": "含卸妝油成分、超大張。", "pain": "濃妝快速卸除、旅遊必備。", "skin": "所有膚質。", "category": "卸妝"},
    {"name": "DHC 潔淨洗面乳", "features": "溫和洗淨、含橄欖油。", "pain": "洗後乾燥、清潔不足。", "skin": "一般肌、混合肌。", "category": "洗面乳"},
    {"name": "Rosette 露姬婷 溫泥潔顏乳 (海泥綠)", "features": "海泥吸附、深層去垢。", "pain": "黑頭粉刺、毛孔粗大。", "skin": "油性肌、混合肌。", "category": "洗面乳"},
    {"name": "Bifesta 碧菲絲特 碳酸潔面慕斯", "features": "碳酸泡泡、深層清潔。", "pain": "手搓泡泡懶、暗沈肌。", "skin": "所有膚質。", "category": "洗面乳"},
    {"name": "Saborino 晚安面膜 (洋甘菊藍)", "features": "一站式夜間保養、舒緩睡眠。", "pain": "晚上下班太累不想保養。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "LuLuLun Over 45 緊緻面膜", "features": "熟齡專用、提升彈力。", "pain": "45歲以上保養、鬆弛、乾燥。", "skin": "熟齡肌。", "category": "面膜"},
    {"name": "Neogence 霓淨思 玻尿酸保濕面膜", "features": "高純度玻尿酸、平價好用。", "pain": "日常保濕需求、缺水。", "skin": "所有膚質。", "category": "面膜"},
    {"name": "My Beauty Diary 我的美麗日記 納豆發酵保濕面膜", "features": "納豆萃取、深層鎖水。", "pain": "極乾肌、水分流失快。", "skin": "乾性肌。", "category": "面膜"},
    {"name": "提提研 激光注白黑面膜", "features": "美白亮膚、備長炭黑布。", "pain": "膚色不均、暗沉、想亮白。", "skin": "混合肌、暗沉肌。", "category": "面膜"},
    {"name": "雪芙蘭 膠原蛋白滋養霜", "features": "膠原蛋白、深層滋潤。", "pain": "乾裂脫皮、冬季修護。", "skin": "乾性肌。", "category": "身體保養"},
    {"name": "Vaseline 凡士林 十效亮白修護潤膚露", "features": "十合一功效、果酸成分。", "pain": "身體斑點、暗沉、想一次搞定。", "skin": "所有膚質。", "category": "身體保養"}
]

added_count = 0
for item in new_items_2:
    if item["name"] not in existing_names:
        data.append(item)
        existing_names.add(item["name"])
        added_count += 1

DB_PATH.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Added {added_count} more items. Total: {len(data)}")
