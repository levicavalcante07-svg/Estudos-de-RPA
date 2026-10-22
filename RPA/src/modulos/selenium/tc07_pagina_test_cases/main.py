"""Test Case 7 — Verificar se a página 'Test Cases' abre corretamente."""
import logging

from src.shared.browser import Browser
from src.utils.constants.constants import URL
from src.utils.constants.selectors import HEADER


def main():
    with Browser() as browser:
        browser.wait_for("page_load")
        logging.info("Home Page carregada")

        browser.find_click(HEADER["test_cases"])
        logging.info("Botão Test Cases clicado")

        if not browser.correct_url(f"{URL}test_cases"):
            raise AssertionError("A página de Test Cases não foi aberta")
        browser.wait_for("visibility", "h2.title b")
        logging.info("Página Test Cases carregada")


if __name__ == "__main__":
    main()
