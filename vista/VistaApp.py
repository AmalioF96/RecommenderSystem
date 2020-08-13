import sys

from Controlador.ControladorApp import ControladorApp

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot

from Vista.MyTableWidget import MyTableWidget

ventana = "";


class App(QMainWindow):


    def __init__(self):
        # Creacion de la vista - Configuracion

        super().__init__()
        self.title = 'SR QUERY'
        self.left = 100
        self.top = 100
        self.width = 1280
        self.height = 720
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


@pyqtSlot()
def on_click(self):
    print("\n")
    for currentQTableWidgetItem in self.tableWidget.selectedItems():
        print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
