import logging

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

import src.utils.constants.constants as C
from src.shared.config import HEADLESS


class Browser:
    """Encapsula o WebDriver e as ações básicas usadas por todos os módulos Selenium.

    Pode ser usado como context manager para garantir que o navegador seja fechado:

        with Browser() as browser:
            browser.find_click("a[href='/login']")
    """

    def __init__(self, url=C.URL, timeout=10):
        options = webdriver.ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        self.browser = webdriver.Chrome(options=options)
        self.timeout = timeout
        self.browser.get(url)

    def find_click(self, selector, by=By.CSS_SELECTOR):
        element = self.browser.find_element(by, selector)
        # Clique via JavaScript evita que anúncios por cima do elemento interceptem o clique
        self.browser.execute_script("arguments[0].click();", element)
        return element

    def find_write(self, selector, text, by=By.CSS_SELECTOR):
        element = self.browser.find_element(by, selector)
        element.send_keys(text)
        return element

    def find_select(self, selector, option, by=By.CSS_SELECTOR):
        element = self.browser.find_element(by, selector)
        Select(element).select_by_visible_text(option)
        return element

    def wait_for(self, condition, selector="", by=By.CSS_SELECTOR, timeout=None):
        """Espera uma condição: 'visibility', 'clickable' ou 'page_load'. Retorna o elemento."""
        wait = WebDriverWait(self.browser, timeout or self.timeout)
        if condition == "visibility":
            return wait.until(EC.visibility_of_element_located((by, selector)))
        if condition == "clickable":
            return wait.until(EC.element_to_be_clickable((by, selector)))
        if condition == "page_load":
            return wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        raise ValueError(f"Condição de espera desconhecida: '{condition}'")

    def correct_url(self, expected_url):
        """Espera a navegação chegar na URL esperada (ignorando âncoras como #google_vignette)."""
        try:
            WebDriverWait(self.browser, self.timeout).until(
                lambda d: d.current_url.split("#")[0] == expected_url
            )
            logging.info("Página correta!")
            return True
        except TimeoutException:
            logging.warning(f"Página incorreta! Esperado: {expected_url} | Atual: {self.browser.current_url}")
            return False

    def accept_alert(self):
        WebDriverWait(self.browser, self.timeout).until(EC.alert_is_present()).accept()

    def quit(self):
        self.browser.quit()

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.quit()
