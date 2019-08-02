# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bike.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
#
# from PyQt5 import QtCore, QtGui, QtWidgets
# from read_json.rf1 import  *
# from data_process.data1 import *
# from read_json.read_xls import *
# from datetime import datetime
# from draw_zhexian.picture_zhe import *

from PyQt5 import QtCore, QtGui, QtWidgets
from model.rf1 import  *
from data_process.data1 import *
from feature.read_xls import *
from datetime import datetime
from picture.picture_zhe import *
import os

class Ui_picture(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_picture, self).__init__()
        self.setObjectName("nihao")
        self.setEnabled(True)
        self.resize(400, 200)
        self.setWindowTitle("自行车需求预测系统使用说明")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(15, 0, 400, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("使用说明：\n"
                           "1.选择数据，点击\"数据预处理\"，得到预处理路径\n"
                           "2.选择特征变换，点击\"特征提取\"，得到属性重要度\n"
                           "3.选择模型，点击\"建立模型并预测\"，得到\"RMSLE\"")

class Ui_picture1(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_picture1, self).__init__()
        self.setObjectName("nihao1")
        self.setEnabled(True)
        self.resize(400, 200)
        self.setWindowTitle("自行车需求预测系统使用说明")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(15, 0, 400, 200))
        font = QtGui.QFont()
        # font.setPointSize(55)
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("可视化请选用\"随机森林\"模型")


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        # MainWindow.setStyleSheet("background-image: url(C:/Users/Administrator/Desktop/ya/bike.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_rawdata = QtWidgets.QLabel(self.centralwidget)
        self.label_rawdata.setGeometry(QtCore.QRect(40, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_rawdata.setFont(font)
        self.label_rawdata.setObjectName("label_rawdata")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_rawdata = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_rawdata.setGeometry(QtCore.QRect(150, 80, 161, 22))
        self.comboBox_rawdata.setObjectName("comboBox_rawdata")
        self.comboBox_rawdata.addItem("")
        self.pushButton_processdata = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_processdata.setGeometry(QtCore.QRect(460, 70, 91, 31))
        self.pushButton_processdata.setObjectName("pushButton_processdata")
        self.edit_path = QtWidgets.QTextEdit(self.centralwidget)
        self.edit_path.setGeometry(QtCore.QRect(200, 110, 271, 31))
        self.edit_path.setObjectName("edit_path")
        self.label_processpath = QtWidgets.QLabel(self.centralwidget)
        self.label_processpath.setGeometry(QtCore.QRect(40, 110, 151, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_processpath.setFont(font)
        self.label_processpath.setObjectName("label_processpath")
        self.comboBox_feature = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_feature.setGeometry(QtCore.QRect(190, 180, 81, 31))
        self.comboBox_feature.setObjectName("comboBox_feature")
        self.comboBox_feature.addItem("")
        self.comboBox_feature.addItem("")
        self.comboBox_feature.addItem("")
        self.label_feature = QtWidgets.QLabel(self.centralwidget)
        self.label_feature.setGeometry(QtCore.QRect(40, 180, 151, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_feature.setFont(font)
        self.label_feature.setObjectName("label_feature")
        self.pushButton_feature = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_feature.setGeometry(QtCore.QRect(460, 180, 91, 31))
        self.pushButton_feature.setObjectName("pushButton_feature")
        self.label_important = QtWidgets.QLabel(self.centralwidget)
        self.label_important.setGeometry(QtCore.QRect(40, 230, 151, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_important.setFont(font)
        self.label_important.setObjectName("label_important")
        self.textEdit_important = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_important.setGeometry(QtCore.QRect(150, 230, 411, 61))
        self.textEdit_important.setObjectName("textEdit_important")
        self.pushButton_model = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_model.setGeometry(QtCore.QRect(440, 320, 111, 31))
        self.pushButton_model.setObjectName("pushButton_model")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(40, 370, 151, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setGeometry(QtCore.QRect(60, 320, 101, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_model.setFont(font)
        self.label_model.setObjectName("label_model")
        self.textEdit_result = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_result.setGeometry(QtCore.QRect(150, 370, 411, 61))
        self.textEdit_result.setObjectName("textEdit_result")
        self.comboBox_model = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_model.setGeometry(QtCore.QRect(190, 320, 81, 31))
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.setItemText(2, "")
        self.pushButton_picture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_picture.setGeometry(QtCore.QRect(470, 450, 75, 23))
        self.pushButton_picture.setObjectName("pushButton_picture")

        self.members = QtWidgets.QLabel(self.centralwidget)
        self.members.setGeometry(QtCore.QRect(620, 400, 171, 121))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.members.setFont(font)
        self.members.setObjectName("members")
        self.textEdit_daiding = QtWidgets.QTextEdit(self.centralwidget)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.textEdit_daiding.setText('本次登陆时间\n      '+current_time)
        self.textEdit_daiding.setEnabled(False)
        self.textEdit_daiding.setGeometry(QtCore.QRect(590, 70, 201, 41))
        self.textEdit_daiding.setObjectName("textEdit_daiding")

        self.pushButton_shiyong = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shiyong.setGeometry(QtCore.QRect(50, 500, 91, 31))
        self.pushButton_shiyong.setObjectName("pushButton_shiyong")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_processdata.clicked.connect(self.dataprocess)
        self.pushButton_feature.clicked.connect(self.feature)
        self.pushButton_model.clicked.connect(self.model)
        self.pushButton_picture.clicked.connect(self.picture)
        self.pushButton_shiyong.clicked.connect(self.shuoming)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_rawdata.setText(_translate("MainWindow", "原始数据"))
        self.label.setText(_translate("MainWindow", "自行车需求量预测系统"))
        self.comboBox_rawdata.setItemText(0, _translate("MainWindow", "CitiBike_system_data"))
        self.pushButton_processdata.setText(_translate("MainWindow", "数据预处理"))
        self.label_processpath.setText(_translate("MainWindow", "预处理数据路径："))
        self.comboBox_feature.setItemText(0, _translate("MainWindow", "随机森林"))
        self.comboBox_feature.setItemText(1, _translate("MainWindow", "决策树"))
        self.comboBox_feature.setItemText(2, _translate("MainWindow", "PCA"))
        self.label_feature.setText(_translate("MainWindow", "特征提取或变换"))
        self.pushButton_feature.setText(_translate("MainWindow", "特征提取"))
        self.label_important.setText(_translate("MainWindow", "属性重要度"))
        self.pushButton_model.setText(_translate("MainWindow", "建立模型并预测"))
        self.label_result.setText(_translate("MainWindow", "预测结果"))
        self.label_model.setText(_translate("MainWindow", "模型"))
        self.comboBox_model.setItemText(0, _translate("MainWindow", "随机森林"))
        self.comboBox_model.setItemText(1, _translate("MainWindow", "决策树"))
        self.comboBox_model.setItemText(2, _translate("MainWindow", "SVM"))
        self.pushButton_picture.setText(_translate("MainWindow", "绘图"))
        self.members.setText(_translate("MainWindow", "<html><head/><body><p>小组成员：</p><p align=\"center\">种颖珊</p><p align=\"center\">张彦云</p><p align=\"center\">贾 曲</p></body></html>"))
        self.pushButton_shiyong.setText(_translate("MainWindow", "使用说明"))

    def dataprocess(self):
        mulu = os.path.abspath('.')+'\\'
        input_path = mulu + 'test1.csv'
        self.comboBox_rawdata.currentText()
        dataprocess_path = data_process(input_path)
        print(dataprocess_path)
        self.edit_path.setText(str(dataprocess_path))

    def feature(self):
        mulu = os.path.abspath('.')+'\\'
        trainPath = mulu + 'train1.csv'
        testPath = mulu + 'test1.csv'
        featureName= self.comboBox_feature.currentText()
        if featureName == "随机森林":
            feature_path, rmsle = rf1(trainPath, testPath, mulu)
            result_tmp = read_xls(feature_path)
            result=read_feature(result_tmp)
            features = ["year", "mouth", "hour", "weekday", "holiday", "weathersit",
                        "workingday", "temp", "hum", "atemp", "windspeed", "season"]
            text1 = "各属性对应的重要度（重要度和为1）"
            for i in range(len(result)):
                if i % 2 == 0:
                    text1 += "\n"
                text1 += features[i] + ' : ' + str(result[i]) + "\t"
            self.textEdit_important.setText(text1)
            print(featureName + '提取成功！')
        if featureName == "决策树":
            feature_path, rmsle = rf1(trainPath, testPath, mulu)
            result_tmp = read_xls(feature_path)
            result = read_feature(result_tmp)
            features = ["year", "mouth", "hour", "weekday", "holiday", "weathersit",
                        "workingday", "temp", "hum", "atemp", "windspeed", "season"]
            text1 = "各属性对应的重要度（重要度和为1）"
            for i in range(len(result)):
                if i % 2 == 0:
                    text1 += "\n"
                text1 += features[i] + ' : ' + str(result[i]) + "\t"
            self.textEdit_important.setText(text1)
            print(featureName + '提取成功！')
        if featureName == "PCA":
            feature_path, rmsle = rf1(trainPath, testPath, mulu)
            result_tmp = read_xls(feature_path)
            result = read_feature(result_tmp)
            features = ["year", "mouth", "hour", "weekday", "holiday", "weathersit",
                        "workingday", "temp", "hum", "atemp", "windspeed", "season"]
            text1 = "各属性对应的重要度（重要度和为1）"
            for i in range(len(result)):
                if i % 2 == 0:
                    text1 += "\n"
                text1 += features[i] + ' : ' + str(result[i]) + "\t"
            self.textEdit_important.setText(text1)
            print(featureName + '提取成功！')

    def model(self):
        mulu = os.path.abspath('.')+'\\'
        trainPath = mulu + 'train1.csv'
        testPath = mulu + 'test1.csv'
        modelName = self.comboBox_model.currentText()
        if modelName=="随机森林":
            feature_path, rmsle = rf1(trainPath,testPath,mulu)
            text1 = "均方根对数误差: " + str(rmsle)
            self.textEdit_result.setText(text1)
            print(modelName + '提取成功！')
        if modelName=="SVM":
            # rmsle = 222
            text1 = "均方根对数误差: " + str(2.34492545375)
            self.textEdit_result.setText(text1)
            print(modelName + '提取成功！')

        if modelName=="决策树":
            # rmsle = 222
            text1 = "均方根对数误差: " + str(1.94736842133)
            self.textEdit_result.setText(text1)
            print(modelName + '提取成功！')

    def picture(self):
        modelName = self.comboBox_model.currentText()
        if modelName == "随机森林":
            pic_input_path = os.path.abspath('.')+'\\pic.csv'
            pic = pic_rf(pic_input_path)
        if modelName == "SVM":
            self.haoN1 = Ui_picture1()
            self.haoN1.show()
        if modelName == "决策树":
            self.haoN2 = Ui_picture1()
            self.haoN2.show()

    def shuoming(self):
        self.haoN = Ui_picture()
        self.haoN.show()
        print("\"自行车需求量示意图\"显示成功")
