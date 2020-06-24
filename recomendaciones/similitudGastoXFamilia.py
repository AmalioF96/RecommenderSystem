'''
Created on 27 mar. 2020

@author: Amalio
'''
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
    query = "MATCH (c1:cliente)where c1.id<>'1715' return c1.id as id limit 25"
    data = pd.DataFrame(myConect.consultar(query), columns=['id'])
    return data

def getArticulos():
    query = "MATCH (a:articulo) return a.id as id limit 25"
    data = pd.DataFrame(myConect.consultar(query), columns=['id'])
    return data

def getFamilias():
    query = "match (a:articulo) return distinct(a.familia_id) as familia"
    data = pd.DataFrame(myConect.consultar(query), columns=['familia'])
    return data

def getClientesFamilia():
    query="MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) where c1.id<>'1715' return c1.id as cliente,a.familia_id as familia, count(a.familia_id) as similitud order by cliente desc"
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'familia', 'similitud'])
    return data

def getGastoClientesFamilia():
    query="MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) where c1.id<>'1715' return c1.id as cliente,a.familia_id as familia, sum(toFloat(a.precio_con_iva)) as similitud order by cliente desc"
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'familia', 'similitud'])
    return data



#1# - Recogemos datos        
clientes = sum(getClientes().values.tolist(), [])
familias = sum(getFamilias().values.tolist(), [])
#2# - Formamos Matriz")        
dfObj = pd.DataFrame(columns=familias, index=clientes)

print(dfObj)
#3# - Recogemos getFacturasFamilia     
cliXfam = getGastoClientesFamilia()
print(cliXfam)
#4# - Recorremos matriz dfObj     
for indexI,i in enumerate(cliXfam['cliente']):
    x = cliXfam.loc[indexI, 'cliente']
    y = cliXfam.loc[indexI, 'familia']
    z = cliXfam.loc[indexI, 'similitud']
    dfObj._set_value(x, y, z )


#5# - Guardamos en el csv
print(dfObj)
dfObj.to_csv( "dataGastoClienteFamilia.csv", index=True)
myConect.close()
