import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from ListaTelefonica import Ui_MainWindow

class AgendaTelefonica(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arquivo_contatos = "contatos.json"
        self.carregar_contatos()

        self.pushButton_add.clicked.connect(self.adicionar_contato)
        self.pushButton_listar.clicked.connect(self.listar_contatos)
        self.pushButton_remover.clicked.connect(self.remover_contato)
        self.pushButton_edit.clicked.connect(self.editar_contato)

    def carregar_contatos(self):
        try:
            with open(self.arquivo_contatos, "r") as file:
                self.contatos = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contatos = {}

    def salvar_contatos(self):
        with open(self.arquivo_contatos, "w") as file:
            json.dump(self.contatos, file, indent=4)

    def adicionar_contato(self):
        nome = self.lineEdit_nome.text().strip()
        telefone = self.lineEdit_telefone.text().strip()
        
        if not nome or not telefone:
            QMessageBox.warning(self, "Erro", "Nome e telefone são obrigatórios!")
            return
        
        self.contatos[nome] = telefone
        self.salvar_contatos()
        self.listar_contatos()
        self.lineEdit_nome.clear()
        self.lineEdit_telefone.clear()

    def listar_contatos(self):
        self.listWidget.clear()
        for nome, telefone in self.contatos.items():
            self.listWidget.addItem(f"{nome}: {telefone}")

    def remover_contato(self):
        item_selecionado = self.listWidget.currentItem()
        if item_selecionado:
            nome = item_selecionado.text().split(":")[0]
            del self.contatos[nome]
            self.salvar_contatos()
            self.listar_contatos()
        else:
            QMessageBox.warning(self, "Erro", "Selecione um contato para remover!")

    def editar_contato(self):
        item_selecionado = self.listWidget.currentItem()
        if item_selecionado:
            nome = item_selecionado.text().split(":")[0]
            novo_nome, ok = QInputDialog.getText(self, "Editar Contato", "Novo Nome:", text=nome)
            if ok and novo_nome:
                novo_telefone, ok = QInputDialog.getText(self, "Editar Contato", "Novo Telefone:", text=self.contatos[nome])
                if ok and novo_telefone:
                    del self.contatos[nome]
                    self.contatos[novo_nome] = novo_telefone
                    self.salvar_contatos()
                    self.listar_contatos()
        else:
            QMessageBox.warning(self, "Erro", "Selecione um contato para editar!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AgendaTelefonica()
    janela.show()
    sys.exit(app.exec_())