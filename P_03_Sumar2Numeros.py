import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "P_03_Sumar2Numeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.txt_suma.setEnabled(False)

    # Área de los Slots
    def sumar(self):
        A = int(self.txt_A.text())
        B = int(self.txt_B.text())
        r = A + B
        self.txt_suma.setText(str(r))

        QMessageBox.information(self, 'Resultado', f'Sum De dos Nuemros: {r}')










if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

