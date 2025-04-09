import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QPushButton
from baratie import Ui_MainWindow

class Restaurante(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.total = 0.0
        self.ui.pushButton_1.clicked.connect(lambda: self.comprar("panqueca"))
        self.ui.pushButton_2.clicked.connect(lambda: self.comprar("escargot"))
        self.ui.pushButton_3.clicked.connect(lambda: self.comprar("lagosta"))
        self.ui.pushButton_4.clicked.connect(lambda: self.comprar("vodka"))
        self.ui.pushButton_5.clicked.connect(self.pedirConta)

    def comprar(self, produto):
        produtos = {
            "panqueca" : 53.90,
            "escargot" : 799.99,
            "lagosta" : 2000,
            "vodka" : 3700000,
        }

        if produto in produtos:
            self.total += produtos[produto]
        
        else:
            print(f"Produto {produto} não encontrado.")

        self.ui.label_total.setText(f"{self.total:.2f}")

    def pedirConta(self):
        self.ui.label_total.setText("00,00")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Restaurante()
    window.show()
    sys.exit(app.exec_())