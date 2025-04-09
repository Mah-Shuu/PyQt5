import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from EspacosVogais import Ui_MainWindow

class Frase(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.checarEspacosEVogais)

    def checarEspacosEVogais(self):
        try:
            frase = str(self.ui.lineEdit.text())
            fraseCheck = frase.upper()
            vogais = ["A","E","I","O","U"]
            qtdeVogais = 0
            qtdeEspacos = 0

            for letra in fraseCheck:
                if letra in vogais:
                    qtdeVogais +=1
                elif letra == " ":
                    qtdeEspacos +=1
            
            self.ui.label_res.setText(f"Quantidade de vogais: {qtdeVogais}\nQuantidade de espaços: {qtdeEspacos}")

        except:
            self.ui.label_res.setText(f"Valor inválido")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Frase()
    window.show()
    sys.exit(app.exec_())