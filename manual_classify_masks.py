# -*- coding: utf-8 -*-
import json

# 手動映射未分類的產品
manual_mapping = {
    "霓淨思 無針水光維他命 C/E": ("專業醫美", "🩺 專業醫美"),
    "露得清 速效保水安瓶面膜": ("小資中價", "🌿 小資中價"),
    "霓淨思 無針水光維他命 B 保濕": ("專業醫美", "🩺 專業醫美"),
    "My Beauty Diary 黑珍珠煥白面膜": ("平價", "✨ 平價"),
    "霓淨思 N7 跑趴超貼妝面膜": ("專業醫美", "🩺 專業醫美"),
    "SexyLook 酵素亮白雙拉提面膜": ("小資中價", "🌿 小資中價"),
    "LEADERS 麗得姿 胺基酸補水面膜": ("小資中價", "🌿 小資中價"),
    "品木宣言 泥娃娃活性碳面膜": ("小資中價", "🌿 小資中價"),
    "Mediheal N.M.F 深層保濕面膜": ("小資中價", "🌿 小資中價"),
    "Lululun Precious 紅盒彈潤面膜": ("小資中價", "🌿 小資中價"),
    "Lululun Precious 白盒亮白面膜": ("小資中價", "🌿 小資中價"),
    "Mediheal Tea Tree 舒緩調理面膜": ("小資中價", "🌿 小資中價"),
    "Mediheal Vita 光透亮白面膜": ("小資中價", "🌿 小資中價"),
    "New Angance玻尿酸保濕面膜10片": ("專業醫美", "🩺 專業醫美"),
    "寵愛之名維B舒緩保濕面膜4片/盒": ("專業醫美", "🩺 專業醫美"),
    "OLAY 水感透白面膜": ("小資中價", "🌿 小資中價"),
    "BC.L Saborino 早安面膜 (經典/各款)": ("小資中價", "🌿 小資中價"),
    "Mediheal 提拉保濕面膜": ("小資中價", "🌿 小資中價"),
    "Biodance 膠原蛋白實感深層全效面膜": ("小資中價", "🌿 小資中價"),
    "Dr. Althea 345 屏障修復霜面膜": ("小資中價", "🌿 小資中價"),
    "Kiehl's 亞馬遜白泥淨緻毛孔面膜": ("小資中價", "🌿 小資中價"),
    "Clarins 克蘭詩 V臉緊緻面膜": ("小資中價", "🌿 小資中價"),
    "Sulwhasoo 雪花秀 與潤修護睡眠面膜": ("小資中價", "🌿 小資中價"),
    "Glamglow 瞬效完美發光面膜 (黑罐)": ("專業醫美", "🩺 專業醫美"),
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
        if name in manual_mapping:
            new_tier, new_level = manual_mapping[name]
            p['tier'] = new_tier
            p['level'] = new_level
            updated_count += 1

# 保存更新後的數據
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print(f'✓ 已手動分類 {updated_count} 件面膜產品')

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
