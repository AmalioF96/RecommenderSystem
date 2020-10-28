'''
Created on 27 oct. 2020

@author: Amalio
'''

#Fechas
MIN_DATE=repr("2018-07-01")
MAX_DATE=repr("2018-07-07")


########### Rutas Ficheros ###########
    # Clusters #

#Conexion NEO4J
'''De momento estas se encuentran en uso en Connection, ya que es un singleton y siempre debe haber una instancia de la clase'''
URL = 'bolt://localhost:11005'
USER = 'neo4j'
PASSWORD = '123'