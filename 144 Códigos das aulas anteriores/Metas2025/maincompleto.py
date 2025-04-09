import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QFileDialog, QAction
from Listasdemetas2 import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar botões às funções
        self.ui.pushButton_AdicionarMeta.clicked.connect(self.add_meta)
        self.ui.pushButton_RemoverMeta.clicked.connect(self.remove_meta)
        self.ui.actionNovo.triggered.connect(self.novo_arquivo)
        self.ui.actionAbrir.triggered.connect(self.abrir_arquivo)
        self.ui.actionSalvar.triggered.connect(self.salvar_arquivo)
        self.ui.actionSair.triggered.connect(self.close)

    def novo_arquivo(self):
        self.ui.listWidget.clear()  # Limpa a lista de metas

    def abrir_arquivo(self):
        caminho = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'r', encoding='utf-8') as f:
                metas = f.readlines()
                self.ui.listWidget.clear()  # Limpa a lista antes de adicionar os itens
                for meta in metas:
                    meta = meta.strip()  # Remove possíveis quebras de linha
                    item = QListWidgetItem(meta)
                    item.setCheckState(0)
                    self.ui.listWidget.addItem(item)

    def salvar_arquivo(self):
        caminho = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'w', encoding='utf-8') as f:
                for i in range(self.ui.listWidget.count()):
                    item = self.ui.listWidget.item(i)
                    f.write(item.text() + "\n")  # Salva o texto de cada item na lista

    def add_meta(self):
        meta = self.ui.lineEdit.text()
        if meta:
            item = QListWidgetItem(meta)
            item.setCheckState(0)
            self.ui.listWidget.addItem(item)
            self.ui.lineEdit.clear()
        
    def remove_meta(self):
        selected_item = self.ui.listWidget.currentRow()
        if selected_item >= 0:
            self.ui.listWidget.takeItem(selected_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())

            
        