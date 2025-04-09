import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from NomeInvertido import Ui_MainWindow

class Inversor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.inverter)

    def inverter(self):
        try:
            nome = str(self.ui.lineEdit.text())

            nome = nome.upper()

            nomeInvertido = nome[::-1]

            self.ui.label_res.setText(f'{nomeInvertido}')

        except:
            self.ui.label_res.setText(f"Valores inválidos")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Inversor()
    window.show()
    sys.exit(app.exec_())