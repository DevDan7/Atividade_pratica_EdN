""" EXERCÍCIO PRÁTICO 1

www.escoladanuvem.org
​
distribuição, venda e compartilhamento.​

Enunciado: Crie uma função que calcule a gorjeta a ser deixada em
um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada.

Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros:

valor_conta (float): O valor total da conta

porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna:

float: O valor da gorjeta calculada """

def calcula_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

    Retorna:
    float: O valor da gorjeta calculada
    """
    return valor_conta * (porcentagem_gorjeta / 100)
# Testes

if __name__ == "__main__":

    # Teste 1
    valor_conta = 100.0
    porcentagem_gorjeta = 15.0
    gorjeta = calcula_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"Valor da conta: R$ {valor_conta:.2f}")
    print(f"Porcentagem da gorjeta: {porcentagem_gorjeta}%")
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")

    # Teste 2
    valor_conta = 200.0
    porcentagem_gorjeta = 10.0
    gorjeta = calcula_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"Valor da conta: R$ {valor_conta:.2f}")
    print(f"Porcentagem da gorjeta: {porcentagem_gorjeta}%")
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    # Teste 3

    valor_conta = 50.0
    porcentagem_gorjeta = 20.0
    gorjeta = calcula_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"Valor da conta: R$ {valor_conta:.2f}")
    print(f"Porcentagem da gorjeta: {porcentagem_gorjeta}%")
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    # Teste 4
    
    valor_conta = 75.0
    porcentagem_gorjeta = 12.0  
    gorjeta = calcula_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"Valor da conta: R$ {valor_conta:.2f}")
    print(f"Porcentagem da gorjeta: {porcentagem_gorjeta}%")
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    