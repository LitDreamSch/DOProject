# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from Ui_MainWindow import Ui_MainWindow
import threading
import time
import win32api
import win32con
import inspect
import ctypes

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

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def Attack(Lcd1, Lcd2, speed):
    Inspect = 60/speed
    while True:
        win32api.keybd_event(17,0,0,0)
        win32api.keybd_event(86,0,0,0)
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        Lcd1.display(Lcd1.value()+1)
        Lcd2.display(Lcd2.value()+1)
        time.sleep(Inspect)



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    startAttack = False
    AttackThread = threading.Thread(target = Attack)

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot(int)
    def on_dial_valueChanged(self, value):
        """
        Slot documentation goes here.

        @param value DESCRIPTION
        @type int
        """
        self.lcdNumber.display(value)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        _translate = QtCore.QCoreApplication.translate
        # TODO: not implemented yet
        if self.startAttack == False: # start attack
            time.sleep(1)
            self.pushButton.setText("STOP")
            self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#16ff06;\">●</span></p></body></html>"))
            self.startAttack = True
            self.dial.setEnabled(False)
            if self.AttackThread.isAlive() is False:
                self.AttackThread = threading.Thread(target = Attack, args=(self.lcdNumber_2, self.lcdNumber_3, self.lcdNumber.value()))
            self.AttackThread.start()


        else:# stop attack
            stop_thread(self.AttackThread)
            self.dial.setEnabled(True)
            self.pushButton.setText("LAUNCH")
            self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0004;\">●</span></p></body></html>"))
            self.startAttack = False
            self.lcdNumber_2.display(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setFixedSize(220, 239)
    ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui.show()
    sys.exit(app.exec_())
