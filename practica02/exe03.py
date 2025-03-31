""" 3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
 """

# Variables

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F, K): ")
unidade_destino = input("Digite a unidade de destino (C, F, K): ")

# Calculations

if unidade_origem == "C" and unidade_destino == "F":
    resultado = (temperatura * 9/5) + 32
elif unidade_origem == "C" and unidade_destino == "K":
    resultado = temperatura + 273.15
elif unidade_origem == "F" and unidade_destino == "C":  
    resultado = (temperatura - 32) * 5/9
elif unidade_origem == "F" and unidade_destino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif unidade_origem == "K" and unidade_destino == "C":
    resultado = temperatura - 273.15
elif unidade_origem == "K" and unidade_destino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
else:
    resultado = temperatura

# Output

print(f"Resultado: {resultado:.2f} {unidade_destino}")

