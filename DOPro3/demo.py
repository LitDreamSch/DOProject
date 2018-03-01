# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_demo import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    SelMainBtn = 1
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    def ClearMainButton(self):
        self.pushButton.setStyleSheet("border-image: url(:/button/img/btn_n.png);\n")
        self.pushButton_2.setStyleSheet("border-image: url(:/button/img/btn_n.png);\n")
        self.pushButton_3.setStyleSheet("border-image: url(:/button/img/btn_n.png);\n")
        self.pushButton_4.setStyleSheet("border-image: url(:/button/img/btn_n.png);\n")
        self.pushButton_5.setStyleSheet("border-image: url(:/button/img/btn_n.png);\n")

    @pyqtSlot()
    def on_pushButton_pressed(self):
        self.pushButton.setStyleSheet("border-image: url(:/button/img/btn_c.png);\n")

    @pyqtSlot()
    def on_pushButton_released(self):
        if self.SelMainBtn != 1:# 当焦点不在自己身上的时候
            self.SelMainBtn = 1
            self.ClearMainButton()
        self.pushButton.setStyleSheet("border-image: url(:/button/img/btn_s.png);\n")

    @pyqtSlot()
    def on_pushButton_2_pressed(self):
        self.pushButton_2.setStyleSheet("border-image: url(:/button/img/btn_c.png);\n")

    @pyqtSlot()
    def on_pushButton_2_released(self):
        if self.SelMainBtn != 2:# 当焦点不在自己身上的时候
            self.SelMainBtn = 2
            self.ClearMainButton()

        self.pushButton_2.setStyleSheet("border-image: url(:/button/img/btn_s.png);\n")

    @pyqtSlot()
    def on_pushButton_3_pressed(self):
        self.pushButton_3.setStyleSheet("border-image: url(:/button/img/btn_c.png);\n")

    @pyqtSlot()
    def on_pushButton_3_released(self):
        if self.SelMainBtn != 3:# 当焦点不在自己身上的时候
            self.ClearMainButton()
            self.SelMainBtn = 3

        self.pushButton_3.setStyleSheet("border-image: url(:/button/img/btn_s.png);\n")

    @pyqtSlot()
    def on_pushButton_4_pressed(self):
        self.pushButton_4.setStyleSheet("border-image: url(:/button/img/btn_c.png);\n")

    @pyqtSlot()
    def on_pushButton_4_released(self):
        if self.SelMainBtn != 4:# 当焦点不在自己身上的时候
            self.ClearMainButton()
            self.SelMainBtn = 4

        self.pushButton_4.setStyleSheet("border-image: url(:/button/img/btn_s.png);\n")

    @pyqtSlot()
    def on_pushButton_5_pressed(self):
        self.pushButton_5.setStyleSheet("border-image: url(:/button/img/btn_c.png);\n")

    @pyqtSlot()
    def on_pushButton_5_released(self):
        if self.SelMainBtn != 5:# 当焦点不在自己身上的时候
            self.ClearMainButton()
            self.SelMainBtn = 5

        self.pushButton_5.setStyleSheet("border-image: url(:/button/img/btn_s.png);\n")


import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
