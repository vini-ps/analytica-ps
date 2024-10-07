import pandas as pd
#Parte Prática 1.2.2

####1
df = pd.read_csv("dataset.csv")

####2
print(df.to_string())

####3
##(a)
filtro_IDH = df[(df['ano']==1991)&(df['idhm'])]

##(b)
IDH = pd.Series(filtra['idhm'])

##(c)
print(IDH.mean())

