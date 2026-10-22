import logging

from src.modulos.selenium.tc08_produtos.data.data import product_details, selectors
from src.utils.constants.constants import URL
from src.utils.constants.selectors import HEADER


class ProductsPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_products(self):
        self.browser.wait_for("page_load")
        logging.info("Home page carregada com sucesso!")
        self.browser.find_click(HEADER["products"])
        logging.info("Página de produtos selecionada!")
        if not self.browser.correct_url(f"{URL}products"):
            raise AssertionError("A página de produtos não foi aberta")
        self.browser.wait_for("visibility", selectors["products_list"])
        logging.info("Lista de produtos visível!")

    def go_to_product_1(self):
        self.browser.find_click(selectors["btn_view_product_1"])
        logging.info("Produto 1 selecionado!")
        if not self.browser.correct_url(f"{URL}product_details/1"):
            raise AssertionError("A página de detalhes do produto 1 não foi aberta")

        for name, selector in product_details.items():
            element = self.browser.wait_for("visibility", selector)
            logging.info(f"{name} está visível: '{element.text}'")

        logging.info("Todos os elementos do produto 1 estão visíveis!")
