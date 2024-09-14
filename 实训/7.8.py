import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('功能模块示例')
        self.setGeometry(100, 100, 400, 300)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 添加功能模块按钮
        buttons = [
            ('用户功能', self.userFunction),
            ('用户管理', self.userManagement),
            ('企业信息管理', self.enterpriseInfoManagement),
            ('项目管理', self.projectManagement),
            ('退出登录', self.quitApplication)
        ]

        for text, slot in buttons:
            button = QPushButton(text, self)
            # 为按钮添加点击事件
            button.clicked.connect(slot)
            layout.addWidget(button)

            # 将布局设置给窗口
        self.setLayout(layout)

    def userFunction(self):
        # 用户功能点击后的处理，这里仅打印信息
        print("用户功能被点击")

    def userManagement(self):
        # 用户管理点击后的处理
        print("用户管理被点击")

    def enterpriseInfoManagement(self):
        # 企业信息管理点击后的处理
        print("企业信息管理被点击")

    def projectManagement(self):
        # 项目管理点击后的处理
        print("项目管理被点击")

    def quitApplication(self):
        # 退出登录按钮，关闭应用程序
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())