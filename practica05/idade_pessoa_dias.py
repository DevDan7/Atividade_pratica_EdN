""" Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento. """

def calcula_idade_em_dias(ano_nascimento: int) -> int:
    """Calcula a idade de uma pessoa em dias, baseado no ano de nascimento.

    Parâmetros:
    ano_nascimento (int): O ano de nascimento da pessoa

    Retorna:
    int: A idade da pessoa em dias
    """
    from datetime import datetime

    # Obtém o ano atual
    ano_atual = datetime.now().year

    # Calcula a idade em anos
    idade_em_anos = ano_atual - ano_nascimento

    # Converte a idade em anos para dias (considerando 365 dias por ano)
    return idade_em_anos * 365
# Testes
if __name__ == "__main__":
    # Teste 1
    ano_nascimento = 2000
    idade_dias = calcula_idade_em_dias(ano_nascimento)
    print(f"Idade em dias: {idade_dias} dias")

    # Teste 2
    ano_nascimento = 1982
    idade_dias = calcula_idade_em_dias(ano_nascimento)
    print(f"Idade em dias: {idade_dias} dias")
    # Teste 3
    ano_nascimento = 1985
    idade_dias = calcula_idade_em_dias(ano_nascimento)
    print(f"Idade em dias: {idade_dias} dias")
