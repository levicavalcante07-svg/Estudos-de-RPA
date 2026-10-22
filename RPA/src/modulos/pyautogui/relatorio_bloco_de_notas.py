"""Abre o Bloco de Notas, escreve um relatório com data e hora e salva o arquivo."""
from datetime import datetime
from time import sleep

import pyautogui


def main():
    pyautogui.PAUSE = 0.5

    pyautogui.press("win")
    pyautogui.write("Bloco de Notas")
    pyautogui.press("enter")
    sleep(1)

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    pyautogui.write("Relatorio automatico", interval=0.03)
    pyautogui.press("enter")
    pyautogui.write(f"Gerado em: {agora}", interval=0.03)
    pyautogui.press("enter")
    pyautogui.write("Aula de PyAutoGUI - automacao visual", interval=0.03)

    pyautogui.hotkey("ctrl", "s")
    sleep(1)
    pyautogui.write("relatorio_pyautogui.txt")
    pyautogui.press("enter")


if __name__ == "__main__":
    main()
