'''
Created on 13 ago. 2020

@author: Amalio
'''
import pandas as pd
from modelo.persistencia.bbdd.Connection import Connection

from math import sqrt
from modelo.persistencia.ComprasDAO import ComprasDAO
import time;
from modelo.persistencia.ClienteDAO import ClienteDAO
# Constantes

RUTA_FILES="../files/clusters/clusters17Octubre/"
minDay="2018-07-1"
maxDay="2018-07-7"

def clientesPorCluster(file):
    """Este metodo lee los csv de los clusters y devuelve un diccionario con los clientes y el numero de compras que se ha realizado de las distintas familia"""
    # Clientes por cluster"
    clusterx = pd.read_csv(RUTA_FILES + file,sep=',')
    clientes = clusterx.iloc[:, 0].tolist();
    return clientes;

   
   #Cambiar nombre

def setImportanciaClienteArticulo(c,a,medida):
    query="MATCH (c:cliente {id:'"+c+"'}) MATCH (a:articulo {id_interno: '"+a+"'}) MERGE (c)-[:IMPORTANCIA {medida: "+medida+"}]-(a);"
    #myConect.consultar(query)
def getComprasDeListaClientes(clientes):
    Compras=ComprasDAO()
    return Compras.getComprasPeriodoDeListaClientes(clientes, minDay, maxDay)
   
def medirDistanciaEntreClientes(fileCluster):
    dfCluster=pd.read_csv(RUTA_FILES + fileCluster,index_col=0,header=0)
    tagClientes = dfCluster.index.values.tolist()
    clientes=ClienteDAO()
    clientes.setDistanciaEuclidea(tagClientes, minDay, maxDay)
    
if __name__ == '__main__':
    #calcularDistanciaEuclideaClientes("ClientesFamilias_clus_1.csv")
    medirDistanciaEntreClientes("ClientesFamilias_clus_1.csv")











