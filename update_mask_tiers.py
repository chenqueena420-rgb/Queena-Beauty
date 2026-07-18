# -*- coding: utf-8 -*-
import json

# 專業醫美面膜產品
professional_masks = [
    "未來美 8分鐘極速/外泌體面膜",
    "未來美 1.5% A醇精華面膜",
    "未來美 EX8分鐘逆時空膠囊亮白面膜",
    "Neogence 霓淨思 無針水光維他命 C/E",
    "Neogence 霓淨思 無針水光維他命 B 保濕",
    "Neogence 霓淨思 無針水光維他命B保濕面膜(5入)",
    "Neogence 霓淨思 超爆水潤澤保濕面膜(5入)",
    "Neogence 霓淨思 高效亮白零觸感面膜(5入)",
    "Neogence 霓淨思 N3 神經醯胺潤澤保濕面膜",
    "DR.WU 玻尿酸保濕微導面膜",
    "DR.WU 玻尿酸保濕微導面膜 (3入)",
    "寵愛之名 極潤保濕礦物雲絲膜",
    "寵愛之名 維B舒緩保濕面膜(4片/盒)",
    "寵愛之名 乙基維他命C生物纖維面膜",
    "Dr.Satin 頂級魚子高效保濕面膜",
    "Dr.Satin 頂級魚子膠原彈力面膜",
    "Dr.Satin 頂級魚子高效保濕面膜(3片入)",
    "Dr.Satin 頂級魚子膠原面膜",
    "Frozhelen 皮可肽肌光修護面膜",
    "Frozhelen 皮可肽肌光修護",
    "BIAEffect 醫美級安瓶面膜",
    "SK-II 青春敷面膜",
    "Dr.Jart+ 活力保濕膠囊面膜",
    "Dr.Jart+ 補水膠囊面膜 (二入)",
    "Target Pro 肌膚專研全效益活面膜",
    "New Angance 玻尿酸保濕面膜(10片)",
    "Bio-essence 碧歐斯 24K 生物金",
    "Bio-essence 碧歐斯 水感舒緩B5極效保濕面膜(7入)",
    "JMSolution 醫美級安瓶緊緻面膜",
    "BANOBAGI PDRN 外泌體毛孔調理",
    "ampm B5 藍銅舒緩保濕面膜",
    "提提研 實驗室系列 01角鯊烷修護面膜",
    "Abib 魚腥草口香糖面膜",
]

# 小資中價面膜產品
mid_range_masks = [
    "肌研 光透潤系列 (美白/保濕)",
    "肌研 光透潤玻尿酸緊緻面膜",
    "肌研 光透潤酵母後生元保濕面膜",
    "肌研 光透潤白金修護保濕面膜",
    "提提研 黑面膜系列 (金箔/浸潤)",
    "提提研 超級纖維超導水",
    "提提研 保濕金箔黑面膜 (Plus)",
    "提提研 浸潤補水黑面膜",
    "提提研 保濕金箔黑面膜 (新版)",
    "提提研 激光注白黑面膜",
    "我的心機 安瓶+面膜組",
    "我的心機 晶球長效保濕面膜",
    "我的心機 晶球長效保濕面膜 (二入)",
    "我的心機 縮毛孔控油安瓶面膜",
    "OLAY 水感透白面膜",
    "NARUKO 茶樹痘痘黑面膜",
    "NARUKO 茶樹痘痘晚安凍膜",
    "NARUKO 森玫瑰水立方保濕面膜",
    "天天美麗 Pro+ 水光舒緩安瓶面膜",
    "專科 極輕透保濕系列",
    "專科 完美保濕特潤面膜",
    "露得新 速效保水安瓶面膜",
    "SEXYLOOK 海茴香外泌體水光面膜",
    "SEXYLOOK 仙人掌煥亮保濕面膜",
    "SEXYLOOK 酵素去角質亮白面膜",
    "SEXYLOOK 酵素亮白雙拉提面膜",
    "SEXYLOOK 酵素亮白面膜",
    "SKINTIFIC 火山固體泥膜棒",
    "MEDIHEAL 高效特強保濕護理棉",
    "MEDIHEAL 茶樹舒緩護理保濕面膜",
    "MEDIHEAL Tea Tree 舒緩調理面膜",
    "MEDIHEAL Vita 光透亮白面膜",
    "MEDI-PEEL 植萃積雪草B5精華面膜",
    "MEDI-PEEL 膠原蛋白撕拉面膜",
    "護妍天使 光透美白爽膚棉",
    "Apivita 仙人掌滋潤面膜 (泥狀)",
    "BCL Saborino 早安面膜 (經典/各款)",
    "BCL Saborino 晚安面膜 (洋甘菊/莓果)",
    "LuLuLun Precious 紅/白盒系列",
    "LuLuLun Over 45 緊緻面膜",
    "LuLuLun 晚安舒緩面膜 (薰衣草)",
    "Minon 氨基酸保濕面膜",
    "Torriden 玻尿酸深層補水面膜",
    "Torriden 潛水艇玻尿酸面膜",
    "ANUA 桃70舒緩面膜",
    "VT CICA 老虎積雪草面膜",
    "BEYOND YOUTH 極藻保濕精華面膜",
    "Utena 佑天蘭 黃金果凍面膜 (玻尿酸/膠原)",
    "Quality 1st 皇后的秘密 高保濕面膜",
    "Melano CC 高浸透維他命 C 面膜",
    "AXIS-Y 611 亮白淡斑精華面膜",
    "Annies Way 胜肽薔薇賦活面膜",
    "Papa Recipe 春雨蜂蜜面膜 (經典/黑蜂)",
    "Papa Recipe 茄子泥/綠泥面膜",
    "Innisfree 火山泥毛孔潔淨面膜",
    "Innisfree 濟州島綠茶面膜",
    "Laneige 蘭芝 晚安水凝膜",
    "Origins 品木宣言 泥娃娃活性碳面膜",
    "Origins 品木宣言 一飲而盡晚安面膜",
    "Fresh 玫瑰潤澤保濕面膜",
    "Beauty of Joseon 複方人蔘眼部精華",
    "41度C 蒸氣眼罩 (綜合組)",
]

