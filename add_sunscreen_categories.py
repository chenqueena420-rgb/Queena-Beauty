# -*- coding: utf-8 -*-
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
data = json.loads(root.joinpath("products-data.json").read_text(encoding="utf-8"))

# 平價防曬產品
budget_products = [
    ("Biore 蜜妮 含水防曬水凝乳", "超微米防禦，如水般清爽", "厚重感、清爽需求", "所有膚質"),
    ("Biore 蜜妮 含水防曬水凝露", "水感質地，解決厚重感", "厚重感", "油性肌"),
    ("Biore 蜜妮 A極效防曬系列", "最高等級防禦，極限運動適用", "戶外防護", "戶外運動肌"),
    ("Biore 蜜妮 控油隔離乳液", "皮脂吸收粉末，防止脫妝", "脫妝、油膩", "油性肌"),
    ("Biore 蜜妮 光感幻白防曬精華", "提亮校色，改善曬黑暗沈", "暗沈、曬黑", "一般肌"),
    ("Skin Aqua 柔光透亮飾底凝露", "薰衣草紫校正蠟黃", "蠟黃、暗沈", "一般肌"),
    ("Skin Aqua 超保濕水感防曬露", "水感轉化技術，CP 值高", "保濕、乾燥", "乾性肌"),
    ("曼秀雷敦 SUNPLAY 戶外強效噴霧", "耐水耐汗耐摩擦", "戶外運動", "活躍肌"),
    ("曼秀雷敦 抗痘隔離霜", "防曬抗痘二合一", "痘痘、防曬", "痘痘肌"),
    ("雪芙蘭 海洋友善極效防水防曬", "預算有限者的環保首選", "環保、防曬", "環保意識者"),
    ("雪芙蘭 純物理溫和防曬", "無酒精，適合幼童與敏肌", "敏感、溫和", "幼童、敏感肌"),
    ("專科 全效防曬水凝乳", "蠶絲蛋白保濕，不乾澀", "保濕、乾澀", "乾性肌"),
    ("專科 全效防曬水凝膠", "肥皂可卸，懶人首選", "卸妝便利", "懶人族"),
    ("妮維雅 三重防護水感凝乳", "涼感配方，改善炎夏悶熱", "涼感、悶熱", "一般肌"),
    ("妮維雅 涼感防曬噴霧", "立即降溫，噴灑方便", "降溫、補擦", "活躍肌"),
    ("凡士林 5D 極護水感防曬", "5D 分層防護，適身體大面積", "身體防護", "一般肌"),
    ("香蕉船 Banana Boat 水感清爽防曬", "戶外曝曬曬傷解決", "曬傷、戶外", "戶外運動肌"),
    ("Suncut 曬可艾 強效防曬噴霧", "解決身體補擦困難", "身體補擦", "活躍肌"),
]

# 小資中價防曬產品
mid_range_products = [
    ("ALLIE 持采高效防曬", "抗摩擦技術、海洋友善", "戶外防護", "所有膚質"),
    ("ALLIE 持采舒爽柔肌", "吸脂抗汗粉體、抗摩擦", "夏天黏膩", "油性肌"),
    ("ALLIE 持采濾鏡 (杏桃茜)", "校色粉體、玻尿酸、控油", "膚色不均", "一般肌"),
    ("SOFINA 漾緁 控油", "超強控油、持妝、防止脫妝", "控油、持妝", "油性肌"),
    ("AHC 向日葵強力防曬棒", "旋轉設計不沾手、向日葵籽油", "便攜補擦", "活躍肌"),
    ("ROUND LAB 白樺樹", "白樺樹汁、玻尿酸、爆水質地", "保濕、水感", "混合肌"),
    ("Beauty of Joseon 穀物", "溫和穀物萃取、不泛白不油膩", "亮白、溫和", "所有膚質"),
    ("Neogence 霓淨思 全天候極效抗陽", "潛水活動首選、海洋友善", "戶外運動", "活躍肌"),
    ("DHC 金靚白水感防曬", "輔酶 Q10 搭配橄欖精華", "美白、抗氧化", "一般肌"),
    ("Kose Suncut 完美防曬凝膠", "高係數超防水", "防水、高係數", "油性肌"),
    ("Skin Aqua 亮白隔離防曬精華", "維他命 C 衍生物，改善暗沈", "亮白、提亮", "一般肌"),
    ("Target Pro 低敏亮白防曬乳", "敏肌專用高係數", "敏感肌", "敏感肌"),
    ("露得清 細白晶透防曬乳", "UVA/UVB 廣譜防護", "廣譜防護", "一般肌"),
    ("Eucerin 控油防曬乳", "L-Carnitine 控油，啞光質地", "控油、啞光", "油性肌"),
]

