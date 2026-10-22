"""Test Case 8 — Verificar a página de produtos e a página de detalhes de um produto."""
from src.modulos.selenium.tc08_produtos.actions.products import ProductsPage
from src.shared.browser import Browser


def main():
    with Browser() as browser:
        products_page = ProductsPage(browser)
        products_page.go_to_products()
        products_page.go_to_product_1()


if __name__ == "__main__":
    main()
