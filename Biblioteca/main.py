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
            database = "bibliotecaqt"
        )

        self.Cursor = self.db_connection.cursor()

    def salvarDados(self):

        titulo = self.ui.lineEdit_titulo.text()
        autor = self.ui.lineEdit_autor.text()
        categoria = self.ui.lineEdit_categoria.text()
        publicacao = self.ui.dateEdit_publi.text()
        resumo = self.ui.textEdit_resumo.toPlainText()
        
        if titulo and autor and categoria and publicacao and resumo:
            print(publicacao)

            try:

                query = "INSERT INTO livros (titulo, autor, categoria, dataPubli, resumo) VALUES (%s, %s, %s, %s, %s)"
                values = (titulo, autor, categoria, publicacao, resumo)
                self.Cursor.execute(query,values)

                self.db_connection.commit()

                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar dados: {err}")

        else:
            QMessageBox.warning(self, "Aviso", "Por favor, preencha todos os campos.")

    def closeEvent(self,event):
        self.Cursor.close()
        self.db_connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())