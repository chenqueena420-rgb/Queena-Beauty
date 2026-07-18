# -*- coding: utf-8 -*-
import json

# 定義品牌到分級的映射
PROFESSIONAL_BRANDS = ['YSL', 'Chanel', 'Dior', 'Giorgio Armani', '理膚寶水', '雅漾', 'CeraVe', '京城之霜']
MID_RANGE_BRANDS = ['妮維雅', '曼秀雷敦', '魔唇', '專科', '施巴', 'DHC', 'Opera', 'SKINTIFIC', '凡士林', 'Maybelline', 'I\'M MEME', 'heme', '喜蜜']
BUDGET_BRANDS = ['雪芙蘭', '凡士林', '曼秀雷敦', '妮維雅', '小蜜媞', 'Carmex', '澳洲', '魔唇']

def determine_tier(name):
    """根據品牌名稱確定分級"""
    # 檢查專業醫美品牌
    for brand in PROFESSIONAL_BRANDS:
        if brand in name:
            return ('專業醫美', '🩺 專業醫美')
    
    # 檢查小資中價品牌
    for brand in MID_RANGE_BRANDS:
        if brand in name:
            return ('小資中價', '🌿 小資中價')
    
    # 檢查平價品牌
    for brand in BUDGET_BRANDS:
        if brand in name:
            return ('平價', '✨ 平價')
    
    # 預設為平價
    return ('平價', '✨ 平價')

data = json.load(open('products-data.json', encoding='utf-8'))

# 更新未分類的唇部產品
updated_count = 0
for p in data:
    if p.get('category') != '唇部':
        continue
    
    if p.get('tier', 'N/A') == 'N/A':
        name = p.get('name', '')
        tier_info = determine_tier(name)
        
        if tier_info:
            new_tier, new_level = tier_info
            p['tier'] = new_tier
            p['level'] = new_level
            updated_count += 1
            print(f'✓ {name} → {new_tier}')

# 保存更新後的數據
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print(f'\n已自動分類 {updated_count} 件唇部產品')

# 統計最終結果
lips = [p for p in data if p.get('category') == '唇部']
by_tier = {}
still_unclassified = []

for p in lips:
    tier = p.get('tier', 'N/A')
    if tier == 'N/A':
        still_unclassified.append(p.get('name', ''))
    by_tier[tier] = by_tier.get(tier, 0) + 1

print(f'\n唇部產品最終統計:')
print(f'  總唇部產品: {len(lips)} 件')
print(f'  專業醫美: {by_tier.get("專業醫美", 0)} 件 🩺')
print(f'  小資中價: {by_tier.get("小資中價", 0)} 件 🌿')
print(f'  平價: {by_tier.get("平價", 0)} 件 ✨')
print(f'  未分類: {by_tier.get("N/A", 0)} 件')

if still_unclassified:
    print(f'\n仍未分類的產品 ({len(still_unclassified)} 件):')
    for name in still_unclassified:
        print(f'  - {name}')
else:
    print('\n✓ 所有唇部產品已完全分類！')
