import sys
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

        hbox_open  = QHBoxLayout()
        hbox_open.addStretch(1)
        hbox_open.addWidget(btn1)

        ### 表格
        self.tableWidget = QTableWidget()

        ### 文本框
        textEdit = QTextEdit()
        # textEdit.setMaximumHeight(500)
        # textEdit.setMinimumHeight(200)


        center_splitter_one = QSplitter(Qt.Vertical)
        center_splitter_one.addWidget(self.tableWidget)
        center_splitter_one.addWidget(textEdit)
        center_splitter_one.setFixedHeight(600)

        # ### 单选按钮1
        # radio_one_layout = QHBoxLayout()
        #
        # label1 = QLabel()
        # label1.setText("抑郁与否")
        # radio_one_layout.addWidget(label1)
        #
        # self.radio1 = QRadioButton('单选按钮1')
        # self.radio1.setChecked(True)
        # self.radio1.toggled.connect(self.buttonState)
        # radio_one_layout.addWidget(self.radio1)
        #
        # self.radio2 = QRadioButton('单选按钮2')
        # self.radio2.toggled.connect(self.buttonState)
        # radio_one_layout.addWidget(self.radio2)
        #
        # self.bg1 = QButtonGroup(self)
        # self.bg1.addButton(self.radio1,11)
        # self.bg1.addButton(self.radio2,12)
        #
        #
        # ### 复选框
        # check_one_layout = QHBoxLayout()
        #
        # self.checkBox1 = QCheckBox('复选框控件1')
        # self.checkBox1.setChecked(True)
        # self.checkBox1.stateChanged.connect(lambda: self.checkboxState(self.checkBox1))
        # check_one_layout.addWidget(self.checkBox1)
        #
        # self.checkBox2 = QCheckBox('复选框控件2')
        # self.checkBox2.stateChanged.connect(lambda: self.checkboxState(self.checkBox2))
        # check_one_layout.addWidget(self.checkBox2)
        #
        # self.checkBox3 = QCheckBox('半选中')
        # self.checkBox3.stateChanged.connect(lambda: self.checkboxState(self.checkBox3))
        # self.checkBox3.setTristate(True)
        # self.checkBox3.setCheckState(Qt.PartiallyChecked)
        # check_one_layout.addWidget(self.checkBox3)

        self.center_second_vbox = QVBoxLayout()


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
        vbox.addWidget(center_splitter_one)
        # vbox.addLayout(radio_one_layout)
        # vbox.addLayout(check_one_layout)
        vbox.addLayout(self.center_second_vbox)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置主窗口的中心窗口
        self.mdi = QWidget()
        self.mdi.setLayout(vbox)
        # self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # 设置——左侧——停靠控件1
        self.pro_items = QDockWidget('Project（别碰 软件会崩）', self)
        self.listWidget = QListWidget()
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setWindowTitle("Dir View")

        self.pro_items.setWidget(self.tree)

        # self.items.setFloating(True)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.pro_items)

        # 设置——右侧——停靠控件1
        self.docked2 = QDockWidget('添加单选', self)

        btn_layout = QFormLayout()
        self.button1 = QPushButton('获取列表中的选项')
        self.button1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()
        btn_layout.addRow(self.button1, self.lineEdit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()
        btn_layout.addRow(self.button2, self.lineEdit2)

        self.button3 = QPushButton('获取整数')
        self.button3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()
        btn_layout.addRow(self.button3, self.lineEdit3)

        self.button4 = QPushButton("创建单选按钮")
        self.button4.clicked.connect(self.newRadio)
        self.lineEdit4 = QLineEdit()
        btn_layout.addRow(self.button4,self.lineEdit4)

        self.addDockWidget(Qt.RightDockWidgetArea,self.docked2)
        self.dockedWidget2 = QWidget(self)
        self.docked2.setWidget(self.dockedWidget2)
        self.dockedWidget2.setLayout(btn_layout)

        # 设置窗口位置
        # self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

    def add(self):
        widget = QPushButton("1")
        self.grid.addWidget(widget,1,1)

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

    # 单选框状态
    def buttonState(self):
        radioButton = self.sender()

        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '> 被选中')
        else:
            print('<' + radioButton.text() + '> 被取消选中状态')

    # 多选框状态
    def checkboxState(self,cb):
        check1Status = self.checkBox1.text() + ', isChecked=' + str(self.checkBox1.isChecked()) + ',checkState=' + str(self.checkBox1.checkState()) + '\n'
        check2Status = self.checkBox2.text() + ', isChecked=' + str(self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState()) + '\n'
        check3Status = self.checkBox3.text() + ', isChecked=' + str(self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState()) + '\n'
        print(check1Status + check2Status + check3Status)

    # 右侧停靠控件事件
    def getItem(self):
        items = ('C','C++','Ruby','Python','Java')
        item, ok =QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.lineEdit1.setText(item)
    def getText(self):
        text, ok =QInputDialog.getText(self,'文本输入框','输入姓名')
        if ok and text:
            self.lineEdit2.setText(text)
    def getInt(self):
        num, ok =QInputDialog.getInt(self,'整数输入框','输入数字')
        if ok and num:
            self.lineEdit3.setText(str(num))
    def newRadio(self):
        radio_two_layout = QHBoxLayout()

        label2 = QLabel()
        label2.setText("add")
        radio_two_layout.addWidget(label2)

        self.radio3 = QRadioButton('add1')
        self.radio3.setChecked(True)
        radio_two_layout.addWidget(self.radio3)

        self.radio4 = QRadioButton('add2')
        radio_two_layout.addWidget(self.radio4)

        self.bg2 = QButtonGroup(self)
        self.bg2.addButton(self.radio3, 13)
        self.bg2.addButton(self.radio4, 14)

        self.center_second_vbox.addLayout(radio_two_layout)
        self.lineEdit4.setText("添加成功")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())