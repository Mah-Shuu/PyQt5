import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from front import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_cadastrar.clicked.connect(self.salvarDados)

        self.db_connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "cadastroqt"
        )

        self.Cursor = self.db_connection.cursor()

    def salvarDados(self):

        nome = self.ui.lineEdit_nome.text().strip()
        dataNasc = self.ui.dateEdit_nasc.text()
        cpf = self.ui.lineEdit_cpf.text().strip()
        cep = self.ui.lineEdit_cep.text().strip()
        rua = self.ui.lineEdit_rua.text().strip()
        numero = self.ui.lineEdit_numero.text().strip()
        complemento = self.ui.lineEdit_complemento.text().strip()
        bairro = self.ui.lineEdit_bairro.text().strip()
        cidade = self.ui.lineEdit_cidade.text().strip()
        estado = self.ui.lineEdit_estado.text().strip()
        email = self.ui.lineEdit_email.text().strip()
        emailConfirm = self.ui.lineEdit_emailConfirm.text().strip()
        senha = self.ui.lineEdit_senha.text().strip()
        senhaConfirm = self.ui.lineEdit_senhaConfirm.text().strip()
        
        if nome and dataNasc and cpf and cep and rua and numero and bairro and cidade and estado and email and emailConfirm and senha and senhaConfirm:
            if email == emailConfirm:
                if senha == senhaConfirm:

                    if complemento:
                        try:

                            query = "INSERT INTO clientes (nome, dataNasc, cpf, cep, rua, numero, complemento, bairro, cidade, estado, email, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            values = (nome, dataNasc, cpf, cep, rua, numero, complemento, bairro, cidade, estado, email, senha)
                            self.Cursor.execute(query,values)

                            self.db_connection.commit()

                            QMessageBox.information(self, "Sucesso", "Dados cadastrados com sucesso!")
                        except mysql.connector.Error as err:
                            QMessageBox.critical(self, "Erro", f"Erro ao salvar dados: {err}")
                    else:
                        try:

                            query = "INSERT INTO clientes (nome, dataNasc, cpf, cep, rua, numero, bairro, cidade, estado, email, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            values = (nome, dataNasc, cpf, cep, rua, numero, bairro, cidade, estado, email, senha)
                            self.Cursor.execute(query,values)

                            self.db_connection.commit()

                            QMessageBox.information(self, "Sucesso", "Dados cadastrados com sucesso!")
                        except mysql.connector.Error as err:
                            QMessageBox.critical(self, "Erro", f"Erro ao salvar dados: {err}")
                else:
                    QMessageBox.warning(self, "Aviso", "Os valores de senha não são equivalentes.")
            else:
                QMessageBox.warning(self, "Aviso", "Os valores de E-mail não são equivalentes.")

        else:
            QMessageBox.warning(self, "Aviso", "Por favor, preencha todos os campos obrigatórios.")

    def closeEvent(self,event):
        self.Cursor.close()
        self.db_connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())