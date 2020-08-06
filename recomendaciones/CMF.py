'''
Created on 29 jun. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection
# Constantes
URL = 'bolt://localhost:11005'
USER = 'neo4j'
PASSWORD = '123'
myConect = Connection(URL, USER, PASSWORD)

def getClientes():
    query = "MATCH (c1:cliente)where c1.id<>'1715' return c1.id as id"
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['id'])
    return data

def getFamilias():
    query = "match (a:articulo) return distinct(a.familia_id) as familia"
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['familia'])
    return data

def getMarcas():
    query = "match (a:articulo) return distinct(a.marca_id) as marca"
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['marca'])
    return data

#FUNCION PARA SACAR UNA SIMILITUD SIMPLE, EL NUMERO DE VECES QUE UN CLIENTE COMPRA ARTICULOS DE UNA FAMILIA
def getClientesFamilia():
    query="MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) where c1.id<>'1715' return c1.id as cliente,a.familia_id as familia, count(a.familia_id) as similitud order by cliente desc"
    
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'familia', 'similitud'])
    return data

#FUNCION PARA SACAR UNA SIMILITUD SIMPLE, EL NUMERO DE VECES QUE UN CLIENTE COMPRA ARTICULOS DE UNA FAMILIA
def getClientesMarca():
    query="MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) where c1.id<>'1715' return c1.id as cliente,a.marca_id as familia, count(a.marca_id) as similitud order by cliente desc"
    
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'marca', 'similitud'])
    return data

def getClientesMarcaFamilia():
    query="MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) where c1.id<>'1715' return c1.id as cliente,a.marca_id as marca, a.familia_id as familia, count(a.marca_id) as similitud order by cliente desc"
    
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'marca','familia', 'similitud'])
    return data

def getMarcasFamilia():
    query="MATCH (a:articulo) return a.marca_id as marca, a.familia_id as familia, count(a.familia_id) as fitness order by fitness desc, marca,familia"
    
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['marca', 'familia', 'similitud'])
    return data

#1# - Recogemos datos        
numClientes = sum(getClientes().values.tolist(), [])
numFamilias = sum(getFamilias().values.tolist(), [])
numMarcas = sum(getMarcas().values.tolist(), [])
#2# - Formamos Matriz")
#Usamos el numero de clientes(filas) y el numero de familias(columnas) para formar la matriz

dfObj=pd.MultiIndex.from_product([numClientes,numMarcas,numFamilias])
#3# - Recogemos getClienteFamilia     
#cliXfam = getClientesFamilia()
cliXmarXfam=getClientesMarcaFamilia()
#4# - Recogemos getClienteMarca    
#cliXmar = getClientesMarca()
#5# - Recogemos getMarcaFamilia     
marXfam = getMarcasFamilia()
print(cliXmarXfam[:4])

#6# - Recorremos matriz dfObj
for indexI,i in enumerate(cliXmarXfam['cliente']):
    #nombreMF=cliXmar.loc[indexI,'marca']+cliXfam.loc[indexI,'familia']

            mf=marXfam.loc[cliXmarXfam.loc[indexI,'marca']][cliXmarXfam.loc[indexI,'familia']]
            dfObj.loc[cliXmarXfam.loc[indexI,'cliente']][cliXmarXfam.loc[indexI,'marca']][cliXmarXfam.loc[indexI,'familia']] = (cliXmarXfam.loc[indexI,'similitud'])%mf


print(dfObj)
#CM + CF  % MF







