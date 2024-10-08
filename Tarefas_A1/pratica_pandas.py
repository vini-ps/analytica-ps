import pandas as pd

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
print(f'IDH medio de 1991 = {IDH.mean():.3f}\n')

####4
##(a)
filtro_mediaIDH = filtro_IDH['idhm'] > IDH.mean()
filtro_siglauf = filtro_IDH['sigla_uf']

##(b) estados com IDH maior que a media calculada na questao 3
filtro_uf = filtro_IDH[filtro_mediaIDH & filtro_siglauf]
print(f'{filtro_uf}\n')

####5
df_ordenado = df.sort_values('idhm')
print(df_ordenado.head(5))

print('\n')
####6
print(f"Estado com menor IDH em 1991: \n{filtro_uf['sigla_uf'].min()} indice {filtro_uf['sigla_uf'].idxmin()}")
print(f"Estado com maior IDH em 1991: \n{filtro_uf['sigla_uf'].max()} indice {filtro_uf['sigla_uf'].idxmax()}")
