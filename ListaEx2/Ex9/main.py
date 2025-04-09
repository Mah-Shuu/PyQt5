import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from cumprimento import Ui_MainWindow

class Cumprimento(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.cumprimentar)

    def cumprimentar(self):
        turno = self.ui.lineEdit.text()

        match turno:
            case "M":
                self.ui.label_res.setText("Bom Dia!")
            case "V":
                self.ui.label_res.setText("Boa Tarde!")
            case "N":
                self.ui.label_res.setText("Boa Noite!")
            case _:
                self.ui.label_res.setText(f"Valor inválido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cumprimento()
    window.show()
    sys.exit(app.exec_())