#   Tendremos que mirar esto y comprender que es lo que importa
# import datetime
# from collections import Counter
# from sklearn.metrics.pairwise import cosine_similarity


# Leer archivos
import pandas as pd
import numpy as np
import datetime

# Importamos archivos
# articulos = pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/articulos.csv", dtype={"id": str})
articulos = pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/articulos.csv", sep=';', error_bad_lines=False, index_col = False , dtype='unicode', encoding="latin_1")
# clientes = pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/clientes_ID.csv", sep=';', error_bad_lines=False, index_col=False, dtype='unicode', encoding="latin_1")
# factura_cabecera = pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/factura_cabecera_julio-2018.csv", sep=';', error_bad_lines=False, index_col=False, dtype='unicode', encoding="latin_1")
factura_detalle = pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/factura_detalle_julio-2018.csv", sep=';', error_bad_lines=False, index_col='FACTURA_ID', dtype='unicode', encoding="latin_1")
# proveedores =  pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/proveedores.csv", sep=';', error_bad_lines=False, index_col=False, dtype='unicode', encoding="latin_1")

# Mostramos Datos
# print(articulos)

# Para eliminar Indices


articulos = articulos.drop(['Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48'],axis = 1)
print(list(articulos.columns))
print(articulos)
print("---------------------------------------------------------------------------")

articulos.drop_duplicates(subset="id", inplace = True)

print("---------------------------------------------------------------------------")
articulos = articulos.dropna(subset=['fecha_act_precio'])
print("---------------------------------------------------------------------------")

# print(articulos_atributos)
articulos["descripcion"].str.strip()
print("---------------------------------------------------------------------------")

# Cogemos factura detalle y recorremos para dejar limpio el csv.

pr = np.array(articulos["id"])

print(pr)
#factura_detalle = factura_detalle[factura_detalle.codigo != articulos]



print(factura_detalle)

articulos.to_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/cleanfileArticulos5.csv", encoding="utf-8")
#print(clientes)
