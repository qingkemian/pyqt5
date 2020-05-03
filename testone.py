import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from test import App
from demo5_3 import Example

class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        first = App()
        self.setCentralWidget(first)

        self.setWindowTitle('Simple menu')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ex()
    sys.exit(app.exec_())