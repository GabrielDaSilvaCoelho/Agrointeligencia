import requests

notes = [
    {"text":"Irrigação concluída sem problemas", "label":"rotina"},
    {"text":"Infestação de pragas detectada, ação imediata necessária", "label":"urgente"},
    {"text":"Verificação do solo realizada, tudo normal", "label":"rotina"},
    {"text":"Doença detectada no talhão sul, aplicar fungicida", "label":"urgente"},

]

for note in notes:
    r = requests.post("http://127.0.0.1:5002/log/note", json=note)
    print(r.json())
