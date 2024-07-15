valor_1 = int(input('Insira o número pra ser realizada a operação matématica: '))
valor_2 = int(input("Insira outro número: "))
operador = input("Insira o operador: ")

if operador == '+':
    resultado = valor_1 + valor_2
    print('Resultado da operação requisitada :', resultado)
elif operador == '-':
    resultado = valor_1 - valor_2
    print('Resultado da operação requisitada :', resultado)
elif operador == '/':
    resultado = valor_1 / valor_2
    print('Resultado da operação requisitada :', resultado)
elif operador == '*':
    resultado = valor_1 * valor_2
    print('Resultado da operação requisitada :', resultado)
else:
    print("Operador inválido. Resete o sistema.")