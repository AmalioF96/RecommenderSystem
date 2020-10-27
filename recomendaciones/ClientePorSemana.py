'''
Created on 30 jul. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection
from modelo.persistencia.ArticuloDAO import ArticuloDAO
from modelo.persistencia.ClienteDAO import ClienteDAO

import datetime


def prepareDataToCluster(myConect):
    #Variables
    articulosDAO=ArticuloDAO(myConect)
    clientesDAO=ClienteDAO(myConect)
    
    dayMin=1;
    dayMax=1
    
    #1# - Recogemos datos  
    clientesPrimeraSemana=articulosDAO.getArticulosPorSemana(dayMin, dayMax)
    articulosPrimeraSemana=clientesDAO.getClientesPorSemanaConFecha()

    #2# - Pasamos los datos a lista
    clientes = sum(clientesPrimeraSemana.values.tolist(), [])
    articulos = sum(articulosPrimeraSemana.values.tolist(), [])
    
    #3# - Formamos Matriz        
    dfObj = pd.DataFrame(columns=articulos, index=clientes) #Usamos el numero de clientes(filas) y el numero de familias(columnas) para formar la matriz
    
    #4# - Obtener el contenido de dfObj
    clienteXarticulo=clientes.getComprasPorCliente(dayMin,dayMax)
    comprasPrimeraSemana=articulosDAO.getComprasArticulosPorSemana(dayMin, dayMax)
    print("\n### comprasPrimeraSemana ###\n",comprasPrimeraSemana,"###\n")
    print("\n### clienteXarticulo ###\n",clienteXarticulo,"###\n")
    
    
    
    
    #5# - Rellenamos la matriz dfObj     
    for indexI,i in enumerate(clienteXarticulo['cliente']):
        
        
        cliente=clienteXarticulo.loc[indexI,'cliente']
        articulo=clienteXarticulo.loc[indexI,'articulo']
        comprasCliente=clienteXarticulo.loc[indexI,'compras']
        #
        aux=comprasPrimeraSemana.loc[comprasPrimeraSemana['articulo'] == articulo, ['compras']]
        comprasTotales=aux.iloc[0].loc["compras"]
        #
        x=comprasCliente/comprasTotales
        
        dfObj.loc[cliente][articulo] = x
    
        if indexI%1000==0:
            print("Iteracion: ",indexI,"\tCliente: ",cliente,'\tArticulo: ',articulo,'\tcomprasCliente: ',comprasCliente, "\tComprasTotales: ",comprasTotales, "\t X: ",x)
        
    
    print(dfObj)
    
    #6# - Guardamos en el csv
    
    dfObj.to_csv( "../files/similarityMatrix/dataClienteArticuloSimple.csv", index=True)

    
   




