'''
Created on 4 mar. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np

from collections import OrderedDict
import operator
from dataclasses import replace
from modelo.persistencia.ClienteDAO import ClienteDAO
from modelo.persistencia.ArticuloDAO import ArticuloDAO
from modelo.persistencia.ComprasDAO import ComprasDAO

#Constantes
RUTA_FILES="D:/Workspaces/R-workspace/ClusteringR/ClustersGasto/"

def clientesPorCluster(file):
    """Este metodo lee los csv de los clusters y devuelve un diccionario con los clientes y el numero de compras que se ha realizado de las distintas familia"""
    # Clientes por cluster"
    clusterx = pd.read_csv(RUTA_FILES + file)
    clientes = clusterx.iloc[:, 0].tolist();
    return clientes;


def gastoMedioDeCluster(listaClientes):
    cliDAO=ClienteDAO()
    '''En base a una lista de clientes obtenemos su gasto medio, es decir, el gasto medio de un cluster'''
    data = cliDAO.gastoMedio(listaClientes)
    return data

    
def familiasDeUnClusterConMayorGastoMedio(listaClientes):
    '''En base a una lista de clientes que forman un cluster, obtenemos el gasto medio que tienen de cada familia.'''
    artDAO=ArticuloDAO()
    data = artDAO.familiasConMayorGastoMedio(listaClientes)
    return data


def obtenerComprasYGasto(listaClientes):
    """Este metodo nos devuelve elnumero de facturas asociadas a una lista de clientes y el gasto que suman"""
    compDAO=ComprasDAO()
    data = compDAO.obtenerComprasYGasto(listaClientes)
    return data


def csvClusterToDicc(file):
    """Este metodo lee los csv de los clusters y devuelve un diccionario con las familias y el numero de compras que se han realizado de la misma. Este metodo es interesante para visualizar los datos"""
    # #Familias por cluster
    # 1#Leemos
    clusterx = pd.read_csv("../files/" + file)
    
    # 2#Eliminamos la primera columna"
    clusterx = clusterx.drop(clusterx.columns[0], axis=1)
    # print(cluster2)
    
    # 3#Creamos el diccionario de datos familia:sumCantidad"
    diccionarioC = {}
    for index in clusterx:
        name = index.replace("X", "")
        diccionarioC[name] = clusterx[index].sum()
    
    # 4#Ordenamos el diccionario"
    return dict(sorted(diccionarioC.items(), key=operator.itemgetter(1), reverse=True))



#clusters = ["clus1.csv", "clus2.csv", "clus3.csv", "clus4.csv", "clus5.csv"]
clusters = ["clusGasto1.csv", "clusGasto2.csv", "clusGasto3.csv"]
listClust = []

lstGastosCluster = []
lstGastosClusterFamilias = []
lstComprasGasto = []

for clus in clusters:
    # Obtenemos clientes de un cluster
    listaClientes = clientesPorCluster(clus)
    # Obtenemos el gasto medio del cluster
    lstGastosCluster.append(gastoMedioDeCluster(str(listaClientes)))
    # Obtenemos el gasto medio del cluster respecto a las familias que compra
    lstGastosClusterFamilias.append(familiasDeUnClusterConMayorGastoMedio(str(listaClientes)))
    lstComprasGasto.append(obtenerComprasYGasto(str(listaClientes)))

#A partir de aqui simplemente se muestran los resultados obtenidos anteriormente

print("\nCluster\tGasto")
for l, i in enumerate(lstGastosCluster):
    print(i, "\t", l)
    
i = 0
print("Cluster\tFamilia\tGasto")
for lst in lstGastosClusterFamilias:
    i += 1
    for j, l in enumerate(lst['familia']):
        print(i, "\t", l, "\t", str(lst.loc[j, 'gastoMedio']).replace(".", ","))    #Con el replace cambiamos los '.' por ',' porque son variables float y tienen un formato que nos nos sirve

i = 0
print("Cluster\tCuantia\tNumCompras")
for lst in lstComprasGasto:
    i += 1
    for j, l in enumerate(lst['cuantia']):
        print(i, "\t", str(l).replace(".", ","), "\t", lst.loc[j, 'compras'])
        

