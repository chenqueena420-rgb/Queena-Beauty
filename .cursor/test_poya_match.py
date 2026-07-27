import json
import pathlib
import urllib.parse
import requests
import time

# Paths
ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "products-data.json"

def check_poya_availability(product_name):
    encoded_name = urllib.parse.quote(product_name)
    url = f"https://www.poyabuy.com.tw/v2/Search?q={encoded_name}"
    try:
        # We look for some indication that products were found. 
        # Usually POYA's search page has product cards if found.
        # This is a simplified check.
        resp = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        if resp.status_code == 200:
            # Check if common "no result" text exists
            if "找不到相關商品" in resp.text or "搜尋不到" in resp.text:
                return False, url
            return True, url
    except Exception as e:
        print(f"Error checking {product_name}: {e}")
    return False, url

def main():
    data = json.loads(DB_PATH.read_text(encoding="utf-8"))
    
    # Let's test first 20 items to see if it works
    test_count = 20
    for i in range(min(test_count, len(data))):
        name = data[i]["name"]
        available, url = check_poya_availability(name)
        print(f"Product: {name} -> POYA Available: {available}")
        time.sleep(1) # Be nice

if __name__ == "__main__":
    main()
