<<<<<<< HEAD
# -*- coding: utf-8 -*-
import json

data = json.load(open('products-data.json', encoding='utf-8'))

# 查找未分類的唇部產品
lips = [p for p in data if p.get('category') == '唇部']
unclassified = [p for p in lips if p.get('tier', 'N/A') == 'N/A']

print(f'未分類的唇部產品 ({len(unclassified)} 件):')
for p in unclassified:
    print(f'  - {p.get("name")}')
=======
# -*- coding: utf-8 -*-
import json

data = json.load(open('products-data.json', encoding='utf-8'))

# 查找未分類的唇部產品
lips = [p for p in data if p.get('category') == '唇部']
unclassified = [p for p in lips if p.get('tier', 'N/A') == 'N/A']

print(f'未分類的唇部產品 ({len(unclassified)} 件):')
for p in unclassified:
    print(f'  - {p.get("name")}')
>>>>>>> 33ffab1a1b782b70eee1328db16ba0503841e839
