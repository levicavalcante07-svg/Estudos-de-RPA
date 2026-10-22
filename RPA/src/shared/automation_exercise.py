"""Ações e dados reutilizados pelos casos de teste do automationexercise.com.

Os testes de login, logout e e-mail existente precisam de uma conta já cadastrada.
Em vez de depender de um cadastro manual, a conta é criada pela API pública do próprio
site antes do teste, deixando cada caso de teste independente dos outros.
"""
import logging

import requests

from src.utils.constants.constants import API_URL
from src.utils.constants.selectors import ACCOUNT_FORM, HEADER, LOGIN_FORM

# Dados fictícios: o site é um ambiente de testes, nunca use dados pessoais reais aqui
TEST_USER = {
    "name": "Usuario Teste RPA",
    "email": "usuario.teste.rpa.estudos@example.com",
    "password": "senha_de_teste_123",
    "birthday": "10",
    "birthmonth": "May",
    "birthyear": "2000",
    "firstname": "Usuario",
    "lastname": "Teste",
    "company": "Estudos RPA",
    "address": "Rua Exemplo, 123",
    "address2": "Apto 45",
    "country": "United States",
    "state": "West Virginia",
    "city": "Charleston",
    "zipcode": "25301",
    "mobile_number": "+1 304-555-1234",
}

SELECT_FIELDS = ("birthday", "birthmonth", "birthyear", "country")
CHECKBOXES = ("gender", "newsletter", "offers")


def create_account_via_api(user=TEST_USER):
    """Cadastra o usuário pela API. Se o e-mail já existir, a conta é reaproveitada."""
    payload = {
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "title": "Mr",
        "birth_date": user["birthday"],
        "birth_month": user["birthmonth"],
        "birth_year": user["birthyear"],
        "firstname": user["firstname"],
        "lastname": user["lastname"],
        "company": user["company"],
        "address1": user["address"],
        "address2": user["address2"],
        "country": user["country"],
        "zipcode": user["zipcode"],
        "state": user["state"],
        "city": user["city"],
        "mobile_number": user["mobile_number"],
    }
    response = requests.post(f"{API_URL}createAccount", data=payload, timeout=20).json()
    logging.info(f"Conta de teste via API: {response['message']}")


def delete_account_via_api(email, password):
    """Remove a conta pela API (útil para limpar restos de execuções interrompidas)."""
    response = requests.delete(
        f"{API_URL}deleteAccount", data={"email": email, "password": password}, timeout=20
    ).json()
    logging.info(f"Remoção de conta via API: {response['message']}")


def login(browser, email, password):
    """Abre a página de login e envia o formulário com as credenciais informadas."""
    browser.find_click(HEADER["login"])
    browser.wait_for("visibility", LOGIN_FORM["title"])
    logging.info("'Login to your account' está visível")
    browser.find_write(LOGIN_FORM["email"], email)
    browser.find_write(LOGIN_FORM["password"], password)
    browser.find_click(LOGIN_FORM["button"])
    logging.info("Formulário de login enviado")


def fill_account_form(browser, user):
    """Preenche o formulário 'Enter Account Information' e clica em 'Create Account'."""
    browser.wait_for("visibility", ACCOUNT_FORM["title"])
    logging.info("'Enter Account Information' está visível")

    for checkbox in CHECKBOXES:
        browser.find_click(ACCOUNT_FORM[checkbox])

    for field, value in user.items():
        if field in ("name", "email"):  # já preenchidos na primeira etapa do cadastro
            continue
        if field in SELECT_FIELDS:
            browser.find_select(ACCOUNT_FORM[field], value)
        else:
            browser.find_write(ACCOUNT_FORM[field], value)

    browser.find_click(ACCOUNT_FORM["create_button"])
    logging.info("Formulário de cadastro preenchido e enviado")
