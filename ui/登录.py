# -*- coding: utf-8 -*-

import sys
import pymysql
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import 注册  # 假设这是你的注册模块


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ut = 0  # 用户类型，0表示普通用户，1表示管理员
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 500, 60))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 120, 200, 40))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 180, 200, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 120, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 180, 61, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(190, 240, 86, 41))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(420, 240, 92, 41))
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 290, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 22))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionzhuce = QtWidgets.QAction(MainWindow)
        self.actionzhuce.setObjectName("actionzhuce")

        self.actionqiyexinxi = QtWidgets.QAction(MainWindow)
        self.actionqiyexinxi.setObjectName("actionqiyexinxi")

        self.actionbangzhu = QtWidgets.QAction(MainWindow)
        self.actionbangzhu.setObjectName("actionbangzhu")

        self.actionbangzhu_2 = QtWidgets.QAction(MainWindow)
        self.actionbangzhu_2.setObjectName("actionbangzhu_2")

        self.menu.addAction(self.actionzhuce)
        self.menu.addAction(self.actionqiyexinxi)
        self.menu.addAction(self.actionbangzhu)
        self.menu.addAction(self.actionbangzhu_2)

        self.menubar.addAction(self.menu.menuAction())

        # 事件绑定
        self.pushButton.clicked.connect(self.login)
        self.radioButton.toggled.connect(self.usertype)
        self.radioButton_2.toggled.connect(self.usertype)
        self.actionzhuce.triggered.connect(self.regist_user)
        self.actionqiyexinxi.triggered.connect(self.flush)
        self.actionbangzhu.triggered.connect(self.flush)
        self.actionbangzhu_2.triggered.connect(self.quit_sys)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户登录"))
        self.label.setText(_translate("MainWindow", "用户登录"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入用户名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密码："))
        self.radioButton.setText(_translate("MainWindow", "管理员"))
        self.radioButton_2.setText(_translate("MainWindow", "普通用户"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.menu.setTitle(_translate("MainWindow", "菜单栏"))
        self.actionzhuce.setText(_translate("MainWindow", "注册"))
        self.actionqiyexinxi.setText(_translate("MainWindow", "企业信息"))
        self.actionbangzhu.setText(_translate("MainWindow", "退出系统"))
        self.actionbangzhu_2.setText(_translate("MainWindow", "帮助"))

    def login(self):
        user = self.lineEdit.text()  # 获取用户名输入框的内容
        pwd = self.lineEdit_2.text()  # 获取密码输入框的内容
        self.usertype()  # 确定用户类型，通过单选按钮选择

        if user == "" or pwd == "":
            QMessageBox.warning(self, "警告", "用户名和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes)
            return

        try:
            self.db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='total',
                                      charset='utf8')
            cursor = self.db.cursor()

            if self.ut == 1:  # 管理员用户
                sql = 'select * from manager where user_name="%s" and user_pwd="%s"' % (user, pwd)
            else:  # 普通用户
                sql = 'select * from consumer where user_name="%s"' % user

            cursor.execute(sql)
            results = cursor.fetchall()
            print('results:', results)

            if results:
                self.hide()
                # 假设 注册.Ui_MainWindow() 是登录后的主窗口
                self.libs = 注册.Ui_MainWindow()
                self.libs.show()
            else:
                QMessageBox.warning(self, '警告', "用户名或密码错误!", QMessageBox.Yes)

        except pymysql.Error as e:
            print("连接MySQL时出错:", e)
            QMessageBox.warning(self, '警告', "连接数据库故障", QMessageBox.Yes)

        finally:
            cursor.close()
            self.db.close()

    def regist_user(self):
        self.hide()  # 隐藏登录窗口
        self.regist = 注册.Ui_MainWindow()
        self.regist.show()  # 显示注册窗口

    def flush(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        if self.ut == 0:
            self.radioButton.setChecked(True)

    def usertype(self):
        if self.radioButton.isChecked():
            self.ut = 1  # 管理员
        elif self.radioButton_2.isChecked():
            self.ut = 0  # 普通用户


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui1 = Ui_MainWindow()
    ui1.show()
    sys.exit(app.exec_())
