# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from Ui_mainUI import Ui_MainWindow
from PyQt5 import QtWidgets
import json
from PyQt5.QtWidgets import QMessageBox
from test_tool import test_ecjtu as tool

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        self.user=json.load(open('user.json'))

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.center()
        self.t = tool()
        self.n=0
        self.key_value=list()
        # self.checkBox.setCheckState(Qt_CheckState=bool(self.user['check']))
        if self.user['check']=='True':
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)
        self.username.setText(self.user['username'])
        self.password.setText(self.user['password'])
        self.file_dialog=QtWidgets.QFileDialog()


    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    @pyqtSlot()
    def on_logBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.t.username = self.username.text()
        self.t.password = self.password.text()
        self.t.login()
    
    @pyqtSlot()
    def on_readTable_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.file_dialog.parent()
        try:
            self.my_file_path = self.file_dialog.getOpenFileName(parent=self, caption=u'打开文件', directory='/')

            print(self.my_file_path)
            self.t.fileUrl = self.my_file_path[0]
            self.key_value=self.t.toTable()
        except IOError:
            print('open_error')

    @pyqtSlot()
    def on_checkBox_pressed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if not self.checkBox.isChecked():
            self.user['check']="True"

            self.user['username']=self.username.text()
            self.user['password']=self.password.text()
            json.dump(self.user,open('user.json','w'))
        else:
            self.user['check']="False"
            self.user['username']='admin'
            self.user['password']='admin'
            json.dump(self.user, open('user.json', 'w'))

    @pyqtSlot()
    def on_NextData_clicked(self):
        """
        Slot documentation goes here.
        """
        print(self.key_value)
        # TODO: not implemented yet
        if self.tableUrl.text()=='':
            reply = QMessageBox.information(self, "警告", "未输入有效url,继续输入点击yes,否则退出程序.", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                sys.exit(1)
        else:
            # self.t.table_url=self.tableUrl.text()
            self.t.openTableUrl(self.tableUrl.text())
            self.to_key_value(self.n)
            self.n+=1

    def to_key_value(self,n):
        for i in self.key_value[n]:
            self.t.to_one(i[0],i[1])

    @pyqtSlot()
    def on_SingleBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        data=self.SingleData.toPlainText()
        self.t.openTableUrl(self.tableUrl.text())
        kv=json.loads(data)

        for i in kv.keys():
            self.t.to_one(i,kv[i])





if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

