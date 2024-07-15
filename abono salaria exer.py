SALARIO_FIXO = 2000

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
sexo = input("Insira seu sexo: (F / M): ").lower()

if sexo == 'f':
    if idade >= 30:
     print(f'Sr(a) {nome}, seu salário é: 1',SALARIO_FIXO + 200)
    else:
        print(f'Sr(a) {nome}, seu salário é: 2',SALARIO_FIXO + 80)
elif sexo == 'm':
    if idade >= 30:
        print(f'Sr(a) {nome}, seu salário é: 3',SALARIO_FIXO + 100)
    else:
        print(f'Sr(a) {nome}, seu salário é: 4',SALARIO_FIXO + 50)
else:
    print("Sexo inválido! .")



