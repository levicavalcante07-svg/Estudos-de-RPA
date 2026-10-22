from selenium.common.exceptions import TimeoutException

from src.shared.automation_exercise import fill_account_form
from src.utils.constants.selectors import ACCOUNT_FORM, ACCOUNT_STATUS, SIGNUP_FORM


class Signup:
    def __init__(self, browser):
        self.browser = browser

    def fill_pre_signup_form(self, user):
        """Envia nome e e-mail. Retorna 'success', 'failed' (e-mail já existe) ou 'error'."""
        self.browser.find_write(SIGNUP_FORM["name"], user["name"])
        self.browser.find_write(SIGNUP_FORM["email"], user["email"])
        self.browser.find_click(SIGNUP_FORM["button"])
        try:
            self.browser.wait_for("visibility", ACCOUNT_FORM["title"], timeout=5)
            return "success"
        except TimeoutException:
            try:
                self.browser.wait_for("visibility", SIGNUP_FORM["error"], timeout=2)
                return "failed"
            except TimeoutException:
                return "error"

    def fill_extended_signup_form(self, user):
        fill_account_form(self.browser, user)
        self.browser.wait_for("visibility", ACCOUNT_STATUS["created"])
        self.browser.find_click(ACCOUNT_STATUS["continue"])
