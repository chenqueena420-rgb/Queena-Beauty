# -*- coding: utf-8 -*-
import json
import urllib.parse

# 專業醫美唇部產品（含特性）
professional_lips = {
    "理膚寶水 全面修復潤唇膏": "5% 泛醇 (B5) 與神經醯胺，針對唇炎與醫美術後。",
    "雅漾 舒緩乾裂修護護唇膏": "冷霜成分與活泉水，提供極度乾裂肌的封閉性保護。",
    "CeraVe 適樂膚 修復護唇膏": "三種神經醯胺與玻尿酸，修復屏障並緩解發癢。",
    "Dior 迪奧 癮誘粉漾潤唇膏": "感溫顯色與滋潤修護，專櫃最受歡迎的精品潤唇膏。",
    "YSL 情挑誘光水唇膏": "高濃度精油注入，具備高級妝感與高顯色度。",
    "Chanel 香奈兒 超炫耀的絲絨唇膏": "提供經典名媛質感的絲絨霧面色彩。",
    "Giorgio Armani 奢華絲絨訂製唇萃": "飽滿顯色且不乾澀，適合細紋困擾者。",
    "京城之霜 豐蜜養潤護唇膏": "含蜂蜜與蜂王乳，針對熟齡肌的抗老與暗沉修復。",
    "Neogence 霓淨思 玻尿酸保濕潤唇膏": "醫美級純淨補水，無添加香料，適合極敏感肌。",
    "Dr.Satin 頂級魚子潤澤護唇精華": "高濃度魚子萃取，針對深度唇紋進行強效修補。",
    "Bio-essence 碧歐斯 24K 生物金護唇膏": "含 24K 金箔，幫助代謝並提亮唇部氣色。",
    "Uriage 依泉 極致修護潤唇膏": "藥妝界長青款，針對反覆脫皮與唇周乾裂。",
    "Bioderma 貝膚黛瑪 賦妍修護潤唇膏": "專業配方舒緩脆弱唇部，提升耐受力。",
    "Blistex 碧唇 專業修護唇膏 (藍罐)": "醫學專業背景，針對嘴唇乾裂到疼痛的急救。",
    "Target Pro 肌膚專研 胜肽緊緻護唇膏": "含胜肽成分，針對唇部鬆弛與乾癟進行緊緻。",
    "Eucerin 伊思妮 萬用修復霜 (唇部可用)": "針對極度受損與紅腫，提供醫學級屏障。",
    "A-DERMA 艾瑪絲 燕麥修護潤唇膏": "燕麥萃取舒緩發炎，適合敏感脆弱性唇部。",
    "Filorga 菲洛嘉 玻尿酸盈潤護唇精華": "內建按摩頭，醫美級澎潤填充技術。",
}

# 小資中價唇部產品（含特性）
mid_range_lips = {
    "妮維雅 超能防曬護唇膏": "SPF50 高係數防曬，適合戶外族防止唇部曬黑。",
    "曼秀雷敦 頂級濃潤柔霜潤唇膏": "遇唇溫即融，提供奶油般的極潤絲滑感。",
    "魔唇 THERAPIND 夜間修護霜": "有機芝麻精華厚敷，掃除隔天早上的死皮。",
    "專科 彈潤護唇精華": "玻尿酸與膠原蛋白添加，適合上口紅前提升水潤度。",
    "DHC 橄欖護唇膏": "純欖精油親膚性極佳，是開架長年銷售冠軍。",
    "施巴潤澤護唇膏 SPF30": "pH5.5 與維他命 E，物理化學雙防曬保護。",
    "Opera 渲漾水色唇膏": "水感顯色，解決乾唇上色不均的困擾。",
    "Opera 渲漾水色唇膏 (限定色)": "熱銷花嫁色，強調日系透明感與持色力。",
    "SKINTIFIC 莓果唇部精華": "莓果萃取亮澤效果，打造流行嘟嘟唇感。",
    "凡士林 全能精華潤唇膏 (淡紋)": "含三肽成分，針對唇部老化感。",
    "Maybelline 媚比琳 超持久霧感液態唇膏": "16小時不掉色，適合長效妝感需求。",
    "I'M MEME 我愛水凝好氣色唇頰露": "自然水感顯色，唇頰兩用高便利性。",
    "heme 喜蜜 純色唇釉": "平價高品質絲緞質地，提供韓系溫柔感色調。",
    "Curél 珂潤 潤浸保濕護唇膏": "神經醯胺成分，針對敏感脫皮肌的低負擔保濕。",
    "Green Pharmacy 綠色藥房 草本護唇膏": "歐洲植萃精油，質地溫潤持久。",
    "Burt's Bees 蜜蜂爺爺 蜂蠟護唇膏": "100% 天然成分，經典薄荷清爽感與蜂蠟滋養。",
    "Za 必備潤色護唇膏": "變色技術搭配潤澤感，提亮唇色不突兀。",
    "Catrice 璀璨唇部去角質霜": "糖粒成分，溫和去除唇部老廢角質並保濕。",
    "1028 唇迷心竅潤澤唇膏": "顯白調色，質地如精華液般滑順。",
    "Integrate 櫻花潤色護唇膏": "修飾暗沉，給予雙唇如櫻花般的粉嫩感。",
    "Melano CC 維他命 C 修護護唇膏": "維他命 C 與 E 誘導體，改善唇色暗沉。",
    "NUXE 巴黎嘉儀 蜂蜜護唇霜": "經典小棕罐，極致修護與霧面封閉質感。",
    "Dr. Bronner's 布朗博士 有機護唇膏": "有機植萃油，適合極簡純素保養者。",
    "Kiehl's 契爾氏 1號護唇膏": "雖然單價稍高，但開架常能見到組合，滋潤度極高。",
    "Fresh 馥蕾詩 澄糖滋養護唇膏": "黃糖成分，經典潤色與修護功能並存。",
    "Blistex 碧唇 冰爽修護潤唇膏": "針對唇部發熱不適感，提供強力清涼鎮定。",
    "Labello 妮維雅果漾系列 (櫻桃)": "德國進口版，潤色效果明顯且持濕。",
    "Solone 經典極潤唇膏": "絲緞質感，高顯色度與中價位定位。",
    "ROMAND 果汁唇釉": "韓系彩妝代表，極致水光與持久染唇效果。",
    "A'pieu 蜂蜜牛奶潤唇油": "極致潤澤感，適合睡前當作唇膜使用。",
    "Laneige 蘭芝 晚安唇膜 (旅行裝)": "開架通路常有小包裝，夜間去死皮效果顯著。",
    "ettusais 艾杜紗 護唇精華液": "高黏稠密封性，給予極度受損唇部全面包覆。",
}

