# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5.Qt import QThread, QSplashScreen, QPixmap
from Ui_MainWindow import Ui_MainWindow
from FindFun import GetInfo
import threading

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    names = []
    sizes = []
    times = []
    mages = []
    FindingThread = threading.Thread(target = GetInfo)
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self): # 检索按钮
        """
        Slot documentation goes here.
        """

        if self.lineEdit.text() == '':# 如果检索输入栏为空
            QMessageBox.information(self,"提示","没有输入检索内容")
            return

        self.listWidget.clear()
        self.names.clear()
        self.sizes.clear()
        self.times.clear()
        self.mages.clear()
        # 开始检索

        # self.names,self.sizes,self.times,self.mages = GetInfo(self.lineEdit.text())
        if self.FindingThread.isAlive() is False:
            self.FindingThread = threading.Thread(target = GetInfo, args=(self.lineEdit.text(),self))
        self.pushButton.setDisabled(True)

        splash = QSplashScreen(QPixmap(":/pic/waiting.png"))
        splash.show()
        app.processEvents()
        self.FindingThread.start()
        while self.FindingThread.isAlive():
            continue
        self.pushButton.setDisabled(False)
        splash.finish(self)
        QMessageBox.information(self,"检索完毕","共检索到"+str(len(self.names))+"个结果")

        # 添加结果到listWidget
        for i in self.names:
            self.listWidget.addItem(i)

    @pyqtSlot(int)
    def on_listWidget_currentRowChanged(self, currentRow):# 当选择的项目更变的时候
        """
        Slot documentation goes here.

        @param currentRow DESCRIPTION
        @type int
        """
        self.lineEdit_2.setText(self.names[currentRow])
        self.lineEdit_3.setText(self.sizes[currentRow])
        self.lineEdit_4.setText(self.times[currentRow])
        self.textBrowser.setText(self.mages[currentRow])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setFixedSize(612,406)
    ui.show()
    sys.exit(app.exec_())
