import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from CalculadoraSal import Ui_MainWindow
 
class CalculadoraSalario(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calcular)
 
    def calcular(self):
        try:
            salarioPorHora = float(self.ui.lineEdit.text())
            horas = float(self.ui.lineEdit_2.text())

            res = salarioPorHora * horas
 
            self.ui.label_res.setText(f"Salário total: R${res:.2f}")
        except:
            self.ui.label_res.setText(f"Valores inválidos")
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraSalario()
    window.show()
    sys.exit(app.exec_())