# 專業醫美防曬產品
professional_products = [
    ("理膚寶水 全護極致抗陽", "專利濾鏡 Mexoryl 400，阻隔超長波 UVA", "抗老、防曬", "所有膚質"),
    ("理膚寶水 全護清爽防曬液", "專利濾鏡、潤色防護、預防色斑", "色斑、曬老", "敏弱肌"),
    ("安耐曬 金鑽高效", "自動修復技術、耐水耐汗", "戶外運動", "活躍肌"),
    ("安耐曬 臉部濾鏡", "美肌光轉化技術、提亮", "澎潤感、提亮", "混合肌"),
    ("雅漾 Avene 超能控油", "TriAsorB 專利濾鏡 (抗藍光)", "控油、抗藍光", "油性肌"),
    ("雅漾 Avene 高效自然", "純物理防曬、抗氧化、高穩定濾劑", "敏感肌、術後", "敏感肌"),
    ("貝膚黛瑪 全能強效", "SUN ACTIVE DEFENSE 專利、純物理", "術後修護", "敏感肌"),
    ("Curél 潤浸保濕輕透", "潤浸保濕 Ceramide (神經醯胺修護)", "保濕、修護", "敏感肌"),
    ("CeraVe 適樂膚 保濕", "MVE 緩釋技術、高效三重神經醯胺", "乾癢、敏感", "敏感肌"),
    ("CeraVe 適樂膚 寬頻", "純物理遮蔽、神經醯胺", "醫美術後、極度敏感", "敏感肌"),
    ("d program 敏感話題", "過敏防禦科技，阻隔花粉與塵埃", "過敏防禦", "敏感肌"),
    ("Vichy 薇姿 極效清爽防曬乳", "清爽控油科技", "控油、清爽", "油性肌"),
    ("Cetaphil 全日護清爽防曬凝乳", "溫和甘油保濕", "保濕、溫和", "敏感肌"),
    ("M.A.C 超顯白系列 妝前乳", "提亮防護", "提亮、妝前", "一般肌"),
]

def create_product(name, brand, features, pain, skin, tier, level):
    return {
        "name": name,
        "brand": brand,
        "features": features,
        "pain": pain,
        "skin": skin,
        "category": "防曬",
        "available_at": ["屈臣氏", "康是美", "寶雅"],
        "links": {
            "屈臣氏": "#",
            "康是美": "#",
            "寶雅": "#"
        },
        "prices": {
            "標籤": "",
            "屈臣氏": None,
            "康是美": None,
            "寶雅": None
        },
        "lowest_price_store": "請點擊連結查看即時價格",
        "tier": tier,
        "level": level
    }

# 提取品牌名稱
def get_brand(name):
    brands = ["Biore", "Skin Aqua", "曼秀雷敦", "雪芙蘭", "專科", "妮維雅", "凡士林", "香蕉船", "自白肌", 
              "Za", "喜蜜", "Suncut", "Kose", "ALLIE", "SOFINA", "AHC", "ROUND LAB", "Beauty of Joseon",
              "Neogence", "DHC", "Target Pro", "露得清", "Eucerin", "理膚寶水", "安耐曬", "雅漾", "貝膚黛瑪",
              "Curél", "CeraVe", "d program", "Vichy", "Cetaphil", "M.A.C", "L'EGERE"]
    for brand in brands:
        if brand in name:
            return brand
    return name.split()[0]

# 添加平價產品
for name, features, pain, skin in budget_products:
    brand = get_brand(name)
    product = create_product(name, brand, features, pain, skin, "平價", "✨ 平價")
    data.append(product)

# 添加小資中價產品
for name, features, pain, skin in mid_range_products:
    brand = get_brand(name)
    product = create_product(name, brand, features, pain, skin, "小資中價", "🌿 小資中價")
    data.append(product)

# 添加專業醫美產品
for name, features, pain, skin in professional_products:
    brand = get_brand(name)
    product = create_product(name, brand, features, pain, skin, "專業醫美", "🌺 專業醫美")
    data.append(product)

# 寫入更新後的 JSON
root.joinpath("products-data.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"已添加 {len(budget_products) + len(mid_range_products) + len(professional_products)} 件防曬產品")
print(f"平價: {len(budget_products)} 件")
print(f"小資中價: {len(mid_range_products)} 件")
print(f"專業醫美: {len(professional_products)} 件")
