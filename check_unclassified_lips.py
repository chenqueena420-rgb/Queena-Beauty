# -*- coding: utf-8 -*-
import json

data = json.load(open('products-data.json', encoding='utf-8'))

# 查找未分類的唇部產品
lips = [p for p in data if p.get('category') == '唇部']
unclassified = [p for p in lips if p.get('tier', 'N/A') == 'N/A']

print(f'未分類的唇部產品 ({len(unclassified)} 件):')
for p in unclassified:
    print(f'  - {p.get("name")}')
