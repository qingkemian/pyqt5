
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
'''
Pyqt 动态的添加控件
'''


class DynAddObject(QDialog):


    def __init__(self, parent=None):
        super(DynAddObject, self).__init__(parent)
        addButton = QPushButton(u"添加控件")
        self.layout = QGridLayout()
        self.layout.addWidget(addButton, 1, 0)
        self.setLayout(self.layout)
        self.addButton.clicked.connect(self.add)


    def add(self):
        btncont = self.layout.count()
        widget = QPushButton(str(btncont), self)
        self.layout.addWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DynAddObject()
    app.exec_()