'''
Created on 16 oct. 2020

@author: Amalio
'''


from recomendaciones import ClientesFamiliaPorSemana as cfs
from clustering import medirDistanciasEuclideasCluster as toCluster

from modelo.utils import Constantes as CONS

import pandas as pd
import numpy as np
import os.path as path
import os


# Constantes



def extraerDatosClientes(fechaStart=CONS.MIN_DATE,fechaEnd=CONS.MAX_DATE):
    
    dfObj = cfs.prepareDataToCluster(fechaStart,fechaEnd)
    resultado = dfObj.to_csv("./files/similarityMatrix/28Octubre/dataClienteFamiliaSimple.csv", index=True)
    
    return resultado != None

def leerClustersYFormatearlos(clusterDirectory=CONS.CLUSTER_DIRECTORY):
    
    porcentaje=0;
    numFiles=5;
    
    if path.exists(clusterDirectory):
        
        clustersCSV = [archivo for archivo in os.listdir(clusterDirectory) if archivo.endswith(".csv")]
            
        for file in clustersCSV:
                
            print("Analizando:",file,"\tCompletado al: ",porcentaje,"%\n")
            #toCluster.medirDistanciaEntreClientes(file)
            porcentaje=porcentaje+100/numFiles;
                
        
        print("Completado al: ",porcentaje,"%\n")
    return 0
    
if __name__ == '__main__':
    print("Elija una opcion")
    print("1. Extraer de Neo4j los datos de 1 semana para clusterizarlos.")
    print("2. Leer los clusters y transformarlos a un formato correcto para Neo4j.")
    x = 2#input("Introduzca la opcion: ")
    
    
    switcher = {
        1:extraerDatosClientes,
        2:leerClustersYFormatearlos(),
        #3: None,
        #4: None
    }
    
    ''' Definimos el argumento que se le pasara a la funcion '''
    argument=""    
    # Get the function from switcher dictionary
    functionRequested = switcher.get(argument, 0)
    # Execute the function
    functionRequested
    
def twelve():
    return "December"
 
