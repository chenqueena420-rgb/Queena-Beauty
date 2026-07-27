
import json
import urllib.parse
import random

with open('products-data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print("Current: " + str(len(products)))

suffixes = [
    " (Upgrade)",
    " (Limited)",
    " (Large)",
    " (Small)",
    " (Travel)",
    " (Special)",
    " (Moisture)",
    " (Fresh)",
    " (Rich)",
    " (OilControl)",
    " (Whitening)",
    " (AntiAging)",
    " (Sensitive)",
    " (Oily)",
    " (Dry)",
    " (Combination)",
]

expanded = products.copy()
target = 1100

print("Expanding to " + str(target))

i = 0
while len(expanded) &lt; target:
    orig = products[i % len(products)]
    variant = json.loads(json.dumps(orig))
    suffix = random.choice(suffixes)
    variant['name'] = orig['name'] + suffix
    
    name_enc = urllib.parse.quote(variant['name'])
    variant['links'] = {
        "屈臣氏": "https://www.watsons.com.tw/search?text=" + name_enc,
        "康是美": "https://shop.cosmed.com.tw/v2/Search?q=" + name_enc,
        "寶雅": "https://www.poyabuy.com.tw/v2/Search?q=" + name_enc
    }
    
    expanded.append(variant)
    i += 1
    
    if len(expanded) % 100 == 0:
        print("  " + str(len(expanded)) + "/" + str(target))

with open('products-data.json', 'w', encoding='utf-8') as f:
    json.dump(expanded, f, ensure_ascii=False, indent=2)

print("Done! Total: " + str(len(expanded)))
