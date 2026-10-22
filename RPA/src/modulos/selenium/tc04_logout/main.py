"""Test Case 4 — Logout: após sair, o usuário deve voltar para a página de login."""
import logging

from src.shared.automation_exercise import TEST_USER, create_account_via_api, login
from src.shared.browser import Browser
from src.utils.constants.constants import URL
from src.utils.constants.selectors import HEADER


def main():
    create_account_via_api(TEST_USER)

    with Browser() as browser:
        logging.info("Iniciando...")
        browser.wait_for("page_load")

        login(browser, TEST_USER["email"], TEST_USER["password"])
        logged_in = browser.wait_for("visibility", HEADER["logged_in_as"])
        logging.info(f"Login realizado: '{logged_in.text}'")

        browser.find_click(HEADER["logout"])
        if not browser.correct_url(f"{URL}login"):
            raise AssertionError("O logout não redirecionou para a página de login")
        logging.info("Usuário desconectado")
        logging.info("Fechando...")


if __name__ == "__main__":
    main()
