# -*- coding: utf-8 -*-
import json

# 定義品牌到分級的映射
PROFESSIONAL_BRANDS = ['未來美', 'Neogence', 'DR.WU', '寵愛之名', 'Dr.Satin', 'Frozhelen', 
                       'BIAEffect', 'SK-II', 'Dr.Jart+', 'Target Pro', 'New Angance', 
                       'Bio-essence', '碧歐斯', 'JMSolution', 'BANOBAGI', 'ampm', 
                       '提提研', 'Abib', 'Dr.', 'Kiehl', 'Clarins', 'Sulwhasoo', 'Glamglow']

MID_RANGE_BRANDS = ['肌研', '我的心機', 'OLAY', 'NARUKO', '天天美麗', '專科', 
                    '露得新', 'SEXYLOOK', 'SKINTIFIC', 'MEDIHEAL', 'MEDI-PEEL', 
                    '護妍天使', 'Apivita', 'BCL', 'LuLuLun', 'Minon', 'Torriden', 
                    'ANUA', 'VT', 'BEYOND', 'Utena', 'Quality', 'Melano', 'AXIS-Y', 
                    'Annies', 'Papa Recipe', 'Innisfree', 'Laneige', 'Origins', 
                    'Fresh', 'Beauty of Joseon', '41度C', '蘭芝']

BUDGET_BRANDS = ['森田', '我的美麗日記', '豐台灣', '廣源良', '雪芙蘭', '曼秀雷敦', 
                 '毛穴撫子', 'Kose', '肌美精', 'Nature Republic', 'Simple', 'TERAECO', 
                 'Mediplus', '美樂思', 'Saborino', '蘆薈']

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
    
    # 預設為平價（如果無法識別）
    return None

data = json.load(open('products-data.json', encoding='utf-8'))

# 更新未分類的面膜
updated_count = 0
for p in data:
    if p.get('category') != '面膜':
        continue
    
    if p.get('tier', 'N/A') == 'N/A':
        name = p.get('name', '')
        tier_info = determine_tier(name)
        
        if tier_info:
            new_tier, new_level = tier_info
            p['tier'] = new_tier
            p['level'] = new_level
            updated_count += 1

# 保存更新後的數據
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print(f'✓ 已自動分類 {updated_count} 件未分類的面膜產品')

# 統計最終結果
masks = [p for p in data if p.get('category') == '面膜']
by_tier = {}
still_unclassified = []

for p in masks:
    tier = p.get('tier', 'N/A')
    if tier == 'N/A':
        still_unclassified.append(p.get('name', ''))
    by_tier[tier] = by_tier.get(tier, 0) + 1

print(f'\n面膜產品最終統計:')
print(f'  總面膜產品: {len(masks)} 件')
print(f'  專業醫美: {by_tier.get("專業醫美", 0)} 件 🩺')
print(f'  小資中價: {by_tier.get("小資中價", 0)} 件 🌿')
print(f'  平價: {by_tier.get("平價", 0)} 件 ✨')
print(f'  未分類: {by_tier.get("N/A", 0)} 件')

if still_unclassified:
    print(f'\n仍未分類的產品 ({len(still_unclassified)} 件):')
    for name in still_unclassified[:10]:
        print(f'  - {name}')
    if len(still_unclassified) > 10:
        print(f'  ... 及其他 {len(still_unclassified) - 10} 件')
