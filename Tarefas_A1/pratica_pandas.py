import pandas as pd
#Parte Prática 1.2.2

####1
df = pd.read_csv("dataset.csv")

####2.
print(df.to_string())

####3
##(a)
filtro_IDH = df[(df['ano']==1991)&(df['idhm'])]

##(b)
IDH = pd.Series(filtro_IDH['idhm'])

##(c)
print(IDH.mean())

####4
##(a)
filtro_mediaIDH = filtro_IDH['idhm'] > IDH.mean()
filtro_siglauf = filtro_IDH['sigla_uf']

##(b)
filtro_uf = filtro_IDH[filtro_mediaIDH & filtro_siglauf]

####5
df_ordenado = df.sort_values('idhm')

df_ordenado.head(5)

####6
