import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

MODEL_PATH = 'cnn_service/cnn_model.h5'
IMAGE_PATH = 'cnn_service/imagem_decodificada.jpg'
IMG_SIZE = (124, 124)
CLASS_NAMES = ['Trigo', 'Soja', 'Milho']

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Modelo não encontrado em {MODEL_PATH}")
if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"Imagem não encontrada em {IMAGE_PATH}")

print("Carregando modelo...")
model = load_model(MODEL_PATH)
print("Modelo carregado com sucesso!")
print(f"Shape esperado de entrada do modelo: {model.input_shape}")

print("Processando imagem...")
img = Image.open(IMAGE_PATH).convert('L')
img = img.resize(IMG_SIZE)
img_array = np.array(img) / 255.0
img_array = img_array.flatten()
img_array = np.expand_dims(img_array, axis=0)
print(f"Shape da imagem processada: {img_array.shape}")

print("Fazendo previsão...")
predicao = model.predict(img_array)

classe_predita_idx = np.argmax(predicao, axis=1)[0]
classe_predita = CLASS_NAMES[classe_predita_idx]

print(f" Classe prevista: {classe_predita}")
print(f"Probabilidades por classe: {predicao}")
