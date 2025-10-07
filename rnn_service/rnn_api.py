from flask import Flask, request, jsonify
import pandas as pd
import os
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

app = Flask(__name__)
DB_PATH = "field_notes_database.csv"
MODEL_PATH = "rnn_model.h5"
TOKENIZER_PATH = "tokenizer.pkl"

@app.route("/log/note", methods=["POST"])
def log_note():
    data = request.json
    if not os.path.exists(DB_PATH):
        df = pd.DataFrame(columns=["text", "label"])
        df.to_csv(DB_PATH, index=False)
    df = pd.read_csv(DB_PATH)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(DB_PATH, index=False)
    return jsonify({"status": "success", "data": data})

@app.route("/predict/note", methods=["POST"])
def predict_note():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(TOKENIZER_PATH):
        return jsonify({"error": "Modelo ainda não treinado"})

    data = request.json
    tokenizer = pickle.load(open(TOKENIZER_PATH, "rb"))
    model = load_model(MODEL_PATH)

    seq = tokenizer.texts_to_sequences([data["text"]])
    seq = pad_sequences(seq, maxlen=50)
    pred = model.predict(seq)
    return jsonify({"prediction": int(pred[0][0] > 0.5)})

if __name__ == "__main__":
    app.run(debug=True)
