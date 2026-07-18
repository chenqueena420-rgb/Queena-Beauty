
import json

# 读取原始产品数据
with open('products-data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# 定义通路信息
stores = {
    '屈臣氏': 'https://www.watsons.com.tw/promo-health-4?utm_source=bing&utm_medium=cpc&utm_campaign=BT_%E5%93%81%E7%89%8C%E5%AD%97_BING&utm_content=%E5%93%81%E7%89%8C%E5%A4%A7%E5%AD%97%E2%94%82Exact&utm_term=%E5%B1%88%E8%87%A3%E6%B0%8F%E7%B6%B2%E8%B7%AF%E5%95%86%E5%BA%97',
    '康是美': 'https://www.cosmed.com.tw/',
    '寶雅': 'https://www.poyabuy.com.tw/'
}

# 为每个产品添加 available_at 和 links 字段
# 默认所有产品在三个通路都有售卖
for product in products:
    product['available_at'] = ['屈臣氏', '康是美', '寶雅']
    product['links'] = {
        '屈臣氏': stores['屈臣氏'],
        '康是美': stores['康是美'],
        '寶雅': stores['寶雅']
    }

# 保存更新后的产品数据
with open('products-data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f'Successfully updated {len(products)} products!')

