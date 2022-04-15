import requests

retorno = requests.post('http://127.0.0.1:8000/usuario', params={"nome":"nao"})

print(retorno.json())

