# -*- coding: utf-8 -*-

from mainwindow2 import Ui_MainWindow
import time
import sys
import os
import re
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from pred import predict
from hogpred import predicthog
from predfine import predictfine
from PIL import Image
from zhixin import ROI
import cv2


class CamShow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)
        self.fileBtn.clicked.connect(self.loadImage)
        self.proce_img.clicked.connect(self.ResizeImage)
        self.recog.clicked.connect(self.Recognition)

        self.ResNet.clicked.connect(self.resnet_1)
        self.ResNet_HOG.clicked.connect(self.ResNet_H)
        self.Fine_ResNet.clicked.connect(self.ResNet_F)

    def loadImage(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, '请选择图片', '.', '图像文件(*.jpg *.bmp *.png)')

        if self.fname:
            jpg = QtGui.QPixmap(self.fname).scaled(640, 480)
            self.Imglabel.setPixmap(jpg)
        else:

            self.Infolabel.setText("打开文件失败")

    def ResizeImage(self):

        img = Image.open(self.fname)
        img = img.convert("L")
        img.save("temp.jpg")
        roiimg = ROI("temp.jpg")
        cv2.imwrite("roi_temp.jpg", roiimg)

        path = os.path.abspath("roi_temp.jpg")

        jpg = QtGui.QPixmap(path).scaled(481, 481)


        self.Imglabel.setPixmap(jpg)



    def resnet_1(self):
        global ResNet_, la
        la = 1
        ResNet_ = predict

        return ResNet_, la

    def ResNet_H(self):
        global ResNet_HOG, la
        la = 2
        ResNet_HOG = predicthog

        return ResNet_HOG, la

    def ResNet_F(self):
        global ResNet_Fine, la
        la = 3
        ResNet_Fine = predictfine

        return ResNet_Fine, la

    def Recognition(self):

        label = re.findall(r"\d+\.?\d*", self.fname)
        start = time.time()
        path = os.path.abspath("temp.jpg")
        x = la
        if x == 1:
            recog_result = ResNet_(path)
            end = time.time()
            sum_time = end - start
            true_label = int(float(label[0]))
            result = '真实类别：' + str(true_label) + '\n'+ recog_result + '\n'+ '运行时间：' + str('%.4f' % sum_time)
            self.Infolabel.setText(result)
        if x == 2:
            recog_result = ResNet_HOG(path)
            end = time.time()
            sum_time = end - start
            true_label = int(float(label[0]))
            result = '真实类别：' + str(true_label) + '\n'+ recog_result + '\n'+ '运行时间：' + str('%.4f' % sum_time)
            self.Infolabel.setText(result)
        if x == 3:
            recog_result = ResNet_Fine(path)
            end = time.time()
            sum_time = end - start
            true_label = int(float(label[0]))
            result = '真实类别：' + str(true_label) + '\n'+ recog_result + '\n'+ '运行时间：' + str('%.4f' % sum_time)
            self.Infolabel.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())
