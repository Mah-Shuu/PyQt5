import sys
import json
from PyQt5 import QtWidgets, QtCore
from form import Ui_MainWindow  

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)  

        self.ui.pushButton_Sair.clicked.connect(self.close)
        self.ui.pushButton_Novo.clicked.connect(self.novo_game)
        self.ui.pushButton_Salvar.clicked.connect(self.salvar_game)
        self.ui.pushButton_Carregar.clicked.connect(self.carregar_game)

    def novo_game(self):
        self.ui.lineEdit_Nome.clear()
        self.ui.lineEdit_Idade.clear()
        self.ui.lineEdit_Altura.clear()
        
        self.ui.radioButton_F.setChecked(False)
        self.ui.radioButton_M.setChecked(False)
        
        self.ui.dateEdit_Data.setDate(QtCore.QDate.currentDate())
        
        QtWidgets.QMessageBox.information(self, "Novo Jogo", "Novo jogo iniciado!")


    def salvar_game(self):
        data = {
            "nome": self.ui.lineEdit_Nome.text(),
            "data_nascimento": self.ui.dateEdit_Data.date().toString("yyyy-MM-dd"),
            "idade": self.ui.lineEdit_Idade.text(),
            "altura": self.ui.lineEdit_Altura.text(),
            "sexo": "Feminino" if self.ui.radioButton_F.isChecked() else "Masculino" if self.ui.radioButton_M.isChecked() else "Não informado"
        }
        
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar Jogo", "", "Arquivos JSON (*.json)")

        if file_path:
            try:
                if not file_path.endswith('.json'):
                    file_path += '.json'

                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

                QtWidgets.QMessageBox.information(self, "Sucesso", "Jogo salvo com sucesso!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao salvar o jogo: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado!")

    def carregar_game(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Carregar Jogo", "", "Arquivos JSON (*.json)")
        
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    
                    data = json.load(file)
                   
                    self.ui.lineEdit_Nome.setText(data.get("nome", ""))
                    self.ui.dateEdit_Data.setDate(QtCore.QDate.fromString(data.get("data_nascimento", "2000-01-01"), "yyyy-MM-dd"))
                    self.ui.lineEdit_Idade.setText(data.get("idade", ""))
                    self.ui.lineEdit_Altura.setText(data.get("altura", ""))
                    
                    if data.get("sexo") == "Feminino":
                        self.ui.radioButton_F.setChecked(True)
                    elif data.get("sexo") == "Masculino":
                        self.ui.radioButton_M.setChecked(True)
                    else:
                        self.ui.radioButton_F.setChecked(False)
                        self.ui.radioButton_M.setChecked(False)
                        
                QtWidgets.QMessageBox.information(self, "Sucesso", "Jogo carregado com sucesso!")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar o jogo: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado!")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())