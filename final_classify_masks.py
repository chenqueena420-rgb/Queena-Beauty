# -*- coding: utf-8 -*-
import json

# 最後的模糊匹配映射
final_mapping = {
    "NEOGENCE 霓淨思超爆水潤澤保濕面膜5入": ("專業醫美", "🩺 專業醫美"),
    "NEOGENCE 霓淨思無針水光維他命B保濕面膜5入": ("專業醫美", "🩺 專業醫美"),
    "NEOGENCE 霓淨思高效亮白零觸感面膜5入": ("專業醫美", "🩺 專業醫美"),
    "SexyLook 酵素亮白面膜": ("小資中價", "🌿 小資中價"),
    "Medipeel 膠原蛋白撕拉面膜": ("小資中價", "🌿 小資中價"),
    "Paparecipe 春雨蜂蜜面膜": ("小資中價", "🌿 小資中價"),
    "Paparecipe 春雨黑蜂蜜面膜": ("小資中價", "🌿 小資中價"),
    "Lush 薄荷清爽面膜": ("小資中價", "🌿 小資中價"),
    "Mediheal 茶樹舒緩護理保濕面膜": ("小資中價", "🌿 小資中價"),
}

data = json.load(open('products-data.json', encoding='utf-8'))

# 更新未分類的面膜
updated_count = 0
for p in data:
    if p.get('category') != '面膜':
        continue
    
    if p.get('tier', 'N/A') == 'N/A':
        name = p.get('name', '')
        
        # 精確匹配
        if name in final_mapping:
            new_tier, new_level = final_mapping[name]
            p['tier'] = new_tier
            p['level'] = new_level
            updated_count += 1

# 保存更新後的數據
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print(f'✓ 已分類 {updated_count} 件面膜產品')

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
    for name in still_unclassified:
        print(f'  - {name}')
else:
    print('\n✓ 所有面膜產品已完全分類！')
