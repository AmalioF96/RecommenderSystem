'''
Created on 16 oct. 2020

@author: Amalio
'''
from modelo.persistencia.bbdd.Connection import Connection as myConect
import pandas as pd
import numpy as np
import datetime


class ArticuloDAO(object):
    '''
    classdocs
    '''
    myConect = None;

    def __init__(self):
        '''
        Constructor
        '''
        
    def getArticulosPorSemana(self, minDay, maxDay):
        '''
        El menor dia es 1 y el mayor 31
        '''
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return DISTINCT(a.id_interno) as articulo".format(min=minDay, max=maxDay)
        data = pd.DataFrame(myConect.consultar(query), columns=['articulo'])
        return data
    
    def getFamiliasPorSemana(self, minDay, maxDay):
        '''
        El menor dia es 1 y el mayor 31
        '''
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND r.fecha >= datetime({min}) AND r.fecha <= datetime({max}) return DISTINCT(a.familia_id) as familia".format(min=minDay, max=maxDay)
        data = pd.DataFrame(myConect.consultar(query), columns=['familia'])
        return data
    
    def getComprasArticulosPorSemana(self, minDay, maxDay):
        '''
        El menor dia es 1 y el mayor 31
        '''
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' and r.fecha >= datetime({min}) AND r.fecha <= datetime({max}) return a.id_interno as articulo, count(a) as compras order by articulo".format(min=minDay, max=maxDay)
        data = pd.DataFrame(myConect.consultar(query), columns=['articulo', 'compras'])
        return data

    def getComprasFamiliaPorSemana(self, minDay, maxDay):
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND r.fecha >= datetime({min}) AND r.fecha <= datetime({max}) return c.id as cliente, a.familia_id as familia, CASE WHEN count(a)>0 THEN 1 ELSE 0 END as compras order by cliente, familia asc".format(min=minDay, max=maxDay)
        data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'familia', 'compras'])
        return data
    
    def familiasConMayorGastoMedio(self, listaClientes):
        '''En base a una lista de clientes que forman un cluster, obtenemos el gasto medio que tienen de cada familia.'''
        query = "MATCH (c:cliente)-[:COMPRA]->(f:factura)-[r2:CONTIENE]->(a:articulo) where toInt(c.id) IN " + listaClientes + " return a.familia_id as familia, sum(toFloat(replace(r2.cantidad,',','.'))*toFloat(a.precio_con_iva))/count(f) as gastoMedio order by gastoMedio desc Limit 20"
        data = pd.DataFrame(myConect.consultar(query), columns=['familia', 'gastoMedio'])
        return data   
