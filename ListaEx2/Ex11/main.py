import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from InvestCD import Ui_MainWindow

class InvestCD(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.precosCD = []
        self.qtde = 0

        self.ui.pushButton.clicked.connect(self.setTamanho)

    def setTamanho(self):
        try:
            self.qtde = int(self.ui.lineEdit.text())

            self.ui.pushButton.clicked.connect(self.setPrecos)

            self.ui.lineEdit.clear()
            self.ui.label_CD.setText(f"Preço do CD {len(self.precosCD)+1}:")

        except:
            self.ui.label_res.setText(f"Valor inválido.")

    def setPrecos(self):  
        # try:
            print(self.ui.lineEdit.text())
            print(self.qtde)
            preco = float(self.ui.lineEdit.text())
            self.precosCD.append(float(self.ui.lineEdit.text()))
            self.ui.lineEdit.setText(f"")
            self.ui.label_CD.setText(f"Preço do CD {len(self.precosCD)+1}:")
        # except:
        #     self.ui.label_res.setText(f"Valor inválido.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvestCD()
    window.show()
    sys.exit(app.exec_())