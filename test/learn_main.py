import sys
import cv2
from matplotlib import pyplot as plt
from skimage import transform, data
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
# 对应父窗口文件
from MainWindow import Ui_MainWindow
# 对应子窗口文件
from getimage import Ui_getimage
import os


# 父窗口
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.vdieo2imagewindow = Vdieo2ImageWindow()
        self.cropimagewindow = CropImageWindow()
        self.labelimagewindow = LabelImageWindow()
        self.labelobjectwindow = LabelObjectWindow()
        self.correctpersonwindow = CorrectPersonWindow()
        self.grouppersonwindow = GroupPersonWindow()

    # 子窗口
    def Video2Image(self):
        self.gridLayout2.addWidget(self.vdieo2imagewindow)  # 将窗口放入girdLayout中
        self.vdieo2imagewindow.show()  # 打开子窗口1


# 子窗口
class Vdieo2ImageWindow(QMainWindow, Ui_getimage):

    def __init__(self):
        super(Vdieo2ImageWindow, self).__init__()
        self.setupUi(self)

    # 退出函数，可以在子窗口的代码中创建指向此函数的事件。
    def Close(self):
        reply = QMessageBox.question(self, '确认框', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.hide()
        else:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())