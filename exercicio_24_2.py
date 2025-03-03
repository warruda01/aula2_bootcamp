#Escreva um programa que solicite ao usuário para digitar um número.
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else 
# para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

try:

    entrada = float(input("Digite um numero --> "))



    if entrada == 0:
        print (f"O número é Zero")
        
    elif entrada > 0:  
        saida1 = "Positivo" 
    else:
        saida1 = "Negativo"
    
    if entrada % 2 ==0:
        saida2 = "Par"
    else:
        saida2 = "Ímpar"
    print (f"O número {entrada} é {saida1} e {saida2}")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

    #PROBLEMA: Quando é zero não consigo pular a linha 19