# 平價唇部產品（含特性）
budget_lips = {
    "雪芙蘭 經典滋潤護唇膏": "維他命 E 國民長青配方，學生族預算首選。",
    "凡士林 經典滋潤護唇膏 (棒狀)": "微晶凍鎖水，基礎保濕且不沾手。",
    "凡士林 經典護唇膏 (玫瑰/原味)": "圓罐裝，極高 CP 值，適合睡前厚敷。",
    "凡士林 白桃修護護唇膏": "平價保濕搭配清甜白桃香，受學生歡迎。",
    "曼秀雷敦 Lip Pure 純淨植物": "100% 食品級成分，孕婦或敏感肌的最佳選擇。",
    "曼秀雷敦 Magic Color 變色潤唇膏": "隨體溫變色，自然粉嫩氣色。",
    "曼秀雷敦 護唇膏 (薄荷)": "經典綠管，夏日降溫或精神不濟時提神用。",
    "曼秀雷敦 薄荷潤唇凍膏 (軟管)": "高滲透密封質地，適合嚴重乾裂急救。",
    "曼秀雷敦 男士潤唇膏": "無色無味極簡，滋潤感紮實不油亮。",
    "曼秀雷敦 水份潤唇膏": "玻尿酸與保濕因子，清爽補水不負擔。",
    "妮維雅 水漾護唇膏": "乳油木果長效保濕，妝前打底萬用款。",
    "小蜜媞 Carmex 修護唇膏 (軟管)": "薄荷醇鎮定，針對嚴重受損與嘴角龜裂。",
    "澳洲神奇萬用木瓜霜": "萬用修復，可用於嘴唇或任何乾燥脫皮處。",
    "魔唇 護唇膏 (滋潤/棒狀)": "日常版的保濕方案，質地穩定高 CP。",
    "妮維雅 潤彩雙層護唇膏": "雙層構造，外層保濕內層給予淡淡妝感。",
    "廣源良 絲瓜保濕護唇膏": "台灣在地植萃，質地輕盈適合南台灣氣候。",
    "Essence 艾森絲 柔軟護唇膏": "開架中最親民的價格，適合隨身必備。",
    "我的心機 玻尿酸超補水護唇膏": "針對乾枯唇部快速補水。",
    "美娜 護唇膏 (經典紅管)": "傳統藥局長青款，對於強效修復有佳評。",
    "Pears 梨牌 潤唇膏": "經典溫和配方，質感細膩且無多餘添加。",
    "Vaseline 凡士林 蘆薈舒緩護唇膏": "清涼舒緩，針對紅腫或灼熱不適唇部。",
    "Blistex 碧唇 舒敏修護潤唇膏": "成分極簡，降低過敏風險的平價選擇。",
    "Dora 朵拉 天然植物油護唇膏": "寶雅常見品牌，高潤度且平價。",
    "Farma dorra 法瑪朵 潤唇膏": "草本配方，溫和對抗乾燥。",
    "Nivea 妮維雅 草莓果漾護唇膏": "經典水果香氣，帶有些微淡紅潤色。",
    "Carmex 小蜜媞 經典護唇膏 (盒裝)": "比軟管更有密封感，適合極乾氣候。",
    "曼秀雷敦 藥用修護唇膏 (XD)": "日版代購長青款，現於開架通路也常出現。",
    "Sebamed 施巴 嬰兒護唇膏": "溫和 pH5.5，專為幼童及超敏感唇部設計。",
    "Palmer's 帕瑪氏 可可脂潤唇膏": "濃郁巧克力香氣，卓越鎖水力。",
    "Biore 蜜妮 高保濕修護潤唇膏": "日本研發配方，提供持久的潤澤膜。",
    "廣源良 蘆薈保濕護唇膏": "天然蘆薈鎮定，適合夏天使用。",
    "潤肌精 玻尿酸滋潤護唇膏": "高濃度美容液感，質地如凝膠般包覆。",
    "Watsons 屈臣氏 骨膠原潤唇膏": "自有品牌高 CP 值代表，主打修補彈力。",
    "Poya 寶雅 專業唇部修護系列": "自有通路推出的機能型護唇。",
    "Medimix 印度皂品牌護唇膏": "草本精油風味，主打天然修復力。",
}

