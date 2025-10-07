from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import base64
import io
from PIL import Image
import os

app = Flask(__name__)
MODEL_PATH = "model_leaf.h5"

@app.route('/predict/leaf_image', methods=['POST'])
def predict_leaf_image():
    data = request.json

    if 'image' not in data:
        return jsonify({"status": "error", "message": "Imagem não fornecida"})

    if not os.path.exists(MODEL_PATH):
        return jsonify({"status": "error", "message": "Modelo não encontrado"})

    model = load_model(MODEL_PATH)

    img_bytes = base64.b64decode(data['image'])
    img = Image.open(io.BytesIO(img_bytes)).resize((128,128))  # ajuste o tamanho conforme treino
    x = np.array(img) / 255.0
    if x.ndim == 2:
        x = np.stack([x]*3, axis=-1)
    x = np.expand_dims(x, axis=0)
    pred = model.predict(x)[0][0]
    label = "saudavel" if pred > 0.5 else "doente"

    return jsonify({"label": label, "score": float(pred)})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
