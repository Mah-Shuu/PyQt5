import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Crescente3Num import Ui_MainWindow

class OrdenarNumeros(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.input_button.clicked.connect(self.ordenar)

    def ordenar(self):
        try:
            num1 = float((self.ui.input_num1.text()))
            num2 = float((self.ui.input_num2.text()))
            num3 = float((self.ui.input_num3.text()))

            lista = [num1,num2,num3]
            lista.sort(reverse=True)
            text = ""

            for num in lista:
                text+=f"{num} "
            
            self.ui.output_num.setText(f"Ordem crescente: {text}")
        except:
            self.ui.output_num.setText(f"Valores inválidos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrdenarNumeros()
    window.show()
    sys.exit(app.exec_())