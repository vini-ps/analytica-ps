from numpy import random
import numpy as np
import math

lista = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])


########4
##(a)
def  media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    media = soma/len(lista)
    return media

media = media(lista)
print(f'media usando iteracao = {media}')

##(b)
def desvio_padrao(lista):
    somatorio = 0
    for i in range(len(lista)):
        potencia = math.pow(lista[i] - media,2)
        somatorio += potencia
    razao = somatorio/len(lista)
    desvio_padrao = math.sqrt(razao)
    return desvio_padrao

desvio_padrao = desvio_padrao(lista)
print(f'desvio padrao usando iteracao = {desvio_padrao}')

########5
##(a)
lista.sort()
print(lista)

##(b)
print(lista.shape)

##(c)
print(lista.mean())

##(d)
print('desvio padrao, maximo e minimo com metodos: ')
print(lista.std())
print(lista.max())
print(lista.min())

##(e)
array_aleatorio = random.randint(11,size=(100))

print(f'media = {array_aleatorio.mean():.2f}')
print(f'desvio padrao = {array_aleatorio.std():.2f}')
print(f'maior valor = {array_aleatorio.max()}')
print(f'menor valor = {array_aleatorio.min()}')
