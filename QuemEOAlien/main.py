import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from alienSimulator import Ui_MainWindow

class Formulario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.verificarOpt)

    def verificarOpt(self):
        if self.ui.radioButton_5.isChecked():
            QMessageBox.information(self, "Acertou", "Boa calabreso")
            self.reset()
        else:
            QMessageBox.information(self, "Errou", "Você destruiu o meu ovo")
            self.reset()

    def reset(self):
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.radioButton_4.setChecked(False)
        self.ui.radioButton_5.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Formulario()
    window.show()
    sys.exit(app.exec_())