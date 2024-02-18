import sys
import math
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


qtCreatorFile = "E_03_distanciaEntre2Puntos.ui"  # Nombre del archivo aquí.
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


        distancia = ((punto_X2 - punto_X1)**2 + (punto_Y2 - punto_Y1)**2)**0.5
        redondeo = round(distancia, 2)
        QMessageBox.information(self, 'Resultado', f'La distancia Entre Dos Puntos: {redondeo}')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


