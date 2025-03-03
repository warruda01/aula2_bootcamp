# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, 
# utilizando try-except, garantir que a entrada seja numérica, 
# tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem 
# de erro se a entrada não for válida.

try:
    valor_celsius = float(input("Digite a temperatura em graus celsius --> "))
    valor_fahre = float((valor_celsius * ( 9/5 )) +32)
    
except ValueError:
    print("O valor deve ser numérico")
else:
    print(f" {valor_celsius} graus Celsius correspondem a {valor_fahre}")