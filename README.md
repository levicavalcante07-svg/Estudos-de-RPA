# 🤖 Estudos de RPA

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4-43B02A?logo=selenium&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.60-2EAD33?logo=playwright&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-desktop-yellow)
![OCR](https://img.shields.io/badge/OCR-Tesseract%20%7C%20EasyOCR-blueviolet)

Automações de processos (**Robotic Process Automation**) desenvolvidas durante o curso de capacitação **AIX_ACADEMY**: testes end-to-end de um e-commerce, web scraping, automação de desktop por reconhecimento de imagem e leitura de documentos com OCR.

---

## 📋 Projetos

### Selenium — casos de teste do [automationexercise.com](https://automationexercise.com)

| # | Automação | O que faz |
|---|---|---|
| TC01 | `selenium/tc01_registrar_usuario` | Cadastro completo de usuário e exclusão da conta. Inclui a [versão antes do SOLID](RPA/src/modulos/selenium/tc01_registrar_usuario/versao_sem_solid.py) para comparação |
| TC02 | `selenium/tc02_login_valido` | Login com credenciais corretas |
| TC03 | `selenium/tc03_login_invalido` | Login com credenciais inválidas e validação da mensagem de erro |
| TC04 | `selenium/tc04_logout` | Logout e verificação do redirecionamento |
| TC05 | `selenium/tc05_cadastro_email_existente` | Cadastro com e-mail já existente |
| TC06 | `selenium/tc06_formulario_contato` | Formulário "Contact Us" com alerta JavaScript |
| TC07 | `selenium/tc07_pagina_test_cases` | Navegação para a página de Test Cases |
| TC08 | `selenium/tc08_produtos` | Lista de produtos e página de detalhes |

### Desafios

| Desafio | Tecnologia | O que faz |
|---|---|---|
| 01 — Preços de produtos | requests + BeautifulSoup | Coleta todos os produtos, salva em CSV e calcula o maior e o menor preço |
| 02 — Cadastro ou login | Selenium | Tenta cadastrar; se o e-mail já existir, faz login, apaga a conta e cadastra de novo |
| 03 — Produtos | Playwright | Web scraping da página de produtos para CSV |
| 04 — Vagas no LinkedIn | Playwright | Busca vagas de RPA e salva as descrições |
| 05 — Vagas com salário | Playwright | Percorre todas as vagas de uma busca e salva as que informam salário |
| FlightRadar24 | Playwright + PyAutoGUI | Aplica filtros no mapa, localiza aeronaves por imagem e coleta dados de um voo ([exemplo de saída](docs/img/flightradar_exemplo.png)) |

### PyAutoGUI — automação de desktop

| Script | O que faz |
|---|---|
| `relatorio_bloco_de_notas.py` | Abre o Bloco de Notas, escreve um relatório com data/hora e salva |
| `desenho_estrela.py` · `desenho_espiral.py` · `desenho_casa.py` | Desenham no Paint (a casa é pintada com o balde de tinta) |
| `aim_bot_jogo.py` · `aim_bot_xbitlabs.py` | Encontram alvos na tela por reconhecimento de imagem e clicam neles |
| `cookie_clicker.py` | Auto-clicker para o Cookie Clicker |
| `posicao_mouse.py` | Utilitário para descobrir coordenadas da tela |

### OCR

| Script | O que faz |
|---|---|
| `easyocr_comprovante.py` | Lê um comprovante de pagamento e extrai valor, data e código de autenticação para JSON, com regex e limpeza dos erros comuns de OCR |
| `tesseract_tempo_reacao.py` | Joga o teste de reação do Human Benchmark lendo a tela com Tesseract |

---

## 🏗️ Arquitetura

```text
RPA/
├── main.py                 # Menu que executa os testes do automationexercise e mostra um resumo
├── .env.example            # Modelo das variáveis de ambiente (credenciais ficam só no .env local)
└── src/
    ├── modulos/
    │   ├── selenium/       # Cada caso de teste: main.py + actions/ (fluxos) + data/ (dados e seletores)
    │   ├── beautifulsoup/
    │   ├── playwright/
    │   ├── pyautogui/
    │   ├── ocr/
    │   └── flightradar/
    ├── shared/             # Código reutilizado entre módulos
    │   ├── browser.py              # Wrapper do Selenium (cliques, esperas, selects, alertas)
    │   ├── automation_exercise.py  # Login, formulário de cadastro e conta de teste via API
    │   ├── linkedin.py             # Login no LinkedIn reaproveitando a sessão salva
    │   ├── config.py               # Caminhos, .env, modo headless e logging
    │   └── images.py               # Leitura de imagens compatível com caminhos acentuados
    ├── utils/constants/    # URLs e seletores compartilhados
    └── assets/             # Imagens de referência para PyAutoGUI e OCR
```

Princípios aplicados:

- **Responsabilidade única:** cada caso de teste separa o fluxo (`actions/`), os dados (`data/`) e a execução (`main.py`).
- **Reuso:** as ações comuns ficam em `shared/` em vez de copiadas em cada módulo.
- **Testes independentes:** os testes que precisam de uma conta existente a criam antes pela API do site, então podem rodar em qualquer ordem.
- **Credenciais fora do código:** logins reais vêm do `.env`, que não é versionado.

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.13+ e Google Chrome. Para o script com Tesseract, instale também o [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki).

```bash
git clone https://github.com/levicavalcante07-svg/Estudos-de-RPA.git
cd Estudos-de-RPA

python -m venv venv
venv\Scripts\activate            # Windows  (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
playwright install chromium

cd RPA
copy .env.example .env           # Linux/macOS: cp .env.example .env  — depois preencha o .env
```

Todos os comandos abaixo são executados **de dentro da pasta `RPA/`**:

```bash
python main.py                   # menu interativo
python main.py all               # roda todos os testes do automationexercise com resumo no final
python main.py 3                 # roda uma opção específica

python -m src.modulos.ocr.easyocr_comprovante
python -m src.modulos.pyautogui.desenho_casa
python -m src.modulos.playwright.desafio05_vagas_com_salario
```

Os arquivos gerados (CSV, JSON, prints) vão para `RPA/output/`. Com `HEADLESS=1` no `.env`, Selenium e Playwright rodam sem abrir janelas.

---

## ⚠️ Observações

- Os scripts de **PyAutoGUI** usam coordenadas mapeadas para uma tela **1920x1080**. Use `posicao_mouse.py` para ajustar à sua tela. Para interromper um script, leve o mouse a um canto da tela (FAILSAFE).
- Os sites de terceiros (LinkedIn, FlightRadar24, Human Benchmark) mudam o HTML com frequência, então alguns seletores podem precisar de ajuste.
- As automações de LinkedIn e FlightRadar foram feitas com fins de estudo. Automatizar essas plataformas pode violar os termos de uso delas.
