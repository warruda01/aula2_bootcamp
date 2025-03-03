#Escreva um programa que calcule a área e a circunferencia de um círculo, recebendo o raio como entrada.
import math
raio = float(input("Digite o raio do círculo --> "))
circ = 2 * math.pi * raio
area = math.pi * raio ** 2
print(f"Circunferência --> {circ:.2f}")
print(f"Área --> {area:.2f}")