import json
import os

# 設定檔案名稱
input_file = 'new_products.txt'
output_file = 'products-data.json'

if not os.path.exists(input_file):
    print(f"❌ 找不到 {input_file}，請確認妳有建立這個檔案！")
    exit()

new_data = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        # 處理隱形空格並去除前後空白
        line = line.replace('\xa0', ' ').strip()
        if not line: continue
        
        # 尋找冒號的位置（不管是全形還是半形）
        sep = "：" if "：" in line else ":"
        if sep not in line:
            continue
            
        full_name_part, desc = line.split(sep, 1)
        
        # 判斷分類
        level = "✨ 平價好物"
        clean_name = full_name_part
        
        if "專業醫美" in full_name_part:
            level = "🩺 專業醫美"
            clean_name = full_name_part.replace("專業醫美", "").strip()
        elif "小資中價" in full_name_part:
            level = "🌿 小資中價"
            clean_name = full_name_part.replace("小資中價", "").strip()
        elif "平價" in full_name_part:
            level = "✨ 平價好物"
            clean_name = full_name_part.replace("平價", "").strip()

        new_data.append({
            "name": clean_name,
            "description": desc.strip(),
            "level": level,
            "category": "唇部"
        })

# 讀取並寫入
data_list = []
if os.path.exists(output_file):
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            data_list = json.load(f)
    except:
        data_list = []

data_list.extend(new_data)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=2)

print(f"📢 掃描完成！")
print(f"✅ 成功抓到 {len(new_data)} 筆新商品。")