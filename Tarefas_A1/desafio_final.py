import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pratica_pandas import *

def diferenca_expect_vida():
    filtro_1991 = df[df['ano']==1991]
    filtro_2010 = df[df['ano']==2010]

    expect_vida1991 = np.array(filtro_1991['expectativa_vida'])
    expect_vida2010 = np.array(filtro_2010['expectativa_vida'])

    diferenca_expect_vida = np.array([])
    for i in range(len(expect_vida1991)):
        diferenca = round(expect_vida2010[i] - expect_vida1991[i],2) 
        diferenca_expect_vida = np.append(diferenca_expect_vida, diferenca)

    return diferenca_expect_vida


def grafico():
    expect_vida = diferenca_expect_vida()
    estados = np.array(filtro_siglauf)

    plt.bar(estados, expect_vida)
    plt.show()

    return 

