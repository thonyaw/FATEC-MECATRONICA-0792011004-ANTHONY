#Lista vazia com as temperaturas
# temperaturas = [23, 5, -6, 34]
temperaturas = []


print(temperaturas)


#Pede para o usuário digitar 5 temperaturas
contador = 0
while contador < 5:
  temperatura = float(input('Informe um temperatura:'))
  #Adiciona temperatura no final
  temperaturas.append(temperatura)
  #Só para ver o comportamento da lista entre as interações
  print(temperaturas)
  contador += 1 #contador = contador + 1

menor = min(temperaturas)
maior = max(temperaturas)
print("Maior valor: {}\nMenor valor: {}".format(maior, menor))

media = sum(temperaturas)/len(temperaturas)
print('A média das temperaturas é: ', media)

temperaturas.sort()
print('Ordenação crescente: {}'.format(temperaturas))

temperaturas.sort(reverse=True)
print('ordenação decrescente: {}'.format(temperaturas))
