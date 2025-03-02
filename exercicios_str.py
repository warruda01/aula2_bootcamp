#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
palavra = input("Digite uma palavra aí --> ")
print(palavra.upper())

#Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
print(palavra.lower())

#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
print(palavra.strip())

#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa --> ")
lista_de_dia_mes_ano = data.split("/")
print(lista_de_dia_mes_ano)

#quebrando em lista
print(f"O dia é: {lista_de_dia_mes_ano[0]}")
print(f"O mes é: {lista_de_dia_mes_ano[1]}")
print(f"O ano é: {lista_de_dia_mes_ano[2]}")

#Escreva um programa que concatene duas strings fornecidas pelo usuário
string1 = input("Forneça a primeira palavra --> ")
string2 = input("Forneça a segunda palavra --> ")
texto = string1 + string2
print (texto)