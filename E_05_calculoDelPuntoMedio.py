import sys
import math
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


qtCreatorFile = "E_05_calculoDelPuntoMedio.ui"  # Nombre del archivo aquí.
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


        distanciaX = (punto_X1 + punto_X2)/2
        distanciaY = (punto_Y1 + punto_Y2)/2
        QMessageBox.information(self, 'Resultado', f'Calculo Del Punto Medio Entre punto1 y punto2:' f'{distanciaX, distanciaY}')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


