'''
Created on 17 oct. 2020

@author: Amalio

Mediante esta clase obtenemos una matriz como la siguiente:

                Familia 1    Familia 2    Familia 3     . . .     Familia n
                
Cliente 1            0            1            1

Cliente 2            1            0            1

Cliente 3            1            1            1
    
    .
    .
    .

Cliente n

Donde 0 representa que un cliente i no ha comprado ningun articulo de una familia y 1 significa lo opuesto.
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection
from modelo.persistencia.ArticuloDAO import ArticuloDAO
from modelo.persistencia.ClienteDAO import ClienteDAO


def prepareDataToCluster(myConect):
    # Variables
    clientesDAO = ClienteDAO(myConect)
    articulosDAO = ArticuloDAO(myConect)
    
    minDay = 1;
    maxDay = 1
    
    # 1# - Recogemos datos  
    clientesPrimeraSemana = clientesDAO.getClientesPorSemana(minDay, maxDay)
    familiasPrimeraSemana = articulosDAO.getFamiliasPorSemana(minDay, maxDay)

    # 2# - Pasamos los datos a lista
    clientes = sum(clientesPrimeraSemana.values.tolist(), [])
    familias = sum(familiasPrimeraSemana.values.tolist(), [])
    
    # 3# - Formamos Matriz        
    dfObj = pd.DataFrame(0, columns=familias, index=clientes)  # Usamos el numero de clientes(filas) y el numero de familias(columnas) para formar la matriz
    
    # 4# - Obtener el contenido de dfObj
    # clienteXfamilia=clientesDAO.getComprasPorCliente(minDay,maxDay)
    comprasFamiliaPrimeraSemana = articulosDAO.getComprasFamiliaPorSemana(minDay, maxDay)
    print("\n### comprasPrimeraSemana ###\n", comprasFamiliaPrimeraSemana, "###\n")
    # print("\n### clienteXarticulo ###\n",clienteXfamilia,"###\n")
    
    # 5# - Rellenamos la matriz dfObj     
    for indexI, i in enumerate(comprasFamiliaPrimeraSemana['cliente']):
        
        cliente = comprasFamiliaPrimeraSemana.loc[indexI, 'cliente']
        familia = comprasFamiliaPrimeraSemana.loc[indexI, 'familia']
        seHaComprado = comprasFamiliaPrimeraSemana.loc[indexI, 'compras']
        #
        '''aux=comprasFamiliaPrimeraSemana.loc[comprasFamiliaPrimeraSemana['familia'] == familia, ['compras']]
        comprasTotales=aux.iloc[0].loc["compras"]
        #
        x=comprasCliente/comprasTotales'''
        
        dfObj.loc[cliente][familia] = seHaComprado
    
        if indexI % 1000 == 0:
            print("Iteracion: ", indexI, "\tCliente: ", cliente, '\tArticulo: ', familia, '\tcomprasCliente: ', seHaComprado)
    
    print(dfObj)
    
    # 6# - Guardamos en el csv
    return dfObj
    
