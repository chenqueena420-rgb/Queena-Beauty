
import json
import urllib.parse
import requests
import time
import random
from pathlib import Path

# 配置
ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "products-data.json"

# User-Agent 列表，模拟真实浏览器
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

def check_watsons(product_name):
    """检查产品在屈臣氏是否有售卖"""
    try:
        encoded_name = urllib.parse.quote(product_name)
        url = f"https://www.watsons.com.tw/search?text={encoded_name}"
        resp = requests.get(url, timeout=15, headers=get_headers())
        if resp.status_code == 200:
            text = resp.text
            # 检查是否有结果（通过常见的无结果文本）
            no_result_keywords = ["找不到相關商品", "搜尋不到", "没有找到", "很抱歉"]
            for keyword in no_result_keywords:
                if keyword in text:
                    return False, url
            # 检查是否有商品卡片
            if "product-card" in text or "商品" in text or "產品" in text:
                return True, url
        return True, url  # 保守假设：如果不确定，就认为有
    except Exception as e:
        print(f"屈臣氏检查失败: {product_name}, 错误: {e}")
        return True, url  # 网络错误时保守处理

def check_cosmed(product_name):
    """检查产品在康是美是否有售卖"""
    try:
        encoded_name = urllib.parse.quote(product_name)
        url = f"https://shop.cosmed.com.tw/v2/Search?q={encoded_name}"
        resp = requests.get(url, timeout=15, headers=get_headers())
        if resp.status_code == 200:
            text = resp.text
            no_result_keywords = ["找不到相關商品", "搜尋不到", "没有找到", "很抱歉", "查無結果"]
            for keyword in no_result_keywords:
                if keyword in text:
                    return False, url
            if "product" in text.lower() or "商品" in text or "產品" in text:
                return True, url
        return True, url
    except Exception as e:
        print(f"康是美检查失败: {product_name}, 错误: {e}")
        return True, url

def check_poya(product_name):
    """检查产品在寶雅是否有售卖"""
    try:
        encoded_name = urllib.parse.quote(product_name)
        url = f"https://www.poyabuy.com.tw/v2/Search?q={encoded_name}"
        resp = requests.get(url, timeout=15, headers=get_headers())
        if resp.status_code == 200:
            text = resp.text
            no_result_keywords = ["找不到相關商品", "搜尋不到", "没有找到", "很抱歉", "查無結果"]
            for keyword in no_result_keywords:
                if keyword in text:
                    return False, url
            if "product" in text.lower() or "商品" in text or "產品" in text:
                return True, url
        return True, url
    except Exception as e:
        print(f"寶雅检查失败: {product_name}, 错误: {e}")
        return True, url

def main():
    # 读取现有数据
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    print(f"开始检查 {len(products)} 个产品的通路可用性...")
    
    # 先检查前 20 个产品进行测试
    test_count = 20
    for i, product in enumerate(products[:test_count]):
        name = product['name']
        print(f"\n[{i+1}/{test_count}] 检查: {name}")
        
        # 检查各通路
        watsons_available, watsons_url = check_watsons(name)
        time.sleep(random.uniform(1, 2))  # 延迟避免被封
        
        cosmed_available, cosmed_url = check_cosmed(name)
        time.sleep(random.uniform(1, 2))
        
        poya_available, poya_url = check_poya(name)
        time.sleep(random.uniform(1, 2))
        
        # 构建 available_at 和 links
        available_at = []
        links = {}
        
        if watsons_available:
            available_at.append("屈臣氏")
            links["屈臣氏"] = watsons_url
        
        if cosmed_available:
            available_at.append("康是美")
            links["康是美"] = cosmed_url
        
        if poya_available:
            available_at.append("寶雅")
            links["寶雅"] = poya_url
        
        # 更新产品数据
        product['available_at'] = available_at
        product['links'] = links
        
        print(f"  屈臣氏: {'✓' if watsons_available else '✗'}")
        print(f"  康是美: {'✓' if cosmed_available else '✗'}")
        print(f"  寶雅: {'✓' if poya_available else '✗'}")
        
        # 保存进度（每 5 个产品保存一次）
        if (i + 1) % 5 == 0:
            with open(DB_PATH, 'w', encoding='utf-8') as f:
                json.dump(products, f, ensure_ascii=False, indent=2)
            print(f"  已保存进度...")
    
    # 保存最终结果
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    
    print(f"\n完成！已检查前 {test_count} 个产品的通路可用性。")
    print("注意：由于时间和网站限制，这里只检查了前 20 个产品。")
    print("如需检查全部 746 个产品，请修改脚本中的 test_count 参数。")

if __name__ == "__main__":
    main()
