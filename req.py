import requests

url = 'http://127.0.0.1:8000'

parametro = {
  "id": 3,
  "nome": "Tiago",
  "senha": "senha"
}

retorno = requests.post(f'{url}/usuario', json=parametro)
print(retorno.json())


lista = requests.get(f'{url}/listaUsuario')
for i in lista:
    print(i)