# -*- coding: utf-8 -*-
import json

# 專業醫美產品列表
professional_products = [
    "理膚寶水 全護極致抗陽 (UVMUNE 400)",
    "理膚寶水 全護清爽防曬液",
    "Anessa 安耐曬 金鑽高效防曬露 (升級版)",
    "Anessa 安耐曬 金鑽高效防曬露 NA",
    "Anessa 安耐曬 金鑽高效防曬露",
    "Anessa 安耐曬 金鑽高效防曬凝膠 NA",
    "Anessa 安耐曬 臉部濾鏡防曬",
    "ANESSA 金鑽高效防曬乳 NA (敏弱肌)",
    "雅漾 Avene 超能控油清爽防曬",
    "雅漾 Avene 高效自然防曬乳",
    "貝膚黛瑪 全能強效防曬乳",
    "Curél 潤浸保濕輕透防曬乳",
    "CeraVe 適樂膚 保濕防曬乳",
    "CeraVe 適樂膚 全效清爽修護防曬乳",
    "CeraVe 適樂膚 寬頻防曬乳",
    "d program 敏感話題 淨化隔離",
    "Vichy 薇姿 極效清爽防曬乳",
    "Target Pro 低敏亮白防曬乳 (防水型)"
]

# 小資中價產品列表
mid_range_products = [
    "ALLIE 持采系列",
    "ALLIE 持采高效防曬水凝乳 EX",
    "ALLIE 持采舒爽柔肌",
    "ALLIE 持采濾鏡 (杏桃茜妍)",
    "AHC 向日葵強力防曬棒",
    "AHC 極致防禦長效水潤防曬乳",
    "AHC 向日葵強力防曬棒 (二入組)",
    "SOFINA 蘇菲娜 iP 輕瑩高效美容防曬乳 03",
    "SOFINA 蘇菲娜 iP 輕瑩高效美容防曬乳 (光透亮)",
    "SOFINA 漾緁 控油瓷效妝前隔離乳",
    "ROUND LAB 白樺樹補水防曬",
    "ROUND LAB 白樺樹保濕防曬霜",
    "Beauty of Joseon 朝鮮美女 大米亮白防曬霜",
    "DHC 金靚白水感防曬",
    "DHC 金靚白水感防曬乳",
    "L`EGERE 安瓶防曬系列",
    "Neogence 霓淨思 全天候極效抗陽",
    "Neogence 霓淨思 全天候長效抗陽防曬乳",
    "Neogence 霓淨思 全天候長效抗陽 (大容量)",
    "Target Pro 肌膚專研低敏亮白防曬乳 (防水型)",
    "Target Pro 肌膚專研低敏亮白防曬乳",
    "Eucerin 控油防曬乳",
    "妮維雅 全護清爽系列 (敏感肌)",
    "妮維雅 全護清爽防曬隔離乳 (敏感肌專用)",
    "妮維雅 專業級防曬乳 (200ml)",
    "妮維雅 專業級防曬乳 (光敏感測試版)",
    "韓國 BEAUSTA 自然完美屏障防曬霜",
    "Mentholatum Skin Aqua 亮白隔離防曬精華",
    "Kose Suncut UV 完美防曬凝膠",
    "Kose Suncut 曬可艾 完美防曬凝膠",
    "Kose Suncut 曬可艾 防曬噴霧 (大容量)",
    "Suncut 曬可艾 強效防曬噴霧",
    "Dr.Satin 魚子校色隔離防曬 (綠)",
    "碧歐斯 超能煥白極光防曬",
    "Neutrogena 露得清 細白晶透防曬乳",
    "SKINTIFIC 啞光防曬霜",
    "SKINTIFIC 積雪草啞光防曬",
    "M.A.C 超顯白系列 妝前乳",
    "蕾吉兒 L`EGERE 安瓶防曬 (單品)",
    "曼秀雷敦 水潤肌亮白隔離防曬精華",
    "Dr.Satin 魚子校色隔離 (綠色款)",
    "妮維雅 專業級防曬 (戶外款)",
    "AHC 極致防禦水潤 (50ML)",
    "ROUND LAB 白樺樹 (補水型)",
    "ALLIE 持采系列 (海洋友善)",
    "蘇菲娜 iP 輕瑩高效 (光透亮)",
    "Target Pro 肌膚專研 (防水型)"
]

