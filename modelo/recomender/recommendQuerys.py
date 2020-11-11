'''
Created on 9 nov. 2020

@author: Amalio
'''
from modelo.persistencia.bbdd.Connection import Connection as myConect
import numpy as np
import pandas as pd

class Recomendations(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def descubrirArticulos(self,idCliente,l):
        query='MATCH (c1:cliente)-[r:SIMILARIDAD]-(a:articulo)\
                WHERE r.similitud>0.1 AND c1.id={idCli}\
                    MATCH p=(c1)-[s:DISTANCIA]-(c2:cliente)-[r2:SIMILARIDAD]-(a2:articulo) \
                        WHERE c2<>c1 AND r2.similitud > -0.1 AND c2.id<>"1076" AND a<>a2\
                            RETURN a2.descripcion AS articuloR, SUM(s.euclideanDistance) as indicesDeSimilitud, \
                            SUM(s.euclideanDistance*r2.similitud) AS calificacionesPonderadas \
                            ORDER BY calificacionesPonderadas DESC Limit {limit}'.format(idCli=repr(idCliente), limit=l)
        
        data = pd.DataFrame(myConect.consultar(query), columns=['articuloR', 'indicesDeSimilitud', 'calificacionesPonderadas'])
        
        return data