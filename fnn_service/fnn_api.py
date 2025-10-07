from flask import Flask, request, jsonify
import pandas as pd
import os
import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense

app = Flask(__name__)
DB_PATH = "soil_database.csv"
MODEL_PATH = "fnn_model.h5"

@app.route("/log/soil_data", methods=["POST"])
def log_soil_data():
    data = request.json
    if not os.path.exists(DB_PATH):
        df = pd.DataFrame(columns=["chuva_mm", "temperatura_c", "umidade", "rendimento_alto"])
        df.to_csv(DB_PATH, index=False)
    df = pd.read_csv(DB_PATH)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(DB_PATH, index=False)
    return jsonify({"status": "success", "data": data})

@app.route("/predict/soil_data", methods=["POST"])
def predict_soil_data():
    if not os.path.exists(MODEL_PATH):
        return jsonify({"error": "Modelo ainda não treinado"})

    data = request.json
    x = np.array([[data["chuva_mm"], data["temperatura_c"], data["umidade"]]])
    model = load_model(MODEL_PATH)
    pred = model.predict(x)
    return jsonify({"prediction": int(pred[0][0] > 0.5)})


if __name__ == "__main__":
    app.run(debug=True)
