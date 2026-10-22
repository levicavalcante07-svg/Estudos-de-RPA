"""Test Case 1 — Registrar usuário: cadastro completo e exclusão da conta criada."""
import logging

from src.modulos.selenium.tc01_registrar_usuario.actions.register_user import RegisterUser
from src.modulos.selenium.tc01_registrar_usuario.data.data import USER
from src.shared.automation_exercise import delete_account_via_api
from src.shared.browser import Browser


def main():
    # Garante que o e-mail esteja livre caso uma execução anterior tenha parado no meio
    delete_account_via_api(USER["email"], USER["password"])

    with Browser() as browser:
        logging.info("Iniciando...")
        browser.wait_for("page_load")
        logging.info("Página totalmente carregada")

        register_user = RegisterUser(browser)
        register_user.start_signup(USER)
        register_user.complete_signup(USER)
        register_user.delete_account()
        logging.info("Fechando...")


if __name__ == "__main__":
    main()
