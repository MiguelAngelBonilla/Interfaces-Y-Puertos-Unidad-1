import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E_01_areaRectangulo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_resultado.clicked.connect(self.calcularArea)

    # Área de los Slots
    def calcularArea(self):
        Altura = float(self.txt_Altura.text())
        Base = float(self.txt_Base.text())
        r = Altura + Base
        QMessageBox.information(self, 'Resultado', f'Area Del Rectangulo: {r}')





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


