'''
Created on 26 oct. 2020

@author: Amalio
'''
from modelo.persistencia.bbdd.Connection import Connection as myConect

import pandas as pd
import numpy as np
import datetime

class ComprasDAO(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def getComprasPeriodoDeListaClientes(self, clientes, minDay, maxDay):
        '''
        El menor dia es 1 y el mayor 31
        '''
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo)\
                        WHERE c.id in {listaClientes} and r.fecha >= datetime({min}) AND r.fecha <= datetime({max})\
                        return c.id as cliente, a.id_interno as articulo, count(a) as compras\
                        order by cliente, articulo".format(listaClientes=[str(c) for c in clientes],min=repr(minDay), max=repr(maxDay))
        print(query)
        data = pd.DataFrame(myConect.consultar(query), columns=['cliente','articulo', 'compras'])
        return data
    
    def obtenerComprasYGasto(self,listaClientes):
        """Este metodo nos devuelve elnumero de facturas asociadas a una lista de clientes y el gasto que suman"""
        query = "MATCH (c:cliente)-[:COMPRA]->(f:factura)-[r2:CONTIENE]->(a:articulo) where toInteger(c.id) IN " + listaClientes + " return sum(toFloat(f.total)) as cuantia, count(f) as compras"
        data = pd.DataFrame(myConect.consultar(query), columns=['cuantia', 'compras'])
        return data