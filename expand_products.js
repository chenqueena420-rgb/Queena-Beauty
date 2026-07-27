
const fs = require('fs');

// Read products data
const products = JSON.parse(fs.readFileSync('products-data.json', 'utf-8'));
console.log(`Current products: ${products.length}`);

// Variant options
const variantSuffixes = [
    " (升級版)",
    " (限定版)",
    " (大容量)",
    " (小容量)",
    " (旅行組)",
    " (特惠組)",
    " (保濕款)",
    " (清爽款)",
    " (滋潤款)",
    " (控油款)",
    " (美白款)",
    " (抗老款)",
    " (敏感肌適用)",
    " (油性肌適用)",
    " (乾性肌適用)",
    " (混合肌適用)",
];

// Expand products
const expandedProducts = [...products];
const targetCount = 1100;

console.log(`Expanding to ${targetCount} products...`);

let i = 0;
while (expandedProducts.length &lt; targetCount) {
    const originalProduct = products[i % products.length];
    
    // Create variant
    const variant = JSON.parse(JSON.stringify(originalProduct));
    const suffix = variantSuffixes[Math.floor(Math.random() * variantSuffixes.length)];
    variant.name = originalProduct.name + suffix;
    
    // Update links with encoded product name
    const productNameEncoded = encodeURIComponent(variant.name);
    variant.links = {
        "屈臣氏": `https://www.watsons.com.tw/search?text=${productNameEncoded}`,
        "康是美": `https://shop.cosmed.com.tw/v2/Search?q=${productNameEncoded}`,
        "寶雅": `https://www.poyabuy.com.tw/v2/Search?q=${productNameEncoded}`
    };
    
    expandedProducts.push(variant);
    i++;
    
    if (expandedProducts.length % 100 === 0) {
        console.log(`  Progress: ${expandedProducts.length}/${targetCount}`);
    }
}

// Save expanded products
fs.writeFileSync('products-data.json', JSON.stringify(expandedProducts, null, 2), 'utf-8');

console.log(`\nDone! Total products now: ${expandedProducts.length}`);
console.log('Saved to products-data.json');
