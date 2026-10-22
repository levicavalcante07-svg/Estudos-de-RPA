from selenium.common.exceptions import TimeoutException

from src.utils.constants.selectors import ACCOUNT_STATUS, HEADER, LOGIN_FORM


class Login:
    def __init__(self, browser):
        self.browser = browser

    def fill_login_form(self, user):
        """Faz login. Retorna 'success', 'failed' (credenciais inválidas) ou 'error'."""
        self.browser.find_write(LOGIN_FORM["email"], user["email"])
        self.browser.find_write(LOGIN_FORM["password"], user["password"])
        self.browser.find_click(LOGIN_FORM["button"])
        try:
            self.browser.wait_for("visibility", HEADER["logged_in_as"], timeout=5)
            return "success"
        except TimeoutException:
            try:
                self.browser.wait_for("visibility", LOGIN_FORM["error"], timeout=2)
                return "failed"
            except TimeoutException:
                return "error"

    def delete_account(self):
        self.browser.find_click(HEADER["delete_account"])
        self.browser.wait_for("visibility", ACCOUNT_STATUS["deleted"])
        self.browser.find_click(HEADER["login"])
        self.browser.wait_for("visibility", LOGIN_FORM["title"])
