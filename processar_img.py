import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

MODEL_PATH = 'cnn_service/cnn_model.h5'
IMAGE_PATH = 'imagem_decodificada.jpg'
IMG_SIZE = (224, 224)

CLASS_NAMES = ['Trigo', 'Soja', 'Milho']

model = load_model(MODEL_PATH)

img = Image.open(IMAGE_PATH).convert('RGB')
img = img.resize(IMG_SIZE)
img_array = np.array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

predicao = model.predict(img_array)

classe_predita_idx = np.argmax(predicao, axis=1)[0]
classe_predita = CLASS_NAMES[classe_predita_idx]

print(f"Classe prevista: {classe_predita}")
print(f"Probabilidades: {predicao}")
