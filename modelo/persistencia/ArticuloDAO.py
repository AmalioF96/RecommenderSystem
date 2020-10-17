'''
Created on 16 oct. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection

import datetime


class ArticuloDAO(object):
    '''
    classdocs
    '''
    myConect = None;

    def __init__(self, conect):
        '''
        Constructor
        '''
        self.myConect = conect
        
    def getArticulosPorSemana(self, minDay, maxDay):
        '''
        El menor dia es 1 y el mayor 31
        '''
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return DISTINCT(a.id_interno) as articulo".format(min=minDay, max=maxDay)
        data = pd.DataFrame(self.myConect.consultar(query), columns=['articulo'])
        return data
    
    def getFamiliasPorSemana(self, minDay, maxDay):
        '''
        El menor dia es 1 y el mayor 31
        '''
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return DISTINCT(a.familia_id) as familia".format(min=minDay, max=maxDay)
        data = pd.DataFrame(self.myConect.consultar(query), columns=['familia'])
        return data
    
    def getComprasArticulosPorSemana(self, minDay, maxDay):
        '''
        El menor dia es 1 y el mayor 31
        '''
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' and toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return a.id_interno as articulo, count(a) as compras order by articulo".format(min=minDay, max=maxDay)
        data = pd.DataFrame(self.myConect.consultar(query), columns=['articulo', 'compras'])
        return data

    def getComprasFamiliaPorSemana(self, minDay, maxDay):
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' and toInteger(substring(r.fecha,0,2))>=1 AND toInteger(substring(r.fecha,0,2))<=1 return c.id as cliente, a.familia_id as familia, CASE WHEN count(a)>0 THEN 1 ELSE 0 END as compras order by cliente, familia asc"
        data = pd.DataFrame(self.myConect.consultar(query), columns=['cliente', 'familia', 'compras'])
        return data
        
