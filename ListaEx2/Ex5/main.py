import sys, math
from PyQt5.QtWidgets import QApplication, QMainWindow
from CalculadoraPintura import Ui_MainWindow
 
class CalculadoraPintura(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calcular)
 
    def calcular(self):
        try:
            area = int(self.ui.lineEdit.text())
            litros = area/3
            latas = math.ceil(litros/18)
 
            self.ui.label_3.setText(f"Área a ser pintada: {area}m² \nQuantidade de litros necessários: {litros:.2f}L\nLatas necessárias: {latas}")
        except:
            self.ui.label_3.setText(f"Valor inválido")
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraPintura()
    window.show()
    sys.exit(app.exec_())