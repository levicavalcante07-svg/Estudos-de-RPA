from src.modulos.selenium.tc06_formulario_contato.data.data import message, selectors
from src.utils.constants.selectors import HEADER


class ContactUs:
    def __init__(self, browser):
        self.browser = browser

    def go_to_contact_us(self):
        self.browser.wait_for("page_load")
        self.browser.find_click(HEADER["contact_us"])
        self.browser.wait_for("visibility", selectors["contact_title"])

    def fill_email_form(self):
        self.browser.find_write(selectors["name_input"], message["name"])
        self.browser.find_write(selectors["email_input"], message["email"])
        self.browser.find_write(selectors["subject_input"], message["subject"])
        self.browser.find_write(selectors["message_input"], message["message"])
        self.browser.find_click(selectors["submit_button"])
        # O site pede confirmação em um alerta JavaScript antes de enviar
        self.browser.accept_alert()

    def back_to_home(self):
        self.browser.wait_for("visibility", selectors["success_message"])
        self.browser.find_click(selectors["btn_home"])
        self.browser.wait_for("page_load")
