""" Desenvolva um programa que consulte informações de
endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP
consultado. """

import requests
import json
import os

def consulta_cep(cep: str) -> dict:
    """Consulta informações de endereço a partir de um CEP.

    Parâmetros:
    cep (str): O CEP a ser consultado
    Retorna:
    dict: As informações de endereço correspondentes ao CEP
    """
    # Faz uma requisição à API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Converte a resposta JSON em um dicionário
        endereco = response.json()
        return endereco
    else:
        print("Erro ao consultar o CEP.")
        return None
# Testes
if __name__ == "__main__":
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Solicita o CEP ao usuário
    cep = input("Digite o CEP (somente números): ")
    
    # Consulta o CEP
    endereco = consulta_cep(cep)
    
    # Exibe as informações de endereço
    if endereco:
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"Estado: {endereco['uf']}")
    # Teste 1
    cep = "01001-000"
    endereco = consulta_cep(cep)
    if endereco:
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"Estado: {endereco['uf']}")
        