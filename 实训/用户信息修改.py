import sys

import qdarkstyle
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QWidget
from PyQt5.QtCore import Qt
import pymysql

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', database='zhanghang', charset='utf8')
        self.cursor = self.db.cursor()

        self.initUI()

    def initUI(self):
        self.lbl_id = QLabel('ID:')
        self.lbl_ac_number = QLabel('账号:')
        self.lbl_bank_name = QLabel('银行名称:')
        self.lbl_bank_address = QLabel('银行地址:')
        self.lbl_balance = QLabel('账户余额:')
        self.lbl_max_month_pay = QLabel('最大月支付:')
        self.lbl_ac_phone = QLabel('账户电话:')
        self.lbl_regist_date = QLabel('注册日期 (YYYY-MM-DD):')
        self.lbl_co_number = QLabel('公司编号:')

        self.le_id = QLineEdit()
        self.le_ac_number = QLineEdit()
        self.le_bank_name = QLineEdit()
        self.le_bank_address = QLineEdit()
        self.le_balance = QLineEdit()
        self.le_max_month_pay = QLineEdit()
        self.le_ac_phone = QLineEdit()
        self.le_regist_date = QLineEdit()
        self.le_co_number = QLineEdit()

        self.btn_load = QPushButton('加载数据')
        self.btn_update = QPushButton('更新数据')
        self.btn_return = QPushButton('返回')  # Add return button

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout(central_widget)
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        hbox7 = QHBoxLayout()
        hbox8 = QHBoxLayout()
        hbox9 = QHBoxLayout()

        hbox1.addWidget(self.lbl_id)
        hbox1.addWidget(self.le_id)
        hbox1.addWidget(self.btn_load)

        hbox2.addWidget(self.lbl_ac_number)
        hbox2.addWidget(self.le_ac_number)

        hbox3.addWidget(self.lbl_bank_name)
        hbox3.addWidget(self.le_bank_name)

        hbox4.addWidget(self.lbl_bank_address)
        hbox4.addWidget(self.le_bank_address)

        hbox5.addWidget(self.lbl_balance)
        hbox5.addWidget(self.le_balance)

        hbox6.addWidget(self.lbl_max_month_pay)
        hbox6.addWidget(self.le_max_month_pay)

        hbox7.addWidget(self.lbl_ac_phone)
        hbox7.addWidget(self.le_ac_phone)

        hbox8.addWidget(self.lbl_regist_date)
        hbox8.addWidget(self.le_regist_date)

        hbox9.addWidget(self.lbl_co_number)
        hbox9.addWidget(self.le_co_number)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)
        vbox.addLayout(hbox8)
        vbox.addLayout(hbox9)
        vbox.addWidget(self.btn_update)
        vbox.addWidget(self.btn_return)  # Add return button to layout

        # Connect signals and slots
        self.btn_load.clicked.connect(self.load_data)
        self.btn_update.clicked.connect(self.update_data)
        self.btn_return.clicked.connect(self.return_to_previous)  # Connect return button

        self.setWindowTitle('修改账户信息')
        self.show()

    def load_data(self):
        a_id = self.le_id.text().strip()
        if a_id.isdigit():
            sql = "SELECT ac_number, bank_name, bank_address, balance, maxMonthpay, ac_phone, regist_date, co_number FROM t_account WHERE a_id = %s"
            self.cursor.execute(sql, (a_id,))
            result = self.cursor.fetchone()
            if result:
                self.le_ac_number.setText(result[0])
                self.le_bank_name.setText(result[1])
                self.le_bank_address.setText(result[2])
                self.le_balance.setText(str(result[3]) if result[3] is not None else '')
                self.le_max_month_pay.setText(str(result[4]) if result[4] is not None else '')
                self.le_ac_phone.setText(result[5])
                self.le_regist_date.setText(result[6].strftime('%Y-%m-%d') if result[6] else '')
                self.le_co_number.setText(result[7])
            else:
                QMessageBox.warning(self, '错误', '未找到该账户ID的信息。')
        else:
            QMessageBox.warning(self, '错误', '请输入有效的账户ID。')

    def update_data(self):
        a_id = self.le_id.text().strip()
        ac_number = self.le_ac_number.text().strip()
        bank_name = self.le_bank_name.text().strip()
        bank_address = self.le_bank_address.text().strip()
        balance = self.le_balance.text().strip()
        max_month_pay = self.le_max_month_pay.text().strip()
        ac_phone = self.le_ac_phone.text().strip()
        regist_date = self.le_regist_date.text().strip()
        co_number = self.le_co_number.text().strip()

        if a_id.isdigit():
            sql = "UPDATE t_account SET ac_number = %s, bank_name = %s, bank_address = %s, balance = %s, maxMonthpay = %s, ac_phone = %s, regist_date = %s, co_number = %s WHERE a_id = %s"
            try:
                self.cursor.execute(sql, (ac_number, bank_name, bank_address, balance, max_month_pay, ac_phone, regist_date, co_number, a_id))
                self.db.commit()
                QMessageBox.information(self, '成功', '账户信息已更新。')
            except Exception as e:
                self.db.rollback()
                QMessageBox.warning(self, '错误', f'更新数据失败：{str(e)}')
        else:
            QMessageBox.warning(self, '错误', '请先加载一个有效的账户ID。')

    def return_to_previous(self):
        QMessageBox.information(self, '返回', '返回到上一个界面。')
        self.close()

    def closeEvent(self, event):
        self.db.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())