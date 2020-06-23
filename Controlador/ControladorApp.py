from Modelo.Connection import Connection

# Variables Conexion

_URL = 'bolt://localhost:11005'
_USER = 'neo4j'
_PASSWORD = '123'

class ControladorApp(object):

    def cargarDatosQuery1(self):
        articulos = Connection.aMasCompradosC(self, str(self.txtID.text()))

        return articulos[0][0]._properties



    def cargarDatosQuery2(self):
        articulos = Connection.frecuenciaArticulo(self, str(self.txtID_Interno.text()))
        print("cargarDatosQuery2")
        print(articulos)
        return articulos[0][0]._properties

    def cargarDatosQuery3(self):
        return list()

    def cargarDatosQuery4(self):
        return list()

    def sacarKeys(self):
       return Connection.sacarKeys(self)

    def crearConexion(self):
        Connection.__init__(self , _URL , _USER , _PASSWORD)