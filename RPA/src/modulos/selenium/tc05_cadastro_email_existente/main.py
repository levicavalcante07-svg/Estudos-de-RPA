"""Test Case 5 — Cadastro com e-mail já existente deve exibir mensagem de erro."""
import logging

from src.shared.automation_exercise import TEST_USER, create_account_via_api
from src.shared.browser import Browser
from src.utils.constants.selectors import HEADER, SIGNUP_FORM

EXPECTED_ERROR = "Email Address already exist!"


def main():
    create_account_via_api(TEST_USER)

    with Browser() as browser:
        logging.info("Iniciando...")
        browser.wait_for("page_load")

        browser.find_click(HEADER["login"])
        browser.wait_for("visibility", SIGNUP_FORM["title"])
        logging.info("'New User Signup!' está visível")

        browser.find_write(SIGNUP_FORM["name"], TEST_USER["name"])
        browser.find_write(SIGNUP_FORM["email"], TEST_USER["email"])
        browser.find_click(SIGNUP_FORM["button"])
        logging.info("Formulário de registro enviado com e-mail já cadastrado")

        error_message = browser.wait_for("visibility", SIGNUP_FORM["error"]).text
        if error_message != EXPECTED_ERROR:
            raise AssertionError(f"Mensagem de erro inesperada: '{error_message}'")
        logging.info(f"Mensagem de erro visível: '{error_message}'")
        logging.info("Fechando...")


if __name__ == "__main__":
    main()
