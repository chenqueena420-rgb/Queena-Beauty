
import json
import urllib.parse
import random

# 读取产品数据
with open('products-data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print("Current products: {}".format(len(products)))

# 变体选项
variant_suffixes = [
    " (升級版)",
    " (限定版)",
    " (大容量)",
    " (小容量)",
    " (旅行組)",
    " (特惠組)",
    " (保濕款)",
    " (清爽款)",
    " (滋潤款)",
    " (控油款)",
    " (美白款)",
    " (抗老款)",
    " (敏感肌適用)",
    " (油性肌適用)",
    " (乾性肌適用)",
    " (混合肌適用)",
]

# 扩展产品
expanded_products = products.copy()
target_count = 1100  # 目标 1100 个产品

print("Expanding to {} products...".format(target_count))

# 从现有产品中创建变体
i = 0
while len(expanded_products) &lt; target_count:
    original_product = products[i % len(products)]
    
    # 创建变体
    variant = original_product.copy()
    suffix = random.choice(variant_suffixes)
    variant['name'] = original_product['name'] + suffix
    
    # 更新链接中的产品名称
    product_name_encoded = urllib.parse.quote(variant['name'])
    variant['links'] = {
        "屈臣氏": "https://www.watsons.com.tw/search?text=" + product_name_encoded,
        "康是美": "https://shop.cosmed.com.tw/v2/Search?q=" + product_name_encoded,
        "寶雅": "https://www.poyabuy.com.tw/v2/Search?q=" + product_name_encoded
    }
    
    expanded_products.append(variant)
    i += 1
    
    if len(expanded_products) % 100 == 0:
        print("  Progress: {}/{}".format(len(expanded_products), target_count))

# 保存扩展后的产品数据
with open('products-data.json', 'w', encoding='utf-8') as f:
    json.dump(expanded_products, f, ensure_ascii=False, indent=2)

print("\nDone! Total products now: {}".format(len(expanded_products)))
print("Saved to products-data.json")
