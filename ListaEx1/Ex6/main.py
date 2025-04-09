import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from ex6 import Ui_MainWindow

class ex6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Fatorial)

    def Fatorial(self):
        if self.ui.lineEdit.text().isnumeric() == True:
            num = float(self.ui.lineEdit.text())
            fat = num
            i = 1

            while i<num:
                fat = fat * (num-i)
                i+=1

            self.ui.num_output.setText(f"{fat}")
            
        else:
            self.ui.num_output.setText(f"Valor inválido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex6()
    window.show()
    sys.exit(app.exec_())