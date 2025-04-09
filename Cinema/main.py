import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QPushButton
from cinema import Ui_MainWindow

class cinema(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label_fundo1.setHidden(True)
        self.ui.label_fundo2.setHidden(True)
        self.ui.label_fundo3.setHidden(True)
        self.ui.label_fundo4.setHidden(True)
        self.ui.label_sinopse1.setHidden(True)
        self.ui.label_sinopse2.setHidden(True)
        self.ui.label_sinopse3.setHidden(True)
        self.ui.label_sinopse4.setHidden(True)

        self.ui.pushButton_resumo1.clicked.connect(lambda: self.exibirResumo("1"))
        self.ui.pushButton_resumo2.clicked.connect(lambda: self.exibirResumo("2"))
        self.ui.pushButton_resumo3.clicked.connect(lambda: self.exibirResumo("3"))
        self.ui.pushButton_resumo4.clicked.connect(lambda: self.exibirResumo("4"))
        self.ui.pushButton_sessoes1.clicked.connect(lambda: self.exibirSessoes("1"))
        self.ui.pushButton_sessoes2.clicked.connect(lambda: self.exibirSessoes("2"))
        self.ui.pushButton_sessoes3.clicked.connect(lambda: self.exibirSessoes("3"))
        self.ui.pushButton_sessoes4.clicked.connect(lambda: self.exibirSessoes("4"))

    def trocarTexto(self,botao,fonte = "sessoes"): 
        match botao:
            case "1":
                if fonte == "sinopse":
                    self.ui.label_sinopse1.setText("Uma abelha sonha em se tornar uma guerreira, mas quando consegue, sente falta de sua antiga vida.")
                else:
                    self.ui.label_sinopse1.setText("Hoje: 09:00 | 14:00 | 19:00 Amanhâ: 09:00 | 14:00 | 19:00")
            case "2":
                if fonte == "sinopse":
                    self.ui.label_sinopse2.setText("Jota é um Jet Sky muito corajoso e curioso, mas vive se metendo em tremendas confusões em alto mar. É sempre o seu fiel e atrapalhado amigo Beto Bote e sua irmã Lili que o ajudam a sair das enrascadas que ele vive em Oceanópolis.")
                else:
                    self.ui.label_sinopse2.setText("Hoje: 09:00 | 14:00 | 19:00 Amanhâ: 09:00 | 14:00 | 19:00")
            case "3":
                if fonte == "sinopse":
                    self.ui.label_sinopse3.setText("Filme conta a história de Marcell Toing, um rato dono do famoso restaurante Ratatoing. Juntamente com Carol e Greg, ele sai em busca de ingredientes raros nos estabelecimentos dos humanos, enfrentando de ratoeiras a gatos famintos.")
                else:
                    self.ui.label_sinopse3.setText("Hoje: 09:00 | 14:00 | 19:00 Amanhâ: 09:00 | 14:00 | 19:00")
            case "4":
                if fonte == "sinopse":
                    self.ui.label_sinopse4.setText("Pancada é um faxineiro que trabalha no Bear Bar Box e seu maior sonho é estrelar um espetáculo de dança. Quando finalmente consegue dar asas à sua fantasia, seus planos mudam por uma brilhante ideia.")
                else:
                    self.ui.label_sinopse4.setText("Hoje: 09:00 | 14:00 | 19:00 Amanhâ: 09:00 | 14:00 | 19:00")



    def exibirResumo(self, botao):
        match botao:
            case "1":
                if self.ui.label_fundo1.isHidden() and self.ui.label_sinopse1.isHidden():
                    self.trocarTexto(botao,"sinopse")
                    self.ui.label_fundo1.setHidden(False)
                    self.ui.label_sinopse1.setHidden(False)
                else:
                    self.ui.label_fundo1.setHidden(True)
                    self.ui.label_sinopse1.setHidden(True)
            case "2":
                if self.ui.label_fundo2.isHidden() and self.ui.label_sinopse2.isHidden():
                    self.trocarTexto(botao,"sinopse")
                    self.ui.label_fundo2.setHidden(False)
                    self.ui.label_sinopse2.setHidden(False)
                else:
                    self.ui.label_fundo2.setHidden(True)
                    self.ui.label_sinopse2.setHidden(True)
            case "3":
                if self.ui.label_fundo3.isHidden() and self.ui.label_sinopse3.isHidden():
                    self.trocarTexto(botao,"sinopse")
                    self.ui.label_fundo3.setHidden(False)
                    self.ui.label_sinopse3.setHidden(False)
                else:
                    self.ui.label_fundo3.setHidden(True)
                    self.ui.label_sinopse3.setHidden(True)
            case "4":
                if self.ui.label_fundo4.isHidden() and self.ui.label_sinopse4.isHidden():
                    self.trocarTexto(botao,"sinopse")
                    self.ui.label_fundo4.setHidden(False)
                    self.ui.label_sinopse4.setHidden(False)
                else:
                    self.ui.label_fundo4.setHidden(True)
                    self.ui.label_sinopse4.setHidden(True)
            

    def exibirSessoes(self, botao):
        match botao:
            case "1":
                if self.ui.label_fundo1.isHidden() and self.ui.label_sinopse1.isHidden():
                    self.trocarTexto(botao)
                    self.ui.label_fundo1.setHidden(False)
                    self.ui.label_sinopse1.setHidden(False)
                else:
                    self.ui.label_fundo1.setHidden(True)
                    self.ui.label_sinopse1.setHidden(True)
            case "2":
                if self.ui.label_fundo2.isHidden() and self.ui.label_sinopse2.isHidden():
                    self.trocarTexto(botao)
                    self.ui.label_fundo2.setHidden(False)
                    self.ui.label_sinopse2.setHidden(False)
                else:
                    self.ui.label_fundo2.setHidden(True)
                    self.ui.label_sinopse2.setHidden(True)
            case "3":
                if self.ui.label_fundo3.isHidden() and self.ui.label_sinopse3.isHidden():
                    self.trocarTexto(botao)
                    self.ui.label_fundo3.setHidden(False)
                    self.ui.label_sinopse3.setHidden(False)
                else:
                    self.ui.label_fundo3.setHidden(True)
                    self.ui.label_sinopse3.setHidden(True)
            case "4":
                if self.ui.label_fundo4.isHidden() and self.ui.label_sinopse4.isHidden():
                    self.trocarTexto(botao)
                    self.ui.label_fundo4.setHidden(False)
                    self.ui.label_sinopse4.setHidden(False)
                else:
                    self.ui.label_fundo4.setHidden(True)
                    self.ui.label_sinopse4.setHidden(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = cinema()
    window.show()
    sys.exit(app.exec_())