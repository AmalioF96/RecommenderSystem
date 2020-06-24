import sys

from PyQt5.QtWidgets import QApplication

from vista.VistaApp import App


class Main(object):

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())
