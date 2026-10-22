"""Versão inicial do Test Case 1, escrita antes de aplicar SOLID.

Mantida para comparação: tudo acontece dentro do __init__, com seletores e dados
misturados no código. Compare com main.py + actions/ + data/ desta mesma pasta.
"""
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


URL = "https://automationexercise.com/"

class User:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 20)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a"))
        )
        
        self.find_n_click(colector = "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a")        
        print("botao login clicado")

        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > h2"))
            )
        print("new user visto")

        self.find_n_write(colector = "input[data-qa='signup-name']", text = "Usuario Sem Solid")
        self.find_n_write(colector = "input[data-qa='signup-email']", text = "usuario.sem.solid.rpa.estudos@example.com")
        self.find_n_click(colector = "#form > div > div > div:nth-child(3) > div > form > button")
        print("Nome e email digitado, botao de signup clicado")

        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#form > div > div > div > div.login-form > h2 > b"))
        )
        print("enter information visto")
        
        self.find_n_click(colector = "input[id='id_gender1']")
        print("genero clicado")
        
        self.find_n_write(colector = "input[data-qa='password']",text= "senha_de_teste_123")
        print("digitou senha")

        self.find_n_select(colector = "select[data-qa='days']", option = "4")
        self.find_n_select(colector = "select[data-qa='months']", option = "December")
        self.find_n_select(colector = "select[data-qa='years']", option = "2000")
        print("data de nascimento selecionada")

        self.find_n_click(colector = "input[id='newsletter']")
        self.find_n_click(colector = "input[id='optin']")
        print("checkboxes marcadas")
        
        self.find_n_write(colector = "input[data-qa='first_name']", text = "Usuario")
        self.find_n_write(colector = "input[data-qa='last_name']", text = "Sem Solid")
        self.find_n_write(colector = "input[data-qa='company']", text = "Estudos RPA")
        self.find_n_write(colector = "input[data-qa='address']", text = "Rua Exemplo, 123")
        self.find_n_write(colector = "input[data-qa='address2']", text = "Apto 45")

        self.find_n_select(colector = "select[data-qa='country']", option = "United States")
        self.find_n_write(colector = "input[data-qa='state']", text = "West Virginia")
        self.find_n_write(colector = "input[data-qa='city']", text = "Charleston")
        self.find_n_write(colector = "input[data-qa='zipcode']", text = "25301")
        self.find_n_write(colector = "input[data-qa='mobile_number']", text = "+1 304-555-1234")
        print("Informações adicionais preenchidas")
        
        self.find_n_click(colector = "button[data-qa='create-account']")
        print("botao de criar conta clicado")
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#form > div > div > div > h2 > b"))
        )
        
        self.find_n_click(colector = "a[data-qa='continue-button']")
        print("botão continuar clicado")
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(10) > a > i"))
        )
        self.find_n_click(colector = "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a")
        print("Botao deletar conta clicado")
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#form > div > div > div > h2 > b"))
        )
        self.find_n_click(colector = "a[data-qa='continue-button']")
        print("conta deletada, botao continuar clicado")
        
    
        
        self.driver.close()

  #  def get_element (self, colector, by=By.CSS_SELECTOR):
  #      element = self.driver.find_element(by, colector)
  #     print(element.text)
  #      return element
   
    def find_n_click (self, colector, by = By.CSS_SELECTOR):
        element = self.driver.find_element(by, colector)
        print(element.text)
        element.click()
        return element
    def find_n_write (self, colector, by = By.CSS_SELECTOR, text = ''):
        element = self.driver.find_element(by, colector)
        print(element.text)
        element.send_keys(text)
        return element
    def find_n_select (self, colector, by = By.CSS_SELECTOR, option = ''):
        element = self.driver.find_element(by, colector)
        select = Select(element)
        select.select_by_visible_text(option)

        return element

if __name__ == "__main__":
    user = User()
