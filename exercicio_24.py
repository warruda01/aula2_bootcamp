#Escreva um programa que solicite ao usuário para digitar um número.
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else 
# para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

try:

    entrada = float(input("Digite um numero --> "))

    if entrada > 0:
        saida1 = "Positivo"
        if entrada % 2 ==0:
            saida2 = "Par"
        else:
            saida2 = "Ímpar"
        print (f"O número {entrada} é {saida1} e {saida2}")   
    elif entrada < 0:
        saida1 = "Negativo"

        if entrada % 2 ==0:
            saida2 = "Par"
        else:
            saida2 = "Ímpar"
        print (f"O número {entrada} é {saida1} e {saida2}")
    else:

        print (f"O número {entrada} é Zero")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")