# -*- coding: utf-8 -*-
import json
data = json.load(open('products-data.json', encoding='utf-8'))
sunscreen = [p for p in data if p.get('category') == '防曬']
unclassified = [p for p in sunscreen if p.get('tier', 'N/A') == 'N/A']
print(f'未分類的防曬產品 ({len(unclassified)} 件):')
for p in unclassified:
    print(f'  - {p.get("name")}')
