#!/usr/bin/env python
'''RMS ROS Node'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RMS.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RMS(object):
    def setupUi(self, RMS):
        RMS.setObjectName("RMS")
        RMS.resize(967, 702)
        self.centralwidget = QtWidgets.QWidget(RMS)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MsgFm = QtWidgets.QFrame(self.centralwidget)
        self.MsgFm.setMaximumSize(QtCore.QSize(1000, 123))
        self.MsgFm.setFrameShape(QtWidgets.QFrame.Box)
        self.MsgFm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MsgFm.setObjectName("MsgFm")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.MsgFm)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.MsgFm)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.MsgFm, 1, 0, 1, 3)
        self.SettingFM = QtWidgets.QFrame(self.centralwidget)
        self.SettingFM.setEnabled(True)
        self.SettingFM.setMinimumSize(QtCore.QSize(200, 400))
        self.SettingFM.setMaximumSize(QtCore.QSize(300, 500))
        self.SettingFM.setFrameShape(QtWidgets.QFrame.Box)
        self.SettingFM.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SettingFM.setObjectName("SettingFM")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SettingFM)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StationKeeping = QtWidgets.QFrame(self.SettingFM)
        self.StationKeeping.setMaximumSize(QtCore.QSize(500, 100))
        self.StationKeeping.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StationKeeping.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StationKeeping.setObjectName("StationKeeping")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.StationKeeping)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.StationKeeping)
        self.checkBox_1.setStyleSheet("")
        self.checkBox_1.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout_2.addWidget(self.checkBox_1, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.StationKeeping)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.PositionKeeping_Lat = QtWidgets.QLineEdit(self.StationKeeping)
        self.PositionKeeping_Lat.setObjectName("PositionKeeping_Lat")
        self.gridLayout_2.addWidget(self.PositionKeeping_Lat, 1, 1, 1, 1)
        self.PositionKeeping_Lon = QtWidgets.QLineEdit(self.StationKeeping)
        self.PositionKeeping_Lon.setObjectName("PositionKeeping_Lon")
        self.gridLayout_2.addWidget(self.PositionKeeping_Lon, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.StationKeeping)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.StationKeeping)
        self.PathFollowing = QtWidgets.QFrame(self.SettingFM)
        self.PathFollowing.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PathFollowing.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PathFollowing.setObjectName("PathFollowing")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.PathFollowing)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_2 = QtWidgets.QCheckBox(self.PathFollowing)
        self.checkBox_2.setStyleSheet("")
        self.checkBox_2.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 0, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.PathFollowing)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)
        self.Point1_Lat = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point1_Lat.setObjectName("Point1_Lat")
        self.gridLayout_5.addWidget(self.Point1_Lat, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.PathFollowing)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 1, 2, 1, 1)
        self.Point1_Lon = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point1_Lon.setObjectName("Point1_Lon")
        self.gridLayout_5.addWidget(self.Point1_Lon, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.PathFollowing)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.PathFollowing)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 3, 0, 1, 1)
        self.Point2_Lat = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point2_Lat.setObjectName("Point2_Lat")
        self.gridLayout_5.addWidget(self.Point2_Lat, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.PathFollowing)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 3, 2, 1, 1)
        self.Point2_Lon = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point2_Lon.setObjectName("Point2_Lon")
        self.gridLayout_5.addWidget(self.Point2_Lon, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.PathFollowing)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 4, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.PathFollowing)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 5, 0, 1, 1)
        self.Point3_Lat = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point3_Lat.setObjectName("Point3_Lat")
        self.gridLayout_5.addWidget(self.Point3_Lat, 5, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.PathFollowing)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 5, 2, 1, 1)
        self.Point3_Lon = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point3_Lon.setObjectName("Point3_Lon")
        self.gridLayout_5.addWidget(self.Point3_Lon, 6, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.PathFollowing)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 6, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.PathFollowing)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 7, 0, 1, 1)
        self.Point4_Lat = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point4_Lat.setObjectName("Point4_Lat")
        self.gridLayout_5.addWidget(self.Point4_Lat, 7, 1, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.PathFollowing)
        self.label_50.setObjectName("label_50")
        self.gridLayout_5.addWidget(self.label_50, 7, 2, 1, 1)
        self.Point4_Lon = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point4_Lon.setObjectName("Point4_Lon")
        self.gridLayout_5.addWidget(self.Point4_Lon, 8, 1, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.PathFollowing)
        self.label_49.setObjectName("label_49")
        self.gridLayout_5.addWidget(self.label_49, 8, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.PathFollowing)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 9, 0, 1, 1)
        self.Point5_Lat = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point5_Lat.setObjectName("Point5_Lat")
        self.gridLayout_5.addWidget(self.Point5_Lat, 9, 1, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.PathFollowing)
        self.label_52.setObjectName("label_52")
        self.gridLayout_5.addWidget(self.label_52, 9, 2, 1, 1)
        self.Point5_Lon = QtWidgets.QLineEdit(self.PathFollowing)
        self.Point5_Lon.setObjectName("Point5_Lon")
        self.gridLayout_5.addWidget(self.Point5_Lon, 10, 1, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.PathFollowing)
        self.label_51.setObjectName("label_51")
        self.gridLayout_5.addWidget(self.label_51, 10, 2, 1, 1)
        self.verticalLayout.addWidget(self.PathFollowing)
        self.gridLayout.addWidget(self.SettingFM, 0, 0, 1, 1)
        self.DisFm = QtWidgets.QFrame(self.centralwidget)
        self.DisFm.setMinimumSize(QtCore.QSize(500, 0))
        self.DisFm.setFrameShape(QtWidgets.QFrame.Box)
        self.DisFm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DisFm.setObjectName("DisFm")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.DisFm)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PushButton_start = QtWidgets.QPushButton(self.DisFm)
        self.PushButton_start.setObjectName("PushButton_start")
        self.gridLayout_4.addWidget(self.PushButton_start, 0, 0, 1, 1)
        self.PushButton_quit = QtWidgets.QPushButton(self.DisFm)
        self.PushButton_quit.setObjectName("PushButton_quit")
        self.gridLayout_4.addWidget(self.PushButton_quit, 0, 3, 1, 1)
        self.PushButton_suspend = QtWidgets.QPushButton(self.DisFm)
        self.PushButton_suspend.setObjectName("PushButton_suspend")
        self.gridLayout_4.addWidget(self.PushButton_suspend, 0, 1, 1, 1)
        self.PushButton_save = QtWidgets.QPushButton(self.DisFm)
        self.PushButton_save.setObjectName("PushButton_save")
        self.gridLayout_4.addWidget(self.PushButton_save, 0, 2, 1, 1)
        self.Map = QtWidgets.QFrame(self.DisFm)
        self.Map.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Map.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Map.setObjectName("Map")
        self.gridLayout_4.addWidget(self.Map, 1, 0, 1, 4)
        self.Status = QtWidgets.QFrame(self.DisFm)
        self.Status.setMaximumSize(QtCore.QSize(2000, 40))
        self.Status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Status.setObjectName("Status")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Status)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.Status)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Date = QtWidgets.QLineEdit(self.Status)
        self.Date.setObjectName("Date")
        self.horizontalLayout.addWidget(self.Date)
        self.label_4 = QtWidgets.QLabel(self.Status)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.Lat_real = QtWidgets.QLineEdit(self.Status)
        self.Lat_real.setObjectName("Lat_real")
        self.horizontalLayout.addWidget(self.Lat_real)
        self.label_5 = QtWidgets.QLabel(self.Status)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.Lon_real = QtWidgets.QLineEdit(self.Status)
        self.Lon_real.setObjectName("Lon_real")
        self.horizontalLayout.addWidget(self.Lon_real)
        self.gridLayout_4.addWidget(self.Status, 2, 0, 1, 4)
        self.gridLayout.addWidget(self.DisFm, 0, 1, 1, 2)
        RMS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RMS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 28))
        self.menubar.setObjectName("menubar")
        RMS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RMS)
        self.statusbar.setObjectName("statusbar")
        RMS.setStatusBar(self.statusbar)

        self.retranslateUi(RMS)
        QtCore.QMetaObject.connectSlotsByName(RMS)

    def retranslateUi(self, RMS):
        _translate = QtCore.QCoreApplication.translate
        RMS.setWindowTitle(_translate("RMS", "WaveGlider远程监控系统"))
        self.checkBox_1.setText(_translate("RMS", "PositionKeeping"))
        self.label_3.setText(_translate("RMS", "Lon:"))
        self.label_2.setText(_translate("RMS", "Lat:"))
        self.checkBox_2.setText(_translate("RMS", "PathFollowing"))
        self.label_12.setText(_translate("RMS", "Point_1"))
        self.label_7.setText(_translate("RMS", "Lat"))
        self.label_13.setText(_translate("RMS", "Lon"))
        self.label_8.setText(_translate("RMS", "Point_2"))
        self.label_14.setText(_translate("RMS", "Lat"))
        self.label_15.setText(_translate("RMS", "Lon"))
        self.label_9.setText(_translate("RMS", "Point_3"))
        self.label_26.setText(_translate("RMS", "Lat"))
        self.label_25.setText(_translate("RMS", "Lon"))
        self.label_10.setText(_translate("RMS", "Point_4"))
        self.label_50.setText(_translate("RMS", "Lat"))
        self.label_49.setText(_translate("RMS", "Lon"))
        self.label_11.setText(_translate("RMS", "Point_5"))
        self.label_52.setText(_translate("RMS", "Lat"))
        self.label_51.setText(_translate("RMS", "Lon"))
        self.PushButton_start.setText(_translate("RMS", "Start"))
        self.PushButton_quit.setText(_translate("RMS", "Quit"))
        self.PushButton_suspend.setText(_translate("RMS", "Suspend"))
        self.PushButton_save.setText(_translate("RMS", "Save"))
        self.label.setText(_translate("RMS", "Date"))
        self.label_4.setText(_translate("RMS", "Lat"))
        self.label_5.setText(_translate("RMS", "Lon"))
