#criar variaveis para armazenar os votos de cada candidato

resposta = input("Quer votar? S/N: ").lower()

contador_1 = 0

contador_2 = 0

contador_3 = 0
while resposta == 's':

  voto = input('\nDigite o numero referente ao seu candidato: \n22 = Bolsonaro. \n13 = Lula. \n12 = Ciro. \n')

  if voto == '22':
    print('Você votou no Bolsonaro! ', end='\n')
    contador_1 += 1

  elif voto == '13':
    print('Você votou no Lula! ', end='\n')
    contador_2 += 1

  elif voto == '12':
    print('Você votou no Ciro! ', end='\n')
    contador_3 += 1

  else:
    print('Candidato inválido. ', end='\n')

  resposta = input('\nQuer votar novamente? S/N: ').lower()

print(f'\nContagem de votos: Bolsonaro tem {contador_1} votos. Lula tem {contador_2} votos. Ciro tem {contador_3} votos', end='')
