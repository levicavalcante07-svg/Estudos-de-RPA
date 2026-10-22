import logging
from time import sleep

import pyautogui as pyag
from playwright.sync_api import Playwright

from src.modulos.flightradar.actions.browser_manager import BrowserManager
from src.modulos.flightradar.data.selectors import FLIGHT_PANEL_REGION, images_path, selectors as sel
from src.shared.config import output_file
from src.shared.images import load_image


class FlightRadar:
    def __init__(self, playwright: Playwright):
        self.bm = BrowserManager(playwright)
        self.page = self.bm.page

    def apply_filters(self):
        """Deixa o mapa em preto e branco, o que facilita achar os aviões por imagem."""
        self.page.locator(sel["SETTINGS"]).wait_for(state="visible", timeout=10000)
        self.page.locator(sel["SETTINGS"]).click()
        self.page.locator(sel["B_AND_W"]).wait_for(state="visible", timeout=10000)
        self.page.locator(sel["B_AND_W"]).click()
        self.page.locator(sel["CLOSE_SETTINGS"]).click()
        self.page.wait_for_timeout(3000)

    def check_planes_helicopters(self):
        """Localiza aviões e helicópteros no mapa por reconhecimento de imagem."""
        planes = list(pyag.locateAllOnScreen(load_image(images_path["aviao"])))
        logging.info(f"Aviões encontrados: {len(planes)}")
        sleep(5)
        helicopters = list(pyag.locateAllOnScreen(load_image(images_path["helicoptero"])))
        logging.info(f"Helicópteros encontrados: {len(helicopters)}")
        sleep(5)

    def scrap_flight_infos(self):
        """Lê os dados do voo selecionado e tira um print do painel de informações."""
        flight = {
            "fly_number": self.page.locator(sel["fly_number"]).all_inner_texts(),
            "fly_code": self.page.locator(sel["fly_code"]).all_inner_texts(),
            "departure_city": self.page.locator(sel["departure_city"]).all_inner_texts(),
            "arrival_city": self.page.locator(sel["arrival_city"]).all_inner_texts(),
        }
        time_remaining = self.page.locator(sel["time_remaining"]).all_inner_texts()
        flight["time_remaining"] = time_remaining[0].split(" in ")[1].strip()

        screenshot_path = output_file("flightradar_flight_info.png")
        pyag.screenshot(imageFilename=str(screenshot_path), region=FLIGHT_PANEL_REGION)
        logging.info(f"Voo: {flight}")
        logging.info(f"Print do painel salvo em {screenshot_path}")
        return flight
