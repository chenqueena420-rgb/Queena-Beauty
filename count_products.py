
import json

with open('products-data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print("Total products: " + str(len(products)))

if len(products) &gt;= 1000:
    print("Great! Already have " + str(len(products)) + " products (1000+ target achieved!)")
else:
    print("Need " + str(1000 - len(products)) + " more products to reach 1000+")
