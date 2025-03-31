""" Crie um programa que consulte a cotação atual de uma
moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última
atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação. """

import requests
import json
import os
from datetime import datetime

def consulta_cotacao(moeda: str) -> dict:
    """Consulta a cotação atual de uma moeda estrangeira em
    relação ao Real Brasileiro (BRL)."""
    # Faz uma requisição à API da AwesomeAPI
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Converte a resposta JSON em um dicionário
        cotacao = response.json()
        return cotacao
    else:
        print("Erro ao consultar a cotação.")
        return None
# Testes
if __name__ == "__main__":
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Solicita o código da moeda ao usuário
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
    
    # Consulta a cotação
    cotacao = consulta_cotacao(moeda)
    
    # Exibe as informações de cotação
    if cotacao:
        cotacao_info = cotacao[f"{moeda}BRL"]
        print(f"Cotação atual: {cotacao_info['ask']}")
        print(f"Valor máximo: {cotacao_info['high']}")
        print(f"Valor mínimo: {cotacao_info['low']}")
        print(f"Data da última atualização: {cotacao_info['create_date']}")
        # Converte a data para um formato legível
        data_atualizacao = datetime.strptime(cotacao_info['create_date'], "%Y-%m-%d %H:%M:%S")
        data_atualizacao_formatada = data_atualizacao.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Data da última atualização: {data_atualizacao_formatada}")
        # Teste 1
        moeda = "USD"
        cotacao = consulta_cotacao(moeda)
        if cotacao:
            cotacao_info = cotacao[f"{moeda}BRL"]
            print(f"Cotação atual: {cotacao_info['ask']}")
            print(f"Valor máximo: {cotacao_info['high']}")
            print(f"Valor mínimo: {cotacao_info['low']}")
            print(f"Data da última atualização: {cotacao_info['create_date']}")
            # Converte a data para um formato legível
            data_atualizacao = datetime.strptime(cotacao_info['create_date'], "%Y-%m-%d %H:%M:%S")
            data_atualizacao_formatada = data_atualizacao.strftime("%d/%m/%Y %H:%M:%S")
            print(f"Data da última atualização: {data_atualizacao_formatada}")
            