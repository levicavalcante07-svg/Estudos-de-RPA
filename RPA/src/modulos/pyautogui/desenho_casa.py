"""Desafio "Jardim de Infância": desenha e pinta uma casinha no Paint.

As coordenadas (paleta de cores, ferramenta balde etc.) foram mapeadas para uma tela
1920x1080 com o Paint maximizado — use posicao_mouse.py para ajustar à sua tela.
"""
from time import sleep

import pyautogui


def draw_square(width, height):
    """Desenha um retângulo a partir da posição atual do mouse."""
    pyautogui.drag(width, 0, duration=0.5, button="left")
    pyautogui.drag(0, height, duration=0.5, button="left")
    pyautogui.drag(-width, 0, duration=0.5, button="left")
    pyautogui.drag(0, -height, duration=0.5, button="left")
    # Repassa o primeiro lado para fechar bem o canto (senão o balde de tinta "vaza")
    pyautogui.drag(width, 0, duration=0.5, button="left")


def main():
    pyautogui.PAUSE = 1

    pyautogui.press("win")
    pyautogui.write("paint")
    pyautogui.press("enter")
    sleep(0.5)

    # Quadro cinza (fundo)
    pyautogui.click(x=1000, y=105)  # cor cinza
    sleep(0.5)
    pyautogui.moveTo(x=150, y=260)
    pyautogui.dragTo(x=1850, y=260, button="left")
    pyautogui.dragTo(x=1850, y=960, button="left")
    pyautogui.dragTo(x=150, y=960, button="left")
    pyautogui.dragTo(x=150, y=260, button="left")
    pyautogui.dragTo(x=1850, y=260, button="left")

    # Corpo da casa
    pyautogui.click(x=970, y=105)  # cor preta
    sleep(0.5)
    pyautogui.moveTo(x=1440, y=650)
    draw_square(300, 300)

    # Telhado
    dist = 200
    pyautogui.moveTo(x=1390, y=650)
    pyautogui.drag(dist, -dist, duration=0.5, button="left")
    pyautogui.drag(dist, dist, duration=0.5, button="left")
    pyautogui.drag(-2 * dist, 0, duration=0.5, button="left")
    pyautogui.drag(dist, -dist, duration=0.5, button="left")

    # Pinta o telhado e a casa com o balde de tinta
    pyautogui.click(x=383, y=117)  # ferramenta balde
    pyautogui.click(x=1064, y=106)  # cor do telhado
    sleep(0.5)
    pyautogui.doubleClick(x=1570, y=500)
    pyautogui.click(x=1030, y=133)  # cor da casa
    sleep(0.5)
    pyautogui.doubleClick(x=1570, y=700)

    # Janela com divisórias
    pyautogui.moveTo(x=1550, y=480)
    draw_square(40, 60)
    pyautogui.moveTo(x=1570, y=480)
    pyautogui.drag(0, 60, duration=0.5, button="left")
    pyautogui.moveTo(x=1550, y=510)
    pyautogui.drag(40, 0, duration=0.5, button="left")


if __name__ == "__main__":
    main()
