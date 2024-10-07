from numpy import random # type: ignore
import numpy as np # type: ignore
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
##(b)
def desvio_padrao(lista):
    media = media(lista)
    somatorio = 0
    for i in range(len(lista)):
        potencia = math.pow(lista[i] - media,2)
        soma += potencia
    razao = soma/len(lista)
    desvio_padrao = math.sqrt(razao)
    return desvio_padrao

########5
##(a)
lista_ordenada = lista.sort()
print(lista_ordenada)

##(b)
print(lista.shape)

##(c)
print(lista.mean())

##(d)
desvio_pd = lista.std()
maximo = lista.max()
minimo = lista.min()

##(e)
array_aleatorio = random.randint(11,size=(100))

print(f'media = {array_aleatorio.mean():.2f}')
print(f'desvio padrao = {array_aleatorio.std():.2f}')
print(f'maior valor = {array_aleatorio.max()}')
print(f'menor valor = {array_aleatorio.min()}')
