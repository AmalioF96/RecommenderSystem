import pandas as pd
import numpy as np

factura_cabecera = pd.read_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/factura_cabecera_julio-2018.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode', encoding="latin_1");

facturaC = factura_cabecera[["ID","CASO_ID","TOTAL","ESTADO"]]

rFCC = factura_cabecera[["ID","ID_CLIENTE","FECHA"]];

dt = pd.DataFrame(facturaC);
dt.to_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/fCabecera.csv",index = False);

#dt = pd.DataFrame(rFCC);
#dt.to_csv("C:/Users/pc1/Documents/UNIVERSIDAD/Tablas MIGUEL/rFCC.csv",index = False);