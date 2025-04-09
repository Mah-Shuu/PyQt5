import sys
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from portifolioDeUmBanana import Ui_MainWindow

class portifolio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.abrirYoutube)
        self.ui.pushButton_2.clicked.connect(self.abrirInstagram)
        self.ui.pushButton_3.clicked.connect(self.abrirX)

    def abrirYoutube(self):
        link = "https://www.youtube.com/user/felipeneto"
        webbrowser.open(link)
    def abrirInstagram(self):
        link = "https://www.instagram.com/felipeneto/"
        webbrowser.open(link)
    def abrirX(self):
        link = "https://x.com/felipeneto"
        webbrowser.open(link)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = portifolio()
    window.show()
    sys.exit(app.exec_())