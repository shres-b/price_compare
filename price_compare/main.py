import requests
from bs4 import BeautifulSoup
import webbrowser
import sys
from lxml import etree
import csv

headers = {
    'Accept' : '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}   

def find_url_from_google(preferred_site, key):
    query = f"site:{preferred_site} {key}"
    search_url = f"https://www.google.com/search?q={query}"

    content = requests.get(search_url, headers = headers).text
    soup = BeautifulSoup(content, 'html.parser')

    search = soup.find(id = 'search')
    first_link = search.find('a')['href']
    print (first_link)
    return first_link


def track_product_price(retailer, product_url):
    response = requests.get(product_url, headers=headers)
    response.raise_for_status()  # Check for errors

    soup = BeautifulSoup(response.content, 'html.parser')
    dom = etree.HTML(str(soup))

    if retailer == 'amazon':
        title = soup.find('span', id='productTitle').text.strip()
        price = soup.find('span', class_='a-offscreen').text.strip()

    elif retailer == 'visions':
        title = str(dom.xpath('//*[@id="detailview-right-container"]/div[1]/span')[0].text.strip())
        price = str(dom.xpath('//*[@id="leftcol-container-771ds"]/div[1]/div[2]/span')[0].text.strip())


    return title, price

def save_list_to_csv(data, filename):
    """Saves a list of 3-element tuples to a CSV file.

    Args:
        data (list): A list of tuples, where each tuple has 3 elements.
        filename (str): The name of the CSV file to create.
    """

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


product = 'Samsung-UN32N5300AFXZC-Glossy-Canada-Version'

results = {
    'Amazon': track_product_price('amazon', find_url_from_google('amazon.ca', product)),
    'Visions': track_product_price('visions', find_url_from_google('visions.ca', product)),
    # ... add more URLs
}

csv_data = [('Seller', 'Product Description', 'Price')]

for retailer, data in results.items():
    if data:
        print(f"{retailer}: {data[0]} - {data[1]}")
        csv_data.append((retailer, data[0], data[1]))
    else:
        print(f"{retailer}: Price not found")

filename = 'product_comparison_report.csv'
save_list_to_csv(csv_data, filename)