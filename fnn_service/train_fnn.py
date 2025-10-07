import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import save_model
import os

CSV_PATH = "soil_database.csv"
MODEL_PATH = "fnn_agro_modelo.h5"

if not os.path.exists(CSV_PATH):
    print(f"{CSV_PATH} não encontrado. Por favor, registre alguns dados primeiro usando /log/soil_data")
    exit()

df = pd.read_csv(CSV_PATH)

if df.shape[0] < 5:
    print("Precisa de pelo menos 5 linhas de dados para treinar o modelo.")
    exit()

X = df[["chuva_mm", "temperatura_c", "umidade"]].values
y = df["rendimento_alto"].values

X = X / X.max(axis=0)

model = Sequential()
model.add(Dense(16, input_dim=3, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X, y, epochs=50, batch_size=4, verbose=1)

model.save(MODEL_PATH)
print(f"Modelo treinado e salvo em {MODEL_PATH}")
