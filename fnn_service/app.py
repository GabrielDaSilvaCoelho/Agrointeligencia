from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)

CSV_PATH = "soil_database.csv"
MODEL_PATH = "fnn_agro_modelo.h5"

@app.route('/log/soil_data', methods=['POST'])
def log_soil_data():
    data = request.json

    if not os.path.exists(CSV_PATH):
        df = pd.DataFrame(columns=["chuva_mm", "temperatura_c", "umidade", "rendimento_alto"])
    else:
        df = pd.read_csv(CSV_PATH)

    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

    df.to_csv(CSV_PATH, index=False)
    return jsonify({"status": "ok", "message": "Dados registrados"})

@app.route('/predict/soil_data', methods=['POST'])
def predict_soil_data():
    data = request.json

    if not os.path.exists(MODEL_PATH):
        return jsonify({"status": "error", "message": "Modelo não encontrado, treine primeiro"})

    model = load_model(MODEL_PATH)

    X_new = np.array([[data['chuva_mm'], data['temperatura_c'], data['umidade']]])
    pred = model.predict(X_new)

    return jsonify({"rendimento_alto": int(pred[0][0] > 0.5)})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
