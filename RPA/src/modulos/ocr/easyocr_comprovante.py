"""OCR com EasyOCR: extrai valor, data e código de autenticação de um comprovante de pagamento."""
import json
import logging
import re

import cv2
import easyocr

from src.shared.config import ASSETS_DIR, output_file
from src.shared.images import load_image

IMAGE_PATH = ASSETS_DIR / "comprovante_pagamento.png"


def extract_text(image_path):
    img = load_image(image_path)

    # Apenas dobramos o tamanho para o EasyOCR enxergar as letras miúdas.
    # Sem cv2.threshold, para NÃO apagar os textos em cinza claro!
    img = cv2.resize(img, None, fx=2, fy=2)

    reader = easyocr.Reader(["pt", "en"])
    resultado = reader.readtext(img)
    return "\n".join(item[1] for item in resultado)


def clean_money_value(texto_bruto):
    """Converte o valor lido pelo OCR (ex: 'R$ 61,20' ou 'RS 61 20') para float."""
    if not texto_bruto:
        return None

    # Remove 'R', '$', 'S' (o OCR às vezes lê '$' como 'S') e espaços
    numero = re.sub(r"[R\$S]", "", texto_bruto).replace(" ", "")

    # Se o OCR não leu a vírgula (ex: "6120"), dividimos por 100 -> 61.20
    if "," not in numero and "." not in numero:
        try:
            return float(numero) / 100
        except ValueError:
            return None

    try:
        return float(numero.replace(",", "."))
    except ValueError:
        return None


def parse_receipt(texto_completo):
    # Busca por âncora: procuramos o rótulo "Valor" e pegamos a linha de baixo
    valor_match = re.search(r"Valor\n(R[\$S]\s?[\d\.,\s]+)", texto_completo, re.IGNORECASE)
    # Data por extenso (ex: "15 de Janeiro de 2023")
    data_match = re.search(r"\d{1,2}\s+de\s+[A-Za-z]+\s+de\s+\d{4}", texto_completo, re.IGNORECASE)
    # Pegamos tudo da linha abaixo do título "Código de Autenticação"
    protocolo_match = re.search(r"Código de Autenticação\n(.+)", texto_completo)

    return {
        "valor_limpo": clean_money_value(valor_match.group(1)) if valor_match else None,
        "valor_bruto": valor_match.group(1).strip() if valor_match else None,
        # Correção rápida caso o OCR leia "Janciro"
        "data": data_match.group().strip().replace("Janciro", "Janeiro") if data_match else None,
        "protocolo": protocolo_match.group(1).strip() if protocolo_match else None,
    }


def main():
    logging.info("Analisando imagem com EasyOCR...")
    texto_completo = extract_text(IMAGE_PATH)
    print(f"\nTexto extraído da imagem:\n{'=' * 50}\n{texto_completo}\n{'=' * 50}")

    dados = parse_receipt(texto_completo)
    path = output_file("resultado_ocr.json")
    with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print(json.dumps(dados, ensure_ascii=False, indent=4))
    logging.info(f"JSON salvo em {path}")


if __name__ == "__main__":
    main()
