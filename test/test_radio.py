from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("QButtonGrounp")
w.resize(300, 150)

# 创建4个 QRadioButton 按钮
cs1 = QRadioButton("特大杯",w)
cs1.move(80, 20)

cs2 = QRadioButton("大杯",w)
cs2.move(80, 40)

cs3 = QRadioButton("中杯",w)
cs3.move(80, 60)

cs4 = QRadioButton("小杯",w)
cs4.move(80, 80)

# 创建一个按键组，并添加按键
cs_group = QButtonGroup(w)
cs_group.addButton(cs1,1)
cs_group.addButton(cs2,2)
cs_group.addButton(cs3,3)
cs_group.addButton(cs4,4)

# 定义槽函数，并打印接收到的参数
def slot(object):
    print("按键被按下了,id 为:", cs_group.id(object))

# 连接槽函数，并制定带的参数会 int 类型
cs_group.buttonClicked.connect(slot)
w.show()

sys.exit(app.exec_())