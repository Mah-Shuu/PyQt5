import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Comparar2Frases import Ui_MainWindow

class Comparador(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.comparar)

    def comparar(self):
        try:
            frase1 = str(self.ui.lineEdit.text())
            frase2 = str(self.ui.lineEdit_2.text())

            tamanho1 = len(frase1)
            tamanho2 = len(frase2)

            if tamanho1 == tamanho2:
                tamanhoComp = "iguais"
            else:
                tamanhoComp = "diferentes"

            if frase1 == frase2:
                conteudoComp = "igual"
            else:
                conteudoComp = "diferente"

            self.ui.label_res.setText(f'Tamanho de "{frase1}": {tamanho1}\nTamanho de "{frase2}": {tamanho2}\nAs duas strings são de tamanhos {tamanhoComp}\nAs duas strings possuem conteúdo {conteudoComp}')



        except:
            self.ui.label_res.setText(f"Valores inválidos")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Comparador()
    window.show()
    sys.exit(app.exec_())