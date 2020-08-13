'''
Created on 13 ago. 2020

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
   

dfCluster=pd.read_csv(RUTA_FILES + "CPSclus5.csv",index_col=0,header=0)
nfilas,ncolumnas=dfCluster.shape
print("LEIDO")
tagClientes = dfCluster.index.values.tolist()
dfObj = pd.DataFrame()
blacklist=[]

for x in range(0, nfilas):
    clienteA=dfCluster.iloc[x].tolist()
    tagA=tagClientes[x]
    for z in range(x, nfilas):
        clienteB=dfCluster.iloc[z].tolist()
        tagB=tagClientes[z]
        if tagB not in blacklist:
            distanciaEuclidea=0
            strDisEu=""
            for y in range(0,ncolumnas):
                if clienteA[y]>0:
                    distanciaEuclidea=(clienteA[y]-clienteB[y])**2
                  
            distanciaEuclidea=sqrt(distanciaEuclidea)
            if(tagA!=tagB):
                dfObj.iloc[x][z]=distanciaEuclidea
            
            
            #print(strDisEu[0:-3])    
            #print("Del cliente ",tagA, " al cliente ",tagB," hay una distancia de: ",distanciaEuclidea)    
            #print()
    blacklist.append(tagA)
    


dfObj.to_csv("../files/procesados/clusterToCsv",index = ['cliente1','cliente2','peso']);















