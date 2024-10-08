# -*- coding: utf-8 -*-

# MainWindow implementation generated from reading ui file 'add_corporate.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate,Qt
import qdarkstyle
import sys
import pymysql
from PyQt5.QtWidgets import QMainWindow
import detail_mg_co


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("企业信息添加")
        MainWindow.resize(900,850)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        MainWindow.setFont(font)

        self.id_label = QtWidgets.QLabel(MainWindow)
        self.id_label.setGeometry(QtCore.QRect(160, 40,100, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")

        self.co_name_label_2 = QtWidgets.QLabel(MainWindow)
        self.co_name_label_2.setGeometry(QtCore.QRect(160, 120, 100,50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.co_name_label_2.setFont(font)
        self.co_name_label_2.setObjectName("co_name_label_2")

        self.major_work_label_3 = QtWidgets.QLabel(MainWindow)
        self.major_work_label_3.setGeometry(QtCore.QRect(160, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.major_work_label_3.setFont(font)
        self.major_work_label_3.setObjectName("major_work_label_3")

        self.regist_address_label_4 = QtWidgets.QLabel(MainWindow)
        self.regist_address_label_4.setGeometry(QtCore.QRect(160, 280, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.regist_address_label_4.setFont(font)
        self.regist_address_label_4.setObjectName("regist_address_label_4")

        self.regist_date_label_5 = QtWidgets.QLabel(MainWindow)
        self.regist_date_label_5.setGeometry(QtCore.QRect(160, 360, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.regist_date_label_5.setFont(font)
        self.regist_date_label_5.setObjectName("regist_date_label_5")

        self.regist_money_label_6 = QtWidgets.QLabel(MainWindow)
        self.regist_money_label_6.setGeometry(QtCore.QRect(160, 440, 190, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.regist_money_label_6.setFont(font)
        self.regist_money_label_6.setObjectName("regist_money_label_6")

        self.co_number_label_7 = QtWidgets.QLabel(MainWindow)
        self.co_number_label_7.setGeometry(QtCore.QRect(160, 520, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.co_number_label_7.setFont(font)
        self.co_number_label_7.setObjectName("co_number_label_7")

        self.legalman_label_8 = QtWidgets.QLabel(MainWindow)
        self.legalman_label_8.setGeometry(QtCore.QRect(160, 600, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.legalman_label_8.setFont(font)
        self.legalman_label_8.setObjectName("legalman_label_8")


        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(390, 700, 90, 50))
        self.pushButton.setObjectName("pushButton")

        self.back_pushButton = QtWidgets.QPushButton(MainWindow)
        self.back_pushButton.setGeometry(QtCore.QRect(360, 775, 150, 50))
        self.back_pushButton.setObjectName("back_pushButton")

        self.id_lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.id_lineEdit.setGeometry(QtCore.QRect(300, 40, 461, 50))
        self.id_lineEdit.setObjectName("id_lineEdit")

        self.co_name_lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.co_name_lineEdit_2.setGeometry(QtCore.QRect(300, 120, 461, 50))
        self.co_name_lineEdit_2.setObjectName("co_name_lineEdit_2")

        self.major_work_lineEdit_3 = QtWidgets.QLineEdit(MainWindow)
        self.major_work_lineEdit_3.setGeometry(QtCore.QRect(300, 200, 461, 50))
        self.major_work_lineEdit_3.setObjectName("major_work_lineEdit_3")

        self.regist_address_lineEdit_4 = QtWidgets.QLineEdit(MainWindow)
        self.regist_address_lineEdit_4.setGeometry(QtCore.QRect(300, 280, 461, 50))
        self.regist_address_lineEdit_4.setObjectName("regist_address_lineEdit_4")

        self.regist_date_lineEdit_5 = QtWidgets.QLineEdit(MainWindow)
        self.regist_date_lineEdit_5.setGeometry(QtCore.QRect(300, 360, 461, 50))
        self.regist_date_lineEdit_5.setObjectName("regist_date_lineEdit_5")

        self.regist_money_lineEdit_6 = QtWidgets.QLineEdit(MainWindow)
        self.regist_money_lineEdit_6.setGeometry(QtCore.QRect(300, 440, 461, 50))
        self.regist_money_lineEdit_6.setObjectName("regist_money_lineEdit_6")

        self.co_number_lineEdit_7 = QtWidgets.QLineEdit(MainWindow)
        self.co_number_lineEdit_7.setGeometry(QtCore.QRect(300, 520, 461, 50))
        self.co_number_lineEdit_7.setObjectName("co_number_lineEdit_7")

        self.legalman_lineEdit_8 = QtWidgets.QLineEdit(MainWindow)
        self.legalman_lineEdit_8.setGeometry(QtCore.QRect(300, 600, 461, 50))
        self.legalman_lineEdit_8.setObjectName("legalman_lineEdit_8")

        self.pushButton.clicked.connect(self.add_corporate_info)
        self.back_pushButton.clicked.connect(self.detail_mg_co)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "添加企业信息"))
        self.id_label.setText(_translate("MainWindow", "企业id"))
        self.co_name_label_2.setText(_translate("MainWindow", "企业名称"))
        self.major_work_label_3.setText(_translate("MainWindow", "主营业务"))
        self.regist_address_label_4.setText(_translate("MainWindow", "注册地址"))
        self.regist_date_label_5.setText(_translate("MainWindow", "注册日期"))
        self.regist_money_label_6.setText(_translate("MainWindow", "注册金额"))
        self.co_number_label_7.setText(_translate("MainWindow", "企业账号"))
        self.legalman_label_8.setText(_translate("MainWindow", "法人"))
        self.pushButton.setText(_translate("MainWindow", "确认添加"))
        self.back_pushButton.setText(_translate("MainWindow", "返回企业列表"))

    def add_corporate_info(self):
        id=self.id_lineEdit.text()
        co_name=self.co_name_lineEdit_2.text()
        major_work=self.major_work_lineEdit_3.text()
        regist_address=self.regist_address_lineEdit_4.text()
        regist_date=self.regist_date_lineEdit_5.text()
        regist_money=self.regist_money_lineEdit_6.text()
        co_number=self.co_number_lineEdit_7.text()
        legalman=self.legalman_lineEdit_8.text()
        print(id,co_name,major_work,regist_address,regist_date,regist_money,co_number,legalman)
        if (id == "" or co_name == "" or major_work == "" or regist_address == "" or regist_date == "" or regist_money == "" or co_number == "" or legalman == ""):
            print(QMessageBox.warning(self, "警告", "添加信息不可为空!", QMessageBox.Yes, QMessageBox.Yes))
            return
        try:
            self.db = pymysql.connect(host='localhost', port=3306, user="root", password='root', database='corporation',
                                      charset='utf8')
        except:
            QMessageBox.warning(self, '警告', "连接数据库故障", QMessageBox.Yes)
            self.db.rollback()
        sql = 'select * from t_corporate where co_id="%s"' % id  # sql指令语句
        cur = self.db.cursor()  # 获取游标
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 通过fetchall获取数据
        print('results1:', results)
        if results:
            QMessageBox.warning(self, '警告', "该信息已存在", QMessageBox.Yes)
        else:
            books = ()
            sql = 'insert into t_coporate () value(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql, books)  # 执行sql语句
            self.db.commit()
            QMessageBox.warning(self, '标题', '已成功添加企业信息，可继续添加', QMessageBox.Yes)
            self.id_lineEdit.clear()
            self.co_name_lineEdit_2.clear()
            self.major_work_lineEdit_3.clear()
            self.regist_address_lineEdit_4.clear()
            self.regist_date_lineEdit_5.setDate(QDate.currentDate())
            self.regist_money_lineEdit_6.clear()
            self.co_number_lineEdit_7.text()
            self.legalman_lineEdit_8.text()
            self.db.close()
            cur.close()


    def detail_mg_co(self):
        self.hide()  # 主界面的隐藏
        self.gtmc = detail_mg_co.Ui_MainWindow()
        #注册界面打开
        self.gtmc.show()

    def quit_sys(self):
        self.close()
        sys.exit()

if __name__ == '__main__':
    from PyQt5.Qt import *
    app = QtWidgets.QApplication(sys.argv) # 创建一个应用程序
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui1 = Ui_MainWindow()    # 创建设计好的窗口对象
    ui1.show()
    sys.exit(app.exec_())