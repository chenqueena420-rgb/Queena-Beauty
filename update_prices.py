import json
import pathlib
import requests
import time
import random
import re
from bs4 import BeautifulSoup

# 配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

REQUEST_DELAY = 1.5  # 延遲避免被封

# 價格提取函數
def extract_price_cosmed(html):
    """從康是美頁面提取價格"""
    soup = BeautifulSoup(html, 'html.parser')
    # 康是美價格通常在特定 class 中
    price_elements = soup.find_all('span', class_=re.compile(r'price|amount'))
    for elem in price_elements:
        text = elem.get_text().strip()
        # 匹配價格格式，如 NT$299 或 299
        match = re.search(r'(\d{1,4}(?:,\d{3})*)', text.replace(',', ''))
        if match:
            return match.group(1)
    return None

def extract_price_poya(html):
    """從寶雅頁面提取價格"""
    soup = BeautifulSoup(html, 'html.parser')
    # 寶雅價格通常在特定 class 中
    price_elements = soup.find_all('span', class_=re.compile(r'price|cost'))
    for elem in price_elements:
        text = elem.get_text().strip()
        match = re.search(r'(\d{1,4}(?:,\d{3})*)', text.replace(',', ''))
        if match:
            return match.group(1)
    return None

def extract_price_watsons(html):
    """從屈臣氏頁面提取價格"""
    soup = BeautifulSoup(html, 'html.parser')
    # 屈臣氏價格通常在特定 class 中
    price_elements = soup.find_all('span', class_=re.compile(r'price|amount|cost'))
    for elem in price_elements:
        text = elem.get_text().strip()
        match = re.search(r'(\d{1,4}(?:,\d{3})*)', text.replace(',', ''))
        if match:
            return match.group(1)
    return None

def fetch_price(store, url):
    """抓取指定商店的價格"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            return "查看官網"
        
        html = response.text
        
        if store == "康是美":
            price = extract_price_cosmed(html)
        elif store == "寶雅":
            price = extract_price_poya(html)
        elif store == "屈臣氏":
            price = extract_price_watsons(html)
        else:
            return "查看官網"
        
        return price if price else "查看官網"
    
    except Exception as e:
        print(f"抓取 {store} 價格失敗: {url} - {e}")
        return "查看官網"

def main():
    # 讀取原始資料
    data_path = pathlib.Path('products-data.json')
    if not data_path.exists():
        print("找不到 products-data.json 檔案")
        return
    
    with data_path.open('r', encoding='utf-8') as f:
        products = json.load(f)
    
    print(f"開始處理 {len(products)} 筆產品...")
    
    # 處理每個產品
    for i, product in enumerate(products, 1):
        name = product.get('name', '未知產品')
        links = product.get('links', {})
        
        prices = {}
        
        # 處理每個商店
        for store in ['屈臣氏', '康是美', '寶雅']:
            url = links.get(store)
            if url:
                print(f"[{i}/{len(products)}] 抓取 {name} - {store}...")
                price = fetch_price(store, url)
                prices[store] = price
                time.sleep(random.uniform(REQUEST_DELAY, REQUEST_DELAY + 1))  # 隨機延遲
            else:
                prices[store] = "查看官網"
        
        # 新增 prices 欄位
        product['prices'] = prices
        
        if i % 50 == 0:
            print(f"已處理 {i} 筆產品...")
    
    # 儲存到新檔案
    output_path = pathlib.Path('products-data-with-prices.json')
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    
    print(f"完成！結果已儲存到 {output_path}")

if __name__ == "__main__":
    main()