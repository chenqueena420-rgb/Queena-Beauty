import json

# 1. 讀取你原本的資料
with open('products-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. 換成你的蝦皮分潤連結 (請把底下的網址換成你在蝦皮聯盟拿到的實際長連結)
SHOPEE_AFFILIATE_LINK = "https://affsrc.com/你的蝦皮分潤連結"

# 3. 迴圈遍歷所有商品，把所有通路按鈕的網址全部改成蝦皮分潤連結
for p in data:
    if 'links' in p and isinstance(p['links'], dict):
        for platform in p['links']:
            # 只要該平台原本有連結，就全部替換成蝦皮連結
            if p['links'][platform] is not None:
                p['links'][platform] = SHOPEE_AFFILIATE_LINK

# 4. 輸出成新檔案確保安全
with open('products-data-updated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("全部改成蝦皮連結完成！請檢查 products-data-updated.json")