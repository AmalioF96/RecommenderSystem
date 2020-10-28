'''
Created on 16 oct. 2020

@author: Amalio
'''
from modelo.persistencia.bbdd.Connection import Connection as myConect

import pandas as pd
import numpy as np

import datetime


class ClienteDAO(object):
    '''
    classdocs
    '''
    myConect = None;

    def __init__(self):
        '''
        Constructor
        '''
    
    def getClientesPorSemanaConFecha(self, fechaI="01/07/2018", fechaE="01/07/2018"):
    
        # para cuando lo hagamos semanalmente
        # cogemos la fecha de hoy
        # now = datetime.now()
        
        # cogemos la fecha en string y la pasamos a datetime
        
        start_date = datetime.datetime.strptime(fechaI, "%d/%m/%Y %H:%M:%S")
        # le sumamos 7 dias a la fecha para hacer 1 semana
        end_date = start_date + datetime.timedelta(days=7)
        # lo pasamos a cadena 
        dateEnd = end_date.strftime("%d/%m/%Y %H:%M:%S")
        
    def getComprasPorCliente(self, minDay=1, maxDay=7):
        '''
        '''
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND r.fecha >= datetime({min}) AND r.fecha <= datetime({max}) return c.id as cliente, a.id_interno as articulo, count(a) as compras order by cliente, articulo".format(min=minDay, max=maxDay)
        data = pd.DataFrame(myConect.consultar(query), columns=['cliente', 'articulo', 'compras'])
        return data
    
    def getClientesPorSemana(self, minDay, maxDay):

        # El menor dia es 1 y el mayor 31
    
        query = "match (c:cliente)-[r:COMPRA]-(f:factura) WHERE c.id<>'1715' AND r.fecha >= datetime({min}) AND r.fecha <= datetime({max}) return DISTINCT(c.id) AS cliente order by cliente".format(min=minDay, max=maxDay)
        
        data = pd.DataFrame(myConect.consultar(query), columns=['cliente'])
        return data
    
    
    def setDistanciaEuclidea(self,clientes,minDay,maxDay):
        '''
            Mediante esta consulta calculamos la distancia euclidea entre un conjunto de
            clientes, segun las compras que han realizado en un periodo de tiempo determinado
        '''
        
        query="MATCH p=(c1:cliente)-[r00:COMPRA]-(:factura)-[r01:CONTIENE]-(a:articulo)-[r11:CONTIENE]-(:factura)-[r10:COMPRA]-(c2:cliente) \
                WHERE \
                    r00.fecha >= datetime({min}) \
                        AND r00.fecha <= datetime({max}) \
                        AND r10.fecha >= datetime({min}) \
                        AND r10.fecha <= datetime({max}) \
                        AND c1.id IN {clientes} \
                        AND c2.id IN {clientes} \
                        AND c1<>c2 \
                WITH c1, c2 , a.id_interno AS arti, COUNT(DISTINCT(r01)) AS w1, COUNT(DISTINCT(r11)) AS w2    \
                WITH c1,c2, gds.alpha.similarity.euclideanDistance(COLLECT(w1),COLLECT(w2)) AS euDis          \
                MERGE (c1)<-[nr:DISTANCIA]->(c2) SET nr.euclideanDistance=euDis".format(clientes=[str(c) for c in clientes],min=repr(minDay), max=repr(maxDay))
        
        
        myConect.consultar(query)

    def gastoMedio(self, listaClientes):
        '''En base a una lista de clientes obtenemos su gasto medio, es decir, el gasto medio de un cluster'''
        query = "MATCH (c:cliente)-[:COMPRA]->(f:factura)-[:CONTIENE]->(a:articulo) where toInt(c.id) IN " + listaClientes + " return sum(toFloat(f.total))/count(f) as gastoMedio"
        data = pd.DataFrame(myConect.consultar(query), columns=['gastoMedio'])