import sys
import math
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


qtCreatorFile = "E_04_EcuacionDePrimerGrado.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_resultado.clicked.connect(self.calcularDEDP)

    # Área de los Slots
    def calcularDEDP(self):
        punto_X1 = float(self.txt_PuntoX1.text())
        punto_X2 = float(self.txt_PuntoX2.text())
        punto_Y1 = float(self.txt_PuntoY1.text())
        punto_Y2 = float(self.txt_PuntoY2.text())

        m = (punto_Y2 - punto_Y1) / (punto_X2 - punto_X1)
        x = punto_X2
        y = punto_Y2
        b = (m * x) - y
        bp = (b * -1)
        QMessageBox.information(self, 'Resultado', f'Despeje de la ecuacion de primer grado y = mx + b: Donde y = : {y}, m = {m}, x ={x}, b = {bp}'
                             )




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


