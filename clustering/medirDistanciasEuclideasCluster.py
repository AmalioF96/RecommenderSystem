'''
Created on 13 ago. 2020

@author: Amalio
'''

from modelo.persistencia.ComprasDAO import ComprasDAO
from modelo.persistencia.ClienteDAO import ClienteDAO

import pandas as pd
from modelo.utils import Constantes as CONS
# Constantes

RUTA_FILES="../files/clusters/clusters17Octubre/"


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
    return Compras.getComprasPeriodoDeListaClientes(clientes, CONS.MIN_DATE, CONS.MAX_DATE)
   
def medirDistanciaEntreClientes(fileCluster):
    dfCluster=pd.read_csv(RUTA_FILES + fileCluster,index_col=0,header=0)
    tagClientes = dfCluster.index.values.tolist()
    clientes=ClienteDAO()
    clientes.setDistanciaEuclidea(tagClientes, CONS.MIN_DATE, CONS.MAX_DATE)
    
if __name__ == '__main__':
    #calcularDistanciaEuclideaClientes("ClientesFamilias_clus_1.csv")
    porcentaje=0;
    numFiles=5;
    for i in range(1,numFiles+1):
        file="ClientesFamilias_clus_"+str(i)+".csv"
        
        print("Analizando:",file,"\tCompletado al: ",porcentaje,"%\n")
        
        medirDistanciaEntreClientes(file)
        
        porcentaje=porcentaje+100/numFiles;

    
    print("Completado al: ",porcentaje,"%\n")









