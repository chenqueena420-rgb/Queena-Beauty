# -*- coding: utf-8 -*-
import json

# 定义品牌到分级的映射
PROFESSIONAL_BRANDS = ['理膚寶水', 'Anessa', '安耐曬', '雅漾', 'Avene', '貝膚黛瑪', 'Curél', 'CeraVe', 'd program', 'Vichy', 'Cetaphil', "M.A.C"]
MID_RANGE_BRANDS = ['ALLIE', 'SOFINA', 'AHC', 'ROUND LAB', 'Beauty of Joseon', 'Neogence', 'DHC', 'Kose', 'Target Pro', '露得新', 'Eucerin', 'Skin Aqua 亮白']
BUDGET_BRANDS = ['Biore', 'Skin Aqua', '曼秀雷敦', '雪芙蘭', '專科', '妮維雅', '凡士林', '香蕉船', '自白肌', 'Za', '喜蜜', 'Suncut', 'SKINTIFIC']

def determine_tier(name):
    """根据品牌名称确定分级"""
    # 检查是否是亮白隔离（小资中价）
    if 'Skin Aqua' in name and ('亮白' in name or '隔離' in name):
        return ('小資中價', '🌿 小資中價')
    
    # 检查专业医美品牌
    for brand in PROFESSIONAL_BRANDS:
        if brand in name:
            return ('專業醫美', '🩺 專業醫美')
    
    # 检查小资中价品牌
    for brand in MID_RANGE_BRANDS:
        if brand in name:
            return ('小資中價', '🌿 小資中價')
    
    # 检查平价品牌
    for brand in BUDGET_BRANDS:
        if brand in name:
            return ('平價', '✨ 平價')
    
    # 默认返回 None，保持原状
    return None

data = json.load(open('products-data.json', encoding='utf-8'))

# 过滤防晒产品
sunscreen = [p for p in data if p.get('category') == '防曬']

# 需要更新的产品
products_to_update = []

for i, p in enumerate(sunscreen):
    name = p.get('name', '')
    current_tier = p.get('tier', 'N/A')
    current_level = p.get('level', 'N/A')
    
    # 检查是否需要更新（tier 为 N/A 或者名称中含有需要分类的品牌）
    new_tier_info = determine_tier(name)
    
    if new_tier_info and (current_tier == 'N/A' or current_tier != new_tier_info[0]):
        new_tier, new_level = new_tier_info
        if current_tier != new_tier or current_level != new_level:
            products_to_update.append({
                'name': name,
                'old_tier': current_tier,
                'old_level': current_level,
                'new_tier': new_tier,
                'new_level': new_level,
                'index': i
            })

print(f'需要更新的防曬產品: {len(products_to_update)} 件\n')

# 按新分级分组显示
by_tier = {}
for p in products_to_update:
    tier = p['new_tier']
    if tier not in by_tier:
        by_tier[tier] = []
    by_tier[tier].append(p)

for tier in ['平價', '小資中價', '專業醫美']:
    if tier in by_tier:
        print(f'{tier}:')
        for p in by_tier[tier]:
            print(f'  {p["name"]}')
            print(f'    {p["old_tier"]} ({p["old_level"]}) → {p["new_tier"]} ({p["new_level"]})')
        print()

# 保存更新索引用于后续更新
json.dump(products_to_update, open('products_to_update.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'已保存更新清单到 products_to_update.json')
