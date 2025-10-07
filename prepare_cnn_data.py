import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
import tensorflow as tf

saudavel_path = r"C:\Users\Wesley\PycharmProjects\Agro-Inteligencia\cnn_service\uploads\saudavel"
doente_path = r"C:\Users\Wesley\PycharmProjects\Agro-Inteligencia\cnn_service\uploads\doente"

IMG_SIZE = (128, 128)

def carregar_dados(pasta, label):
    imagens = []
    labels = []
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        try:
            img = Image.open(caminho_arquivo).convert('RGB')  # garante 3 canais
            img = img.resize(IMG_SIZE)
            imagens.append(np.array(img))
            labels.append(label)
        except Exception as e:
            print(f"Erro ao abrir {arquivo}: {e}")
    return imagens, labels

imagens_saudavel, labels_saudavel = carregar_dados(saudavel_path, 1)
imagens_doente, labels_doente = carregar_dados(doente_path, 0)

X = np.array(imagens_saudavel + imagens_doente, dtype=np.float32) / 255.0  # normaliza
y = np.array(labels_saudavel + labels_doente)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Tamanho treino: {X_train.shape}, Tamanho teste: {X_test.shape}")
print(f"Labels treino: {np.bincount(y_train)}, Labels teste: {np.bincount(y_test)}")

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), batch_size=4)
