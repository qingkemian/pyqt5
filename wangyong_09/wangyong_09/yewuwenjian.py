from jiemian_02 import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui



class My_Main_window(Ui_MainWindow):
    def setupBusi(self, MainWindow):
        toolBox = QtWidgets.QToolBox()

        #  设置左侧导航栏 toolBox 初始化时的宽度
        toolBox.setStyleSheet("QToolBoxButton { min-width:180px}")

        # 设置左侧导航栏 toolBox 在左右拉拽时的最小宽度
        toolBox.setMinimumWidth(100)

        toolBox.addItem(QtWidgets.QPushButton("Tab Content 1"), "Tab &1")
        toolBox.addItem(QtWidgets.QLabel("Tab Content 2"), "生产动态分析测试与建模")
        toolBox.addItem(QtWidgets.QPlainTextEdit('Text 3'), QtGui.QIcon('snapshot.png'), "设置")
        toolBox.setCurrentIndex(0)  # 设置软件启动时默认打开导航栏的第几个 Item；这里设置的是打开第1个 Item。
        self.verticalLayout.addWidget(toolBox)

        # #  下面两行为设置 QSplitter 分割器伸缩大小因子，但是这样设置全屏后导航栏放大了不好看
        # self.splitter.setStretchFactor(0, 30)  # 分割器左边第1个占比例30%
        # self.splitter.setStretchFactor(1, 70)  # 分割器左边第1个占比例70%

        #  下面一行为设置 QSplitter 分割器伸缩大小因子，但是这样设置全屏后导航栏放大了比较好看；不清楚原因。
        self.splitter.setStretchFactor(0, 0)  # 此函数用于设定：控件是否可伸缩。第一个参数用于指定控件的序号。第二个函数大于0时，表示控件可伸缩，小于0时，表示控件不可伸缩。
        self.splitter.setStretchFactor(1, 1)  # 此函数用于设定：控件是否可伸缩。第一个参数用于指定控件的序号。第二个函数大于0时，表示控件可伸缩，小于0时，表示控件不可伸缩。

        #  设置 QSplitter 分割器各部分最小化时的情况，设置为“False”意味着左右拉动分隔栏时各部分不会消失；此设置也可以在界面设计时在 QtDesigner 里设置。
        self.splitter.setChildrenCollapsible(False)

        #  设置 QSplitter 分割器随主窗口自适应大小变化。此设置也可以在界面设计时在 QtDesigner 里设置。
        self.splitter.setAutoFillBackground(True)






