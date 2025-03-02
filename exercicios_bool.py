# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
var1 = True
var2 = False
print(var1 and var2)

#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
var1 = bool(input("Digite o primeiro valor Lógico --> "))
var2 = bool(input("Digite o segundo valor Lógico --> "))
print (var1 or var2)

#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
var_invert = bool(input("Digite um valor Lógico --> "))
print(not var_invert)

#Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
var1 = (input("Digite o primeiro valor --> "))
var2 = (input("Digite o segundo valor --> "))
resultado = (var1 == var2)
print("Resultado da igualdade -->", resultado)

#Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
var1 = input("Digite o primeiro valor --> ")
var2 = input("Digite o segundo valor --> ")
resultado = (var1 != var2)
print("Resultado da igualdade -->", resultado)