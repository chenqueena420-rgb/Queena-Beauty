# -*- coding: utf-8 -*-
import json

data = json.load(open('products-data.json', encoding='utf-8'))

# 檢查所有防曬產品的分類
sunscreen = [p for p in data if p.get('category') == '防曬']

print(f'防曬產品總數: {len(sunscreen)}')

# 按分類統計
by_tier = {}
unclassified = []

for p in sunscreen:
    tier = p.get('tier', 'N/A')
    if tier == 'N/A':
        unclassified.append(p.get('name', ''))
    by_tier[tier] = by_tier.get(tier, 0) + 1

print(f'\n按分類統計:')
for tier, count in sorted(by_tier.items()):
    print(f'  {tier}: {count} 件')

if unclassified:
    print(f'\n未分類產品 ({len(unclassified)} 件):')
    for name in unclassified:
        print(f'  - {name}')
else:
    print('\n✓ 所有防曬產品均已正確分類！')

# 檢查是否有重複產品名稱
names = [p.get('name', '') for p in sunscreen]
duplicates = [name for name in names if names.count(name) > 1]
if duplicates:
    print(f'\n重複產品名稱 ({len(set(duplicates))} 個):')
    for name in set(duplicates):
        print(f'  - {name} (出現 {names.count(name)} 次)')
