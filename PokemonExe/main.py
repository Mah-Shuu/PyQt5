import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from pokemonExe import Ui_MainWindow

class SeletorPersonagem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.musicPath = os.path.abspath("audio/LavenderTown.mp3")
        self.url = QUrl.fromLocalFile(self.musicPath)
        self.player.setMedia(QMediaContent(self.url))
        self.player.play()

        self.ui.pushButtonPikachu.clicked.connect(lambda: self.selectCharacter("Pikachu"))
        self.ui.pushButtonCharmander.clicked.connect(lambda: self.selectCharacter("Charmander"))
        self.ui.pushButtonSquirtle.clicked.connect(lambda: self.selectCharacter("Squirtle"))
        self.ui.pushButtonBulbassauro.clicked.connect(lambda: self.selectCharacter("Bulbassauro"))
        self.ui.pushButtonEevee.clicked.connect(lambda: self.selectCharacter("Eevee"))
        self.ui.pushButtonHypno.clicked.connect(lambda: self.selectCharacter("Hypno"))
        self.ui.pushButtonPlay.clicked.connect(self.risadaEnfadonha)

    def selectCharacter(self, nomePersonagem):
        caminhoImagem = {
            "Pikachu" : "imagens/pikachu.png",
            "Charmander" : "imagens/charmander.jpg",
            "Squirtle" : "imagens/squirtle.png",
            "Eevee" : "imagens/eevee.jpg",
            "Bulbassauro" : "imagens/bulbassauro.png",
            "Hypno" : "imagens/hypno.webp"
        }
        if nomePersonagem in caminhoImagem:
            pixmap = QPixmap(caminhoImagem[nomePersonagem])
            self.ui.labelPersonagem.setPixmap(pixmap)
        else:
            print(f"Imagem de {nomePersonagem} não encontrada.")

    def risadaEnfadonha(self):
        self.player.stop()
        self.musicPath = os.path.abspath("audio/risada.mp3")
        self.url = QUrl.fromLocalFile(self.musicPath)
        self.player.setMedia(QMediaContent(self.url))
        self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeletorPersonagem()
    window.show()
    sys.exit(app.exec_())