contador = 0
while contador < 40:
    contador += 1
    print(f'\nProduto número {contador}.')
    custo = int (input('\nInsira o preço de custo: '))
    venda = int(input('\nInsira o preço de venda: '))

    resultado = venda - custo

    if resultado > 0:
        print(f'\nEste produto lhe-dá o lucro de {resultado} reais!', end='')
    elif resultado == 0:
        print('\nVocê não tem lucro com este produto!', end='')
    else:
        print(f'\nEste produto te dá {resultado * -1} reais de prejuízo! ', end= '')
