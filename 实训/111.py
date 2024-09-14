from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import 管理员主页面  # 这里需要根据实际情况导入管理员主页面的模块

class 登录页面(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 60, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 110, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.login_user)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录页面"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))

    def login_user(self):
        user = self.lineEdit.text().strip()  # 获取用户名
        pwd = self.lineEdit_2.text().strip()  # 获取密码

        # 调用验证函数
        if self.validate_user(user, pwd):
            # 隐藏当前登录窗口并打开主窗口
            self.hide()
            self.main_window = 管理员主页面.Ui_MainWindow()
            self.main_window.show()
        else:
            # 显示错误消息框
            QtWidgets.QMessageBox.warning(self, "登录失败", "用户名或密码错误。")
            self.lineEdit.clear()  # 清空用户名输入框
            self.lineEdit_2.clear()  # 清空密码输入框
            self.lineEdit.setFocus()  # 设置焦点回用户名输入框

    def validate_user(self, user, pwd):
        try:
            # 连接数据库
            db = pymysql.connect(host='localhost', port=3306, user="root", password='root', database='zhanghang', charset='utf8')
            cur = db.cursor()

            # SQL 查询语句
            sql = "SELECT * FROM users WHERE user_name = %s AND user_pwd = %s"
            cur.execute(sql, (user, pwd))

            # 获取查询结果
            result = cur.fetchone()

            if result:
                return True  # 用户名和密码正确
            else:
                return False  # 用户名或密码错误

        except pymysql.Error as e:
            print(f"数据库错误：{e}")
            return False  # 处理数据库连接或查询错误

        finally:
            cur.close()  # 关闭游标
            db.close()  # 关闭数据库连接

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = 登录页面()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
