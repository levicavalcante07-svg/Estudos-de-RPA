"""Test Case 6 — Formulário 'Contact Us': preenchimento, envio e volta para a home."""
import logging

from src.modulos.selenium.tc06_formulario_contato.actions.contact_us import ContactUs
from src.shared.browser import Browser


def main():
    with Browser() as browser:
        contact_us = ContactUs(browser)
        contact_us.go_to_contact_us()
        logging.info("Página de contato acessada")
        contact_us.fill_email_form()
        logging.info("Formulário preenchido e enviado")
        contact_us.back_to_home()
        logging.info("Voltou para a página inicial")


if __name__ == "__main__":
    main()
