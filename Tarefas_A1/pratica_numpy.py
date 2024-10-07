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
##(b)
def desvio_padrao(lista):
    media = media(lista)
    somatorio = 0
    for i in range(len(lista)):
        potencia = math.pow(lista[i] - media,2)
        soma += potencia
    razao = soma/len(lista)
    desvio_padrao = math.sqrt(razao)

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
