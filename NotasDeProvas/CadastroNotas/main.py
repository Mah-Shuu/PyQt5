import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from cadastroNotas import Ui_MainWindow

class FormularioNotas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dados_candidatos = {}

        self.ui.pushButton_cancelar.clicked.connect(self.cancelar)
        self.ui.pushButton_salvar.clicked.connect(self.salvarDados)

    def cancelar(self):
        self.ui.lineEdit_cpf.clear()

        self.ui.spinBox_portugues.setValue(0)
        self.ui.spinBox_matematica.setValue(0)
        self.ui.spinBox_cg.setValue(0)
        self.ui.spinBox_ce.setValue(0)

    def salvarJson(self):
        try:
            if os.path.exists('dados_candidatos'):
                with open('dados_candidatos.json', 'r') as f:
                    dados_existentes = json.load(f)

                dados_existentes.update(self.dados_candidatos)

                with open('dados_candidatos.json', 'w') as f:
                    json.dump(dados_existentes, f, indent=4)

            else:
                with open('dados_candidatos.json','w') as f:
                    json.dump(self.dados_candidatos, f, indent=4)

        except Exception as e:
            QMessageBox.critical(self, 'Erro ao salvar', f'Ocorreu um erro ao salvar os dados: {e}')

    def salvarDados(self):
        cpf = str(self.ui.lineEdit_cpf.text())
        if len(cpf) == 11:

            if cpf in self.dados_candidatos:
                QMessageBox.warning(self, 'Erro', 'Este CPF já foi cadastrado.')
                return
            
            fatia_um = cpf[:3]
            fatia_dois = cpf[3:6]
            fatia_tres = cpf[6:9]
            fatia_quatro = cpf[9:]

            cpf_formatado = "{}.{}.{}-{}".format(
                fatia_um,
                fatia_dois,
                fatia_tres,
                fatia_quatro
            )
            
            self.dados_candidatos[cpf] = {
                "notaPortugues": self.ui.spinBox_portugues.value()*2,
                "notaMatematica": self.ui.spinBox_matematica.value()*2,
                "notaConhecimentosGerais": self.ui.spinBox_cg.value()*2,
                "notaConhecimentosEspecificos": self.ui.spinBox_ce.value()*2,
                "mediaTotal": self.ui.spinBox_portugues.value() + self.ui.spinBox_matematica.value() + self.ui.spinBox_cg.value() + self.ui.spinBox_ce.value()
            }

            self.salvarDados()

            QMessageBox.information(self, "Dados salvos", "Dados salvos com sucesso.")

            self.cancelar()

        else:
            QMessageBox.warning(self, "Erro", "CPF inválido.")

    # def carregarJogo(self):
    #     file_path, _ = QFileDialog.getOpenFileName(self, "Carregar Jogo", "", "Arquivos JSON (*.json)")

    #     if file_path:
    #         try:
    #             with open(file_path, "r", encoding="utf-8") as file:
    #                 data = json.load(file)

    #                 self.ui.lineEdit_nome.setText(data.get("nome", ""))
    #                 self.ui.lineEdit_idade.setText(data.get("idade", ""))
    #                 self.ui.lineEdit_altura.setText(data.get("altura", ""))
    #                 self.ui.dateEdit.setDate(QtCore.QDate.fromString(data.get("dataNasc", "200-01-01"), "yyyy-MM-dd"))

    #                 if data.get("sexo") == "Feminino":
    #                     self.ui.radioButton_feminino.setChecked(True)
    #                 elif data.get("sexo") == "Masculino":
    #                     self.ui.radioButton_masculino.setChecked(True)
    #                 else:
    #                     self.ui.radioButton_feminino.setChecked(False)
    #                     self.ui.radioButton_masculino.setChecked(False)

    #             QMessageBox.information(self, "Sucesso", "Jogo Carregado com sucesso.")

    #         except Exception as e:
    #             QMessageBox.critical(self, "Erro", f"Erro ao carregar jogo: {e}.")
        
    #     else:
    #         QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormularioNotas()
    window.show()
    sys.exit(app.exec_())