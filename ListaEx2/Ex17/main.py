import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from NomeVertical import Ui_MainWindow

class Vertical(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.verticalizar)

    def verticalizar(self):
        try:
            nome = str(self.ui.lineEdit.text())
            texto = ""

            for letra in nome:
                texto+=f"{letra}\n"

            self.ui.label_res.setText(f'{texto}')

        except:
            self.ui.label_res.setText(f"Valor inválido")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Vertical()
    window.show()
    sys.exit(app.exec_())