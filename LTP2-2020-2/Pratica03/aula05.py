from os import system
#Nossa calculadora

def mostrar_menu():
  system('clear')
  print('0 - Sair')
  print('+ - Somar')
  print('- - Subtrair')
  print('* - Multiplicar')
  print('/ - Dividir')
  print('Sen - Seno')
  print('Cos - Cosseno')
  print('^ - Elevado')
  print('Raiz - Calcular a raiz')

def somar():
  numero1 = float(input('Número 1: '))
  numero2 = float(input('+ \nNumero2: '))
  resultado = numero1 + numero2
  print('O resultado é: ', resultado)

def subtrair():
  numero1 = float(input('Número 1: '))
  numero2 = float(input('- \nNumero2: '))
  resultado = numero1 - numero2
  print('O resultado é: ', resultado)

def multiplicar():
  numero1 = float(input('Número 1: '))
  numero2 = float(input('* \nNumero2: '))
  resultado = numero1 * numero2
  print('O resultado é: ', resultado)
  
def dividir():
  numero1 = float(input('Número 1: '))
  numero2 = float(input('/ \nNumero2: '))
  resultado = numero1 / numero2
  print('O resultado é: ', resultado)

def elevar():
  numero1 = float(input('Número 1: '))
  numero2 = float(input('^ \nNumero2: '))
  resultado = numero1 ** numero2
  print('O resultado é: ', resultado)

ligado = True

while ligado == True:
  mostrar_menu()
  print('0 - Sair')
  opcao = input('Opção: ')
  if opcao == '0':
    ligado = False
  elif opcao == '+':
    somar()
  elif opcao == '-':
    subtrair()
  elif opcao == '*':
    multiplicar()
  elif opcao == '/':
    dividir()
  elif opcao == '^':
    elevar()

  input('Aperte qualquer tecla para continuar...')



print('Até logo!')
