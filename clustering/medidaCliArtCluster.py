'''
Created on 18 ago. 2020

@author: Amalio
'''

import pandas as pd
from modelo.persistencia.bbdd.Connection import Connection

from math import sqrt


RUTA_FILES="../files/clusters/clustersJulio/"




def clientesPorCluster(file):
    """Este metodo lee los csv de los clusters y devuelve un diccionario con los clientes y el numero de compras que se ha realizado de las distintas familia"""
    # Clientes por cluster"
    clusterx = pd.read_csv(RUTA_FILES + file,sep=',')
    clientes = clusterx.iloc[:, 0].tolist();
    return clientes;

dfCluster=pd.read_csv(RUTA_FILES + "CPSclus5.csv",index_col=0,header=0)
nfilas,ncolumnas=dfCluster.shape
print("LEIDO")
tagClientes = dfCluster.index.values.tolist()
matrixImportanciaArticulo=[]

cliente=dfCluster.iloc[0]

listaClientes=dfCluster.index.values.tolist()
listaArticulos=dfCluster.columns.values.tolist()

print("Start:",0,"End:",len(listaClientes))

for i in range(len(listaClientes)):
    for j in range(len(listaArticulos)):
        c,a,m=str(listaClientes[i]), str(listaArticulos[j]), str(dfCluster.iloc[i][j])
        matrixImportanciaArticulo.append([c,a,m])
    if i%100==0:    
        print("i:",i)
        
dfObj=pd.DataFrame(matrixImportanciaArticulo)
dfObj.to_csv("../files/procesados/medidaEntreClienteArticuloCluster5.csv",index = False ,header = ['cliente','articulo','peso']);




