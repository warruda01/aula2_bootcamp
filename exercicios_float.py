#Escreva um programa que receba dois números flutuantes e realize sua adição
numero_01 = float(input("Escreva o primeiro numero --> "))
numero_02 = float(input("Escreva o segundo numero --> "))
adicao_float = numero_01 + numero_02
print(adicao_float)

#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
media = (numero_01 + numero_02) / 2

# Desenvolva um programa que calcule a potência de um número 
# (base e expoente fornecidos pelo usuário).
numero_pot_01 = float(input("Escreva o primeiro numero --> "))
numero_pot_02 = float(input("Escreva o segundo numero --> "))
potencia = numero_pot_01 ** numero_pot_02
print(potencia)

#Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = (numero_01 * ( 9/5 )) +32
print(celsius)

#Escreva um programa que calcule a área e a circunferencia de um círculo, recebendo o raio como entrada.
import math
raio = float(input("Digite o raio do círculo --> "))
circ = 2 * math.pi * raio
area = math.pi * raio ** 2
print(f"Circunferência --> {circ:.2f}")
print(f"Área --> {area:.2f}")

