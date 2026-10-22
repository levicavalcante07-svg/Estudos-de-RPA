"""Aim bot no Aim Trainer da xbitlabs: Playwright abre o jogo e o PyAutoGUI clica nos alvos.

Para parar antes do fim, leve o mouse até um canto da tela (FAILSAFE do PyAutoGUI).
"""
import time

import pyautogui
from playwright.sync_api import sync_playwright

from src.shared.config import ASSETS_DIR
from src.shared.images import load_image

MAXIMIZE_BROWSER = ASSETS_DIR / "maximizar.png"
MAXIMIZE_GAME = ASSETS_DIR / "maximizar_jogo.png"
TARGET_IMAGE = ASSETS_DIR / "blue_ball_2.png"
RESULT_TITLE = "xpath=/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/h3"


def main():
    pyautogui.FAILSAFE = True
    target = load_image(TARGET_IMAGE)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,  # o PyAutoGUI precisa enxergar a janela
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"],
            ignore_default_args=["--enable-automation"],
        )
        page = browser.new_context().new_page()
        page.goto("https://www.xbitlabs.com/aim-trainer/", wait_until="load")
        time.sleep(0.5)

        pyautogui.click(pyautogui.locateOnScreen(load_image(MAXIMIZE_BROWSER), confidence=0.7))
        time.sleep(0.5)
        pyautogui.click(pyautogui.locateOnScreen(load_image(MAXIMIZE_GAME), confidence=0.7))
        time.sleep(0.5)
        page.click("xpath=/html/body/div[3]/div[2]")
        time.sleep(0.5)
        page.get_by_text("Start").first.click()
        time.sleep(3)

        # Clica nos alvos até aparecer a tela de resultado
        while not page.locator(RESULT_TITLE).is_visible():
            try:
                pyautogui.click(pyautogui.locateOnScreen(target, confidence=0.75))
                print("Bola azul encontrada")
            except pyautogui.ImageNotFoundException:
                print("Bola azul não encontrada")

        browser.close()


if __name__ == "__main__":
    main()
