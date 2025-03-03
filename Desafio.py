#Desafio - Refatorar o projeto da aula anterior evitando Bugs!
#Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser 
# convertidas para um número de ponto flutuante e prevenção de valores negativos para 
# salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar 
# verificações adicionais após a tentativa de conversão para garantir que os valores sejam 
# positivos.


CONSTANTE_BONUS = 1000.00

try:
# O programa deve começar solicitando ao usuário que insira seu nome.
    nome_usuario = input("Digite seu nome --> ")

#Verificar se o nome é vazio
    if len (nome_usuario)== 0: #Porque ele pode castear para String
        raise ValueError("O nome não pode ser vazio")
 
    elif nome_usuario.isdigit():
        raise ValueError("O nome não pode conter números")

    else:
        print("Nome Válido")

except ValueError as e:
    print(e)
    exit()
else:
# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.
    
    try:
        salario = float(input("Digite o seu salário -->"))
    
        if salario == 0:
            raise ValueError("O salário não pode ser zero")
        elif salario < 0:
             raise ValueError("O salário não pode ser negativo")

        else:
            print("Valor Válido")
    except ValueError as e:
        print(e)
        exit()
    else:

# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, 
# que também pode ser um número decimal

        try:

            
            porcentagem_bonus = float(input("Digite a porcentagem (em %) do Bônus --> "))

            if salario < 0:
                raise ValueError("O salário não pode ser negativo")
            else:
                print("Valor Válido")

        except ValueError as e:
            print(e)
            exit()
        else:
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
            valor_bonus = float((salario * porcentagem_bonus/100) + salario + CONSTANTE_BONUS)

# Finalmente, o programa deve imprimir uma mensagem no seguinte formato:
# "Olá [nome], o seu valor bônus foi de 5000".
# poderia ser --> print("Olá " + nome + ", seu bonus foi de " + str(bonus))
            print(f"Olá {nome_usuario}, o seu valor de bonus foi de {valor_bonus:.2f}")