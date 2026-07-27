
import json
import re

# 读取更新后的产品数据
with open('products-data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# 读取 index.html 文件
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 更新 productData 数据
# 找到 productData 的部分
product_data_str = json.dumps(products, ensure_ascii=False, separators=(',', ':'))
# 替换原来的 productData
html_content = re.sub(
    r'const productData = \[.*?\];',
    f'const productData = {product_data_str};',
    html_content,
    flags=re.DOTALL
)

# 修改 renderCard 函数
new_render_card = '''function renderCard(row) {
  const p = row.p;
  const em = CAT_EMOJI[p.category] || CAT_EMOJI["其他"];
  const cc = catClass(p.category);
  const hint =
    row.score > 0 && row.hits.length
      ? '<p class="match-hint">匹配：' + esc(row.hits.slice(0, 5).join(" · ")) + (row.hits.length > 5 ? "…" : "") + "</p>"
      : "";
  const sc = row.score > 0 ? '<span class="badge-score">相關 ' + row.score.toFixed(1) + "</span>" : "";
  
  // 價格區間判斷邏輯
  let priceDisplay;
  if (!p.price) {
    priceDisplay = '價格查詢中';
  } else if (p.price < 500) {
    priceDisplay = '平價';
  } else if (p.price <= 1500) {
    priceDisplay = '中位';
  } else {
    priceDisplay = '專櫃';
  }
  
  let buyButtons = '';
  if (p.links) {
    if (p.links['屈臣氏']) {
      buyButtons += '<a class="btn-buy wat" href="' + escAttr(p.links['屈臣氏']) + '" target="_blank" rel="noopener noreferrer">去屈臣氏買</a>';
    }
    if (p.links['康是美']) {
      buyButtons += '<a class="btn-buy cosmed" href="' + escAttr(p.links['康是美']) + '" target="_blank" rel="noopener noreferrer">去康是美買</a>';
    }
    if (p.links['寶雅']) {
      buyButtons += '<a class="btn-buy poya" href="' + escAttr(p.links['寶雅']) + '" target="_blank" rel="noopener noreferrer">去寶雅買</a>';
    }
  }
  
  return (
    '<article class="card">' +
    '<div class="card-visual ' +
    cc +
    '" aria-hidden="true"><span style="position:relative;z-index:1;text-shadow:0 2px 12px rgba(0,0,0,.15)">' +
    em +
    "</span></div>" +
    '<div class="card-body">' +
    '<div class="badges"><span class="badge-cat">' +
    esc(p.category) +
    "</span>" +
    sc +
    "</div>" +
    "<h2>" +
    esc(p.name) +
    "</h2>" +
    '<p class="price-note">售價分級：' + priceDisplay + '</p>' +
    '<dl class="dl">' +
    "<dt>核心成分與特性</dt><dd>" +
    esc(p.features) +
    "</dd>" +
    '<dt>解決痛點</dt><dd class="pain">' +
    esc(p.pain) +
    "</dd>" +
    "<dt>適合膚質</dt><dd>" +
    esc(p.skin) +
    "</dd></dl>" +
    hint +
    '<div class="buy-actions">' +
    buyButtons +
    "</div>" +
    '<p class="buy-foot">將開啟通路頁面（需連線）</p>' +
    "</div></article>"
  );
}'''

# 替换 renderCard 函数
html_content = re.sub(
    r'function renderCard\(row\) \{[\s\S]*?\}',
    new_render_card,
    html_content
)

# 保存更新后的 index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully updated index.html!')

