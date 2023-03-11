# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 900)  # 947, 907

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)


        self.groupBox.setGeometry(QtCore.QRect(80, 20, 800, 651))  # 静脉图像显示窗口10, 20, 851, 651 左 上 右 下
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(r'qt2.jpg')))
        self.setPalette(window_pale)


        self.groupBox.setObjectName("groupBox")
        self.Imglabel = QtWidgets.QLabel(self.groupBox)
        self.Imglabel.setGeometry(QtCore.QRect(110, 50, 681, 571))   # 修改主界面图片的位置
        self.Imglabel.setText("")
        self.Imglabel.setObjectName("Imglabel")


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(660, 690, 240, 151))  # 识别结果显示 350, 690, 521, 151
        self.groupBox_2.setObjectName("groupBox_2")


        self.Infolabel = QtWidgets.QLabel(self.groupBox_2)
        self.Infolabel.setGeometry(QtCore.QRect(20, 40, 461, 61))
        self.Infolabel.setText("")
        self.Infolabel.setObjectName("Infolabel")


        self.fileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fileBtn.setGeometry(QtCore.QRect(20, 690, 140, 151))  # 选择静脉图像窗口 40, 690, 271, 151
        self.fileBtn.setObjectName("fileBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.proce_img = QtWidgets.QPushButton(self.centralwidget)
        self.proce_img.setGeometry(QtCore.QRect(180, 690, 140, 151))  # 数据预处理 40, 690, 271, 151
        self.proce_img.setObjectName("fileBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.img_proce = QtWidgets.QMenuBar(MainWindow)
        self.img_proce.setGeometry(QtCore.QRect(0, 0, 947, 26))
        self.img_proce.setObjectName("menubar")
        MainWindow.setMenuBar(self.img_proce)

        """
        模型选择
        """
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 680, 140, 161))  # 识别结果显示 350, 690, 521, 151
        self.groupBox_3.setObjectName("groupBox_2")

        self.ResNet = QtWidgets.QPushButton(self.centralwidget)
        self.ResNet.setGeometry(QtCore.QRect(360, 710, 100, 30))
        self.ResNet.setObjectName("fileBtn")
        MainWindow.setCentralWidget(self.centralwidget)


        self.ResNet_HOG = QtWidgets.QPushButton(self.centralwidget)
        self.ResNet_HOG.setGeometry(QtCore.QRect(360, 755, 100, 30))
        self.ResNet_HOG.setObjectName("fileBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.ResNet_HOG_ = QtWidgets.QMenuBar(MainWindow)
        self.ResNet_HOG_.setGeometry(QtCore.QRect(0, 0, 947, 26))
        self.ResNet_HOG_.setObjectName("menubar")
        MainWindow.setMenuBar(self.ResNet_HOG_)


        self.Fine_ResNet = QtWidgets.QPushButton(self.centralwidget)
        self.Fine_ResNet.setGeometry(QtCore.QRect(360, 800, 100, 30))
        self.Fine_ResNet.setObjectName("fileBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.Fine_ResNet_ = QtWidgets.QMenuBar(MainWindow)
        self.Fine_ResNet_.setGeometry(QtCore.QRect(0, 0, 947, 26))
        self.Fine_ResNet_.setObjectName("menubar")
        MainWindow.setMenuBar(self.Fine_ResNet_)


        self.recog = QtWidgets.QPushButton(self.centralwidget)
        self.recog.setGeometry(QtCore.QRect(500, 690, 140, 151))  # 开始识别 40, 690, 271, 151
        self.recog.setObjectName("fileBtn")
        MainWindow.setCentralWidget(self.centralwidget)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "手背静脉识别系统"))
        self.groupBox.setTitle(_translate("MainWindow", "静脉图像显示窗口"))

        self.groupBox_2.setTitle(_translate("MainWindow", "识别结果显示"))
        self.groupBox_3.setTitle(_translate("MainWindow", "模型选择"))
        self.ResNet.setText(_translate("MainWindow", "ResNet"))
        self.ResNet_HOG.setText(_translate("MainWindow", "ResNet_HOG"))
        self.Fine_ResNet.setText(_translate("MainWindow", "LK-ResNet"))


        self.fileBtn.setText(_translate("MainWindow", "选择静脉图像"))
        self.proce_img.setText(_translate("MainWindow", "数据预处理"))
        self.recog.setText(_translate("MainWindow", "开始识别"))
