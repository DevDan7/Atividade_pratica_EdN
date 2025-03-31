""" Crie uma função que verifique se uma palavra ou frase é um
palíndromo (lê-se igual de trás para frente, ignorando
espaços e pontuação).

Se o resultado é True, responda “Sim”, se o resultado for
False, responda “Não” """

def eh_palindromo(texto: str) -> bool:
    """Verifica se uma palavra ou frase é um palíndromo.

    Parâmetros:
    texto (str): A palavra ou frase a ser verificada
    Retorna:
    bool: True se for um palíndromo, False caso contrário
    """
    # Remove espaços e pontuação, e converte para minúsculas
    texto = ''.join(c for c in texto if c.isalnum()).lower()
    # Verifica se o texto é igual ao seu reverso
    return texto == texto[::-1]
# Testes

if __name__ == "__main__":  
    exemplos = [
        "A mala nada na lama",
        "A torre da derrota",
        "A cara rajada da jaraca",
        "A grama é amarga",
        "A sacada da casa",
        "A torre da derrota",
        "A mala nada na lama",
        "Anotaram a data da maratona",
        "O lobo ama o bolo",
        "O galo ama o lago",
        "O rato roeu a roupa do rei de Roma"
    ]
    for exemplo in exemplos:
        resultado = eh_palindromo(exemplo)
        print(f"'{exemplo}' é palíndromo? {'Sim' if resultado else 'Não'}")

