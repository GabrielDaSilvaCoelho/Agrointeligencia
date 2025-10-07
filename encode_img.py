import base64

with open("uploads/saudavel/img_1759847212.46901.jpg", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode("utf-8")

print(img_b64)
