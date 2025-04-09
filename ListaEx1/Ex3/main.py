import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ex3 import Ui_MainWindow

class ex3(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionSair.triggered.connect(self.close)
        self.ui.input_button.clicked.connect(self.maiorNum)

    def maiorNum(self):
        try:
            num1 = float((self.ui.input_num1.text()))
            num2 = float((self.ui.input_num2.text()))
            num3 = float((self.ui.input_num3.text()))

            maior = max(num1,num2,num3)
            self.ui.output_num.setText(f"{maior}")
        except:
            self.ui.output_num.setText(f"Valores inválidos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex3()
    window.show()
    sys.exit(app.exec_())