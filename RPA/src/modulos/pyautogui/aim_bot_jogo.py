"""Aim bot para jogo FPS: procura a bola azul na tela e mira nela com movimentos relativos.

Roda por DURACAO_SEGUNDOS e para sozinho (ou com Ctrl+C no terminal).
"""
import time

import pyautogui

from src.shared.config import ASSETS_DIR
from src.shared.images import load_image

TARGET_IMAGE = ASSETS_DIR / "blue_ball.png"
DURACAO_SEGUNDOS = 60


def main():
    # Tempo para dar Alt+Tab e abrir o jogo
    time.sleep(5)

    # Em jogos FPS o mouse fica preso no centro e os movimentos relativos podem encostar nas
    # bordas, o que dispararia o FAILSAFE. Por isso ele é desligado e o bot tem tempo limite.
    pyautogui.FAILSAFE = False
    target = load_image(TARGET_IMAGE)

    width, height = pyautogui.size()
    center_x = width / 2
    center_y = height / 2
    # Procura o alvo só na região central da tela (mais rápido)
    region = (int(width * 0.2), int(height * 0.2), int(width * 0.6), int(height * 0.6))
    print(f"Tela: {width}x{height} | Mira no centro: {center_x},{center_y}")

    fim = time.time() + DURACAO_SEGUNDOS
    while time.time() < fim:
        try:
            target_location = pyautogui.locateOnScreen(
                target, region=region, grayscale=True, confidence=0.6
            )
            target_x, target_y = pyautogui.center(target_location)

            # Distância do alvo até a mira (centro da tela)
            rel_x = int(target_x - center_x)
            rel_y = int(target_y - center_y)
            print(f"Alvo a {rel_x},{rel_y} pixels do centro. Mirando!")

            pyautogui.move(rel_x, rel_y, duration=0.5)
            pyautogui.click()
            time.sleep(0.1)  # pausa pro jogo registrar o tiro

        except pyautogui.ImageNotFoundException:
            print("Bola azul não encontrada")
            time.sleep(0.1)

    print("Tempo limite atingido, encerrando.")


if __name__ == "__main__":
    main()
