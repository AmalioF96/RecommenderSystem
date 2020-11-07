'''
Created on 16 oct. 2020

@author: Amalio
'''


#from recomendaciones import ClientesFamiliaPorSemana as cfs
from modelo.utils import Constantes as CONS
import pandas as pd
import numpy as np

# Constantes



def extraerDatosClientes(fechaStart=CONS.MIN_DATE,fechaEnd=CONS.MAX_DATE):
    
  #  dfObj = cfs.prepareDataToCluster(fechaStart,fechaEnd)
    
   # dfObj.to_csv("./files/similarityMatrix/28Octubre/dataClienteFamiliaSimple.csv", index=True)

    return


if __name__ == '__main__':
    print("Elija una opcion")
    print("1. Extraer de Neo4j los datos de 1 semana para clusterizarlos.")
    print("2. Leer los clusters y transformarlos a un formato correcto para Neo4j.")
    x = input("Introduzca la opcion: ")
    
    #extraerDatosClientes()


