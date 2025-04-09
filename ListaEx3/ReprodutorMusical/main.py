import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from ReprodutorMusical import Ui_MainWindow

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

        self.ui.horizontalSlider_volume.valueChanged.connect(self.volumeControl)

    def play(self):
        musicPath = os.path.abspath("music/musica.mp3")
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

    def volumeControl(self):
        volume = self.ui.horizontalSlider_volume.value()

        self.player.setVolume(volume)
        print(f"Volume ajustado para: {volume}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Player()
    window.show()
    sys.exit(app.exec_())