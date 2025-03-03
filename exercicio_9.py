#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Escreva a temperatura em Celsius --> "))
fahre = (celsius * ( 9/5 )) +32
print(f"{celsius} graus Celsius correspondem a {fahre:.2f} graus Fahrenheit")