'''
Created on 16 oct. 2020

@author: Amalio
'''

from modelo.persistencia.Connection import Connection
from recomendaciones import ClientesFamiliaPorSemana as cfs

import pandas as pd
import numpy as np

# Constantes
URL = 'bolt://localhost:11005'
USER = 'neo4j'
PASSWORD = '123'
myConect = Connection(URL, USER, PASSWORD)


def extraerDatosClientes(fecha="01-07-2018"):
    dfObj = cfs.prepareDataToCluster(myConect)
    dfObj.to_csv("./files/similarityMatrix/dataClienteFamiliaSimple.csv", index=True)

    return


if __name__ == '__main__':
    print("Elija una opcion")
    print("1. Extraer de Neo4j los datos de 1 semana para clusterizarlos.")
    print("2. Leer los clusters y transformarlos a un formato correcto para Neo4j.")
    x = input("Introduzca la opcion: ")
    
    extraerDatosClientes()

myConect.close()
