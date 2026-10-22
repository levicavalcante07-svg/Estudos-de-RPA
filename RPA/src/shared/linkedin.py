"""Login no LinkedIn reaproveitando a sessão salva (usado pelos desafios 04 e 05).

As credenciais vêm do .env (LINKEDIN_EMAIL / LINKEDIN_PASSWORD). Depois do primeiro login,
os cookies ficam em RPA/.auth/ — esse arquivo dá acesso à conta, por isso é ignorado pelo git.
"""
import logging

from src.shared.config import auth_file, get_env

STATE_FILE = auth_file("linkedin_state.json")


def open_logged_in_page(browser, viewport=None):
    """Retorna (context, page) já logados no LinkedIn."""
    has_session = STATE_FILE.exists()
    context = browser.new_context(storage_state=STATE_FILE if has_session else None, viewport=viewport)
    page = context.new_page()
    page.goto("https://www.linkedin.com/feed/")

    if "/feed" not in page.url:  # sem sessão salva ou sessão expirada
        logging.info("Fazendo login no LinkedIn...")
        page.goto("https://www.linkedin.com/login")
        page.locator("#username").fill(get_env("LINKEDIN_EMAIL"))
        page.locator("#password").fill(get_env("LINKEDIN_PASSWORD"))
        page.locator("button[type='submit']").click()
        # Tempo extra para resolver manualmente um captcha ou a verificação em duas etapas
        page.wait_for_url("**/feed/**", timeout=120_000)
        context.storage_state(path=STATE_FILE)
        logging.info("Sessão salva para as próximas execuções")

    return context, page
