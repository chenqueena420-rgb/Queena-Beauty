
import json
import urllib.parse

# 读取产品数据
with open('products-data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# 更新每个产品的链接为正确的搜索链接
for product in products:
    product_name = product['name']
    
    # 屈臣氏搜索链接 - 确认正确格式
    watsons_url = "https://www.watsons.com.tw/search?text=" + urllib.parse.quote(product_name)
    
    # 康是美搜索链接 - 确认正确格式
    cosmed_url = "https://shop.cosmed.com.tw/v2/Search?q=" + urllib.parse.quote(product_name)
    
    # 寶雅搜索链接 - 确认正确格式
    poya_url = "https://www.poyabuy.com.tw/v2/Search?q=" + urllib.parse.quote(product_name)
    
    product['links'] = {
        "屈臣氏": watsons_url,
        "康是美": cosmed_url,
        "寶雅": poya_url
    }

# 保存更新后的产品数据
with open('products-data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f'Successfully optimized search links for {len(products)} products!')
print('\n验证链接格式：')
print(f'屈臣氏: {products[0]["links"]["屈臣氏"]}')
print(f'康是美: {products[0]["links"]["康是美"]}')
print(f'寶雅: {products[0]["links"]["寶雅"]}')
