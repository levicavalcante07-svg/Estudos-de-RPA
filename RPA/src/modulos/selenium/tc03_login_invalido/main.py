"""Test Case 3 — Login com credenciais inválidas deve exibir mensagem de erro."""
import logging

from src.modulos.selenium.tc03_login_invalido.data.data import EXPECTED_ERROR, INVALID_USER
from src.shared.automation_exercise import login
from src.shared.browser import Browser
from src.utils.constants.selectors import LOGIN_FORM


def main():
    with Browser() as browser:
        logging.info("Iniciando...")
        browser.wait_for("page_load")

        login(browser, INVALID_USER["email"], INVALID_USER["password"])

        error_message = browser.wait_for("visibility", LOGIN_FORM["error"]).text
        if error_message != EXPECTED_ERROR:
            raise AssertionError(f"Mensagem de erro inesperada: '{error_message}'")
        logging.info(f"Mensagem de erro de login visível: '{error_message}'")
        logging.info("Fechando...")


if __name__ == "__main__":
    main()
