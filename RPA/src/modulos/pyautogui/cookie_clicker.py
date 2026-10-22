"""Cookie Clicker: clica sem parar no cookie do jogo (orteil.dashnet.org/cookieclicker).

A posição do cookie é fixa — use posicao_mouse.py para descobrir a coordenada na sua tela.
Para parar, leve o mouse até um canto da tela (FAILSAFE do PyAutoGUI).
"""
import time

import pyautogui

COOKIE_POSITION = (330, 507)


def main():
    pyautogui.FAILSAFE = True
    time.sleep(1.5)  # tempo para trocar para a janela do jogo
    while True:
        pyautogui.click(*COOKIE_POSITION)


if __name__ == "__main__":
    main()
