# -*- coding: utf-8 -*-

# MainWindow implementation generated from reading ui file 'loginer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

import pymysql
import qdarkstyle
import register
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

import ac_show_andupdate
import detail_mg_ac
import detail_mg_co


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ut = 0
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        self.login_label = QtWidgets.QLabel(MainWindow)
        self.login_label.setGeometry(QtCore.QRect(180, 50, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(15)

        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 230, 350, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_guan_radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.login_guan_radioButton.setObjectName("login_guan_radioButton")
        self.horizontalLayout.addWidget(self.login_guan_radioButton)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.login_leader_radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.login_guan_radioButton.setObjectName("login_leader_radioButton")
        self.horizontalLayout.addWidget(self.login_leader_radioButton)
        self.login_pushButton = QtWidgets.QPushButton(MainWindow)
        self.login_pushButton.setGeometry(QtCore.QRect(210, 300, 75, 23))
        self.login_pushButton.setObjectName("login_pushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(75, 100, 401, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.login_id_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_id_label.setFont(font)
        self.login_id_label.setObjectName("login_id_label")
        self.gridLayout.addWidget(self.login_id_label, 0, 0, 1, 1)
        self.login_password_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_password_label.setFont(font)
        self.login_password_label.setObjectName("login_password_label")
        self.gridLayout.addWidget(self.login_password_label, 1, 0, 1, 1)
        self.login_id_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_id_lineEdit.setFont(font)
        self.login_id_lineEdit.setObjectName("login_id_lineEdit")
        self.gridLayout.addWidget(self.login_id_lineEdit, 0, 1, 1, 1)
        self.login_password_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_password_lineEdit.setFont(font)
        self.login_password_lineEdit.setObjectName("login_password_lineEdit")
        self.gridLayout.addWidget(self.login_password_lineEdit, 1, 1, 1, 1)

        #创建菜单
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 26))
        self.menubar.setObjectName("menubar")
        self.menuview = QtWidgets.QMenu(self.menubar)
        self.menuview.setObjectName("menuview")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #创建菜单项
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.menuview.addAction(self.action1)
        self.menuview.addAction(self.action2)
        self.menuview.addAction(self.action3)
        self.menuview.addAction(self.action4)
        self.menubar.addAction(self.menuview.menuAction())

        #事件绑定
        self.login_pushButton.clicked.connect(self.login)
        self.login_guan_radioButton.toggled.connect(self.usertype)
        self.radioButton.toggled.connect(self.usertype)
        self.login_leader_radioButton.toggled.connect(self.usertype)
        self.action1.triggered.connect(self.regist_user)
        self.action2.triggered.connect(self.flush)
        self.action3.triggered.connect(self.flush)
        self.action4.triggered.connect(self.quit_sys)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_label.setText(_translate("MainWindow", "用户登录"))
        self.login_guan_radioButton.setText(_translate("MainWindow", "管理员"))
        self.login_leader_radioButton.setText(_translate("MainWindow", "企业管理用户"))
        self.radioButton.setText(_translate("MainWindow", "普通用户"))
        self.login_pushButton.setText(_translate("MainWindow", "登录"))
        self.login_id_label.setText(_translate("MainWindow", "账号："))
        self.login_password_label.setText(_translate("MainWindow", "密码："))
        self.login_id_lineEdit.setPlaceholderText(_translate("MainWindow", "请输入账号"))
        self.login_password_lineEdit.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.menuview.setTitle(_translate("MainWindow", "菜单栏"))
        self.action1.setText(_translate("MainWindow", "注册"))
        self.action2.setText(_translate("MainWindow", "登录"))
        self.action3.setText(_translate("MainWindow", "退出登录"))
        self.action4.setText(_translate("MainWindow", "退出系统"))

    def login(self):
        user = self.login_id_lineEdit.text()
        pwd = self.login_password_lineEdit.text()
        self.usertype()
        print(self.ut)
        if (user == "" or pwd == ""):
            print(QMessageBox.warning(self, "警告", "用户名和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes))
            return
        try:
            self.db = pymysql.connect(host='localhost', port=3306, user="root", password='root',
                                      database='financial_system', charset='utf8')
        except:
            QMessageBox.warning(self, '警告', "连接数据库故障", QMessageBox.Yes)
            self.db.rollback()

        if self.ut == 1:  # 管理员用户
            sql = 'select * from t_manage where user_name="%s"' % user  # sql指令语句
            cur = self.db.cursor()  # 获取游标
            cur.execute(sql)  # 执行sql语句
            results = cur.fetchall()  # 通过fetchall获取数据
            print('results:', results)
            self.hide()
            # 转入主界面
            self.libs = detail_mg_ac.Ui_MainWindow()
            self.libs.show()

        if self.ut == 2:  # 企业leader用户
            sql = 'select * from consumer_leader where leader_id="%s"' % user  # sql指令语句
            cur = self.db.cursor()  # 获取游标
            cur.execute(sql)  # 执行sql语句
            results = cur.fetchall()  # 通过fetchall获取数据
            print('results:', results)
            self.hide()
            # 转入主界面
            self.libs = detail_mg_co.Ui_MainWindow()
            self.libs.show()

        elif self.ut == 3:  # 普通用户
            sql = 'select * from t_consumer where user_name="%s"' % user  # sql指令语句
            cur = self.db.cursor()  # 获取游标
            cur.execute(sql)  # 执行sql语句
            results = cur.fetchall()  # 通过fetchall获取数据
            print('results:', results)
            self.hide()
            # 转入主界面
            self.libs = ac_show_andupdate.CorporateModifyApp()
            self.libs.show()

        elif self.ut is None:
            print(
            QMessageBox.warning(self, "警告", "请选择您的用户类型！", QMessageBox.Yes, QMessageBox.Yes))
            return

    def usertype(self):
        if self.login_guan_radioButton.isChecked():
            self.ut = 1  # 管理员用户
        elif self.login_leader_radioButton.isChecked():
            self.ut = 2  # 另一个管理员用户类型（如果需要）
        elif self.radioButton.isChecked():  # 假设这是普通用户的单选按钮
            self.ut = 3  # 普通用户
        else:
            self.ut = None  # 或者其他默认值，表示未选择任何用户类型

    def regist_user(self):
        self.hide()  # 主界面的隐藏
        self.regist = register.Ui_MainWindow()
        #注册界面打开
        self.regist.show()

    def flush(self):
        self.login_id_label.clear()
        self.login_password_label.clear()
        if self.ut == 0:
            self.login_pushButton.setChecked(True)

    def quit_sys(self):
        self.close()
        sys.exit()


if __name__ == '__main__':
    from PyQt5.Qt import *

    app = QtWidgets.QApplication(sys.argv)  # 创建一个应用程序
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui1 = Ui_MainWindow()  # 创建设计好的窗口对象
    ui1.show()
    sys.exit(app.exec_())
