import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from fotoIdade import Ui_MainWindow

class GerarImagem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.abrirFoto)


    def abrirFoto(self):
        idade = self.ui.spinBox.value()

        if idade>=0:
            if idade<=3:
                imagemPath = 'bebe.jpg'
            elif idade<=11:
                imagemPath = 'crianca.jpg'
            elif idade<=18:
                imagemPath = 'adolescente.jpg'
            elif idade<=60:
                imagemPath = 'adulto.jpg'
            elif idade<99:  
                imagemPath = 'idoso.jpg'
            elif idade==99:
                imagemPath = 'caveira.webp'
        else:
            QMessageBox.warning(self, "Erro", "Idade inválida.")

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