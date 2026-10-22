"""Desafio 03 — Web scraping dos produtos com Playwright, salvando o resultado em CSV."""
import csv
import logging

from playwright.sync_api import sync_playwright

from src.shared.config import HEADLESS, output_file
from src.utils.constants.constants import URL


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()
        page.goto(URL)

        page.click("a[href='/products']")
        products = []
        products_name = page.locator(".product-overlay p")
        products_price = page.locator(".product-overlay h2")
        products_id = page.locator(".product-overlay a")
        for i in range(products_name.count()):
            products.append({
                "name": products_name.nth(i).inner_text(),
                "price": products_price.nth(i).inner_text(),
                "id": products_id.nth(i).get_attribute("data-product-id"),
            })
        browser.close()

    path = output_file("desafio03_produtos.csv")
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "id"])
        writer.writeheader()
        writer.writerows(products)

    logging.info(f"{len(products)} produtos salvos em {path}")


if __name__ == "__main__":
    main()
