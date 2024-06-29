import httpx
from selectolax.parser import HTMLParser
from urllib.parse import urljoin
from dataclasses import asdict, dataclass
import csv
import time

@dataclass
class Item:
    BrandName: str | None = None
    ProductName: str | None = None
    Price: str | None = None
    SalesPrice: str | None = None

def get_html(baseurl, **kwargs):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
    try:
        resp = httpx.get(baseurl + str(kwargs.get("page", "")), headers=headers, follow_redirects=True)
        resp.raise_for_status()
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}. Page Limit Exceeded!")
        raise

    return HTMLParser(resp.text)

def extract_text(html, sel):
    element = html.css_first(sel)
    return element.text(strip=True) if element else None

def parse_search_page(html):
    products = html.css("div.product-info")
    for product in products:
        yield urljoin("https://www.capital.com.ph/", product.css_first("a").attributes["href"])

def item_page(html):
    regular_price = extract_text(html, "div.price__sale span[data-regular-price]")
    sale_price = extract_text(html, "div.price__sale span[data-sale-price]")
    if regular_price == sale_price:
        sale_price = None

    return Item(
        BrandName=extract_text(html, "div.product__section-details h3"),
        ProductName=extract_text(html, "h1.product__section-title.product-title"),
        Price=regular_price,
        SalesPrice=sale_price
    )

def write_raw_data(products, filename="products_raw.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["BrandName", "ProductName", "Price", "SalesPrice"])
        writer.writeheader()
        for product in products:
            writer.writerow(asdict(product))

def scrape_data():
    products = []
    baseurl = "https://www.capital.com.ph/collections/mens-footwear?page="
    page = 1

    while True:
        print("Getting data from page", page)
        try:
            html = get_html(baseurl, page=page)
            urls = list(parse_search_page(html))  # Convert generator to list to check length
            if not urls:  # If no URLs found, assume end of pages
                print(f"No products found on page {page}. Exiting.")
                break

            for url in urls:
                print(url)
                html = get_html(url)
                products.append(item_page(html))
            page += 1

        except httpx.HTTPStatusError:
            print(f"Page {page} not found. Exiting.")
            break

    write_raw_data(products)
    print("Raw data has been written to data/raw/products_raw.csv")

if __name__ == "__main__":
    scrape_data()
