import sys




from PyQt5.QtSql import *

from PyQt5.QtCore import Qt, QModelIndex

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, \
    QPlainTextEdit, QTableWidgetItem, QMessageBox, QHBoxLayout, QGridLayout

from Modelo.Connection import HelloWorldExample
class Example(QWidget):

    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        # Crear conexion

        HelloWorldExample.__init__(self, 'bolt://localhost:11005' , 'neo4j' , '123')
        message = ""

        self.textAreaConsulta = QPlainTextEdit(self)
        self.textAreaConsulta.insertPlainText(HelloWorldExample.pintarAlgo(self))
        self.textAreaConsulta.move(10, 10)
        self.textAreaConsulta.resize(400, 200)


        # Creacion de text Area

        self.textArea = QPlainTextEdit(self)
        self.textArea.insertPlainText("You can write text here.\n")
        self.textArea.move(10, 10)
        self.textArea.resize(400, 200)

        # posicionamiento labels de introduzcion de datos

        grid = QGridLayout()

        grid.addWidget(self.textAreaConsulta)

        # Posicionamiento de los objetos dentro de la interfaz

        btnCargar = QPushButton('Cargar Datos')

        btnCargar.clicked.connect(self.cargarDatos)



        btnInsertar = QPushButton('Insertar')

        btnInsertar.clicked.connect(self.insertarDatos)



        btnEliminar = QPushButton('Eliminar')

        btnEliminar.clicked.connect(self.eliminarDatos)



        hbx = QHBoxLayout()

        hbx.addWidget(btnCargar)

        hbx.addWidget(btnInsertar)

        hbx.addWidget(btnEliminar)



        vbx = QVBoxLayout()

        vbx.addLayout(grid)

        vbx.addLayout(hbx)

        vbx.setAlignment(Qt.AlignTop)

        vbx.addWidget(self.textArea)



        self.setWindowTitle("PyQT :: SQLite Data Access")

        self.resize(362, 320)

        self.setLayout(vbx)



    def cargarDatos(self, event):

        index = 0

        query = QSqlQuery()

        query.exec_("select * from person")



        while query.next():

            ids = query.value(0)

            nombre = query.value(1)

            apellido = query.value(2)



            self.table.setRowCount(index + 1)

            self.table.setItem(index, 0, QTableWidgetItem(str(ids)))

            self.table.setItem(index, 1, QTableWidgetItem(nombre))

            self.table.setItem(index, 2, QTableWidgetItem(apellido))



            index += 1



    def insertarDatos(self, event):

        ids = int(self.txtID.text())

        nombre = self.txtName.text()

        apellido = self.txtApellido.text()



        query = QSqlQuery()

        query.exec_("insert into person values({0}, '{1}', '{2}')".format(ids, nombre, apellido))



    def eliminarDatos(self, event):

        selected = self.table.currentIndex()

        if not selected.isValid() or len(self.table.selectedItems()) < 1:

            return



        ids = self.table.selectedItems()[0]

        query = QSqlQuery()

        query.exec_("delete from person where id = " + ids.text())



        self.table.removeRow(selected.row())

        self.table.setCurrentIndex(QModelIndex())



    def db_connect(self, filename, server):

        db = QSqlDatabase.addDatabase(server)

        db.setDatabaseName(filename)

        if not db.open():

            QMessageBox.critical(None, "Cannot open database",

                    "Unable to establish a database connection.\n"

                    "This example needs SQLite support. Please read the Qt SQL "

                    "driver documentation for information how to build it.\n\n"

                    "Click Cancel to exit.", QMessageBox.Cancel)

            return False

        return True



    def db_create(self):

        query = QSqlQuery()

        query.exec_("create table person(id int primary key, "

                    "firstname varchar(20), lastname varchar(20))")

        query.exec_("insert into person values(101, 'Danny', 'Young')")

        query.exec_("insert into person values(102, 'Christine', 'Holand')")

        query.exec_("insert into person values(103, 'Lars', 'Gordon')")

        query.exec_("insert into person values(104, 'Roberto', 'Robitaille')")

        query.exec_("insert into person values(105, 'Maria', 'Papadopoulos')")



    def init(self, filename, server):

        import os

        if not os.path.exists(filename):

            self.db_connect(filename, server)

            self.db_create()

        else:

            self.db_connect(filename, server)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ejm = Example()

    ejm.init('datafile', 'QSQLITE')

    ejm.show()

    sys.exit(app.exec_())