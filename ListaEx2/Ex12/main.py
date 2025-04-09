import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Fatorial import Ui_MainWindow

class Fatorial(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        try:
            num = int(self.ui.lineEdit.text())
            fat = num
            i = num
            texto = ""

            while i!=0:
                if i == 1:
                    texto+=f"{i}"
                    break
                fat = fat * (i-1)
                texto+= f"{i} x "
                i-=1
                
            
            self.ui.label_res.setText(f"Fatorial de {num}:\n{num}! = {texto} = {fat}")
        except:
            self.ui.label_res.setText(f"Valor inválido.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Fatorial()
    window.show()
    sys.exit(app.exec_())