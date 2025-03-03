#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa --> ")
lista_de_dia_mes_ano = data.split("/")
print(lista_de_dia_mes_ano)

#quebrando em lista
print(f"O dia é: {lista_de_dia_mes_ano[0]}")
print(f"O mes é: {lista_de_dia_mes_ano[1]}")
print(f"O ano é: {lista_de_dia_mes_ano[2]}")