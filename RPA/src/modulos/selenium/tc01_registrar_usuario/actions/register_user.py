import logging

from src.shared.automation_exercise import fill_account_form
from src.utils.constants.selectors import ACCOUNT_STATUS, HEADER, SIGNUP_FORM


class RegisterUser:
    def __init__(self, browser):
        self.browser = browser

    def start_signup(self, user):
        self.browser.find_click(HEADER["login"])
        logging.info("Botão Login clicado")
        self.browser.wait_for("visibility", SIGNUP_FORM["title"])
        logging.info("'New User Signup!' está visível")
        self.browser.find_write(SIGNUP_FORM["name"], user["name"])
        self.browser.find_write(SIGNUP_FORM["email"], user["email"])
        self.browser.find_click(SIGNUP_FORM["button"])
        logging.info("Nome e email preenchidos. Botão Signup clicado")

    def complete_signup(self, user):
        fill_account_form(self.browser, user)

        self.browser.wait_for("visibility", ACCOUNT_STATUS["created"])
        logging.info("Conta criada com sucesso")

        self.browser.find_click(ACCOUNT_STATUS["continue"])
        logging.info("Botão Continue clicado")

    def delete_account(self):
        logged_in = self.browser.wait_for("visibility", HEADER["logged_in_as"])
        logging.info(f"'{logged_in.text}' está visível")

        self.browser.find_click(HEADER["delete_account"])
        logging.info("Botão Delete Account clicado")

        self.browser.wait_for("visibility", ACCOUNT_STATUS["deleted"])
        logging.info("Conta deletada com sucesso")

        self.browser.find_click(ACCOUNT_STATUS["continue"])
        logging.info("Botão Continue clicado")
