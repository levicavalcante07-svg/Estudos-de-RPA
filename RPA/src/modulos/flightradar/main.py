"""Desafio FlightRadar24 — Playwright + PyAutoGUI.

Faz login, aplica o filtro preto e branco no mapa e, depois que um voo é selecionado
(há 15 segundos para clicar em um avião), coleta as informações do voo e tira um print.
"""
from time import sleep

from playwright.sync_api import sync_playwright

from src.modulos.flightradar.actions.flight_radar import FlightRadar


def main():
    with sync_playwright() as p:
        fr = FlightRadar(p)
        fr.bm.login()
        fr.apply_filters()
        sleep(15)  # tempo para selecionar um voo no mapa
        fr.scrap_flight_infos()


if __name__ == "__main__":
    main()
