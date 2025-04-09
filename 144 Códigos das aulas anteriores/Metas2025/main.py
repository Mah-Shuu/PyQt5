from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from Listasdemetas import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botões às funções
        self.pushButton_AdicionarMeta.clicked.connect(self.add_meta)
        self.pushButton_RemoverMeta.clicked.connect(self.remove_meta)

        #Criar Funções dos botões
    def add_meta(self):
        meta = self.lineEdit.text()
        if meta:
            item = QListWidgetItem(meta)
            item.setCheckState(0)
            self.listWidget.addItem(item)
            self.lineEdit.clear()
        
    def remove_meta(self):
        selected_item = self.listWidget.currentRow()
        if selected_item >= 0:
            self.listWidget.takeItem(selected_item)

if __name__ == "__main__":
    app = QApplication([])
    window = main()
    window.show()
    app.exec_()
            
        