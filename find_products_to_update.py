# -*- coding: utf-8 -*-
import json

data = json.load(open('products-data.json', encoding='utf-8'))

# 查找已存在的防晒产品
sunscreen = [p for p in data if p.get('category') == '防曬']
print(f'现有防曬产品: {len(sunscreen)}')

keywords = ['理膚寶水', 'Anessa', '安耐曬', '雅漾', 'Avene', '貝膚黛瑪', 'Curél', 'CeraVe', 'd program', 
            'ALLIE', 'SOFINA', 'AHC', 'ROUND LAB', 'Beauty of Joseon', 'SKINTIFIC', 
            'Biore', 'Skin Aqua', '曼秀雷敦', '雪芙蘭', '專科', '妮維雅']

print('\n需要检查更新的产品:')
for keyword in keywords:
    matches = [p for p in sunscreen if keyword in p.get('name', '')]
    if matches:
        print(f'\n{keyword}:')
        for p in matches:
            print(f'  {p.get("name")} - {p.get("level", "N/A")} (tier: {p.get("tier", "N/A")})')
