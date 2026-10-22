"""Menu para executar as automações do automationexercise.com.

Execute a partir da pasta RPA/:
    python main.py         -> mostra o menu
    python main.py 3       -> executa direto a opção 3
    python main.py all     -> executa todas e mostra um resumo no final
"""
import importlib
import logging
import sys
import time

import src.shared.config  # noqa: F401  (configura o logging e carrega o .env)

AUTOMATIONS = {
    "1": ("TC01 - Registrar usuário", "src.modulos.selenium.tc01_registrar_usuario.main"),
    "2": ("TC02 - Login com sucesso", "src.modulos.selenium.tc02_login_valido.main"),
    "3": ("TC03 - Login com falha", "src.modulos.selenium.tc03_login_invalido.main"),
    "4": ("TC04 - Logout do usuário", "src.modulos.selenium.tc04_logout.main"),
    "5": ("TC05 - Registrar com e-mail existente", "src.modulos.selenium.tc05_cadastro_email_existente.main"),
    "6": ("TC06 - Formulário Contact Us", "src.modulos.selenium.tc06_formulario_contato.main"),
    "7": ("TC07 - Página Test Cases", "src.modulos.selenium.tc07_pagina_test_cases.main"),
    "8": ("TC08 - Produtos e detalhes do produto", "src.modulos.selenium.tc08_produtos.main"),
    "9": ("Desafio 01 - Scraping de preços (requests + BeautifulSoup)", "src.modulos.beautifulsoup.desafio01_precos_produtos.main"),
    "10": ("Desafio 02 - Cadastro ou login automático", "src.modulos.selenium.desafio02_cadastro_ou_login.main"),
    "11": ("Desafio 03 - Scraping de produtos (Playwright)", "src.modulos.playwright.desafio03_produtos.main"),
}


def run(option):
    """Executa uma automação e retorna True se ela terminou sem erros."""
    name, module_path = AUTOMATIONS[option]
    logging.info(f"===== {name} =====")
    try:
        importlib.import_module(module_path).main()
        logging.info(f"[OK] {name}")
        return True
    except Exception as e:
        logging.error(f"[FALHA] {name}: {type(e).__name__}: {e}")
        return False


def run_all():
    results = {}
    for option in AUTOMATIONS:
        results[option] = run(option)
        time.sleep(1)

    print("\n===== RESUMO =====")
    for option, success in results.items():
        print(f"{'[OK]   ' if success else '[FALHA]'} {AUTOMATIONS[option][0]}")
    print(f"{sum(results.values())}/{len(results)} executadas com sucesso")
    return all(results.values())


def main():
    if len(sys.argv) > 1:
        option = sys.argv[1]
    else:
        print("Escolha uma opção:")
        for key, (name, _) in AUTOMATIONS.items():
            print(f"{key:>3} - {name}")
        print("all - Executar todas")
        option = input("Opção: ").strip()

    if option == "all":
        success = run_all()
    elif option in AUTOMATIONS:
        success = run(option)
    else:
        print(f"Opção inválida: '{option}'")
        success = False

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
