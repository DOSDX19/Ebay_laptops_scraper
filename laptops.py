"""
eBay Laptop Scraper
-------------------
Scrapes laptop listings from eBay (1TB SSD, 32GB RAM) and saves them into laptops.xlsx
Author: Ahmed Qureshi
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Dictionary to store scraped data
laptops_dict = {
    'Name': [],
    'Price': [],
    'Shipping': [],
    'Link': [],
}

# Request headers to mimic a browser
HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/138.0.0.0 Safari/537.36'
    )
}

# Base eBay search URL (with filters for 1TB SSD & 32GB RAM laptops)
BASE_URL = (
    "https://www.ebay.com/sch/i.html"
    "?_fsrp=1&_from=R40&_nkw=laptop&_sacat=0"
    "&SSD%2520Capacity=1%2520TB&rt=nc"
    "&RAM%2520Size=32%2520GB&_dcat=177&_pgn={}"
)

page_no = 1

while True:
    print(f"Scraping page {page_no}...")
    url = BASE_URL.format(page_no)
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Failed to retrieve page {page_no}. Retrying...")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('ul', class_='srp-results')
    if not container:
        print("No results container found. Stopping...")
        break

    laptops = container.find_all('li', class_='s-item')
    if not laptops:
        print("No laptops found. Stopping...")
        break

    for laptop in laptops[4:]:  # Skip top sponsored items
        name = laptop.find('span', attrs={'role': 'heading'})
        price = laptop.find('span', class_='s-item__price')
        shipping = laptop.find('span', class_='s-item__logisticsCost')
        link_tag = laptop.find('a', class_='s-item__link')

        laptops_dict['Name'].append(name.text if name else 'No info')
        laptops_dict['Price'].append(price.text if price else 'No info')
        laptops_dict['Shipping'].append(shipping.text if shipping else 'No info')
        laptops_dict['Link'].append(link_tag['href'] if link_tag else 'No info')

    next_button = soup.find('button', class_='pagination__next')
    if not next_button or 'pagination__next--disabled' in next_button.get('class', []):
        print("No more pages. Scraping finished.")
        break

    page_no += 1

# Save results to Excel
df = pd.DataFrame(laptops_dict)
df.to_excel('laptops.xlsx', index=False)
print(f"Scraping complete. {len(df)} items saved to laptops.xlsx")
