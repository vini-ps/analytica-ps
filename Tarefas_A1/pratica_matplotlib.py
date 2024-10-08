import matplotlib.pyplot as plt
import numpy as np 
from pratica_pandas import *

def populacao_urbanaBR():
    x = np.array(filtro_IDH1991["sigla_uf"])
    y = np.array(filtro_IDH1991["populacao_urbana"])
    porcentagem = y/sum(y)

    plt.bar(x,porcentagem)
    plt.show()
    print('Proporcao da Populacao Urbana entre os estados brasileiros para o ano de 1991:\n')
    for i in range(len(y)):
        print(f'{x[i]} = {porcentagem[i]*100:.2f}% do Brasil')
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

    print(f"desvio padrao de 1991, 2000, 2010 respectivamento:")
    print(f"{ano91.std():.5f}, {ano00.std():.5f}, {ano10.std():.5f}")
    print("A partir dos graficos e desvio padrao dos valores de idhm dos anos estudos, eh possivel perceber uma")
    print("diminuicao da desigualdade do Brasil, considerando todo o período analisado")
    return 


def idh_vs_vida():
    idhm = np.array(df['idhm'])
    expectativa_vida = np.array(df['expectativa_vida'])
    
    plt.scatter(idhm,expectativa_vida)

    plt.show()
    print("Sim, o grafico mostra que existe uma relacao diretamente proporcional entre as medidas")
    return


