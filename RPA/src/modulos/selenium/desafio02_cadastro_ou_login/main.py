"""Desafio 02 — Cadastro ou login automático.

Planejamento:
    1. Entrar no site
    2. Abrir a página de login/cadastro
    3. Testar se a conta já existe:
        - SE não existe: prosseguir e criar a conta
        - SE existe: fazer login, deletar a conta e tentar o cadastro de novo
    4. Fechar o site retornando logs
"""
import logging

from src.modulos.selenium.desafio02_cadastro_ou_login.actions.login import Login
from src.modulos.selenium.desafio02_cadastro_ou_login.actions.signup import Signup
from src.modulos.selenium.desafio02_cadastro_ou_login.data.data import USER
from src.shared.browser import Browser
from src.utils.constants.selectors import HEADER, LOGIN_FORM

MAX_ATTEMPTS = 3


def main():
    with Browser() as browser:
        login = Login(browser)
        signup = Signup(browser)

        browser.wait_for("page_load")
        browser.find_click(HEADER["login"])
        browser.wait_for("visibility", LOGIN_FORM["title"])

        for attempt in range(1, MAX_ATTEMPTS + 1):
            logging.info(f"Tentativa {attempt} de cadastro...")
            state_signup = signup.fill_pre_signup_form(USER)

            if state_signup == "success":
                signup.fill_extended_signup_form(USER)
                logging.info("Conta criada com sucesso!")
                return

            if state_signup == "failed":
                logging.info("E-mail já existe. Fazendo login para deletar a conta...")
                if login.fill_login_form(USER) != "success":
                    raise RuntimeError("Não foi possível criar a conta nem fazer login.")
                login.delete_account()
                logging.info("Conta deletada. Tentando o cadastro novamente.")
            else:
                raise RuntimeError("Nem sucesso nem falha foram detectados após o pré-cadastro.")

        raise RuntimeError(f"Conta não foi criada após {MAX_ATTEMPTS} tentativas.")


if __name__ == "__main__":
    main()
