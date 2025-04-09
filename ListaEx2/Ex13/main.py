import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Vetor5Num import Ui_MainWindow

class Vetor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lista = []

        self.ui.pushButton.clicked.connect(self.setLista)

    def setLista(self):
        try:
            num = int(self.ui.lineEdit.text())
            self.lista.append(num)
            self.ui.label_2.setText(f"Digite o número da posição {len(self.lista)+1}:")

            if len(self.lista) == 5:
                self.ui.label_res.setText(f"Lista: {self.lista}")
                self.lista = []
                self.ui.label_2.setText(f"Digite o número da posição {len(self.lista)+1}:")

        except:
            self.ui.label_res.setText(f"Valor inválido")
            
        self.ui.lineEdit.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Vetor()
    window.show()
    sys.exit(app.exec_())