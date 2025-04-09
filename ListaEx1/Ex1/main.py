import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QPushButton
from Ex1 import Ui_MainWindow

class ex1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.exibirNome)
        self.ui.actionNovo.triggered.connect(self.novoArquivo)
        self.ui.actionAbrir.triggered.connect(self.abrirArquivo)
        self.ui.actionSalvar.triggered.connect(self.salvarArquivo)
        self.ui.actionSair.triggered.connect(self.close)

    def exibirNome(self):
        nome = self.ui.input_nome.text()
        self.ui.output_nome.setText(f"Olá, {nome}")

    def novoArquivo(self):
        self.ui.input_nome.clear()

    def abrirArquivo(self):
        caminho = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'r', encoding='utf-8') as f:
                self.ui.input_nome.setText(f.read())

    def salvarArquivo(self):
        caminho = QFileDialog.getSaveFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(self.ui.input_nome.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex1()
    window.show()
    sys.exit(app.exec_())