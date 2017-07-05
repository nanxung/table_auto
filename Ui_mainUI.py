# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cb/桌面/table_auto/mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(700, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/lo/logo3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.username = QtWidgets.QLineEdit(self.centralWidget)
        self.username.setGeometry(QtCore.QRect(80, 20, 171, 31))
        self.username.setObjectName("username")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 51, 51))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self.centralWidget)
        self.password.setGeometry(QtCore.QRect(320, 20, 171, 31))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.logBtn = QtWidgets.QPushButton(self.centralWidget)
        self.logBtn.setGeometry(QtCore.QRect(20, 370, 151, 71))
        self.logBtn.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.logBtn.setObjectName("logBtn")
        self.readTable = QtWidgets.QPushButton(self.centralWidget)
        self.readTable.setGeometry(QtCore.QRect(30, 70, 621, 51))
        self.readTable.setStyleSheet("")
        self.readTable.setObjectName("readTable")
        self.tableUrl = QtWidgets.QLineEdit(self.centralWidget)
        self.tableUrl.setGeometry(QtCore.QRect(170, 300, 471, 31))
        self.tableUrl.setObjectName("tableUrl")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 290, 131, 51))
        self.label_3.setObjectName("label_3")
        self.NextData = QtWidgets.QPushButton(self.centralWidget)
        self.NextData.setGeometry(QtCore.QRect(450, 350, 191, 111))
        self.NextData.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.NextData.setObjectName("NextData")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(520, 20, 131, 31))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 131, 51))
        self.label_4.setObjectName("label_4")
        self.SingleData = QtWidgets.QTextEdit(self.centralWidget)
        self.SingleData.setGeometry(QtCore.QRect(170, 130, 471, 151))
        self.SingleData.setAcceptRichText(False)
        self.SingleData.setObjectName("SingleData")
        self.SingleBtn = QtWidgets.QPushButton(self.centralWidget)
        self.SingleBtn.setGeometry(QtCore.QRect(240, 360, 151, 91))
        self.SingleBtn.setObjectName("SingleBtn")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(20, 470, 641, 121))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动化表单填写工具"))
        self.label.setText(_translate("MainWindow", "账号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.logBtn.setText(_translate("MainWindow", "登录系统"))
        self.readTable.setText(_translate("MainWindow", "读取json数据文件"))
        self.label_3.setText(_translate("MainWindow", "表格URL地址"))
        self.NextData.setText(_translate("MainWindow", "填入下一条数据"))
        self.checkBox.setText(_translate("MainWindow", "记住账号密码"))
        self.label_4.setText(_translate("MainWindow", "输入单条数据用例"))
        self.SingleBtn.setText(_translate("MainWindow", "单点测试"))
        self.label_5.setText(_translate("MainWindow", "作者:南寻\n"
"\n"
"Life is short , I use Python!\n"
"\n"
"github主页：https://github.com/nanxung"))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

