import requests, base64, os

saudavel = "uploads/saudavel"
doente = "uploads/doente"

for filename in os.listdir(saudavel):
    with open(os.path.join(saudavel, filename), "rb") as f:
        img_str = base64.b64encode(f.read()).decode("utf-8")
    data = {"image": img_str, "label": "saudavel"}
    r = requests.post("http://127.0.0.1:5001/log/leaf_image", json=data)
    print(r.json())

for filename in os.listdir(doente):
    with open(os.path.join(doente, filename), "rb") as f:
        img_str = base64.b64encode(f.read()).decode("utf-8")
    data = {"image": img_str, "label": "doente"}
    r = requests.post("http://127.0.0.1:5001/log/leaf_image", json=data)
    print(r.json())
