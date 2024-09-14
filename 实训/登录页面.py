import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import pymysql
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import 企业信息增加
import 企业账号修改


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ut = 0
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 80, 201, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 120, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 72, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 10, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(170, 170, 115, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(310, 170, 115, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 230, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionenter = QtWidgets.QAction(MainWindow)
        self.actionenter.setObjectName("actionenter")
        self.actionregister = QtWidgets.QAction(MainWindow)
        self.actionregister.setObjectName("actionregister")
        self.actionback = QtWidgets.QAction(MainWindow)
        self.actionback.setObjectName("actionback")
        self.menu.addAction(self.actionenter)
        self.menu.addAction(self.actionregister)
        self.menu.addAction(self.actionback)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入用户名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label_2.setText(_translate("MainWindow", "密码:"))
        self.label_3.setText(_translate("MainWindow", "用户登录"))
        self.radioButton.setText(_translate("MainWindow", "管理员"))
        self.radioButton_2.setText(_translate("MainWindow", "普通用户"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.menu.setTitle(_translate("MainWindow", "菜单栏"))
        self.actionenter.setText(_translate("MainWindow", "登录"))
        self.actionregister.setText(_translate("MainWindow", "注册"))
        self.actionback.setText(_translate("MainWindow", "退出"))

    def login(self):
        user = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        print(user, pwd)
        self.usertype()
        print(self.ut)
        if user == "" or pwd == "":
            print(QMessageBox.warning(self, "警告", "用户名和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes))
            return

        try:
            self.db = pymysql.connect(host='localhost', port=3306, user="root", password='root', database='zhanghang',
                                      charset='utf8')
            print("数据库连接成功")
        except :
            print("数据库连接失败:")
            QMessageBox.warning(self, '警告', "连接数据库故障", QMessageBox.Yes)
            self.db.rollback()

        if self.ut == 1:  # 管理员用户
            sql = "select * from manager where user_name=%s and user_pwd=%s"
            cur = self.db.cursor()  # 获取游标
            cur.execute(sql, (user, pwd))  # 执行sql语句
            results = cur.fetchall()  # 通过fetchall获取数据
            print('results:', results)
        else:  # 普通用户
            sql = "select * from consumer where user_name=%s and user_pwd=%s"
            cur = self.db.cursor()  # 获取游标
            cur.execute(sql, (user, pwd))  # 执行sql语句
            results = cur.fetchall()  # 通过fetchall获取数据
            print('results:', results)



    def usertype(self):
        info = 0
        if self.radioButton.isChecked():           # 如果单选按钮1- 管理员被选择
            self.radioButton_2.setChecked(True)          # 设置被选择
            info = 1
        else:
            self.radioButton.setChecked(False)
            info = 0
        if self.radioButton_2.isChecked():           # 如果选择的是普通用户
            self.radioButton_2.setChecked(True)
            info = 0
        else:
            self.radioButton_2.setChecked(False)
            info = 1
        self.ut = info

    def regist_user(self):
        self.hide()  # 主界面的隐藏
        # self.regist = register.Ui_MainWindow()
        #注册界面打开
        self.regist.show()
    def quit_sys(self):
        self.close()
        sys.exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui1 = Ui_MainWindow()
    ui1.show()
    sys.exit(app.exec_())
