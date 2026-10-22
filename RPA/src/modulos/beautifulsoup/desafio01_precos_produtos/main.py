"""Desafio 01 — Web scraping dos produtos com requests + BeautifulSoup.

Coleta nome, preço, id e link de todos os produtos da home, salva em CSV
e mostra o maior e o menor preço.
"""
import logging

from src.modulos.beautifulsoup.desafio01_precos_produtos.actions.data_handler import DataHandler
from src.modulos.beautifulsoup.desafio01_precos_produtos.actions.scraper import Scraper
from src.utils.constants.constants import URL


def main():
    scraper = Scraper(URL)
    products = scraper.get_products()
    logging.info(f"{len(products)} produtos encontrados")

    data_handler = DataHandler(products)
    path = data_handler.save_to_csv("desafio01_produtos.csv")
    logging.info(f"CSV salvo em {path}")

    max_price, min_price = data_handler.max_min()
    logging.info(f"Maior preço: Rs. {max_price:.0f}")
    logging.info(f"Menor preço: Rs. {min_price:.0f}")


if __name__ == "__main__":
    main()
