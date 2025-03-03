#Exercício 23: Calculadora Simples. 
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador 
# (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas 
# não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador 
# fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    numero_01 = float(input("Digite o primeiro numero --> "))
    operacao = input ("Digite a operação (+, -, *, /) --> ")
    numero_02 = float(input("Digite o segundo numero --> "))

    if operacao == '+':
        resultado = numero_01 + numero_02
    
    elif operacao == '-':
        resultado = numero_01 - numero_02
    elif operacao == '*':
        resultado = numero_01 * numero_02
    elif operacao == "/" and operacao != 0:
        resultado = numero_01 / numero_02
    
    else:
         print("Operador inválido ou divisão por zero")  
    print(f"O resultado é --> {resultado}") 
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")