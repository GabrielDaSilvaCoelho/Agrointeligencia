from flask import Flask, request, jsonify
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os

app = Flask(__name__)

CSV_PATH = "field_notes_database.csv"
MODEL_PATH = "rnn_agro_modelo.h5"
TOKENIZER_PATH = "tokenizer.pkl"

@app.route('/log/note', methods=['POST'])
def log_note():
    data = request.json
    if not os.path.exists(CSV_PATH):
        df = pd.DataFrame(columns=["text", "label"])
        df.to_csv(CSV_PATH, index=False)
    else:
        df = pd.read_csv(CSV_PATH)

    df = df.append(data, ignore_index=True)
    df.to_csv(CSV_PATH, index=False)
    return jsonify({"status": "ok", "message": "Nota registrada"})

@app.route('/predict', methods=['POST'])
def predict():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(TOKENIZER_PATH):
        return jsonify({"status": "error", "message": "Modelo ou tokenizer não encontrados, treine primeiro"})

    model = load_model(MODEL_PATH)
    with open(TOKENIZER_PATH, "rb") as f:
        tokenizer = pickle.load(f)

    data = request.json
    seq = tokenizer.texts_to_sequences([data['text']])
    seq_padded = pad_sequences(seq, maxlen=50)

    pred = model.predict(seq_padded)
    label = "urgente" if pred[0][0] > 0.5 else "rotina"
    return jsonify({"label": label})

if __name__ == '__main__':
    app.run(debug=True, port=5002)

