import pandas as pd
import numpy as np

factura_detalle = pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/factura_detalle_julio-2018.csv", sep=',', error_bad_lines=False, index_col= False, dtype='unicode', encoding="latin_1");

# Conseguimos eliminar todos los id Factura duplicados, quedandonos unicamente con un id Valido por cada Factura.
factura_detalle.drop_duplicates(subset="FACTURA_ID", inplace = True);

mFactura_Id = np.array(factura_detalle["FACTURA_ID"]);

# obtenemos el total de facturas

print(mFactura_Id)
print(len(mFactura_Id))
facturaCabecera = pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/factura_cabecera_julio-2018.csv", sep=',', error_bad_lines=False, index_col = False , dtype='unicode', encoding="latin_1");

mFacturaCabecera = np.array(facturaCabecera);

indice = len(mFacturaCabecera);

i = 0;

while(i < indice):
    if not mFacturaCabecera[i][0] in mFactura_Id:
        print(mFacturaCabecera[i][0]);
        mFacturaCabecera = np.delete(mFacturaCabecera,i,axis = 0);
        i = i - 1;
        indice = indice - 1;
    if i % 1000 == 0:
        print("Esto es i ", i);
        print("----------------");
    i = i + 1;

print("Fin");
dt = pd.DataFrame(mFacturaCabecera);
dt.to_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/mFacturaCabecera.csv",index = False);