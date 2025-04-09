import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from Ex2 import Ui_MainWindow

class ex2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNovo.triggered.connect(self.novo_arquivo)
        self.ui.actionAbrir.triggered.connect(self.abrir_arquivo)
        self.ui.actionSalvar.triggered.connect(self.salvar_arquivo)
        self.ui.actionSair.triggered.connect(self.close)
        self.ui.input_button.clicked.connect(self.soma)

    def soma(self):
        num1 = float(self.ui.input_num1.text())
        num2 = float(self.ui.input_num2.text())

        res = num1+num2

        self.ui.output_sum.setText(f"{res}")

    def novo_arquivo(self):
        self.ui.input_num1.clear()
        self.ui.input_num2.clear()
        self.ui.output_sum.clear()

    def abrir_arquivo(self):
        caminho = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'r', encoding='utf-8') as f:
                self.ui.textEdit.setText(f.read())

    def salvar_arquivo(self):
        caminho = QFileDialog.getSaveFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(self.ui.textEdit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex2()
    window.show()
    sys.exit(app.exec_())