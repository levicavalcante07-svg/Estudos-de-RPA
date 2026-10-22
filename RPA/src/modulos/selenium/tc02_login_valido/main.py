"""Test Case 2 — Login com e-mail e senha corretos, seguido da exclusão da conta."""
import logging

from src.shared.automation_exercise import TEST_USER, create_account_via_api, login
from src.shared.browser import Browser
from src.utils.constants.selectors import ACCOUNT_STATUS, HEADER


def main():
    create_account_via_api(TEST_USER)

    with Browser() as browser:
        logging.info("Iniciando...")
        browser.wait_for("page_load")

        login(browser, TEST_USER["email"], TEST_USER["password"])
        logged_in = browser.wait_for("visibility", HEADER["logged_in_as"])
        logging.info(f"Login realizado: '{logged_in.text}'")

        browser.find_click(HEADER["delete_account"])
        browser.wait_for("visibility", ACCOUNT_STATUS["deleted"])
        logging.info("Conta deletada")
        logging.info("Fechando...")


if __name__ == "__main__":
    main()
