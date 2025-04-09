import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from SomaTodosOsNum import Ui_MainWindow
 
class SomaNumN(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calcular)
 
    def calcular(self):
        numero = int(self.ui.lineEdit.text())
        soma = sum(range(1,numero + 1))
 
        self.ui.label_res.setText(f"Soma dos número até N: {soma}")
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SomaNumN()
    window.show()
    sys.exit(app.exec_())