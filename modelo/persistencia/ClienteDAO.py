'''
Created on 16 oct. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection

import datetime


class ClienteDAO(object):
    '''
    classdocs
    '''
    myConect = None;

    def __init__(self, conect):
        '''
        Constructor
        '''
        self.myConect = conect
    
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
        query = "match (c:cliente)-[r:COMPRA]-(f:factura)-[r2:CONTIENE]-(a:articulo) WHERE c.id<>'1715' AND toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return c.id as cliente, a.id_interno as articulo, count(a) as compras".format(min=minDay, max=maxDay)
        data = pd.DataFrame(self.myConect.consultar(query), columns=['cliente', 'articulo', 'compras'])
        return data
    
    def getClientesPorSemana(self, minDay, maxDay):

        # El menor dia es 1 y el mayor 31
    
        query = "match (c:cliente)-[r:COMPRA]-(f:factura) WHERE c.id<>'1715' AND toInteger(substring(r.fecha,0,2))>={min} AND toInteger(substring(r.fecha,0,2))<={max} return DISTINCT(c.id) AS cliente order by cliente".format(min=minDay, max=maxDay)
        
        data = pd.DataFrame(self.myConect.consultar(query), columns=['cliente'])
        return data
    
    
