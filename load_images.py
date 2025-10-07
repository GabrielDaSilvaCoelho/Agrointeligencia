import os
from PIL import Image

saudavel_path = r"C:\Users\Wesley\PycharmProjects\Agro-Inteligencia\cnn_service\uploads\saudavel"
doente_path = r"C:\Users\Wesley\PycharmProjects\Agro-Inteligencia\cnn_service\uploads\doente"

def carregar_imagens(pasta):
    imagens = []
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        try:
            img = Image.open(caminho_arquivo)
            imagens.append(img)
        except Exception as e:
            print(f"Erro ao abrir {arquivo}: {e}")
    return imagens

imagens_saudavel = carregar_imagens(saudavel_path)
imagens_doente = carregar_imagens(doente_path)

print(f"Imagens saudáveis: {len(imagens_saudavel)}")
print(f"Imagens doentes: {len(imagens_doente)}")
