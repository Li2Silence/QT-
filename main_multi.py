'''
多线程减少界面卡顿
'''

from mainwindow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import *
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from predict import predict
from PyQt5.Qt import (QApplication, QWidget, QPushButton,
                      QThread,QMutex,pyqtSignal)

qmut_1 = QMutex() # 创建线程锁
# qmut_2 = QMutex()
# 继承QThread
class Thread_1(QThread):  # 线程1
    def __init__(self, fname):
        super().__init__()
        self.fname = fname

    def run(self):
        qmut_1.lock() # 加锁
        result = predict(self.fname)
        qmut_1.unlock() # 解锁
        return result

class CamShow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)
        self.fileBtn.clicked.connect(self.loadImage)


    # 打开文件功能
    def loadImage(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, '请选择图片','.','图像文件(*.jpg *.jpeg *.png)')
        if self.fname:
            print(self.fname)
            self.Infolabel.setText("文件打开成功\n"+self.fname)
            # self.Imglabel.set
            jpg = QtGui.QPixmap(self.fname).scaled(self.Imglabel.width(), self.Imglabel.height())

            # print(jpg)
            self.Imglabel.setPixmap(jpg)


            # 开启线程
            self.thread_1 = Thread_1(self.fname)  # 创建线程
            result = self.thread_1.start()  # 开始线程

            # result = predict(self.fname)
            self.Infolabel.setText(result)



        else:
            # print("打开文件失败")
            self.Infolabel.setText("打开文件失败")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())
