'''
Created on 4 ago. 2020

@author: Amalio
'''

import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection

from collections import OrderedDict
import operator
from dataclasses import replace
from math import sqrt

# Constantes
URL = 'bolt://localhost:11005'
USER = 'neo4j'
PASSWORD = '123'
myConect = Connection(URL, USER, PASSWORD)
RUTA_FILES="../files/clusters/"

def clientesPorCluster(file):
    """Este metodo lee los csv de los clusters y devuelve un diccionario con los clientes y el numero de compras que se ha realizado de las distintas familia"""
    # Clientes por cluster"
    clusterx = pd.read_csv(RUTA_FILES + file,sep=',')
    clientes = clusterx.iloc[:, 0].tolist();
    return clientes;

def setDistanciaEuclidea(c1,c2,distancia):
    query="MATCH (c1:cliente {id:'"+c1+"'}) MATCH (c2:cliente {id: '"+c2+"'}) MERGE (c1)-[:SIMILARIDAD {de: "+distancia+"}]-(c2);"
    myConect.consultar(query)
   
   #Cambiar nombre
def setImportanciaClienteArticulo(c,a,medida):
    query="MATCH (c:cliente {id:'"+c+"'}) MATCH (a:articulo {id_interno: '"+a+"'}) MERGE (c)-[:IMPORTANCIA {medida: "+medida+"}]-(a);"
    myConect.consultar(query)
   
   
clusters = ["CPSclus1.csv", "CPSclus2.csv", "CPSclus3.csv"]
dfCluster=pd.read_csv(RUTA_FILES + "clusFalso.csv",index_col=0,header=0)
nfilas,ncolumnas=dfCluster.shape

tagClientes = dfCluster.index.values.tolist()
dfObj = pd.DataFrame(columns=tagClientes, index=tagClientes)

 
for x in range(0, nfilas):
    clienteA=dfCluster.iloc[x].tolist()
    tagA=tagClientes[x]
    for z in range(x, nfilas):
        clienteB=dfCluster.iloc[z].tolist()
        tagB=tagClientes[z]
        distanciaEuclidea=0
        strDisEu=""
        for y in range(0,ncolumnas):
            if clienteA[y]>0:
                distanciaEuclidea=(clienteA[y]-clienteB[y])**2
                strDisEu=strDisEu+"({}-{})^2 + ".format(clienteA[y],clienteB[y])
                 
                
        distanciaEuclidea=sqrt(distanciaEuclidea)
        #if(tagA!=tagB):
            #setDistanciaEuclidea(str(tagA),str(tagB),str(distanciaEuclidea))
        
        dfObj.loc[tagA][tagB]=distanciaEuclidea
        #print(strDisEu[0:-3])    
        #print("Del cliente ",tagA, " al cliente ",tagB," hay una distancia de: ",distanciaEuclidea)    
        #print()

cliente=dfCluster.iloc[0]
#print(dfObj.values.tolist())

listaClientes=dfCluster.index.values.tolist()
listaArticulos=dfCluster.columns.values.tolist()

print(dfCluster.iloc[0][0])

for i in range(len(listaClientes)):
    for j in range(len(listaArticulos)):
        c,a,m=str(listaClientes[i]), str(listaArticulos[j]), str(dfCluster.iloc[i][j])
        setImportanciaClienteArticulo(c,a,m)
'''
for cli,art in dfCluster.iterrows():
    print("Cliente",cli)
    for a in dfCluster.columns.values:
        print("\tArticulo",a," - peso - ", art.values)
        '''

#dfObj.to_csv("matrizDistancia.csv", index=True)

