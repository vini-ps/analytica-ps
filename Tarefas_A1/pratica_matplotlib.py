import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
from pratica_pandas import *

def populacao_urbanaBR():
    x = np.array(filtro_IDH1991["sigla_uf"])
    y = np.array(filtro_IDH1991["populacao_urbana"])
    porcentagem = y/sum(y)

    plt.bar(x,porcentagem)
    plt.show()
    return 


#populacao_urbanaBR()

def desigualdade_brasil():
    #filtro do IDH de 1991 foi importado da pratica_pandas
    filtro_IDH2000 = df[(df['ano']==2000)&(df['idhm'])]
    filtro_IDH2010 = df[(df['ano']==2010)&(df['idhm'])]

    ano91 = np.array(filtro_IDH1991['idhm'])
    ano00 = np.array(filtro_IDH2000['idhm'])
    ano10 = np.array(filtro_IDH2010['idhm'])

    plt.hist([ano91,ano00,ano10], color = ('red','green','blue'), width = 0.015)
    plt.show()
    return 


def idh_vs_vida():
    idhm = np.array(df['idhm'])
    expectativa_vida = np.array(df['expectativa_vida'])
    
    plt.scatter(idhm,expectativa_vida)

    plt.show()
