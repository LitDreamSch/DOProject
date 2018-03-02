# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot,QFile
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_demo import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    MainBTNSelect = 1
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # QSS
        with open("style.qss","r") as f:
            qss = f.read()
        self.setStyleSheet(qss)

    def ClearMainBtn(self):
        self.setStyleSheet('''.QPushButton:hover {
                                  border-image: url(:/button/img/btn_s.png);
                                }''')
        self.pushButton.setStyleSheet("border-image: url(:/button/img/btn_n.png);")
        self.pushButton_2.setStyleSheet("border-image: url(:/button/img/btn_n.png);")
        self.pushButton_3.setStyleSheet("border-image: url(:/button/img/btn_n.png);")
        self.pushButton_4.setStyleSheet("border-image: url(:/button/img/btn_n.png);")
        self.pushButton_5.setStyleSheet("border-image: url(:/button/img/btn_n.png);")

    @pyqtSlot()
    def on_pushButton_clicked(self):# 收件箱
        """
        Slot documentation goes here.
        """
        print(self.MainBTNSelect)
        if self.MainBTNSelect != 1:# 更换选项卡到收件箱页面
            self.MainBTNSelect = 1
            self.ClearMainBtn()
            self.pushButton.setStyleSheet("border-image:url(:/button/img/btn_c.png)")

    @pyqtSlot()
    def on_pushButton_2_clicked(self):# 写邮件
        """
        Slot documentation goes here.
        """
        print(self.MainBTNSelect)
        if self.MainBTNSelect != 2:# 更换选项卡到收件箱页面
            self.MainBTNSelect = 2
            self.ClearMainBtn()
            self.pushButton_2.setStyleSheet("border-image:url(:/button/img/btn_c.png)")

    @pyqtSlot()
    def on_pushButton_3_clicked(self):# 联系人
        """
        Slot documentation goes here.
        """
        print(self.MainBTNSelect)
        if self.MainBTNSelect != 3:# 更换选项卡到收件箱页面
            self.MainBTNSelect = 3
            self.ClearMainBtn()
            self.pushButton_3.setStyleSheet("border-image:url(:/button/img/btn_c.png)")

    @pyqtSlot()
    def on_pushButton_4_clicked(self):# 个人
        """
        Slot documentation goes here.
        """
        print(self.MainBTNSelect)
        if self.MainBTNSelect != 4:# 更换选项卡到收件箱页面
            self.MainBTNSelect = 4
            self.ClearMainBtn()
            self.pushButton_4.setStyleSheet("border-image:url(:/button/img/btn_c.png)")

    @pyqtSlot()
    def on_pushButton_5_clicked(self):# 发件箱
        """
        Slot documentation goes here.
        """
        print(self.MainBTNSelect)
        if self.MainBTNSelect != 5:# 更换选项卡到收件箱页面
            self.MainBTNSelect = 5
            self.ClearMainBtn()
            self.pushButton_5.setStyleSheet("border-image:url(:/button/img/btn_c.png)")



import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
