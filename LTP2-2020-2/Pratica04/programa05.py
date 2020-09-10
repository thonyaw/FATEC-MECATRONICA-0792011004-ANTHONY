
'''
nomes = []

continuar = True

while continuar == True:
  nome = input('Informe um nome: ')
  nomes.append(nome)
  print(nomes)
  if input('Deseja continuar?\n') == 's':
    continuar = True
  else:
    continuar = False

'''

# preenchendo manualmente
nomes = ['Anthony', 'Julia', 'Gabriel', 'Ana', 'Paula']
nomes.sort()

nome = input('Quem deseja prcurar? ')

if nome in nomes:
  print('Encontrei na posição:', nomes.index(nome))
else:
  print('Registro não encontrado.')
