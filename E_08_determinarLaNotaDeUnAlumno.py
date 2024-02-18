import sys
import math
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E_08_determinarLaNotaDeUnAlumno.ui"  # Nombre del archivo aquí.
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
        n = float(self.txt_Num.text())
        cal = ''
        if n == 10:
            cal = 'A'

        elif n >= 9:
            cal = 'B'
        elif n >= 8:
            cal = 'C'

        elif n >= 7:
            cal = 'D'

        elif n >= 6:
            cal = 'E'
        else:
            cal = 'F'

        QMessageBox.information(self, 'Resultado', f'Tu nota De acuerdo a tu calificacion es: {cal}')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