# 平價產品列表
budget_products = [
    "Biore 含水防曬系列 (水凝乳/水凝露)",
    "Biore 蜜妮 含水防曬水凝乳",
    "Biore 蜜妮 含水防曬水凝乳 (經典款)",
    "Biore 蜜妮 含水防曬保濕水凝乳",
    "Biore 蜜妮 A 極效防曬系列",
    "Biore 蜜妮 A 極效防曬精華",
    "Biore 蜜妮 A 極效防曬乳 (戶外專用)",
    "Biore 蜜妮 A 極效防曬 (戶外精華)",
    "Biore 蜜妮 控油隔離乳液",
    "Biore 蜜妮 UV Aqua Rich 光感幻白防曬精華",
    "Biore 蜜妮 高防曬約會必備隔離乳",
    "Biore 蜜妮 高防曬 (經典隔離)",
    "Biore 蜜妮 控油隔離 (乳液款)",
    "Biore 蜜妮 光感幻白 (精華款)",
    "Biore 蜜妮 A 極效防曬 (烈日款)",
    "專科 全效防曬系列 (水凝乳/水凝露)",
    "專科 全效防曬水凝乳 (亮顏粉)",
    "專科 全效防曬水凝乳",
    "專科 全效防曬水凝膠",
    "專科 完美防曬水凝膠",
    "專科 完美水感防曬乳",
    "專科 全效防曬 (補水型)",
    "專科 全效系列 (水凝乳)",
    "曼秀雷敦 水潤肌柔光透亮隔離乳",
    "曼秀雷敦 水潤肌柔光透亮飾底凝露",
    "曼秀雷敦 SUNPLAY 戶外強效型",
    "曼秀雷敦 SUNPLAY 戶外強效 (噴霧款)",
    "曼秀雷敦 抗痘隔離霜",
    "曼秀雷敦 Skin Aqua 超保濕水感防曬露",
    "曼秀雷敦 柔光透亮隔離 (薰衣草)",
    "曼秀雷敦 SUNPLAY (登山款)",
    "Skin Aqua 曼秀雷敦 超保濕水感 (大容量)",
    "妮維雅 三重防護水感防曬凝乳 (涼感舒緩)",
    "妮維雅 涼感防曬噴霧",
    "妮維雅 SUN 水感清透防曬凝露",
    "妮維雅 三重防護 (涼感版)",
    "妮維雅 涼感噴霧 (強效型)",
    "雪芙蘭 海洋友善極效防水防曬乳",
    "雪芙蘭 純物理溫和防曬",
    "雪芙蘭 防曬水凝乳 (SPF50+)",
    "雪芙蘭 防曬水凝乳 (涼感版)",
    "雪芙蘭 海洋友善 (小資款)",
    "雪芙蘭 涼感水凝乳 (降溫款)",
    "凡士林 5D 極護水感防曬",
    "凡士林 5D 防曬 (身體用)",
    "凡士林 5D 極護 (水感型)",
    "自白肌 玻尿酸涼感防曬乳液",
    "自白肌 玻尿酸涼感 (噴霧型)",
    "Za 美白隔離霜 (經典版)",
    "Za 美白隔離 (經典潤色)",
    "喜蜜 HEME 清透水感防曬凝膠",
    "喜蜜 HEME 水感防曬 (40ml)",
    "香蕉船 Banana Boat 水感清爽防曬乳",
    "香蕉船 水感清爽 SPF50",
    "香蕉船 水感清爽 (速乾型)",
    "我的美麗日記 蜜若藍高保濕防曬",
    "我的美麗日記 蜜若藍 (辦公室款)",
    "我的美麗日記 水感防曬 (保濕款)",
    "SKINTIFIC 啞光防曬 (控油款)",
    "L`EGERE 安瓶防曬 (美白系列)",
    "專科 完美水感 (凝膠款)",
    "Biore 蜜妮 高防曬 (潤色款)",
    "曼秀雷敦 抗痘隔離 (潤色款)",
    "雪芙蘭 純物理 (敏肌專用)",
    "Skin Aqua 曼秀雷敦 (保濕露)"
]

# 載入現有數據
data = json.load(open('products-data.json', encoding='utf-8'))

# 創建產品名稱到分類的映射
tier_mapping = {}

# 添加專業醫美產品
for product in professional_products:
    tier_mapping[product] = ('專業醫美', '🩺 專業醫美')

# 添加小資中價產品
for product in mid_range_products:
    tier_mapping[product] = ('小資中價', '🌿 小資中價')

# 添加平價產品
for product in budget_products:
    tier_mapping[product] = ('平價', '✨ 平價')

# 更新數據庫中的產品
updated_count = 0
for product in data:
    if product.get('category') == '防曬':
        name = product.get('name', '')
        if name in tier_mapping:
            new_tier, new_level = tier_mapping[name]
            if product.get('tier') != new_tier or product.get('level') != new_level:
                product['tier'] = new_tier
                product['level'] = new_level
                updated_count += 1

# 保存更新後的數據
json.dump(data, open('products-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print(f'✓ 已更新 {updated_count} 件防曬產品的分類')

# 統計最終結果
sunscreen = [p for p in data if p.get('category') == '防曬']
by_tier = {}
for p in sunscreen:
    tier = p.get('tier', 'N/A')
    by_tier[tier] = by_tier.get(tier, 0) + 1

print(f'\n最終統計:')
print(f'  總防曬產品: {len(sunscreen)} 件')
print(f'  平價: {by_tier.get("平價", 0)} 件 ✨')
print(f'  小資中價: {by_tier.get("小資中價", 0)} 件 🌿')
print(f'  專業醫美: {by_tier.get("專業醫美", 0)} 件 🩺')
print(f'  未分類: {by_tier.get("N/A", 0)} 件')