data = json.load(open('products-data.json', encoding='utf-8'))

# 創建產品名稱到分類和特性的映射
tier_mapping = {}

# 添加專業醫美唇部產品
for product, features in professional_lips.items():
    tier_mapping[product] = {
        'tier': '專業醫美',
        'level': '🩺 專業醫美',
        'features': features
    }

# 添加小資中價唇部產品
for product, features in mid_range_lips.items():
    tier_mapping[product] = {
        'tier': '小資中價',
        'level': '🌿 小資中價',
        'features': features
    }

# 添加平價唇部產品
for product, features in budget_lips.items():
    tier_mapping[product] = {
        'tier': '平價',
        'level': '✨ 平價',
        'features': features
    }

# 更新或新增唇部產品
updated_count = 0
added_count = 0

for product in data:
    if product.get('category') == '唇部':
        name = product.get('name', '')
        if name in tier_mapping:
            info = tier_mapping[name]
            if product.get('tier') != info['tier'] or product.get('level') != info['level'] or product.get('features') != info['features']:
                product['tier'] = info['tier']
                product['level'] = info['level']
                product['features'] = info['features']
                updated_count += 1

# 檢查是否需要新增不存在的產品
existing_lip_names = {p.get('name', '') for p in data if p.get('category') == '唇部'}
for name, info in tier_mapping.items():
    if name not in existing_lip_names:
        # 提取品牌名稱
        brand = name.split()[0]
        
        # 創建搜尋連結
        search_query = urllib.parse.quote(name)
        
        new_product = {
            "name": name,
            "brand": brand,
            "features": info['features'],
            "pain": "唇部護理",
            "skin": "所有膚質",
            "category": "唇部",
            "available_at": ["屈臣氏", "康是美", "寶雅"],
            "links": {
                "屈臣氏": f"https://www.watsons.com.tw/search?text={search_query}",
                "康是美": f"https://shop.cosmed.com.tw/v2/Search?q={search_query}",
                "寶雅": f"https://www.poyabuy.com.tw/v2/Search?q={search_query}"
            },
            "prices": {
                "標籤": "",
                "屈臣氏": None,
                "康是美": None,
                "寶雅": None
            },
            "lowest_price_store": "請點擊連結查看即時價格",
            "tier": info['tier'],
            "level": info['level']
        }
        data.append(new_product)
        added_count += 1

# 同時更新現有產品的連結
for product in data:
    if product.get('category') == '唇部':
        name = product.get('name', '')
        search_query = urllib.parse.quote(name)
        
        # 更新連結
        if product.get('links'):
            product['links']['屈臣氏'] = f"https://www.watsons.com.tw/search?text={search_query}"
            product['links']['康是美'] = f"https://shop.cosmed.com.tw/v2/Search?q={search_query}"
            product['links']['寶雅'] = f"https://www.poyabuy.com.tw/v2/Search?q={search_query}"

# 保存更新後的數據
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print(f'✓ 已更新唇部產品分類和特性')
print(f'  已更新: {updated_count} 件')
print(f'  新增: {added_count} 件')

# 統計最終結果
lips = [p for p in data if p.get('category') == '唇部']
by_tier = {}
for p in lips:
    tier = p.get('tier', 'N/A')
    by_tier[tier] = by_tier.get(tier, 0) + 1

print(f'\n唇部產品最終統計:')
print(f'  總唇部產品: {len(lips)} 件')
print(f'  專業醫美: {by_tier.get("專業醫美", 0)} 件 🩺')
print(f'  小資中價: {by_tier.get("小資中價", 0)} 件 🌿')
print(f'  平價: {by_tier.get("平價", 0)} 件 ✨')
print(f'  未分類: {by_tier.get("N/A", 0)} 件')
