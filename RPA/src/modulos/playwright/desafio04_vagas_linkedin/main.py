"""Desafio 04 — LinkedIn: busca vagas de RPA e salva a descrição das 3 primeiras em CSV."""
import csv
import logging

from playwright.sync_api import sync_playwright

from src.shared.config import HEADLESS, output_file
from src.shared.linkedin import open_logged_in_page

SEARCH = "RPA"
# Classes geradas automaticamente pelo LinkedIn: mudam com frequência e podem precisar de ajuste
JOB_CARD = "#workspace > div > div > div._604db7f0._246b1fe4.bebff295._7391903f > div > div > div:nth-child({}) > div"
JOB_POSITIONS = (1, 3, 5)


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        context, page = open_logged_in_page(browser)

        page.goto("https://www.linkedin.com/jobs/")
        page.get_by_test_id("typeahead-input").fill(SEARCH)
        page.get_by_test_id("typeahead-input").press("Enter")

        vagas = []
        for number, position in enumerate(JOB_POSITIONS, start=1):
            page.click(JOB_CARD.format(position))
            page.wait_for_timeout(2000)  # espera o painel de descrição atualizar
            vagas.append({
                "vaga": number,
                "descricao": page.get_by_test_id("expandable-text-box").first.inner_text(),
            })

        context.close()
        browser.close()

    path = output_file("desafio04_vagas.csv")
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["vaga", "descricao"])
        writer.writeheader()
        writer.writerows(vagas)
    logging.info(f"{len(vagas)} vagas salvas em {path}")


if __name__ == "__main__":
    main()
