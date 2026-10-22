"""OCR com Tesseract: joga o teste de tempo de reação do Human Benchmark.

Os textos que o robô procura na tela ("Reaction Time Test", "Wait for green", "Click!")
são lidos por OCR a partir de imagens de referência, e o tempo de cada rodada é lido
por OCR a partir de um screenshot da página.
"""
import logging
import os
import re
from time import sleep

import pytesseract
from PIL import Image
from playwright.sync_api import sync_playwright

from src.shared.config import ASSETS_DIR, HEADLESS, output_file

# Se o Tesseract não estiver no PATH, defina TESSERACT_CMD no .env
if os.getenv("TESSERACT_CMD"):
    pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_CMD")

ROUNDS = 5
CLICK_POSITION = (960, 540)


def extract_first_line(image_path):
    with Image.open(image_path) as img:
        texto_completo = pytesseract.image_to_string(img.convert("RGB")).strip()
    return texto_completo.split("\n")[0].strip()


def read_reaction_time(page, rodada):
    # Screenshot da página com a pontuação, convertido para escala de cinza (melhora o OCR)
    screenshot_path = output_file(f"screenshot_rodada_{rodada}.png")
    page.screenshot(path=screenshot_path)
    with Image.open(screenshot_path) as img:
        texto_ocr = pytesseract.image_to_string(img.convert("L"), lang="eng")
    screenshot_path.unlink()

    # Procura o padrão de milissegundos (ex: "215 ms")
    numeros = re.findall(r"\d+", texto_ocr)
    if numeros:
        return f"{numeros[0]} ms"
    logging.warning(f"Texto bruto lido pelo OCR: {texto_ocr.strip()}")
    return "Não identificado pelo OCR"


def main():
    logging.info("Extraindo textos das imagens de referência...")
    reaction_text = extract_first_line(ASSETS_DIR / "reaction_time.png")
    wait_green_text = extract_first_line(ASSETS_DIR / "wait_for_green.png")
    click_text = extract_first_line(ASSETS_DIR / "click.png")

    historico = output_file("historico_reacao_ocr.txt")
    if not historico.exists():
        historico.write_text("--- HISTÓRICO DE REAÇÃO VIA OCR ---\n", encoding="utf-8")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        page = browser.new_page()
        page.goto("https://www.humanbenchmark.com/tests/reactiontime")

        page.get_by_text(reaction_text).first.wait_for(state="visible", timeout=10000)
        page.mouse.click(*CLICK_POSITION)
        logging.info("Iniciou o jogo!")

        for rodada in range(1, ROUNDS + 1):
            logging.info(f"[Rodada {rodada}] Esperando a tela vermelha...")
            page.get_by_text(wait_green_text).first.wait_for(state="visible", timeout=10000)
            page.get_by_text(click_text).first.wait_for(state="visible", timeout=10000)
            page.mouse.click(*CLICK_POSITION)  # clica assim que ficar verde

            sleep(0.2)  # tempo para a tela de pontuação renderizar
            tempo = read_reaction_time(page, rodada)
            logging.info(f"Tempo registrado via OCR: {tempo}")
            with open(historico, "a", encoding="utf-8") as f:
                f.write(f"Rodada {rodada}: {tempo}\n")

            sleep(1)
            if rodada < ROUNDS:
                page.mouse.click(*CLICK_POSITION)  # avança para a próxima rodada
                sleep(0.5)

        browser.close()

    logging.info(f"Teste finalizado! Histórico salvo em {historico}")


if __name__ == "__main__":
    main()
