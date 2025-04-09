import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from Ex4 import Ui_MainWindow

class ex4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionSair.triggered.connect(self.close)
        self.ui.input_button.clicked.connect(self.maiorNum)

    def maiorNum(self):
        num1ver = (self.ui.input_num1.text())
        num2ver = (self.ui.input_num2.text())
        num3ver = (self.ui.input_num3.text())
        num4ver = (self.ui.input_num4.text())
        num5ver = (self.ui.input_num5.text())
        num6ver = (self.ui.input_num6.text())
        num7ver = (self.ui.input_num7.text())
        num8ver = (self.ui.input_num8.text())
        num9ver = (self.ui.input_num9.text())
        num10ver = (self.ui.input_num10.text())

        lista = [num1ver,num2ver,num3ver,num4ver,num5ver,num6ver,num7ver,num8ver,num9ver,num10ver]
        verificacao = True
        maior = int(0)

        for x in lista:
            if x.isnumeric() == True:
                continue
            else:
                verificacao = False
                break

        if verificacao == True:
            for x in lista:
                print(x)
                print(maior)
                if float(x)>maior:
                    maior = float(x)
            
            self.ui.output_num.setText(f"{maior}")
        else:
            self.ui.output_num.setText(f"Valores inválidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex4()
    window.show()
    sys.exit(app.exec_())