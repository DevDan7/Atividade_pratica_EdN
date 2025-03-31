""" Crie um programa que gera um perfil de usuário aleatório usando a
API 'Random User Generator'. O programa deve exibir o nome, email
e país do usuário gerado." """

import requests
import json
import os
import random
import string

def gera_perfil_usuario():
    """Gera um perfil de usuário aleatório usando a API 'Random User Generator'.

    Retorna:
    dict: O perfil do usuário gerado
    """
    # Faz uma requisição à API para obter um perfil de usuário aleatório
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Converte a resposta JSON em um dicionário
        perfil = response.json()
        # Extrai os dados do usuário
        usuario = perfil['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        return {
            "nome": nome,
            "email": email,
            "pais": pais
        }
    else:
        print("Erro ao obter o perfil do usuário.")
        return None
# Testes
if __name__ == "__main__":
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Gera o perfil do usuário
    perfil_usuario = gera_perfil_usuario()
    
    # Exibe o perfil gerado
    if perfil_usuario:
        print(f"Nome: {perfil_usuario['nome']}")
        print(f"Email: {perfil_usuario['email']}")
        print(f"País: {perfil_usuario['pais']}")
    # Teste 1
    perfil_usuario = gera_perfil_usuario()
    if perfil_usuario:
        print(f"Nome: {perfil_usuario['nome']}")
        print(f"Email: {perfil_usuario['email']}")
        print(f"País: {perfil_usuario['pais']}")
    