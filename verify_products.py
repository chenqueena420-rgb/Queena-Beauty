
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 读取产品数据
with open('products-data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print("Verifying all products...")
print("Total products: {}".format(len(products)))

# 检查所有产品
all_good = True
missing_fields = []
invalid_links = []

for i, product in enumerate(products):
    name = product.get('name', 'Unknown')
    
    # 检查 available_at
    if 'available_at' not in product:
        missing_fields.append((i+1, name, 'available_at'))
        all_good = False
    elif not isinstance(product['available_at'], list):
        missing_fields.append((i+1, name, 'available_at (not list)'))
        all_good = False
    
    # 检查 links
    if 'links' not in product:
        missing_fields.append((i+1, name, 'links'))
        all_good = False
    elif not isinstance(product['links'], dict):
        missing_fields.append((i+1, name, 'links (not dict)'))
        all_good = False
    else:
        # 检查链接格式
        links = product['links']
        for platform, url in links.items():
            if not url.startswith('http'):
                invalid_links.append((i+1, name, platform, url))
                all_good = False

if all_good:
    print("\n✓ All products are good!")
    print("All products have:")
    print("  - available_at field (list)")
    print("  - links field (dict)")
    print("  - Valid URLs starting with http")
    
    # 显示前 5 个产品的信息
    print("\nSample products (first 5):")
    for i, product in enumerate(products[:5]):
        print("\n  [{}] {}".format(i+1, product['name']))
        print("  available_at: {}".format(product['available_at']))
        print("  links keys: {}".format(list(product['links'].keys())))
else:
    print("\nIssues found:")
    if missing_fields:
        print("\nMissing fields:")
        for item in missing_fields[:10]:
            print("  [{}] {} - Missing: {}".format(item[0], item[1], item[2]))
        if len(missing_fields) &gt; 10:
            print("  ... and {} more".format(len(missing_fields) - 10))
    
    if invalid_links:
        print("\nInvalid links:")
        for item in invalid_links[:10]:
            print("  [{}] {} - {}: {}".format(item[0], item[1], item[2], item[3]))
        if len(invalid_links) &gt; 10:
            print("  ... and {} more".format(len(invalid_links) - 10))
