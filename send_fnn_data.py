import requests

data = {"chuva_mm":120, "temperatura_c":28, "umidade":0.3, "rendimento_alto":1}
r = requests.post("http://127.0.0.1:5000/log/soil_data", json=data)
print(r.json())
