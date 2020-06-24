'''
Created on 14 mar. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection
# Constantes
URL = 'bolt://localhost:11005'
USER = 'neo4j'
PASSWORD = '1234'
myConect = Connection(URL, USER, PASSWORD)


def getClientes():
    query = "MATCH (c1:cliente)where c1.id<>'1715' return c1.id as id"
    data = pd.DataFrame(myConect.consultar(query), columns=['id'])
    return data


def getFacturas():
    query = "MATCH (f:factura) return f.id as id"
    data = pd.DataFrame(myConect.consultar(query), columns=['id'])
    return data


def getFamilias():
    query = "match (a:articulo) return distinct(a.familia_id) as familia"
    data = pd.DataFrame(myConect.consultar(query), columns=['familia'])
    return data
    
    
def getFacturasFamilia():
    query = "MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo)where c1.id<>'1075' return f1.id as fac1 , a.familia_id as familia, count(a) as similitud order by fac1"
    data = pd.DataFrame(myConect.consultar(query), columns=['fac', 'familia', 'similitud'])
    return data

def getClientesFamilia():
    query="MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) where c1.id<>'1715' return c1.id as cliente,a.familia_id as familia, count(a.familia_id) as similitud order by cliente desc"
    data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'familia', 'similitud'])
    return data

def getArticulos():
    query = "MATCH (a:articulo) return a.id as id limit 25"
    data = pd.DataFrame(myConect.consultar(query), columns=['id'])
    return data

    
def getSimilitudFacturasCliente(id):
    query = "MATCH (c1:cliente {id:'" + id + "'})-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo)<-[rb2:CONTIENE]-(f2:factura)<-[rb1:COMPRA]-(c1:cliente {id:'" + id + "'}) where f1.id<f2.id return f1.id as fac1, f2.id as fac2,count(a) as similitud order by similitud"
    data = pd.DataFrame(myConect.consultar(query), columns=['fac1', 'fac2' , 'similitud'])
    x = np.argmax(np.array(data['similitud']))
    data = data[data.index >= x]  # Nos quedamos con los que tienen mejor similitud
    
    # data.to_csv('../files/similarity.csv', ';', index=False, columns=['fac1', 'fac2' ,'similitud'])
    return data


def getFitnessCliente(id, lista):
    query = "MATCH (c1:cliente {id:'" + id + "'})-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) where f1.id IN " + lista + " return a.id as articulo,sum(toFloat(ra2.cantidad)) as cantidad ,count(f1) as numFacturas,sum(toFloat(ra2.cantidad))*(toFloat(count(f1))/10) as fitness order by fitness desc"
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['articulo', 'cantidad' , 'numFacturas', 'fitness'])
    return data


def getFitnessClienteSinLista(id):
    query = "MATCH (c1:cliente {id:'" + id + "'})-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) return a.id as articulo,sum(toFloat(ra2.cantidad)) as cantidad ,count(f1) as numFacturas,sum(toFloat(ra2.cantidad))*(toFloat(count(f1))/10) as fitness order by fitness desc"
    print(query)
    data = pd.DataFrame(myConect.consultar(query), columns=['articulo', 'cantidad' , 'numFacturas', 'fitness'])
    return data


def getSimilitudesClientesT3():
    listaClientes = getClientes().values.tolist();
    listaArticulos = getArticulos().values.tolist();
    
    print(listaClientes)
    print(listaArticulos)
    
    array = pd.DataFrame(listaClientes, columns=[listaArticulos]);
    '''
    for cliente in listaClientes.iterrows():
        for articulo in listaArticulos.iterrows():
            array[cliente['id']][articulo['id']]=-1
    '''    
    print((array))
    query = "MATCH (c1:cliente)-[ra1:COMPRA]->(f1:factura)-[ra2:CONTIENE]->(a:articulo) return c1.id as cliente, a.id as articulo ,sum(toFloat(ra2.cantidad))*(toFloat(count(f1))/10) as fitness order by cliente desc"          

        
def init():
    clientes = getClientes()
    for index, row in clientes.iterrows():
        idCliente = row['id']
        similitudes = getSimilitudFacturasCliente(idCliente)
        lista = [];
        for index, row in similitudes.iterrows():
            if(str(row['fac1'])not in lista):
                lista.append(str(row['fac1']))
            if(str(row['fac2'])not in lista):
                lista.append(str(row['fac2']))
       
        fitness = getFitnessCliente(idCliente, str(lista))
# data=pd.read_csv("../files/similarity.csv",sep=";",quotechar='"',encoding="utf8",usecols=['fac1','fac2','similitud'])

'''
similitudes = getSimilitudFacturasCliente('78625')
print(similitudes);
print()
print("##################################")
lista = []
for index, row in similitudes.iterrows():
            if(str(row['fac1'])not in lista):
                lista.append(str(row['fac1']))
            if(str(row['fac2'])not in lista):
                lista.append(str(row['fac2']))
                
data = getFitnessClienteSinLista('78625')
print(data)
# init()
'''

#1# - Recogemos datos        
clientes = sum(getClientes().values.tolist(), [])
familias = sum(getFamilias().values.tolist(), [])
#2# - Formamos Matriz")        
dfObj = pd.DataFrame(columns=familias, index=clientes)

print(dfObj)
#3# - Recogemos getFacturasFamilia     
cliXfam = getClientesFamilia()
print(cliXfam)
#4# - Recorremos matriz dfObj     
for indexI,i in enumerate(cliXfam['cliente']):
    dfObj.loc[cliXfam.loc[indexI,'cliente']][cliXfam.loc[indexI,'familia']] =  cliXfam.loc[indexI,'similitud']


#5# - Guardamos en el csv
#print(dfObj)
dfObj.to_csv( "../files/similarityMatrix/dataClienteFamilia.csv", index=True)
myConect.close()