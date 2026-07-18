# -*- coding: utf-8 -*-
import json

data = json.load(open('products-data.json', encoding='utf-8'))
print(f'總產品數: {len(data)}')

sunscreen = [p for p in data if p.get('category') == '防曬']
print(f'防曬產品數: {len(sunscreen)}')

# 按 level 分組統計
by_level = {}
for p in sunscreen:
    level = p.get('level', 'N/A')
    by_level[level] = by_level.get(level, 0) + 1

print('\n按等級統計:')
for level, count in sorted(by_level.items()):
    print(f'  {level}: {count} 件')

print('\n最後 5 件防曬產品:')
for p in sunscreen[-5:]:
    print(f'  - {p["name"]} ({p.get("level", "N/A")})')