# 平價面膜產品
budget_masks = [
    "森田藥妝 玻尿酸複合精華面膜",
    "森田藥妝 六重玻尿酸面膜",
    "森田藥妝 多重玻尿酸複合精華",
    "森田藥妝 神經醯胺修護面膜",
    "我的美麗日記 黑珍珠煥白面膜",
    "我的美麗日記 官燕窩全能滋養面膜",
    "我的美麗日記 蜜若藍超能補水面膜",
    "我的美麗日記 復活草水嫩修護面膜",
    "我的美麗日記 納豆發酵保濕面膜",
    "我的美麗日記 官燕窩面膜 (經典款)",
    "我的心機 玻尿酸保濕面膜",
    "我的心機 玻尿酸鎖水黑面膜",
    "我的心機 濃潤黑珍珠絲光黑面膜",
    "豐台灣 蘆薈絲瓜沁潤面膜",
    "廣源良 蘆薈敷臉凝露",
    "廣源良 絲瓜保濕敷臉膏",
    "廣源良 蘆薈保濕凝膠 (Bella Beauty)",
    "雪芙蘭 米淨水潤修護面膜",
    "曼秀雷敦 Acnes 抗痘補水面膜",
    "毛穴撫子 日本國產米面膜",
    "LuLuLun Pure 基礎保濕 (粉)",
    "LuLuLun 綠色平衡面膜",
    "LuLuLun 區域限定/保養系列",
    "Kose Clear Turn 膠原蛋白面膜",
    "Kose Clear Turn 維他命C面膜",
    "Kose 透明質酸面膜 (大包裝)",
    "Kose 嬰兒肌面膜",
    "肌美精 超浸透 3D 立體面膜",
    "Nature Republic 蘆薈凝膠面膜",
    "Simple 清妍 極致補水長效面膜",
    "TERAECO 蘆薈舒緩超水嫩面膜",
    "Mediplus 美樂思 酵素洗顏/面膜",
    "SexyLook 酵素亮白亮白面膜 (單片)",
    "Saborino 早安面膜 (經典款)",
    "我的心機 玻尿酸保濕鎖水黑面膜 (多入)",
    "森田藥妝 複合玻尿酸 (日常)",
    "我的美麗日記 黑珍珠 (經典)",
    "提提研 浸潤補水 (單片)",
    "LuLuLun 粉色 (盒裝)",
    "專科 保濕系列 (單片)",
    "肌研 光透潤 (單片裝)",
    "NARUKO 茶樹黑面膜 (單片)",
    "SexyLook 酵素系列 (常規)",
    "我的心機 安瓶組 (日常)",
    "廣源良 絲瓜系列 (常備)",
    "雪芙蘭 植萃系列 (日常)",
]

data = json.load(open('products-data.json', encoding='utf-8'))

# 創建產品名稱到分類的映射
tier_mapping = {}

# 添加專業醫美面膜
for product in professional_masks:
    tier_mapping[product] = ('專業醫美', '🩺 專業醫美')

# 添加小資中價面膜
for product in mid_range_masks:
    tier_mapping[product] = ('小資中價', '🌿 小資中價')

# 添加平價面膜
for product in budget_masks:
    tier_mapping[product] = ('平價', '✨ 平價')

# 更新或新增面膜產品
updated_count = 0
added_count = 0

for product in data:
    if product.get('category') == '面膜':
        name = product.get('name', '')
        if name in tier_mapping:
            new_tier, new_level = tier_mapping[name]
            if product.get('tier') != new_tier or product.get('level') != new_level:
                product['tier'] = new_tier
                product['level'] = new_level
                updated_count += 1

# 檢查是否需要新增不存在的產品
existing_mask_names = {p.get('name', '') for p in data if p.get('category') == '面膜'}
for name, (tier, level) in tier_mapping.items():
    if name not in existing_mask_names:
        # 提取品牌名稱
        brand = name.split()[0]
        new_product = {
            "name": name,
            "brand": brand,
            "features": "",
            "pain": "",
            "skin": "",
            "category": "面膜",
            "available_at": ["屈臣氏", "康是美", "寶雅"],
            "links": {
                "屈臣氏": "#",
                "康是美": "#",
                "寶雅": "#"
            },
            "prices": {
                "標籤": "",
                "屈臣氏": None,
                "康是美": None,
                "寶雅": None
            },
            "lowest_price_store": "請點擊連結查看即時價格",
            "tier": tier,
            "level": level
        }
        data.append(new_product)
        added_count += 1

# 保存更新後的數據
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print(f'✓ 已更新面膜產品分類')
print(f'  已更新: {updated_count} 件')
print(f'  新增: {added_count} 件')

# 統計最終結果
masks = [p for p in data if p.get('category') == '面膜']
by_tier = {}
for p in masks:
    tier = p.get('tier', 'N/A')
    by_tier[tier] = by_tier.get(tier, 0) + 1

print(f'\n面膜產品最終統計:')
print(f'  總面膜產品: {len(masks)} 件')
print(f'  專業醫美: {by_tier.get("專業醫美", 0)} 件 🩺')
print(f'  小資中價: {by_tier.get("小資中價", 0)} 件 🌿')
print(f'  平價: {by_tier.get("平價", 0)} 件 ✨')
print(f'  未分類: {by_tier.get("N/A", 0)} 件')
