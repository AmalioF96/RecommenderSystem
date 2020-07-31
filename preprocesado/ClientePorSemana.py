'''
Created on 30 jul. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection

import datetime
from mock.mock import inplace
# Constantes
URL = 'bolt://localhost:11005'
USER = 'neo4j'
PASSWORD = '123'
myConect = Connection(URL, USER, PASSWORD)


def getClientesPorSemanaConFecha(fecha="01/07/2018"):
    
    # para cuando lo hagamos semanalmente
    # cogemos la fecha de hoy
    # now = datetime.now()
    
    # cogemos la fecha en string y la pasamos a datetime
    
    start_date = datetime.datetime.strptime(fecha, "%d/%m/%Y %H:%M:%S")
    # le sumamos 7 dias a la fecha para hacer 1 semana
    end_date = start_date + datetime.timedelta(days=7)
    # lo pasamos a cadena 
    dateEnd = end_date.strftime("%d/%m/%Y %H:%M:%S")
    
def getClientesPorSemana(minDay,maxDay):
    '''
    El menor dia es 1 y el mayor 31
    '''
    query = "match (c:cliente)-[r:COMPRA]-(f:factura) WHERE c.id<>'1715' AND toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return DISTINCT(c.id) AS cliente order by cliente".format(min=minDay,max=maxDay)
    
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente'])
    return data

def getArticulosPorSemana(minDay,maxDay):
    '''
    El menor dia es 1 y el mayor 31
    '''
    query="match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return DISTINCT(a.descripcion) as articulo".format(min=minDay,max=maxDay)
    data = pd.DataFrame(myConect.consultar(query), columns=['articulo'])
    return data

def getComprasPorCliente(minDay,maxDay):
    '''
    '''
    query="match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return c.id as cliente, a.descripcion as articulo, count(a) as compras".format(min=minDay,max=maxDay)
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente','articulo','compras'])
    return data

dayMin=1;
dayMax=7

#1# - Recogemos datos  
clientesPrimeraSemana=getClientesPorSemana(dayMin, dayMax)
articulosPrimeraSemana=getArticulosPorSemana(dayMin,dayMax)

#2# - Pasamos los datos a lista
clientes = sum(clientesPrimeraSemana.values.tolist(), [])
articulos = sum(articulosPrimeraSemana.values.tolist(), [])

#3# - Formamos Matriz        
dfObj = pd.DataFrame(columns=articulos, index=clientes) #Usamos el numero de clientes(filas) y el numero de familias(columnas) para formar la matriz

#4# - Obtener el contenido de dfObj
clienteXarticulo=getComprasPorCliente(dayMin,dayMax)

#5# - Rellenamos la matriz dfObj     
for indexI,i in enumerate(clienteXarticulo['cliente']):
    dfObj.loc[clienteXarticulo.loc[indexI,'cliente']][clienteXarticulo.loc[indexI,'articulo']] =  clienteXarticulo.loc[indexI,'compras']


print(dfObj)

#6# - Guardamos en el csv

dfObj.to_csv( "../files/similarityMatrix/dataClienteArticuloSimple.csv", index=True)
myConect.close()


