import sys
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap
from GerarImagem import Ui_MainWindow

class GerarImagem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.abrir_zap)

    def abrir_zap(self):
        imagemPath = 'batman.jpg'

        pixmap = QPixmap(imagemPath)

        if pixmap.isNull():
            print("Erro ao carregar a imagem.")
        else:
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GerarImagem()
    window.show()
    sys.exit(app.exec_())