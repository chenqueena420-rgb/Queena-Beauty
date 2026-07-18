# -*- coding: utf-8 -*-
import json

# 手动分类这9件未分类的产品
manual_classifications = {
    "L`EGERE 安瓶防曬系列": ("小資中價", "🌿 小資中價"),
    "ANESSA 金鑽高效防曬凝膠NA": ("專業醫美", "🩺 專業醫美"),
    "ANESSA 金鑽高效防曬乳NA(敏弱肌)": ("專業醫美", "🩺 專業醫美"),
    "NIVEA SUN 水感清透防曬凝露": ("平價", "✨ 平價"),
    "Banana Boat 水感清爽防曬乳SPF50": ("平價", "✨ 平價"),
    "韓國BEAUSTA自然完美屏障防曬霜15ML": ("小資中價", "🌿 小資中價"),
    "NEOGENCE 霓淨思全天候長效抗陽防曬乳50ml": ("小資中價", "🌿 小資中價"),
    "Allie 持采UV高效防曬水凝乳EX": ("小資中價", "🌿 小資中價"),
    "Sofina Primavista 漾緁 控油瓷效妝前隔離乳": ("小資中價", "🌿 小資中價"),
}

data = json.load(open('products-data.json', encoding='utf-8'))

updated_count = 0
for p in data:
    if p.get('category') != '防曬':
        continue
    
    name = p.get('name', '')
    
    # 检查是否在手动分类列表中
    for key, (tier, level) in manual_classifications.items():
        if key in name or name in key:
            if p.get('tier', 'N/A') == 'N/A':
                p['tier'] = tier
                p['level'] = level
                updated_count += 1
                print(f'✓ {name} → {tier} ({level})')
                break

# 写入更新后的数据
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'\n已更新 {updated_count} 件未分類的防曬產品')

# 验证更新结果
sunscreen = [p for p in data if p.get('category') == '防曬']
by_tier = {}
for p in sunscreen:
    tier = p.get('tier', 'N/A')
    by_tier[tier] = by_tier.get(tier, 0) + 1

print(f'\n最終統計:')
print(f'  總防曬產品: {len(sunscreen)} 件')
print(f'  平價: {by_tier.get("平價", 0)} 件 ✨')
print(f'  小資中價: {by_tier.get("小資中價", 0)} 件 🌿')
print(f'  專業醫美: {by_tier.get("專業醫美", 0)} 件 🩺')
print(f'  未分類: {by_tier.get("N/A", 0)} 件')
