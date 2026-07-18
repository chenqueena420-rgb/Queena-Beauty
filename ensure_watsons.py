import json
import urllib.parse
from pathlib import Path

DATA_PATH = Path(r'c:\Users\queena\Desktop\my beauty\products-data.json')

with DATA_PATH.open('r', encoding='utf-8') as f:
    products = json.load(f)

for product in products:
    if 'available_at' not in product or not isinstance(product['available_at'], list):
        product['available_at'] = []
    if '屈臣氏' not in product['available_at']:
        product['available_at'].append('屈臣氏')

    if 'links' not in product or not isinstance(product['links'], dict):
        product['links'] = {}
    if '屈臣氏' not in product['links'] or product['links'].get('屈臣氏', '') == '':
        name = product.get('name', '').strip()
        if name:
            product['links']['屈臣氏'] = 'https://www.watsons.com.tw/search?text=' + urllib.parse.quote(name)

with DATA_PATH.open('w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print('Ensured Watsons channel for', len(products), 'products.')