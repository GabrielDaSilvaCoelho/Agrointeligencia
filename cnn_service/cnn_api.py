from flask import Flask, request, jsonify
import os
import base64
from datetime import datetime
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)
UPLOAD_DIR = "uploads"
MODEL_PATH = "cnn_model.h5"

@app.route("/log/leaf_image", methods=["POST"])
def log_leaf_image():
    data = request.json
    img_base64 = data["image"]
    label = data["label"]
    label_dir = os.path.join(UPLOAD_DIR, label)
    os.makedirs(label_dir, exist_ok=True)
    img_data = base64.b64decode(img_base64)
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}.jpg"
    filepath = os.path.join(label_dir, filename)
    with open(filepath, "wb") as f:
        f.write(img_data)
    return jsonify({"status": "success", "file": filename})

@app.route("/predict/leaf_image", methods=["POST"])
def predict_leaf_image():
    if not os.path.exists(MODEL_PATH):
        return jsonify({"error": "Modelo ainda não treinado"})

    data = request.json
    img_base64 = data["image"]
    img_data = base64.b64decode(img_base64)
    filename = "temp.jpg"
    with open(filename, "wb") as f:
        f.write(img_data)

    img = load_img(filename, target_size=(64, 64))
    x = img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)

    model = load_model(MODEL_PATH)
    pred = model.predict(x)
    os.remove(filename)

    return jsonify({"prediction": int(pred[0][0] > 0.5)})

if __name__ == "__main__":
    app.run(debug=True)
