from fastapi import FastAPI
from model import Usuarios

app = FastAPI()

lista = []


@app.get('/listaUsuario')
def listaUsuario():
    '''Listar todos os usuarios'''
    return lista


@app.post('/usuario')
def inserirUsuario(usuario: Usuarios):
    '''Inserir novos usuarios'''
    try:
        lista.append(usuario)      
        return 'Cadastrado com sucesso'
    except:
        return 'Erro'
        

