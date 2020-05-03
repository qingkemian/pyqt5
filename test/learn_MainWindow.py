from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1080, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setGeometry(QtCore.QRect(0, 0, 1080, 200))
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(30)
        self.gridLayout.setObjectName("gridLayout")

        # 提取图片按钮
        self.GetImg = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GetImg.setMinimumSize(QtCore.QSize(230, 36))
        self.GetImg.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.GetImg.setFont(font)
        self.GetImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GetImg.setObjectName("GetImg")
        self.gridLayout.addWidget(self.GetImg, 0, 0, 1, 1)

        # 目标标注按钮
        self.Label_Object = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Label_Object.setMinimumSize(QtCore.QSize(230, 36))
        self.Label_Object.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.Label_Object.setFont(font)
        self.Label_Object.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Label_Object.setObjectName("Label_Object")
        self.gridLayout.addWidget(self.Label_Object, 0, 1, 1, 1)

        # 对目标标注的纠错按钮
        self.CorrectObject = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CorrectObject.setMinimumSize(QtCore.QSize(230, 36))
        self.CorrectObject.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.CorrectObject.setFont(font)
        self.CorrectObject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CorrectObject.setObjectName("CorrectObject")
        self.gridLayout.addWidget(self.CorrectObject, 0, 2, 1, 1)
        self.CorrectPerson = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CorrectPerson.setMinimumSize(QtCore.QSize(230, 36))
        self.CorrectPerson.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.CorrectPerson.setFont(font)
        self.CorrectPerson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CorrectPerson.setObjectName("CorrectPerson")
        self.gridLayout.addWidget(self.CorrectPerson, 1, 2, 1, 1)

        # 将行人分类按钮
        self.GroupPerson = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GroupPerson.setMinimumSize(QtCore.QSize(230, 36))
        self.GroupPerson.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.GroupPerson.setFont(font)
        self.GroupPerson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GroupPerson.setObjectName("GroupPerson")
        self.gridLayout.addWidget(self.GroupPerson, 1, 1, 1, 1)

        # 裁剪图片按钮
        self.CropImg = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CropImg.setMinimumSize(QtCore.QSize(230, 36))
        self.CropImg.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.CropImg.setFont(font)
        self.CropImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CropImg.setObjectName("CropImg")
        self.gridLayout.addWidget(self.CropImg, 1, 0, 1, 1)

        # self.gridLayoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        # self.gridLayoutWidget2.setGeometry(QtCore.QRect(0, 0, 1380, 720))
        # self.gridLayoutWidget2.setObjectName("gridLayoutWidget2")
        self.gridLayout2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout2.setGeometry(QtCore.QRect(0, 0, 1080, 500))
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setSpacing(0)
        self.gridLayout2.setObjectName("gridLayout2")


        # 工具栏
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # 按钮事件
        self.retranslateUi(MainWindow)
        self.GetImg.clicked.connect(MainWindow.Video2Image)
        self.Label_Object.clicked.connect(MainWindow.Video2Image)
        self.CorrectObject.clicked.connect(MainWindow.Video2Image)
        self.CorrectPerson.clicked.connect(MainWindow.Video2Image)
        self.GroupPerson.clicked.connect(MainWindow.Video2Image)
        self.CropImg.clicked.connect(MainWindow.Video2Image)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # 文本设置
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "行人重识别数据集标注软件"))
        self.GetImg.setText(_translate("MainWindow", "1"))
        self.Label_Object.setText(_translate("MainWindow", "2"))
        self.CorrectObject.setText(_translate("MainWindow", "3"))
        self.CorrectPerson.setText(_translate("MainWindow", "4"))
        self.GroupPerson.setText(_translate("MainWindow", "5"))
        self.CropImg.setText(_translate("MainWindow", "6"))