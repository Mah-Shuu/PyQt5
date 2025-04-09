import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from Ex5 import Ui_MainWindow

class ex5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.parImpar)

    def parImpar(self):
        if self.ui.lineEdit.text().isnumeric() == True:
            num = float(self.ui.lineEdit.text())
            if num%2 == 0:
                self.ui.num_output.setText(f"O número é par.")
            else:
                self.ui.num_output.setText(f"O número é ímpar.")
        else:
            self.ui.num_output.setText(f"Valor inválido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex5()
    window.show()
    sys.exit(app.exec_())