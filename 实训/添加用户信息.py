import sys

import qdarkstyle
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
import mysql.connector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('添加账户信息')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # 标签和输入框
        self.label_ac_number = QLabel('账户号码:', self)
        self.edit_ac_number = QLineEdit(self)
        layout.addWidget(self.label_ac_number)
        layout.addWidget(self.edit_ac_number)

        self.label_bank_name = QLabel('银行名称:', self)
        self.edit_bank_name = QLineEdit(self)
        layout.addWidget(self.label_bank_name)
        layout.addWidget(self.edit_bank_name)

        self.label_bank_address = QLabel('银行地址:', self)
        self.edit_bank_address = QLineEdit(self)
        layout.addWidget(self.label_bank_address)
        layout.addWidget(self.edit_bank_address)

        self.label_balance = QLabel('账户余额:', self)
        self.edit_balance = QLineEdit(self)
        layout.addWidget(self.label_balance)
        layout.addWidget(self.edit_balance)

        self.label_max_month_pay = QLabel('最大月支付:', self)
        self.edit_max_month_pay = QLineEdit(self)
        layout.addWidget(self.label_max_month_pay)
        layout.addWidget(self.edit_max_month_pay)

        self.label_ac_phone = QLabel('账户电话:', self)
        self.edit_ac_phone = QLineEdit(self)
        layout.addWidget(self.label_ac_phone)
        layout.addWidget(self.edit_ac_phone)

        self.label_regist_date = QLabel('注册日期(YYYY-MM-DD):', self)
        self.edit_regist_date = QLineEdit(self)
        layout.addWidget(self.label_regist_date)
        layout.addWidget(self.edit_regist_date)

        self.label_co_number = QLabel('公司号码:', self)
        self.edit_co_number = QLineEdit(self)
        layout.addWidget(self.label_co_number)
        layout.addWidget(self.edit_co_number)

        # 提交按钮
        self.btn_submit = QPushButton('提交', self)
        self.btn_submit.clicked.connect(self.submit_data)
        layout.addWidget(self.btn_submit)

        central_widget.setLayout(layout)

    def submit_data(self):
        # 从输入框获取数据
        ac_number = self.edit_ac_number.text().strip()
        bank_name = self.edit_bank_name.text().strip()
        bank_address = self.edit_bank_address.text().strip()
        balance = self.edit_balance.text().strip()
        max_month_pay = self.edit_max_month_pay.text().strip()
        ac_phone = self.edit_ac_phone.text().strip()
        regist_date = self.edit_regist_date.text().strip()
        co_number = self.edit_co_number.text().strip()

        # 数据验证（这里可以根据需要添加更多的验证逻辑）

        # 连接到数据库并插入数据
        try:
            conn = mysql.connector.connect(
                host='localhost', port=3306, user='root', passwd='root', database='zhanghang', charset='utf8'
            )

            cursor = conn.cursor()

            # 执行插入语句
            sql = "INSERT INTO t_account (ac_number, bank_name, bank_address, balabce, maxMonthpay, ac_phone, regist_date, co_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (ac_number, bank_name, bank_address, balance, max_month_pay, ac_phone, regist_date, co_number))

            conn.commit()

            QMessageBox.information(self, '成功', '账户信息添加成功！')

        except mysql.connector.Error as e:
            print(f"Error inserting data into MySQL table: {e}")
            QMessageBox.warning(self, '错误', f'添加账户信息时出错：{e}')

        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())
