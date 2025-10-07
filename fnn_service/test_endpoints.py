import requests

fnn_data = {"chuva_mm": 120, "temperatura_c": 25.4, "umidade": 70}

try:
    res_log = requests.post("http://127.0.0.1:5000/log/soil_data", json=fnn_data)
    print("FNN log:", res_log.json())
except Exception as e:
    print("Erro no log FNN:", e)

try:
    res_pred = requests.post("http://127.0.0.1:5000/predict/soil_data", json=fnn_data)
    print("FNN predict:", res_pred.json())
except Exception as e:
    print("Erro na predição FNN:", e)
