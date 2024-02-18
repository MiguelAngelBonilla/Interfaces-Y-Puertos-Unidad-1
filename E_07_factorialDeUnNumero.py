import sys
import math
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


qtCreatorFile = "E_07_factorialDeUnNumero.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_resultado.clicked.connect(self.determinarNota)

    # Área de los Slots
    def determinarNota(self):
        n = int(self.txt_Num.text())
        fact = 1
        for y in range(1, n + 1):
            fact *= y
        QMessageBox.information(self, 'Resultado', f'El Factorial es: {fact}')








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


