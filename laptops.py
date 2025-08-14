import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
# https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&_nkw=laptop&_sacat=0&SSD%2520Capacity=1%2520TB&rt=nc&RAM%2520Size=32%2520GB&_dcat=177

laptops_dict = {
    'Name': [],
    'Price': [],
    'Shipping': [],
    'Link': [],
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}

cookies = {
    'utag_main__sn': '1',
    's': 'CgAD4ACBonZlDYTI3ODU0YTUxOTgwYWI0MzA5OTAwNDkxZmZlZDEyNzlnzLe6',
    'ns1': 'CgAD4ACBonZlDYTI3ODU0YTUxOTgwYWI0MzA5OTAwNDkxZmZlZDEyNzlnzLe6',
    'nonsession': 'BAQAAAZhdx0gSAAaAADMAAWp9fUwwAMoAIGxesMxhMjc4NTRhNTE5ODBhYjQzMDk5MDA0OTFmZmVkMTI3OQDLAAJonFDUMjOB2/bzmzoEv8kDrXxqGRfdUvLBtw**',
    'ebay': '%5Ejs%3D1%5Esbf%3D%23000000%5E',
    'dp1': 'bpbf/%2380000000000400c000000000000000006a7d7d4c^bl/SD6c5eb0cc^',
    'cto_bundle': 'cAjki19xMzlheEpXWXh2N21nNGp2ZXd5aDhCZE5ZcVZOdVhmSFRWZnZxUktRWGJrZURSS2JuZXdUdzNTZjd0WVRwRFAlMkYzTW5iQ1hBQTdhdXk2UUNDNFc0TXptNVVWaWpiR1JmSkFmOTlYS2JzVWc4V1lVY2Zva3BjOHcyS0Z2d0t2MUVC',
    '_scid_r': 'RLAPcczQFnocHr5aGjfB8GdFy_F7iBtE1S_eMA',
    '_scid': 'OjAPcczQFnocHr5aGjfB8GdFy_F7iBtE',
    '_pin_unauth': 'dWlkPU5URTFNVGs0WXpNdFlqYzFOQzAwWXpZMExXRXpOV1V0TVdZMU5EVTVORFZpT1dReQ',
    '_gcl_au': '1.1.920031779.1755072608',
    '__uzmlj2': '9c6R5SfMyUCsfm7nDv7tKlltRYm9FglhOik1wmcSOao=',
    '__uzmfj2': '7f60005294db92-0c5f-40ae-9c3c-af93356fc69e1755072557442171748-8351739bd34c2f9a16',
    '__uzmf': '7f60005294db92-0c5f-40ae-9c3c-af93356fc69e1755072461422269503-c5ef1dce37d9b00437',
    '__uzme': '7803',
    '__uzmdj2': '1755072729',
    '__uzmd': '1755072730',
    '__uzmcj2': '119911649061',
    '__uzmc': '673663767903',
    '__uzmbj2': '1755072557',
    '__uzmb': '1755072461',
    '__uzmaj2': '3ab28706-99b2-4689-a6bc-7cd72d8a1ea2',
    '__uzma': '4045e9a9-3c51-4dc0-90d2-25c231c165d7',
    '__ssuzjsr2': 'a9be0cd8e',
    '__ssds': '2',
    '__gsas': 'ID=07e8af1dc9d5f0d0:T=1755072596:RT=1755072596:S=ALNI_MbWQ-xP60IQDd95wVVfvGaadgmjyw',
    '__deba': 'FaEhTnol7dpw7k56sLAUYxb9yL_MkotmBuljF5MhUy4GLsLsldvcidHeU0idFhHsXR8UW1J2_XMwSXzXGqPFGOg5gqFbjLFZWIPFMNCKeNlZtd_VcqsAI8ps9B8FV7YLfBXyw7lfJ9myxB1gCwDC3A==',
    '_ScCbts': '%5B%5D',
}

page_no = 1
while True:
    url = f'https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&_nkw=laptop&_sacat=0&SSD%2520Capacity=1%2520TB&rt=nc&RAM%2520Size=32%2520GB&_dcat=177&_pgn={page_no}'
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code != 200: 
        continue
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('ul', class_ = 'srp-results')
    laptops = container.find_all('li', class_ = 's-item')
    for laptop in laptops[4:]:
        # getting the name of the laptop
        if laptop.find('span', attrs = {'role': 'heading'}) is not None:
            name = laptop.find('span', attrs = {'role': 'heading'}).text
            laptops_dict['Name'].append(name)
        else:
            name = 'No info'
            print(name)
        # Getting the price of the laptop
        if laptop.find('span', class_ = 's-item__price').text is not None: 
            price = laptop.find('span', class_ = 's-item__price').text
            laptops_dict['Price'].append(price)
        else:
            price = 'No info'
            print(price)
        # Getting the shipping info
        if laptop.find('span', class_ = 's-item__logisticsCost').text is not None:
            shipping = laptop.find('span', class_ = 's-item__logisticsCost').text
            laptops_dict['Shipping'].append(shipping)
        else: 
            shipping = 'No info'
            print(shipping)
        # Getting the link of the laptop
        if laptop.find('a', class_ = 's-item__link')['href'] is not None:
            link = laptop.find('a', class_ = 's-item__link')['href']
            laptops_dict['Link'].append(link)
        else:
            link = 'No info'
            print(link)

    next_as_button = soup.find('button', class_ = 'pagination__next')
    if next_as_button is not None:
        break
    else:
        page_no += 1


df = pd.DataFrame(laptops_dict)

df.to_excel('laptops.xlsx')