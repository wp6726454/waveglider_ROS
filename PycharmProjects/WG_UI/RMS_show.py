from RMS import Ui_RMS
import rospy
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QTimer,QCoreApplication, QDateTime
from std_msgs.msg import UInt64MultiArray
#from PyQt5.QtGui import QPixmap
#import time

class RMS_show(QMainWindow,Ui_RMS):

    def __init__(self,parent=None):
        super(RMS_show,self).__init__(parent)
        self.setupUi(self)
        self.PrepWidgets()
        self.PrepParameters()
        self.CallBackFunctions()
        self.Timer=QTimer()
 #ros节点定义，并创建订阅者与发布者
        rospy.init_node('RMS_UI', anonymous=True)
        rate = rospy.Rate(10)  # 10hz
        self.pathfollowing_pub = rospy.Publisher('/waypoints', UInt64MultiArray, queue_size=10)
        self.stationkeeping_pub = rospy.Publisher('/set_point', UInt64MultiArray, queue_size=10)
        rospy.Subscriber("/position_real", UInt64MultiArray, self.position_show)
        rate.sleep()

    def PrepWidgets(self):
        self.checkBox_1.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.PushButton_start.setEnabled(False)
        self.PushButton_suspend.setEnabled(False)
        self.PushButton_save.setEnabled(False)
        self.PushButton_quit.setEnabled(False)
        self.PositionKeeping_Lat.setEnabled(False)
        self.PositionKeeping_Lon.setEnabled(False)
        self.Point1_Lat.setEnabled(False)
        self.Point1_Lon.setEnabled(False)
        self.Point2_Lat.setEnabled(False)
        self.Point2_Lon.setEnabled(False)
        self.Point3_Lat.setEnabled(False)
        self.Point3_Lon.setEnabled(False)
        self.Point4_Lat.setEnabled(False)
        self.Point4_Lon.setEnabled(False)
        self.Point5_Lat.setEnabled(False)
        self.Point5_Lon.setEnabled(False)

    def PrepParameters(self):

        self.RecordPath='/home/wp/PycharmProjects/WG_UI'
        self.Lat_real.setValue(Lat_real_get)
        self.Lon_real.setValue(Lon_real_get)

    def CallBackFunctions(self):
        self.Timer.timeout.connect(self.showtime)
        self.PushButton_start.clicked.connect(self.start)
        self.PushButton_suspend.clicked.connect(self.suspend)
        self.PushButton_save.clicked.connect(self.record)
        self.PushButton_quit.clicked.connect(self.ExitApp)
        self.checkBox_1.clicked.connect(self.checkBox_1_fun)
        self.checkBox_2.clicked.connect(self.checkBox_2_fun)


    def checkBox_1_fun(self):
        if self.checkBox_1.isChecked():
            self.PushButton_start.setEnabled(True)
            self.PositionKeeping_Lat.setEnabled(True)
            self.PositionKeeping_Lon.setEnabled(True)
            self.Point1_Lat.setEnabled(False)
            self.Point1_Lon.setEnabled(False)
            self.Point2_Lat.setEnabled(False)
            self.Point2_Lon.setEnabled(False)
            self.Point3_Lat.setEnabled(False)
            self.Point3_Lon.setEnabled(False)
            self.Point4_Lat.setEnabled(False)
            self.Point4_Lon.setEnabled(False)
            self.Point5_Lat.setEnabled(False)
            self.Point5_Lon.setEnabled(False)
        else:
            self.PositionKeeping_Lat.setEnabled(False)
            self.PositionKeeping_Lon.setEnabled(False)

    def checkBox_2_fun(self):
        if self.checkBox_2.isChecked():
            self.PushButton_start.setEnabled(True)
            self.PositionKeeping_Lat.setEnabled(False)
            self.PositionKeeping_Lon.setEnabled(False)
            self.Point1_Lat.setEnabled(True)
            self.Point1_Lon.setEnabled(True)
            self.Point2_Lat.setEnabled(True)
            self.Point2_Lon.setEnabled(True)
            self.Point3_Lat.setEnabled(True)
            self.Point3_Lon.setEnabled(True)
            self.Point4_Lat.setEnabled(True)
            self.Point4_Lon.setEnabled(True)
            self.Point5_Lat.setEnabled(True)
            self.Point5_Lon.setEnabled(True)
        else:
            self.Point1_Lat.setEnabled(False)
            self.Point1_Lon.setEnabled(False)
            self.Point2_Lat.setEnabled(False)
            self.Point2_Lon.setEnabled(False)
            self.Point3_Lat.setEnabled(False)
            self.Point3_Lon.setEnabled(False)
            self.Point4_Lat.setEnabled(False)
            self.Point4_Lon.setEnabled(False)
            self.Point5_Lat.setEnabled(False)
            self.Point5_Lon.setEnabled(False)

    def Start(self):
        self.PushButton_start.setEnabled(False)
        self.PushButton_suspend.setEnabled(True)
        self.PushButton_save.setEnabled(True)
        self.PushButton_quit.setEnabled(True)
        self.checkBox_1.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.PositionKeeping_Lat.setEnabled(False)
        self.PositionKeeping_Lon.setEnabled(False)
        self.Point1_Lat.setEnabled(False)
        self.Point1_Lon.setEnabled(False)
        self.Point2_Lat.setEnabled(False)
        self.Point2_Lon.setEnabled(False)
        self.Point3_Lat.setEnabled(False)
        self.Point3_Lon.setEnabled(False)
        self.Point4_Lat.setEnabled(False)
        self.Point4_Lon.setEnabled(False)
        self.Point5_Lat.setEnabled(False)
        self.Point5_Lon.setEnabled(False)
        self.textEdit.setText('开始')

        if self.checkBox_1.isChecked():
            try:
                setpoint= np.array([PositionKeeping_Lat.value(), PositionKeeping_Lon.value()])
                self.stationkeeping_pub(setpoint)
            except Exception:
                self.textEdit.setText("Fail to load set point")
        elif self.checkBox_2.isChecked():
            try:
                waypoints= np.array([Point1_Lat.value(), Point1_Lon.value()],[Point2_Lat.value(),Point2_Lon.value()], [Point3_Lat.value(), Point3_Lon.value()], [Point4_Lat.value(), Point4_Lon.value()], [Point5_Lat.value(), Point5_Lon.value()])
                self.fathfollowing_pub(waypoints)
            except Exception:
                self.textEdit.setText("Fail to load waypoints")


    def suspend(self):
        self.PushButton_start.setEnabled(True)
        self.PushButton_suspend.setEnabled(False)
        self.PushButton_save.setEnabled(True)
        self.PushButton_quit.setEnabled(True)
        self.checkBox_1.setEnabled(True)
        self.checkBox_2.setEnabled(True)


    def ExitApp(self):
        self.Timer.Stop()
        self.textEdit.setPlainText('Exiting the application..')
        QCoreApplication.quit()


    def showtime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.Date.setText(timeDisplay)

    def position_show(self, data):
        global Lat_real_get
        Lat_real_get = data.data[0]
        global Lon_real_get
        Lon_real_get = data.data[1]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=RMS_show()
    ui.show()
    sys.exit(app.exec_())