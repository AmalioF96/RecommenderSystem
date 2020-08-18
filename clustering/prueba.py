'''
Created on 18 ago. 2020

@author: Amalio
'''


import pandas as pd

df = pd.read_csv("../files/procesados/clusterToCsv.csv", sep=',', index_col=0)

print(df)
#df=df.drop('0',1)
print(df)

df.to_csv("../files/procesados/similaridadEntreClienteCluster5.csv",index = False ,header = ['cliente1','cliente2','peso']);