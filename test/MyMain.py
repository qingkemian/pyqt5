import sys
# from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np

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

        ### 顶部打开按钮
        btn1 = QPushButton("打开")
        btn1.clicked.connect(self.openfile)
        btn1.clicked.connect(self.creat_table_show)

        hbox_open = hbox = QHBoxLayout()
        hbox_open.addStretch(1)
        hbox_open.addWidget(btn1)

        ### 表格
        self.tableWidget = QTableWidget()

        radio_one_layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)

        self.button1.toggled.connect(self.buttonState)
        radio_one_layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        radio_one_layout.addWidget(self.button2)

        btn3 = QPushButton("按钮3")
        textEdit = QTextEdit()

        ### 底部
        okButton = QPushButton("确定")
        cancelButton = QPushButton("取消")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(0)
        vbox.addLayout(hbox_open)
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(textEdit)
        vbox.addLayout(radio_one_layout)
        vbox.addWidget(btn3)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置主窗口的中心窗口
        self.mdi = QWidget()
        self.mdi.setLayout(vbox)
        # self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # 设置停靠控件1
        self.items = QDockWidget('Project（别碰 软件会崩）', self)
        self.listWidget = QListWidget()
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setWindowTitle("Dir View")

        self.items.setWidget(self.tree)

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

    # 获取文件路径
    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.xlsx , *.xls)')
        global path_openfile_name
        path_openfile_name = openfile_name[0]

    # 读取表格、显示表格
    def creat_table_show(self):
        if len(path_openfile_name) > 0:
            input_table = pd.read_excel(path_openfile_name)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
            input_table_header = input_table.columns.values.tolist()

            self.tableWidget.setColumnCount(input_table_colunms)
            self.tableWidget.setRowCount(input_table_rows)
            self.tableWidget.setHorizontalHeaderLabels(input_table_header)

            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items)
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.tableWidget.setItem(i, j, newItem)
        else:
            pass

    def buttonState(self):
        radioButton = self.sender()

        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '> 被选中')
        else:
            print('<' + radioButton.text() + '> 被取消选中状态')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())