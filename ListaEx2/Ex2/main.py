import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Tabuada import Ui_MainWindow

class Tabuada(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.exibirTabuada)

    def exibirTabuada(self):
        numero = int(self.ui.lineEdit.text())
        tabuadaText = ""

        for i in range(0,11):
            tabuadaText += f"{numero} x {i} = {numero * i}\n"

        self.ui.label_res.setText(tabuadaText)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tabuada()
    window.show()
    sys.exit(app.exec_())