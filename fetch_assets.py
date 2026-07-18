import json
import re
import time
import urllib.parse
import urllib.request
from html import unescape

JSON_PATH = 'products-data.json'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
REQUEST_DELAY = 1.2
TIMEOUT = 30

STORE_CONFIG = {
    '屈臣氏': {
        'search_template': 'https://www.watsons.com.tw/search?text={}',
        'patterns': [
            r'href=["\'](https?://www\.watsons\.com\.tw/(?:product|Product|prod|search)[^"\']+)["\']',
            r'href=["\'](/(?:product|Product|prod|search)[^"\']+)["\']',
            r'href=["\'](/[^"\']*product[^"\']+)["\']',
            r'"(https?://www\.watsons\.com\.tw/[^"\']*product[^"\']+)"',
            r'"(/[^"\']*product[^"\']+)"',
        ],
    },
    '康是美': {
        'search_template': 'https://shop.cosmed.com.tw/v2/Search?q={}',
        'patterns': [
            r'href=["\'](https?://shop\.cosmed.com\.tw/[^"\']+)["\']',
            r'href=["\'](/v2/Product[^"\']+)["\']',
            r'href=["\'](/ProductDetail[^"\']+)["\']',
            r'"(https?://shop\.cosmed.com\.tw/[^"\']*Product[^"\']+)"',
            r'"(/v2/Product[^"\']+)"',
            r'"(/ProductDetail[^"\']+)"',
        ],
    },
    '寶雅': {
        'search_template': 'https://www.poyabuy.com.tw/v2/Search?q={}',
        'patterns': [
            r'href=["\'](https?://www\.poyabuy\.com\.tw/[^"\']+)["\']',
            r'href=["\'](/v2/Product[^"\']+)["\']',
            r'href=["\'](/ProductDetail[^"\']+)["\']',
            r'"(https?://www\.poyabuy\.com\.tw/[^"\']*Product[^"\']+)"',
            r'"(/v2/Product[^"\']+)"',
            r'"(/ProductDetail[^"\']+)"',
        ],
    },
}

IMAGE_PATTERNS = [
    r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
    r'<meta[^>]+name=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
    r'<meta[^>]+property=["\']og:image:secure_url["\'][^>]+content=["\']([^"\']+)["\']',
    r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\'][^"\']*'+r'{}'+r'[^"\']*["\']',
    r'<img[^>]+data-src=["\']([^"\']+)["\']',
    r'<img[^>]+src=["\']([^"\']+)["\']',
]


def fetch_html(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            charset = resp.headers.get_content_charset() or 'utf-8'
            return resp.read().decode(charset, errors='ignore')
    except Exception as exc:
        print(f'Warning: fetch failed for {url} -> {exc}')
        return None


def normalize_url(url, base_url=None):
    if not url:
        return None
    url = unescape(url.strip())
    if url.startswith('//'):
        return 'https:' + url
    if url.startswith('http://') or url.startswith('https://'):
        return url
    if base_url:
        return urllib.parse.urljoin(base_url, url)
    return url


def extract_candidates(html, base_url, patterns):
    if not html:
        return []
    candidates = []
    for pattern in patterns:
        for match in re.finditer(pattern, html, flags=re.IGNORECASE):
            href = match.group(1).strip()
            href = normalize_url(href, base_url)
            if href and href not in candidates:
                candidates.append(href)
    return candidates


def choose_best_candidate(candidates, query):
    if not candidates:
        return None
    if not query:
        return candidates[0]
    query_lower = urllib.parse.unquote(query).lower()
    for candidate in candidates:
        if query_lower in candidate.lower():
            return candidate
    return candidates[0]


def build_search_url(store, query):
    encoded = urllib.parse.quote(query)
    template = STORE_CONFIG[store]['search_template']
    return template.format(encoded)


def find_store_product_link(store, query):
    search_url = build_search_url(store, query)
    html = fetch_html(search_url)
    time.sleep(REQUEST_DELAY)
    if not html:
        return None
    patterns = STORE_CONFIG[store]['patterns']
    candidates = extract_candidates(html, search_url, patterns)
    if candidates:
        return choose_best_candidate(candidates, query)
    # Fallback: try raw URLs in JSON or script payloads
    if store == '屈臣氏':
        fallback = re.findall(r'https?://www\.watsons\.com\.tw/[^"\'>\s]+', html, flags=re.IGNORECASE)
    elif store == '康是美':
        fallback = re.findall(r'https?://shop\.cosmed\.com\.tw/[^"\'>\s]+', html, flags=re.IGNORECASE)
    else:
        fallback = re.findall(r'https?://www\.poyabuy\.com\.tw/[^"\'>\s]+', html, flags=re.IGNORECASE)
    fallback = [normalize_url(url, search_url) for url in fallback]
    return choose_best_candidate(fallback, query)


def extract_image_from_html(html, query=None):
    if not html:
        return None
    for pattern in IMAGE_PATTERNS:
        formatted = pattern.format(re.escape(query)) if '{}' in pattern else pattern
        match = re.search(formatted, html, flags=re.IGNORECASE)
        if match:
            image_url = normalize_url(match.group(1))
            if image_url and image_url.startswith('http'):
                return image_url
    return None


def resolve_image_url(product, store_links):
    # Prefer linker product pages first
    for store in ['屈臣氏', '康是美', '寶雅']:
        link = store_links.get(store)
        if not link:
            continue
        html = fetch_html(link)
        time.sleep(REQUEST_DELAY)
        if not html:
            continue
        image_url = extract_image_from_html(html, product.get('name', ''))
        if image_url:
            return image_url
    # fallback: use Watsons search page for a generic thumbnail
    search_html = fetch_html(build_search_url('屈臣氏', product.get('name', '')))
    time.sleep(REQUEST_DELAY)
    return extract_image_from_html(search_html, product.get('name', ''))


def main():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        products = json.load(f)

    updated_count = 0
    image_count = 0
    unchanged_count = 0

    for index, product in enumerate(products, start=1):
        name = product.get('name', '').strip()
        if not name:
            print(f'[{index}] Skipping product with missing name')
            unchanged_count += 1
            continue

        if 'available_at' not in product or not isinstance(product['available_at'], list):
            product['available_at'] = []
        if '屈臣氏' not in product['available_at']:
            product['available_at'].append('屈臣氏')

        links = product.get('links') or {}
        if not isinstance(links, dict):
            links = {}

        # Preserve existing links and only fill missing Watsons link
        if '屈臣氏' not in links or links.get('屈臣氏', '') == '':
            if name:
                links['屈臣氏'] = 'https://www.watsons.com.tw/search?text=' + urllib.parse.quote(name)
                updated_count += 1

        for store in ['康是美', '寶雅']:
            if store not in links:
                links[store] = ""

        product['links'] = links

        if not product.get('image_url'):
            image_url = resolve_image_url(product, links)
            if image_url:
                product['image_url'] = image_url
                image_count += 1

        if index % 10 == 0:
            print(f'Processed {index}/{len(products)} items...')

    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f'Updated {updated_count} links, set image_url for {image_count}, unchanged {unchanged_count}')


if __name__ == '__main__':
    main()
