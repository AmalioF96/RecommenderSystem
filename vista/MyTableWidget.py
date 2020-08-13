from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QPushButton, QTableWidget, QLabel, QLineEdit, QGridLayout, \
    QHBoxLayout, QTableWidgetItem

from Controlador.ControladorApp import ControladorApp


class MyTableWidget(QWidget):

    def __init__(self, parent):
        # Crear conexion con bbdd
        ControladorApp.crearConexion(self)

        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabInfo = QWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(1000, 512)

        # Add tabs
        self.tabs.addTab(self.tabInfo, "Info")
        self.tabs.addTab(self.tab1, "Query 1")
        self.tabs.addTab(self.tab2, "Query 2")
        self.tabs.addTab(self.tab3, "Query 3")
        self.tabs.addTab(self.tab4, "Query 4")

        # Create the info tabs
        # Cambiar por metodo
        self.tabInfo.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tabInfo.layout.addWidget(self.pushButton1)
        self.tabInfo.setLayout(self.tabInfo.layout)

        # Sacar etiquetas
        self.keys = ControladorApp.sacarKeys(self)

        # Create the query 1 tabs
        self.query1(self.keys[0])
        self.query2(self.keys[1])
        self.query3(self.keys[2])
        self.query4(self.keys[3])

        self.tab1.setLayout(self.tab1.layout)
        self.tab2.setLayout(self.tab2.layout)
        self.tab3.setLayout(self.tab3.layout)
        self.tab4.setLayout(self.tab4.layout)
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def query1(self, keys):
        self.table1 = QTableWidget(0, len(keys[0][0]))

        # predefinir con las keys devueltas en la consulta

        print(keys[0][0])

        self.table1.setHorizontalHeaderLabels(keys[0][0])

        self.table1.setAlternatingRowColors(True)

        self.table1.setEditTriggers(QTableWidget.NoEditTriggers)

        self.table1.setSelectionBehavior(QTableWidget.SelectRows)

        self.table1.setSelectionMode(QTableWidget.SingleSelection)

        self.lblID = QLabel("ID:")

        self.txtID = QLineEdit()

        self.txtID.setPlaceholderText("Numero identificador unico")

        grid = QGridLayout()

        grid.addWidget(self.lblID, 0, 0)

        grid.addWidget(self.txtID, 0, 1)

        btnCargar = QPushButton('Cargar Datos')

        btnCargar.clicked.connect(self.cargarDatosQuery1)

        hbx = QHBoxLayout()

        hbx.addWidget(btnCargar)

        self.tab1.layout = QVBoxLayout()

        self.tab1.layout.addLayout(grid)

        self.tab1.layout.addLayout(hbx)

        self.tab1.layout.setAlignment(Qt.AlignTop)

        self.tab1.layout.addWidget(self.table1)

    def query2(self, keys):
        self.table2 = QTableWidget(0, len(keys[0][0]))

        # predefinir con las keys devueltas en la consulta

        print(keys[0][0])

        self.table2.setHorizontalHeaderLabels(keys[0][0])

        self.table2.setAlternatingRowColors(True)

        self.table2.setEditTriggers(QTableWidget.NoEditTriggers)

        self.table2.setSelectionBehavior(QTableWidget.SelectRows)

        self.table2.setSelectionMode(QTableWidget.SingleSelection)

        self.lblID_Interno = QLabel("ID_INTERNO:")

        self.txtID_Interno = QLineEdit()

        self.txtID_Interno.setPlaceholderText("Numero identificador unico")

        grid = QGridLayout()

        grid.addWidget(self.lblID_Interno, 0, 0)

        grid.addWidget(self.txtID_Interno, 0, 1)

        btnCargar = QPushButton('Cargar Datos')

        btnCargar.clicked.connect(self.cargarDatosQuery2)

        hbx = QHBoxLayout()

        hbx.addWidget(btnCargar)

        self.tab2.layout = QVBoxLayout()

        self.tab2.layout.addLayout(grid)

        self.tab2.layout.addLayout(hbx)

        self.tab2.layout.setAlignment(Qt.AlignTop)

        self.tab2.layout.addWidget(self.table2)

    def query3(self, keys):
        self.table3 = QTableWidget(0, len(keys[0][0]))

        # predefinir con las keys devueltas en la consulta

        self.table3.setHorizontalHeaderLabels(keys[0][0])

        self.table3.setAlternatingRowColors(True)

        self.table3.setEditTriggers(QTableWidget.NoEditTriggers)

        self.table3.setSelectionBehavior(QTableWidget.SelectRows)

        self.table3.setSelectionMode(QTableWidget.SingleSelection)

        btnCargar = QPushButton('Cargar Datos')

        btnCargar.clicked.connect(self.cargarDatosQuery3)

        hbx = QHBoxLayout()

        hbx.addWidget(btnCargar)

        self.tab3.layout = QVBoxLayout()

        self.tab3.layout.addLayout(hbx)

        self.tab3.layout.setAlignment(Qt.AlignTop)

        self.tab3.layout.addWidget(self.table3)

    def query4(self, keys):
        self.table4 = QTableWidget(0, len(keys[0][0]))

        # predefinir con las keys devueltas en la consulta

        self.table4.setHorizontalHeaderLabels(keys[0][0])

        self.table4.setAlternatingRowColors(True)

        self.table4.setEditTriggers(QTableWidget.NoEditTriggers)

        self.table4.setSelectionBehavior(QTableWidget.SelectRows)

        self.table4.setSelectionMode(QTableWidget.SingleSelection)

        btnCargar = QPushButton('Cargar Datos')

        btnCargar.clicked.connect(self.cargarDatosQuery4)

        hbx = QHBoxLayout()

        hbx.addWidget(btnCargar)

        self.tab4.layout = QVBoxLayout()

        self.tab4.layout.addLayout(hbx)

        self.tab4.layout.setAlignment(Qt.AlignTop)

        self.tab4.layout.addWidget(self.table4)

    def cargarDatosQuery1(self, event):
        print(self.keys)
        datos = ControladorApp.cargarDatosQuery1(self)
        self.rellenarTablaQuery1(datos,self.keys[0][0][0])# Hay que mejorar el tratamiento de los Record

    def cargarDatosQuery2(self, event):
        datos = ControladorApp.cargarDatosQuery2(self)
        self.rellenarTablaQuery2(datos, self.keys[1][0][0])  # Hay que mejorar el tratamiento de los Record

    def cargarDatosQuery3(self, event):
        print("hola")
        # Esta echo solo falta la consulta
        # datos = ControladorApp.cargarDatosQuery3(self)
        # self.rellenarTablaQuery3(datos,self.keys[2][0][0])  # Hay que mejorar el tratamiento de los Record

    def cargarDatosQuery4(self, event):
        print("hola")
        # Esta echo solo falta la consulta
        # datos = ControladorApp.cargarDatosQuery4(self)
        # self.rellenarTablaQuery4(datos,self.keys[3][0][0])  # Hay que mejorar el tratamiento de los Record

    # HAY QUE DESCUBRIR COMO HACER PARA LLAMAR A LOS SELF.TABLE 1 2 3 4 CON UN FOR PARA HACER UN CODIGO TODO CONJUNTO!!!

    def rellenarTablaQuery1(self, datos,keys):
        i = 0
        self.table1.setRowCount(i + 1)  # Para saltar a la siguiente fila
        for key in keys:
            self.table1.setItem(0, i, QTableWidgetItem(datos[key]))
            i += 1

    def rellenarTablaQuery2(self, datos , keys):
        keys = datos.keys()
        self.table2.setHorizontalHeaderLabels(keys)
        print("pe")
        i = 0
        for key in keys:
            #self.table2.setRowCount(i + 1)  # Para saltar a la siguiente fila
            self.table2.setItem(i, 0, QTableWidgetItem(datos[key]))
            i += 1

    def rellenarTablaQuery3(self, datos,keys):

        i = 0
        for key in keys:
            self.table3.setRowCount(i + 1)  # Para saltar a la siguiente fila
            self.table3.setItem(0, i, QTableWidgetItem(datos[key]))
            i += 1

    def rellenarTablaQuery4(self, datos,keys):

        i = 0
        for key in keys:
            self.table4.setRowCount(i + 1)  # Para saltar a la siguiente fila
            self.table4.setItem(0, i, QTableWidgetItem(datos[key]))
            i += 1



