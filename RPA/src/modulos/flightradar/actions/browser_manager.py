import logging

from playwright.sync_api import Playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from src.modulos.flightradar.data.selectors import URL, selectors as sel
from src.shared.config import auth_file, get_env


class BrowserManager:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(
            headless=False,  # o PyAutoGUI precisa enxergar a janela
            channel="chrome",  # usa o Google Chrome instalado na máquina
            ignore_default_args=["--enable-automation"],
            args=["--disable-blink-features=AutomationControlled"],
        )
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto(URL, wait_until="domcontentloaded")
        try:
            self.page.locator(sel["AGREE_COOKIES"]).click(timeout=5000)
            self.page.locator(sel["CLOSE_POPUP"]).click(timeout=5000)
        except PlaywrightTimeoutError:
            logging.info("Popups não encontrados ou já fechados.")

        self.page.wait_for_timeout(3000)

    def login(self):
        """Login com a conta Google definida no .env (GOOGLE_EMAIL / GOOGLE_PASSWORD)."""
        self.page.locator(sel["LOGIN"]).click()
        self.page.locator(sel["GOOGLE_LOGIN"]).click()

        self.page.locator(sel["email_input"]).wait_for(state="visible")
        self.page.locator(sel["email_input"]).fill(get_env("GOOGLE_EMAIL"))
        self.page.locator(sel["email_input"]).press("Enter")

        self.page.locator(sel["password_input"]).wait_for(state="visible")
        self.page.locator(sel["password_input"]).fill(get_env("GOOGLE_PASSWORD"))
        self.page.locator(sel["password_input"]).press("Enter")

        # Os cookies da sessão vão para RPA/.auth/ (ignorado pelo git)
        self.context.storage_state(path=auth_file("flightradar_state.json"))
