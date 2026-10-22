"""Mostra a posição do mouse a cada 2 segundos — útil para descobrir coordenadas na tela."""
import time

import pyautogui


def main():
    for _ in range(6):
        print(f"Posição atual do mouse: {pyautogui.position()}")
        time.sleep(2)


if __name__ == "__main__":
    main()
