import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import 添加用户信息
import 用户信息删除
import 用户信息修改
import 用户界面

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('用户信息管理系统')

        # 创建按钮并设置位置
        btn_add = QPushButton('用户信息添加', self)
        btn_add.setGeometry(50, 50, 150, 50)

        btn_delete = QPushButton('用户信息删除', self)
        btn_delete.setGeometry(50, 120, 150, 50)

        btn_modify = QPushButton('用户信息修改', self)
        btn_modify.setGeometry(50, 190, 150, 50)

        btn_back = QPushButton('返回上一级', self)
        btn_back.setGeometry(50, 260, 150, 50)

        # 按钮点击事件绑定
        btn_add.clicked.connect(self.on_btn_add_clicked)
        btn_delete.clicked.connect(self.on_btn_delete_clicked)
        btn_modify.clicked.connect(self.on_btn_modify_clicked)
        btn_back.clicked.connect(self.on_btn_back_clicked)

    def on_btn_add_clicked(self):
        # 点击“用户信息增加”按钮触发的操作
        print("跳转到用户信息增加页面")
        # 这里可以调用其他界面或相关的逻辑处理函数
        # self.hide()
        # 登录界面打开
        self.log = 添加用户信息.MainWindow()
        self.log.show()

    def on_btn_delete_clicked(self):
        # 点击“用户信息删除”按钮触发的操作
        print("跳转到用户信息删除页面")
        # 这里可以调用其他界面或相关的逻辑处理函数
        # self.hide()
        # 登录界面打开
        self.libs = 用户信息删除.Ui_MainWindow()
        self.libs.show()

    def on_btn_modify_clicked(self):
        # 点击“用户信息修改”按钮触发的操作
        print("跳转到用户信息修改页面")
        # 这里可以调用其他界面或相关的逻辑处理函数
        # self.hide()
        # 登录界面打开
        self.log = 用户信息修改.Ui_MainWindow()
        self.log.show()

    def on_btn_back_clicked(self):
        # 点击“返回上一级”按钮触发的操作
        print("返回上一级页面")
        # 这里可以调用返回上一级页面的逻辑处理函数
        self.hide()
        # 登录界面打开
        self.log = 用户界面.Ui_MainWindow()
        self.log.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())
