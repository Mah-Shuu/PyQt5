import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QFileDialog
from ListaDeMetas import Ui_MainWindow

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_add.clicked.connect(self.addMeta)
        self.ui.pushButton_rmv.clicked.connect(self.rmvMeta)

        self.ui.actionNovo.triggered.connect(self.novo_arquivo)
        self.ui.actionAbrir.triggered.connect(self.abrir_arquivo)
        self.ui.actionSalvar.triggered.connect(self.salvar_arquivo)
        self.ui.actionSair.triggered.connect(self.close)

    def addMeta(self):
        meta = self.ui.lineEdit.text()
        if meta:
            item = QListWidgetItem(meta)
            self.ui.listaMetas.addItem(item)
            item.setCheckState(0)

            self.ui.lineEdit.clear()

    def rmvMeta(self):
        selectedItem = self.ui.listaMetas.currentRow()
        if selectedItem >= 0:
            self.ui.listaMetas.takeItem(selectedItem)

    def novo_arquivo(self):
        self.ui.listaMetas.clear()

    def abrir_arquivo(self):
        caminho = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'r', encoding='utf-8') as f:
                metas = f.readlines()
                self.ui.listaMetas.clear()
                for meta in metas:
                    meta = meta.strip()
                    item = QListWidgetItem(meta)
                    item.setCheckState(0)
                    self.ui.listaMetas.addItem(item)

    def salvar_arquivo(self):
        caminho = QFileDialog.getSaveFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'w', encoding='utf-8') as f:
                for i in range(self.ui.listaMetas.count()):
                    item = self.ui.listaMetas.item(i)
                    f.write(item.text() + "\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())