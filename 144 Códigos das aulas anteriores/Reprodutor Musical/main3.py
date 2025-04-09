import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from pause import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.isPaused = False

        self.ui.pushButton_Tocar.clicked.connect(self.tocar_musica)
        self.ui.pushButton_Parar.clicked.connect(self.parar_musica)
        self.ui.pushButton_Pausar.clicked.connect(self.pausar_musica)

    def tocar_musica(self):
        caminho_musica = os.path.abspath("musicas/Sp.mp3") 
        print("Local da musica:", caminho_musica)

        if self.isPaused:  
            self.player.play()
            self.isPaused = False
        
        else:
            url = QUrl.fromLocalFile(caminho_musica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")

            else:
                print("Erro: Caminho do arquivo inválido.")

    def parar_musica(self):
        self.player.stop()
        self.isPaused = False
        print("Música parou")

    def pausar_musica(self):
        self.player.pause()
        self.isPaused = True
        print("Música pausou")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())