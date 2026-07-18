# -*- coding: utf-8 -*-
import json

# 專業醫美唇部產品
professional_lips = [
    "YSL 情挑誘光水唇膏",
    "Chanel 香奈兒 超炫耀的絲絨唇膏",
    "Dior 迪奧 癮誘粉漾潤唇膏",
    "Giorgio Armani 奢華絲絨訂製唇萃",
    "理膚寶水 全面修復潤唇膏",
    "雅漾 舒緩乾裂修護護唇膏",
    "CeraVe 適樂膚 修復護唇膏",
    "京城之霜 豐蜜養潤護唇膏",
]

# 小資中價唇部產品
mid_range_lips = [
    "妮維雅 超能防曬護唇膏",
    "曼秀雷敦 頂級濃潤柔霜潤唇膏",
    "魔唇 THERAPIND 夜間修護霜",
    "魔唇 護唇膏(滋潤)",
    "專科 彈潤護唇精華",
    "施巴潤澤護唇膏 SPF30",
    "DHC 橄欖護唇膏",
    "Opera 渲漾水色唇膏",
    "Opera 渲漾水色唇膏 (限定色)",
    "SKINTIFIC 莓果唇部精華",
    "凡士林 全能精華潤唇膏 (淡紋)",
    "Maybelline 媚比琳 超持久霧感液態唇膏",
    "I'M MEME 我愛水凝好氣色唇頰露",
    "heme 喜蜜 純色唇釉",
]

# 平價唇部產品
budget_lips = [
    "雪芙蘭 經典滋潤護唇膏",
    "凡士林 經典滋潤護唇膏 (棒狀)",
    "凡士林 經典護唇膏 (玫瑰/原味)",
    "凡士林 白桃修護護唇膏",
    "曼秀雷敦 Lip Pure 純淨植物",
    "曼秀雷敦 Magic Color 變色潤唇膏",
    "曼秀雷敦 Magic Color (蜂蠟款)",
    "曼秀雷敦 護唇膏 (薄荷)",
    "曼秀雷敦 薄荷潤唇凍膏 (軟管)",
    "曼秀雷敦 水份潤唇膏",
    "曼秀雷敦 男士潤唇膏",
    "妮維雅 水漾護唇膏",
    "小蜜媞 Carmex 修護唇膏 (軟管)",
    "澳洲神奇萬用木瓜霜",
    "魔唇 護唇膏 (滋潤)",
]

data = json.load(open('products-data.json', encoding='utf-8'))

# 創建產品名稱到分類的映射
tier_mapping = {}

# 添加專業醫美唇部產品
for product in professional_lips:
    tier_mapping[product] = ('專業醫美', '🩺 專業醫美')

# 添加小資中價唇部產品
for product in mid_range_lips:
    tier_mapping[product] = ('小資中價', '🌿 小資中價')

# 添加平價唇部產品
for product in budget_lips:
    tier_mapping[product] = ('平價', '✨ 平價')

# 更新或新增唇部產品
updated_count = 0
added_count = 0

for product in data:
    if product.get('category') == '唇部':
        name = product.get('name', '')
        if name in tier_mapping:
            new_tier, new_level = tier_mapping[name]
            if product.get('tier') != new_tier or product.get('level') != new_level:
                product['tier'] = new_tier
                product['level'] = new_level
                updated_count += 1

# 檢查是否需要新增不存在的產品
existing_lip_names = {p.get('name', '') for p in data if p.get('category') == '唇部'}
for name, (tier, level) in tier_mapping.items():
    if name not in existing_lip_names:
        # 提取品牌名稱
        brand = name.split()[0]
        new_product = {
            "name": name,
            "brand": brand,
            "features": "",
            "pain": "",
            "skin": "",
            "category": "唇部",
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

print(f'✓ 已更新唇部產品分類')
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
