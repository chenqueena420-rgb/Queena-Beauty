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

# 更新所有防晒产品
updated_count = 0
for i, p in enumerate(data):
    if p.get('category') != '防曬':
        continue
    
    name = p.get('name', '')
    current_tier = p.get('tier', 'N/A')
    
    # 尝试确定正确的分级
    new_tier_info = determine_tier(name)
    
    if new_tier_info:
        new_tier, new_level = new_tier_info
        if current_tier != new_tier:
            p['tier'] = new_tier
            p['level'] = new_level
            updated_count += 1

# 写入更新后的数据
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'✓ 已更新 {updated_count} 件防曬產品的分類')

# 验证更新结果
sunscreen = [p for p in data if p.get('category') == '防曬']
by_tier = {}
for p in sunscreen:
    tier = p.get('tier', 'N/A')
    by_tier[tier] = by_tier.get(tier, 0) + 1

print(f'\n更新後統計:')
print(f'  總防曬產品: {len(sunscreen)} 件')
print(f'  平價: {by_tier.get("平價", 0)} 件')
print(f'  小資中價: {by_tier.get("小資中價", 0)} 件')
print(f'  專業醫美: {by_tier.get("專業醫美", 0)} 件')
print(f'  未分類: {by_tier.get("N/A", 0)} 件')
