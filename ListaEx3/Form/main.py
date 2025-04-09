import sys
import json
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from formulario import Ui_MainWindow

class Formulario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_novoJogo.clicked.connect(self.novoJogo)
        self.ui.pushButton_carregarJogo.clicked.connect(self.carregarJogo)
        self.ui.pushButton_salvarJogo.clicked.connect(self.salvarJogo)
        self.ui.pushButton_sair.clicked.connect(self.close)

    def novoJogo(self):
        self.ui.lineEdit_nome.clear()
        self.ui.lineEdit_idade.clear()
        self.ui.lineEdit_altura.clear()

        self.ui.radioButton_masculino.setChecked(False)
        self.ui.radioButton_feminino.setChecked(False)

        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())

        QMessageBox.information(self, "Novo Jogo", "Novo jogo iniciado")

    def salvarJogo(self):
        data = {
            "nome": self.ui.lineEdit_nome.text(),
            "dataNasc": self.ui.dateEdit.date().toString("yyyy-MM-dd"),
            "idade": self.ui.lineEdit_idade.text(),
            "altura": self.ui.lineEdit_altura.text(),
            "sexo": "Feminino" if self.ui.radioButton_feminino.isChecked() else "Masculino" if self.ui.radioButton_masculino.isChecked() else "Não informado"
        }

        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Jogo", "", "Arquivos JSON (*.json)")

        if file_path:
            try:
                if not file_path.endswith('.json'):
                    file_path += '.json'

                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

                QMessageBox.information(self, "Sucesso", "Jogo salvo com sucesso.")

            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar jogo: {e}.")

        else:
            QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado.")

    def carregarJogo(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Carregar Jogo", "", "Arquivos JSON (*.json)")

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                    self.ui.lineEdit_nome.setText(data.get("nome", ""))
                    self.ui.lineEdit_idade.setText(data.get("idade", ""))
                    self.ui.lineEdit_altura.setText(data.get("altura", ""))
                    self.ui.dateEdit.setDate(QtCore.QDate.fromString(data.get("dataNasc", "200-01-01"), "yyyy-MM-dd"))

                    if data.get("sexo") == "Feminino":
                        self.ui.radioButton_feminino.setChecked(True)
                    elif data.get("sexo") == "Masculino":
                        self.ui.radioButton_masculino.setChecked(True)
                    else:
                        self.ui.radioButton_feminino.setChecked(False)
                        self.ui.radioButton_masculino.setChecked(False)

                QMessageBox.information(self, "Sucesso", "Jogo Carregado com sucesso.")

            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao carregar jogo: {e}.")
        
        else:
            QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Formulario()
    window.show()
    sys.exit(app.exec_())