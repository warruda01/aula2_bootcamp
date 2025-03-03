try:
    resultado = len("Wilber")
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("tudo ocorreu bem")



print("-------------------------------")
try:
    resultado = len(3)
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("tudo ocorreu bem")
finally:
    print("O importante é participar")

print("-------------------------------")
numero = int(input("Insira um numero: "))
if isinstance(numero,int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

print("-------------------------------")
idade = 15

if idade < 18:
    print("Não pode dirigir")
else:
    print("Pode dirigir")

print("-------------------------------")
idade = 18

if idade < 18:
    print("Não pode dirigir")
elif idade == 18:
    print("Pode dirigir")
else:
    print("Pode dirigir")