import sys, math
from PyQt5.QtWidgets import QApplication, QMainWindow
from TempoDownload import Ui_MainWindow
 
class CalculadoraDownloadTime(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calcularTempo)
 
    def calcularTempo(self):
        try:
            tamanho = int(self.ui.lineEdit.text())
            velocidade = int(self.ui.lineEdit_2.text())
            
            res = ((tamanho*8)/velocidade)
            minutos = math.floor(res/60)
            segundos = res%60
 
            self.ui.label_res.setText(f"Tempo estimado pro download: {minutos} minuto(s) e {segundos} segundo(s)")
        except:
            self.ui.label_res.setText(f"Valor inválido")
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculadoraDownloadTime()
    window.show()
    sys.exit(app.exec_())