
import json
from collections import Counter
import sys
import io

# 设置输出编码为 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 读取产品数据
with open('products-data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print("Total products: {}".format(len(products)))
print("\nCategory stats:")

# 统计分类
category_count = Counter()
for product in products:
    category = product.get('category', 'Uncategorized')
    category_count[category] += 1

# 按分类排序显示
for category, count in sorted(category_count.items()):
    print("  {}: {} products".format(category, count))

print("\nFirst 10 products:")
for i, product in enumerate(products[:10]):
    print("  [{}] {} ({})".format(i+1, product['name'], product['category']))
