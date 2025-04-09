import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Num5Simulator import Ui_MainWindow

class CincoNum(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        try:
            num1 = float((self.ui.lineEdit.text()))
            num2 = float((self.ui.lineEdit_2.text()))
            num3 = float((self.ui.lineEdit_3.text()))
            num4 = float((self.ui.lineEdit_4.text()))
            num5 = float((self.ui.lineEdit_5.text()))

            lista = [num1,num2,num3,num4,num5]

            maior = max(num1,num2,num3,num4,num5)
            soma = sum(lista)
            media = soma/5

            self.ui.label_res.setText(f"Maior número: {maior}\nSoma de todos os números: {soma}\nMédia dos números: {media}")
        except:
            self.ui.label_res.setText(f"Valores inválidos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CincoNum()
    window.show()
    sys.exit(app.exec_())