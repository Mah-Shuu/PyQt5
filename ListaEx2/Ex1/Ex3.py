# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ex3.ui'
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
        self.input_button = QtWidgets.QPushButton(self.centralwidget)
        self.input_button.setGeometry(QtCore.QRect(329, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_button.setFont(font)
        self.input_button.setObjectName("input_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 351, 125, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.output_num = QtWidgets.QLabel(self.centralwidget)
        self.output_num.setGeometry(QtCore.QRect(391, 351, 161, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.output_num.setFont(font)
        self.output_num.setText("")
        self.output_num.setObjectName("output_num")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 210, 419, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.numA = QtWidgets.QVBoxLayout()
        self.numA.setObjectName("numA")
        self.label_num1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_num1.setFont(font)
        self.label_num1.setObjectName("label_num1")
        self.numA.addWidget(self.label_num1)
        self.input_num1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_num1.setObjectName("input_num1")
        self.numA.addWidget(self.input_num1)
        self.horizontalLayout.addLayout(self.numA)
        self.numB = QtWidgets.QVBoxLayout()
        self.numB.setObjectName("numB")
        self.label_num2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_num2.setFont(font)
        self.label_num2.setObjectName("label_num2")
        self.numB.addWidget(self.label_num2)
        self.input_num2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_num2.setObjectName("input_num2")
        self.numB.addWidget(self.input_num2)
        self.horizontalLayout.addLayout(self.numB)
        self.numC = QtWidgets.QVBoxLayout()
        self.numC.setObjectName("numC")
        self.label_num3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_num3.setFont(font)
        self.label_num3.setObjectName("label_num3")
        self.numC.addWidget(self.label_num3)
        self.input_num3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_num3.setObjectName("input_num3")
        self.numC.addWidget(self.input_num3)
        self.horizontalLayout.addLayout(self.numC)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNovo = QtWidgets.QAction(MainWindow)
        self.actionNovo.setObjectName("actionNovo")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuArquivo.addAction(self.actionNovo)
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_button.setText(_translate("MainWindow", "Comparar"))
        self.label.setText(_translate("MainWindow", "O maior número é:"))
        self.label_num1.setText(_translate("MainWindow", "Número A"))
        self.label_num2.setText(_translate("MainWindow", "Número B"))
        self.label_num3.setText(_translate("MainWindow", "Número C"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionNovo.setText(_translate("MainWindow", "Novo"))
        self.actionNovo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSair.setShortcut(_translate("MainWindow", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
