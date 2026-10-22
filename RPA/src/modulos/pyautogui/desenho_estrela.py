"""Abre o Paint e desenha uma estrela dentro de um quadrado (coordenadas para tela 1920x1080)."""
from time import sleep

import pyautogui


def main():
    pyautogui.PAUSE = 0.5

    pyautogui.press("win")
    pyautogui.write("paint")
    pyautogui.press("enter")
    sleep(1)

    # Estrela
    pyautogui.moveTo(x=1440, y=450)
    pyautogui.dragTo(x=1040, y=450, duration=0.5, button="left")
    pyautogui.dragTo(x=1400, y=650, duration=0.5, button="left")
    pyautogui.dragTo(x=1240, y=350, duration=0.5, button="left")
    pyautogui.dragTo(x=1080, y=650, duration=0.5, button="left")
    pyautogui.dragTo(x=1440, y=450, duration=0.5, button="left")

    # Quadrado
    pyautogui.moveTo(x=1440, y=350)
    pyautogui.dragTo(x=1040, y=350, duration=0.5, button="left")
    pyautogui.dragTo(x=1040, y=650, duration=0.5, button="left")
    pyautogui.dragTo(x=1440, y=650, duration=0.5, button="left")
    pyautogui.dragTo(x=1440, y=350, duration=0.5, button="left")


if __name__ == "__main__":
    main()
