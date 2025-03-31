""" Crie um programa que verifique se uma senha é forte. Uma
senha forte deve ter pelo menos 8 caracteres e conter pelo
menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite
'sair'. """

def eh_senha_forte(senha: str) -> bool:
    """Verifica se uma senha é forte.

    Parâmetros:
    senha (str): A senha a ser verificada
    Retorna:
    bool: True se for uma senha forte, False caso contrário
    """
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    # Verifica se a senha contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False
    return True
# Testes
if __name__ == "__main__":
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            break
        if eh_senha_forte(senha):
            print("Senha forte!")
        else:
            print("Senha fraca. Tente novamente.")
    # Teste 1
    senha = "senha123"
    print(f"Senha: {senha}")
    print(f"É forte? {'Sim' if eh_senha_forte(senha) else 'Não'}")
    
            