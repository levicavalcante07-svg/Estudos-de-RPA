from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from src.modulos.beautifulsoup.desafio01_precos_produtos.data.data import content


class Scraper:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.content, "html.parser")
        self.items = []

    def get_products(self):
        names = self.soup.select(content["name"])
        prices = self.soup.select(content["price"])
        ids = self.soup.select(content["id"])
        hrefs = self.soup.select(content["href"])

        for name, price, product_id, href in zip(names, prices, ids, hrefs):
            self.items.append({
                "name": name.get_text(strip=True),
                "price": price.get_text(strip=True),
                "id": product_id.get("data-product-id").strip(),
                "href": urljoin(self.url, href.get("href").strip()),
            })
        return self.items
