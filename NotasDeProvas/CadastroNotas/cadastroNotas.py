# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroNotas.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 91, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(120, 90, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_cpf.setFont(font)
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")
        self.pushButton_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(410, 420, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_cancelar.setFont(font)
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setGeometry(QtCore.QRect(220, 420, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_salvar.setFont(font)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.spinBox_matematica = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_matematica.setGeometry(QtCore.QRect(690, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBox_matematica.setFont(font)
        self.spinBox_matematica.setMaximum(20)
        self.spinBox_matematica.setObjectName("spinBox_matematica")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox_portugues = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_portugues.setGeometry(QtCore.QRect(690, 270, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBox_portugues.setFont(font)
        self.spinBox_portugues.setMaximum(20)
        self.spinBox_portugues.setObjectName("spinBox_portugues")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox_cg = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_cg.setGeometry(QtCore.QRect(690, 310, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBox_cg.setFont(font)
        self.spinBox_cg.setMaximum(10)
        self.spinBox_cg.setObjectName("spinBox_cg")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 350, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.spinBox_ce = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ce.setGeometry(QtCore.QRect(690, 350, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBox_ce.setFont(font)
        self.spinBox_ce.setMaximum(50)
        self.spinBox_ce.setObjectName("spinBox_ce")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 350, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 310, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 270, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 230, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 20, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 150, 691, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CPF:"))
        self.label_3.setText(_translate("MainWindow", "Matemática"))
        self.pushButton_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar notas"))
        self.label_4.setText(_translate("MainWindow", "Português"))
        self.label_5.setText(_translate("MainWindow", "Conhecimentos Gerais"))
        self.label_6.setText(_translate("MainWindow", "Conhecimentos Específicos"))
        self.label_2.setText(_translate("MainWindow", "-----------------------------------------------"))
        self.label_7.setText(_translate("MainWindow", "------------------------------------------------------------------"))
        self.label_8.setText(_translate("MainWindow", "----------------------------------------------------------------------"))
        self.label_9.setText(_translate("MainWindow", "------------------------------------------------------------------------"))
        self.label_10.setText(_translate("MainWindow", "Cadastro de Notas dos Candidatos"))
        self.label_11.setText(_translate("MainWindow", "Selecione a quantidade de questões acertadas em cada prova do candidato:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
