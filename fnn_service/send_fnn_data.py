import requests

soil_data = [
    {"chuva_mm":120, "temperatura_c":28, "umidade":0.3, "rendimento_alto":1},
    {"chuva_mm":80, "temperatura_c":30, "umidade":0.25, "rendimento_alto":0},
    {"chuva_mm":150, "temperatura_c":25, "umidade":0.35, "rendimento_alto":1},
    {"chuva_mm":60, "temperatura_c":32, "umidade":0.2, "rendimento_alto":0},
    {"chuva_mm":100, "temperatura_c":27, "umidade":0.28, "rendimento_alto":1},
]

for data in soil_data:
    r = requests.post("http://127.0.0.1:5000/log/soil_data", json=data)
    print(r.json())
