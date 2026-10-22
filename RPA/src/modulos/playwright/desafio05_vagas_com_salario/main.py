"""Desafio 05 — LinkedIn: percorre as vagas de uma busca e salva as que informam salário."""
import csv
import logging

from playwright.sync_api import sync_playwright

from src.shared.config import HEADLESS, output_file
from src.shared.linkedin import open_logged_in_page

VAGA_ESCOLHIDA = "Torneiro mecânico"
PAIS_ESCOLHIDO = "Brasil"


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        context, page = open_logged_in_page(browser, viewport={"width": 1920, "height": 1080})

        page.goto("https://www.linkedin.com/jobs/")
        page.get_by_test_id("typeahead-input").fill(VAGA_ESCOLHIDA)
        page.get_by_test_id("typeahead-input").press("Enter")
        page.get_by_role("radio", name="Filtrar Vagas").click()
        page.wait_for_timeout(4000)

        # Troca a localidade da busca para o país escolhido
        page.locator("//*[@id='workspace']/div/header/div/div[1]/div").click()
        page.wait_for_timeout(4000)
        page.locator("[aria-label='Limpar localidade']").click()
        page.wait_for_timeout(4000)
        page.locator("[aria-label='Localidade']").fill(PAIS_ESCOLHIDO)
        page.wait_for_timeout(4000)
        for _ in range(3):
            page.keyboard.press("Tab")
            page.wait_for_timeout(2000)
        page.keyboard.press("Enter")
        page.wait_for_timeout(2000)

        vagas = page.locator("[data-testid='lazy-column']").get_by_role("button")
        total_vagas = vagas.count()
        logging.info(f"{total_vagas} vagas encontradas")
        vagas_salvas = []
        index_xpath = 1

        for i in range(total_vagas):
            try:
                meu_xpath = f"xpath=//*[@id='workspace']/div/div/div[1]/div/div/div[{index_xpath}]"
                alvo = page.locator(meu_xpath)

                if alvo.count() == 0:
                    logging.info(f"LinkedIn resetou a lista na vaga {i}! Voltando o XPath pro 1...")
                    index_xpath = 1
                    meu_xpath = f"xpath=//*[@id='workspace']/div/div/div[1]/div/div/div[{index_xpath}]"
                    alvo = page.locator(meu_xpath)

                alvo.click(force=True)
                page.wait_for_timeout(1500)

                descricao_completa = page.get_by_test_id("expandable-text-box").first.inner_text()
                titulo_vaga = vagas.nth(i).inner_text()

                if "salário" in descricao_completa.lower() or "salario" in descricao_completa.lower():
                    logging.info(f"Vaga com salário encontrada: {titulo_vaga}")
                    vagas_salvas.append({"titulo": titulo_vaga, "descricao": descricao_completa})

                index_xpath += 1

            except Exception as e:
                logging.warning(f"Erro na vaga {i}: {e}")
                index_xpath += 1

        context.close()
        browser.close()

    path = output_file("desafio05_vagas_com_salario.csv")
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["titulo", "descricao"])
        writer.writeheader()
        writer.writerows(vagas_salvas)
    logging.info(f"{len(vagas_salvas)} vagas com salário salvas em {path}")


if __name__ == "__main__":
    main()
