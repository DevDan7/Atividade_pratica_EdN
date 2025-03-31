import requests 
import random
import string

def gerar_senha():
    while True:
        try:
            tamanho = int(input("Digite a quantidade de caracteres para a senha (entre 4 e 10): "))
            if 4 <= tamanho <= 10:
                break
            else:
                print("O tamanho deve ser entre 4 e 10. Por favor, tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres, k=tamanho))
    print(f"Senha gerada: {senha}")

if __name__ == '__main__':
    gerar_senha()

