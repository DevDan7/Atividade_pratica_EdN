""" Crie um programa que gera uma senha aleatória com o
módulo random, utilizando caracteres especiais,
possibilitando o usuário a informar a quantidade de
caracteres dessa senha aleatória. """

import random
import string
import os

def gera_senha(tamanho: int) -> str:
    """Gera uma senha aleatória com o tamanho especificado.

    Parâmetros:
    tamanho (int): O tamanho da senha a ser gerada
    Retorna:
    str: A senha gerada
    """
    # Define os caracteres que podem ser usados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
# Testes
if __name__ == "__main__":
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Solicita o tamanho da senha ao usuário
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    
    # Gera a senha
    senha_gerada = gera_senha(tamanho)
    
    # Exibe a senha gerada
    print(f"Senha gerada: {senha_gerada}")
    # Teste 1
    tamanho = 12
    senha_gerada = gera_senha(tamanho)
    print(f"Senha gerada: {senha_gerada}")