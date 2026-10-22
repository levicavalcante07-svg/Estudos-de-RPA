"""Configurações compartilhadas: caminhos do projeto, variáveis de ambiente e logging.

Todos os caminhos são calculados a partir deste arquivo, então os scripts funcionam
independente da pasta de onde forem executados.
"""
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]  # pasta RPA/
ASSETS_DIR = ROOT_DIR / "src" / "assets"
OUTPUT_DIR = ROOT_DIR / "output"  # arquivos gerados pelas automações (ignorado pelo git)
AUTH_DIR = ROOT_DIR / ".auth"     # sessões de navegador salvas (ignorado pelo git)

load_dotenv(ROOT_DIR / ".env")

# HEADLESS=1 roda os navegadores sem abrir janela
HEADLESS = os.getenv("HEADLESS", "0") == "1"

logging.basicConfig(
    level=logging.INFO,  # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",  # Formato de hora curto para facilitar a leitura no terminal
)


def get_env(name):
    """Lê uma variável obrigatória do .env, com uma mensagem clara caso esteja faltando."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Variável '{name}' não definida. Copie RPA/.env.example para RPA/.env e preencha."
        )
    return value


def output_file(name):
    """Caminho para salvar um arquivo gerado (CSV, JSON, prints...) na pasta output/."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    return OUTPUT_DIR / name


def auth_file(name):
    """Caminho para salvar sessões de login. Esses arquivos contêm cookies: nunca commitar!"""
    AUTH_DIR.mkdir(exist_ok=True)
    return AUTH_DIR / name
