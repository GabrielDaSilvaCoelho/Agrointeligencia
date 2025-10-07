import requests

fnn_data = {"chuva_mm": 120, "temperatura_c": 25.4, "umidade": 70}

res_log = requests.post("http://127.0.0.1:5000/log/soil_data", json=fnn_data)
try:
    print("FNN log:", res_log.json())
except:
    print("Erro FNN log:", res_log.text)

res_pred = requests.post("http://127.0.0.1:5000/predict/soil_data", json=fnn_data)
try:
    print("FNN predict:", res_pred.json())
except:
    print("Erro FNN predict:", res_pred.text)
