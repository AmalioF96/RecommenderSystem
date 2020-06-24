'''
Created on 14 mar. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from persistencia.Conect import Connection
# Constantes
URL = 'bolt://localhost:11005'
USER = 'neo4j'
PASSWORD = '123'
myConect = Connection(URL, USER, PASSWORD)

def getClientes():
    '''Obtenemos una lista con todos los clientes de la aplicacion'''
    query = "MATCH (c1:cliente)where c1.id<>'1715' return c1.id as id"
    data = pd.DataFrame(myConect.consultar(query), columns=['id'])
    return data

def getFamilias():
    '''Obtenemos una lista con todos las familias de la aplicacion'''
    query = "match (a:articulo) return distinct(a.familia_id) as familia"
    data = pd.DataFrame(myConect.consultar(query), columns=['familia'])
    return data

def getClientesFamilia():
    '''Obtenemos una lista con todos la cantidad de familias que compra cada cliente'''
    query="MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) where c1.id<>'1715' return c1.id as cliente,a.familia_id as familia, count(a.familia_id) as similitud order by cliente desc"
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'familia', 'similitud'])
    return data


#1# - Recogemos datos        
clientes = sum(getClientes().values.tolist(), [])
familias = sum(getFamilias().values.tolist(), [])
#2# - Formamos Matriz que proximamente será el csv a clusterizar        
dfObj = pd.DataFrame(columns=familias, index=clientes)
#print(dfObj)

#3# - Recogemos getFacturasFamilia     
cliXfam = getClientesFamilia()
print(cliXfam)
#4# - Recorremos matriz dfObj     
for indexI,i in enumerate(cliXfam['cliente']):
    dfObj.loc[cliXfam.loc[indexI,'cliente']][cliXfam.loc[indexI,'familia']] =  cliXfam.loc[indexI,'similitud']


#5# - Guardamos en el csv
#print(dfObj)
dfObj.to_csv( "dataClienteFamilia.csv", index=True)
myConect.close()