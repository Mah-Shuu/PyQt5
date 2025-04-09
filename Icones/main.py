import sys
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from icones import Ui_MainWindow

class link(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.abrir_zap)

    def abrir_zap(self):
        whatsappLink = "google.com"
        webbrowser.open(whatsappLink)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = link()
    window.show()
    sys.exit(app.exec_())