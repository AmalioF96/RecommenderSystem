'''
Created on 4 mar. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection

#Constantes
URL = 'bolt://localhost:11005'
USER = 'neo4j'
PASSWORD = '123'

clientes = pd.read_csv("../files/clientes.csv",sep=",",quotechar='"',encoding="utf8",usecols=['ID'])
facturas = pd.read_csv("../files/facturas.csv",sep=",",quotechar='"',encoding="utf8",usecols=['ID','TOTAL'])
articulos = pd.read_csv("../files/articulos.csv",sep=",",quotechar='"',encoding="utf8",usecols=['ID','DESCRIPCION'])

print(clientes)