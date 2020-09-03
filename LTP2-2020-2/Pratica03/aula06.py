from os import system
from math import sin, cos, radians, sqrt
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
  print('^ - Potência')
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

def potencia():
  base = float(input('Base: '))
  expoente = float(input('^ \nExpoente: '))
  resultado = base ** expoente
  print('O resultado é: ', resultado)

def seno():
  angulo = float(input('Ângulo: '))
  print('Seno de {} é {}'.format(angulo, sin(radians(angulo))))

def coseno():
  angulo = float(input('Ângulo: '))
  print('Coseno de {} é {}'.format(angulo, cos(radians(angulo))))

def raiz():
  numero = float(input('Digite o número: '))
  print('Raíz quadrada de {} é {}'.format(numero, sqrt(numero)))

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
    potencia()
  elif opcao == 'Sen':
    seno()
  elif opcao == 'Cos':
    coseno()
  elif opcao == 'Raiz':
    raiz()

  input('Aperte qualquer tecla para continuar...')



print('Até logo!')
