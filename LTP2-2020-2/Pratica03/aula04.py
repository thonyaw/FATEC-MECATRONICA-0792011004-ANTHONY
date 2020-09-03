#Nossa calculadora

def mostrar_menu():
  print('0 - Sair')
  print('+ - Somar')
  print('- - Subtrair')
  print('* - Multiplicar')
  print('/ - Dividir')
  print('Sen - Seno')
  print('Cos - Cosseno')
  print('^ - Elevado')
  print('Raiz - Calcular a raiz')


ligado = True

while ligado == True:
  mostrar_menu()
  print('0 - Sair')
  opcao = input('Opção: ')
  if opcao == '0':
    ligado = False

print('Até logo!')
