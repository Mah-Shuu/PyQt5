import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Vetor10NumInverso import Ui_MainWindow

class Vetor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lista = []

        self.ui.pushButton.clicked.connect(self.setLista)
        self.ui.pushButton_2.clicked.connect(self.LimparLista)

    def setLista(self):
        try:
            num = int(self.ui.lineEdit.text())
            self.lista.append(num)
            self.ui.label_2.setText(f"Digite o número da posição {len(self.lista)+1}:")

            if len(self.lista) == 10:
                self.lista.reverse()
                self.ui.label_res.setText(f"Lista: {self.lista}")
                self.lista = []
                self.ui.label_2.setText(f"Digite o número da posição {len(self.lista)+1}:")

        except:
            self.ui.label_res.setText(f"Valor inválido")
            
        self.ui.lineEdit.setText("")

    def LimparLista(self):
        self.lista = []
        self.ui.label_2.setText(f"Digite o número da posição {len(self.lista)+1}:")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Vetor()
    window.show()
    sys.exit(app.exec_())