import pandas as pd
import numpy as np

# Tratamiento de datos sobre Articulos
articulos = pd.read_csv("../files/originales/articulos.csv", sep=',', error_bad_lines=False, index_col = False , dtype='unicode', encoding="latin_1");

#articulos = articulos.drop(['Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48'],axis = 1);
articulos.drop_duplicates(subset="id", inplace = True);
articulos = articulos.dropna(subset=['fecha_act_precio']);
articulos["descripcion"] = articulos["descripcion"].str.strip();

# Matrix de indices de los articulos ( Para trabajar con factura detalle)

mIndicesArticulos = np.array(articulos["id"]);
print('2255' in mIndicesArticulos);
# Tratamiento de datos sobre Factura Detalle

factura_detalle = pd.read_csv("../files/originales/factura_detalle_julio-2018.csv", sep=',', error_bad_lines=False, index_col= False, dtype='unicode', encoding="latin_1");

mFacturaDetalle = np.array(factura_detalle);
mFacturaDetalleDef = np.array([]);
c = 0;

print(mIndicesArticulos)

for i in range(len(mFacturaDetalle)):
    if not mFacturaDetalle[i][1] in mIndicesArticulos:
        print(mFacturaDetalle[i][1]);
        mFacturaDetalle = np.delete(mFacturaDetalle,i,axis = 0);
        i = i - 1;
    if i % 1000 == 0:
        print("Esto es i ", i);
        print("----------------");

print("Fin");
dt = pd.DataFrame(mIndicesArticulos);
dt.to_csv("../files/procesados/mIndicesArticulos3.csv",index = False);

df = pd.DataFrame(mFacturaDetalle);
df.to_csv("../files/procesados/mFacturaDetalle3.csv",index = False);

