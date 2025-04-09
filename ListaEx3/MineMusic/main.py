import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from MinePlayer import Ui_MainWindow

class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.isPaused = False

        self.ui.pushButton_play.clicked.connect(self.play)
        self.ui.pushButton_parar.clicked.connect(self.stop)
        self.ui.pushButton_pausar.clicked.connect(self.pause)

    def play(self):
        musica = self.ui.lineEdit.text()
        
        musicPath = os.path.abspath(f"music/{musica}.mp3")
        print("Local da música:", musicPath)

        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:

            url = QUrl.fromLocalFile(musicPath)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")

            else:
                print("Erro: Caminho do arquivo inválido.")

    def stop(self):
        self.player.stop()
        self.isPaused = False
        print("Música parada.")

    def pause(self):
        self.player.pause()
        self.isPaused = True
        print("Música pausada.")

os.environ["QT_MULTIMEDIA_PREFERRED_PLUGINS"] = "windowsmediafoundation"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Player()
    window.show()
    sys.exit(app.exec_())