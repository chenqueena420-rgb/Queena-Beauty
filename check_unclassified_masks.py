# -*- coding: utf-8 -*-
import json

data = json.load(open('products-data.json', encoding='utf-8'))

# 查找未分類的面膜
masks = [p for p in data if p.get('category') == '面膜']
unclassified = [p for p in masks if p.get('tier', 'N/A') == 'N/A']

print(f'未分類的面膜產品 ({len(unclassified)} 件):')
for p in unclassified[:20]:  # 只显示前20个
    print(f'  - {p.get("name")}')

if len(unclassified) > 20:
    print(f'  ... 及其他 {len(unclassified) - 20} 件')
