#Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada

entrada = input("Digite a palavra ou frase a ser testada-->")

if isinstance(entrada,str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado [::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")

else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# for i in range(0, tamanho-1, 1):
# if palavra_quebrada[i] == palavra_quebrada[tamanho-1]:
#     if palavra_quebrada[1] == palavra_quebrada[tamanho-2]:
# print (palavra_quebrada)