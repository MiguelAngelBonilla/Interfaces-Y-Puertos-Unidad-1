import sys
import math
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


qtCreatorFile = "E_06_promedioDe5Calificaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_resultado.clicked.connect(self.calcularPromedio)

    # Área de los Slots
    def calcularPromedio(self):


        calificaciones= []
        calificaciones.append(float(self.txt_Cal1.text()))
        calificaciones.append(float(self.txt_Cal2.text()))
        calificaciones.append(float(self.txt_Cal3.text()))
        calificaciones.append(float(self.txt_Cal4.text()))
        calificaciones.append(float(self.txt_Cal5.text()))
        promedio = sum(calificaciones)/len(calificaciones)
        QMessageBox.information(self, 'Resultado', f'Promedio:' f'{promedio}')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


