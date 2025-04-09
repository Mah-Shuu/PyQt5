import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        self.setWindowTitle('Login')

        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        usuario = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()

        print(f"Usuario: {usuario}\nSenha: {senha}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Login()
    mainWindow.show()
    sys.exit(app.exec_())