# -*- coding: utf-8 -*-
import json

data = json.load(open('products-data.json', encoding='utf-8'))

# 按類別統計
categories = {}
for p in data:
    cat = p.get('category', 'N/A')
    if cat not in categories:
        categories[cat] = {'products': 0, 'tiers': {}}
    categories[cat]['products'] += 1
    
    tier = p.get('tier', 'N/A')
    if tier not in categories[cat]['tiers']:
        categories[cat]['tiers'][tier] = 0
    categories[cat]['tiers'][tier] += 1

print('商品類別統計:')
print(f'═' * 60)
for cat in sorted(categories.keys()):
    info = categories[cat]
    print(f'\n{cat}: {info["products"]} 件')
    for tier, count in sorted(info['tiers'].items()):
        if tier != 'N/A':
            print(f'  {tier}: {count} 件')
    if 'N/A' in info['tiers']:
        print(f'  未分類: {info["tiers"]["N/A"]} 件')

print(f'\n{"═" * 60}')
print(f'總商品數: {len(data)} 件')
