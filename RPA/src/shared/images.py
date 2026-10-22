"""Leitura de imagens compatível com caminhos que têm acentos.

No Windows, cv2.imread não consegue abrir arquivos cujo caminho tem acentos
(ex.: "Códigos - Programação") e retorna None. Como o PyAutoGUI usa o OpenCV na busca
por imagem, o mesmo problema aparece em locateOnScreen. Lendo os bytes com o numpy e
decodificando com cv2.imdecode, o caminho deixa de ser um problema.
"""
import cv2
import numpy as np


def load_image(path):
    """Carrega a imagem como array BGR (formato do OpenCV), aceito por cv2, EasyOCR e PyAutoGUI."""
    img = cv2.imdecode(np.fromfile(str(path), dtype=np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Imagem não encontrada ou inválida: {path}")
    return img
