# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail_mg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QHeaderView,QAbstractItemView,QTableWidgetItem
import qdarkstyle
import sys
import pymysql

import add_corporate
import co_show_andupdate
import del_corporate
import detail_mg_ac
import loginer,register,add_account


class Ui_MainWindow(QMainWindow):
    #该类的构造方法
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.pages = 1
        self.currentpage = 1
        self.prepage = 1
        self.nextpage = 1
        self.count = 0
        self.page_num = 5
        self.setupUi(self)
        self.page_control()
        self.draw_libs_info()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 651)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(10, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(10, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(10, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(150, 20, 700, 31))
        self.lineEdit1.setObjectName("lineEdit1")
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton8.setGeometry(QtCore.QRect(900, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton8.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton8.setIcon(icon1)
        self.pushButton8.setObjectName("pushButton8")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)#下拉框
        self.comboBox.setGeometry(QtCore.QRect(1200, 20, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setCurrentIndex(0)  #第0个下拉框
        #创建数据表格的对象
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        #设置数据表格的位置和大小
        self.tableWidget.setGeometry(QtCore.QRect(120, 70,1350, 450))
        #设置数据表格是否有滚动条
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)#设置滚动条
        #设置数据表格的名字
        self.tableWidget.setObjectName("tableWidget")
        #设置数据表格的列数
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(11)#行数
        #创建数据表格的行
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)#共11行
        #创建对应的列
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 表格自适应窗口大小
        # self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选中整行
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑

        #各行设置颜色
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setStyleSheet("alternate-background-color: rgb(0, 0, 0)"
                                     "; background-color: rgb(100, 100, 100);")
        # 支持表头排序功能
        # self.tableWidget.setSortingEnabled(True)
        # self.tableWidget.horizontalHeader().setStyleSheet("::section{background-color: pink; color: blue; font-weight: bold}")
        # self.tableWidget.verticalHeader().hide()

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(370, 530, 90, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(510, 530,50, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(480, 530, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.setText(str(self.currentpage))
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(590, 530, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(660, 530, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(760, 530, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton7.setFont(font)
        self.pushButton7.setObjectName("pushButton7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action3)
        self.menu.addAction(self.action4)
        self.menubar.addAction(self.menu.menuAction())

        # 菜单栏事件绑定
        self.action1.triggered.connect(self.detail_mg_ac)
        self.action2.triggered.connect(self.login_user)
        self.action3.triggered.connect(self.login_user)
        self.action4.triggered.connect(self.quit_sys)
        # 书籍操作事件绑定
        self.pushButton1.clicked.connect(self.add_corporate)  # 添加书籍
        self.pushButton2.clicked.connect(self.del_corporate)  # 删除企业信息
        self.pushButton3.clicked.connect(self.co_show_andupdate)

        # 书籍查询事件绑定
        self.pushButton8.clicked.connect(self.find_info)
        # 指定页事件绑定
        self.pushButton5.clicked.connect(self.page_info)
        # 上一页事件绑定
        self.pushButton6.clicked.connect(self.pre_page_info)
        # 下一页事件绑定
        self.pushButton7.clicked.connect(self.next_page_info)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "企业管理系统"))
        self.pushButton1.setText(_translate("MainWindow", "添加企业"))
        self.pushButton2.setText(_translate("MainWindow", "删除企业"))
        self.pushButton3.setText(_translate("MainWindow", "修改企业"))
        self.pushButton8.setText(_translate("MainWindow", "查询"))
        self.comboBox.setItemText(0, _translate("MainWindow", "按企业id查询"))
        self.comboBox.setItemText(1, _translate("MainWindow", "按企业名称查询"))
        self.comboBox.setItemText(2, _translate("MainWindow", "按主营业务查询"))
        self.comboBox.setItemText(3, _translate("MainWindow", "按注册地址查询"))
        self.comboBox.setItemText(4, _translate("MainWindow", "按企业法人查询"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "企业id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "企业名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "主营业务"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "注册地址"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "注册日期"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "注册金额"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "企业账号"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "法人"))
        self.label1.setText(_translate("MainWindow", "跳转到第"))
        self.label2.setText(_translate("MainWindow", "/"+str(self.pages)+"页"))
        self.pushButton5.setText(_translate("MainWindow", "跳转"))
        self.pushButton6.setText(_translate("MainWindow", "上一页"))
        self.pushButton7.setText(_translate("MainWindow", "下一页"))
        self.menu.setTitle(_translate("MainWindow", "菜单栏"))
        self.action1.setText(_translate("MainWindow", "查看企业信息"))
        self.action2.setText(_translate("MainWindow", "登录"))
        self.action3.setText(_translate("MainWindow", "退出登录"))
        self.action4.setText(_translate("MainWindow", "退出系统"))

    def login_user(self):
        self.hide()
        # 登录界面打开
        self.log = loginer.Ui_MainWindow()
        self.log.show()


    def add_corporate(self):
        self.hide()
        # 登录界面打开
        self.addac = add_corporate.Ui_MainWindow()
        self.addac.show()

    def del_corporate(self):
        self.hide()
        # 登录界面打开
        self.delco = del_corporate.CorporateModifyApp()
        self.delco.show()

    def co_show_andupdate(self):
        self.hide()
        # 登录界面打开
        self.delco = co_show_andupdate.CorporateModifyApp()
        self.delco.show()

    def detail_mg_ac(self):
        self.hide()  # 主界面的隐藏
        self.gtmc = 企业信息.Ui_MainWindow()
        #注册界面打开
        self.gtmc.show()

    def quit_sys(self):
        self.hide()
        sys.exit()



    def flush(self):#刷新
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()

    def find_info(self):#书籍查询 '''查询中的翻页没做'''
        text = self.lineEdit1.text()#查询内容
        choice = self.comboBox.currentText()  # 查询分类
        print(choice)
        if text == "":
            self.draw_libs_info()
        else:
            if choice == '按公司id查询':
                sql = "select * from t_corporate where co_id like '%" + text + "%'"
                self.search_libs_info(sql)
            elif choice == '按企业名称查询':
                sql = "select * from t_corporate where co_name='%s'" % text
                self.search_libs_info(sql)
            elif choice == '按主营业务查询':
                sql = "select * from t_corporate where major_work like '%" + text + "%'"
                self.search_libs_info(sql)
            elif choice == '按注册地址查询':
                sql = "select * from t_corporate where regist_address like '%" + text + "%'"
                self.search_libs_info(sql)
            elif choice == '按公司法人查询':
                sql = "select * from t_corporate where legakman like '%" + text + "%'"
                self.search_libs_info(sql)

    def connect_sql_and_show(self,sql):
        # 连接数据库并获取企业信息
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', database='zhanghang',
                             charset='utf8')
        cur = db.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        # print('results:', results)
        db.close()
        cur.close()
        return results

    def search_libs_info(self,sql):
        self.flush()  # 界面刷新
        items = self.connect_sql_and_show(sql)
        # 界面显示按书名筛选的书籍信息
        for i in range(len(items)):
            item = items[i]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(row, j, item)



    def draw_libs_info(self,sql='select * from t_corporate'):
        items = self.connect_sql_and_show(sql)
        # self.flush()  # 界面刷新
        # sql = 'select * from t_corporate'
        # items = self.connect_sql_and_show(sql)
        count = len(items)#查询到书籍的信息条数
        num = self.currentpage#当前页   第1页 (num-1)*self.page_num - self.page_num*num-1  0-4  第2页 5-9 第3页 10-11
        if num == self.pages:
            self.flush()
            # 界面显示按书名筛选的书籍信息
            for i in range((num-1)*self.page_num,count):#遍历结果，将每一行数据进行遍历
                print((num-1)*self.page_num,count)
                item = items[i]
                row = 0
                self.tableWidget.insertRow(row)     #将行对象添加到表格
                for j in range(len(item)):
                    item = QTableWidgetItem(str(items[i][j]))
                    print(row,j)
                    self.tableWidget.setItem(row, j, item)
        else:
            self.flush()
            # 界面显示按书名筛选的书籍信息
            for i in range((num-1)*self.page_num,self.page_num*num):
                item = items[i]
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                for j in range(len(item)):
                    item = QTableWidgetItem(str(items[i][j]))
                    self.tableWidget.setItem(row, j, item)

    def page_control(self,sql='select * from t_corporate'):#页面处理
        #连接数据库，获得查询的书籍信息条数count
        items = self.connect_sql_and_show(sql)
        self.count = len(items)
        #总页数
        if self.count//self.page_num==0:
            self.pages = self.count//self.page_num
        else:
            self.pages = self.count // self.page_num + 1
        self.label2.setText('/'+str(self.pages)+'页')
        self.prepage = self.currentpage - 1#上一页
        if self.prepage < 1:
            self.prepage = self.currentpage
        elif self.prepage > self.pages:
            self.prepage = self.pages
        else:
            self.prepage = self.prepage
        self.nextpage = self.currentpage + 1#下一页
        if self.nextpage < 1:
            self.nextpage = self.currentpage
        elif self.nextpage > self.pages:
            self.nextpage = self.pages
        else:
            self.nextpage = self.nextpage

    def page_info(self):#指定页翻页按钮获取翻页信息
        self.page_control()
        index = int(self.lineEdit2.text())
        if index <= self.pages and index >= 1:
            self.currentpage = index
        elif index < 1:
            self.currentpage = 1
        elif index > self.pages:
            self.currentpage = self.pages
        else:
            self.currentpage = self.currentpage
        self.lineEdit2.setText(str(self.currentpage))
        self.prepage = self.currentpage - 1
        self.nextpage = self.currentpage + 1
        self.draw_libs_info()


    def pre_page_info(self):#上一页
        self.page_control()
        self.currentpage = self.prepage
        self.nextpage = self.currentpage + 1
        self.prepage = self.prepage - 1
        if self.prepage < 1:
            self.prepage = 1
        self.lineEdit2.setText(str(self.currentpage))
        self.draw_libs_info()

    def next_page_info(self):#下一页
        self.page_control()
        self.prepage = self.currentpage
        self.currentpage = self.nextpage
        self.nextpage = self.currentpage + 1
        if self.nextpage > self.pages:
            self.nextpage = self.pages
            self.prepage = self.currentpage - 1
        self.lineEdit2.setText(str(self.currentpage))
        self.draw_libs_info()



if __name__ == '__main__':
    from PyQt5.Qt import *
    app = QtWidgets.QApplication(sys.argv) # 创建一个应用程序
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui1 = Ui_MainWindow()    # 创建设计好的窗口对象
    ui1.show()
    sys.exit(app.exec_())