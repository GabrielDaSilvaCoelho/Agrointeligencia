import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

DB_PATH = "field_notes_database.csv"
MODEL_PATH = "rnn_model.h5"
TOKENIZER_PATH = "tokenizer.pkl"

df = pd.read_csv(DB_PATH)
texts = df["text"].astype(str).tolist()
labels = df["label"].map({"rotina":0, "urgente":1}).tolist()

tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=50)

model = Sequential([
    Embedding(1000, 16, input_length=50),
    LSTM(16),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(padded, np.array(labels), epochs=10, batch_size=4, verbose=1)
model.save(MODEL_PATH)
pickle.dump(tokenizer, open(TOKENIZER_PATH, "wb"))
print("Modelo RNN salvo com sucesso!")
