import sys
# from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 菜单栏、工具栏选项
        exitAct = QAction(QIcon('./img/close.ico'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        self.statusBar()

        # 设置菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addAction("New")
        fileMenu.addAction("cascade")
        fileMenu.addAction("Tiled")

        fileMenu.triggered.connect(self.windowaction)

        # 设置工具栏
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        # 设置主窗口的中心窗口的控件
        okButton = QPushButton("确定")
        cancelButton = QPushButton("取消")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        btn3 = QPushButton("按钮3")
        textEdit = QTextEdit()

        vbox.addStretch(0)
        vbox.addWidget(textEdit)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置主窗口的中心窗口
        self.mdi = QWidget()
        self.mdi.setLayout(vbox)
        # self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # 设置停靠控件1
        self.items = QDockWidget('Dockable', self)
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        self.items.setWidget(self.listWidget)

        # self.items.setFloating(True)

        # self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.items)

        # 设置停靠控件2
        self.items2 = QDockWidget('Dockable2', self)
        self.listWidget2 = QListWidget()
        self.listWidget2.addItem('item1')
        self.listWidget2.addItem('item2')
        self.listWidget2.addItem('item3')

        self.items2.setWidget(self.listWidget2)

        self.items2.setMaximumHeight(200)

        self.addDockWidget(Qt.RightDockWidgetArea, self.items2)

        # 设置窗口位置
        # self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

    # 菜单栏活动
    def windowaction(self, q):
        print(q.text())
        if q.text() == "New":
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())