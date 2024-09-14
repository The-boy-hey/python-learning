import sys
import pymysql
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QWidget

class Ui_MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()

    def initUI(self):
        # 创建标签和文本框
        self.lbl_ac_number = QLabel('账户号码:')
        self.lbl_bank_name = QLabel('银行名称:')
        self.lbl_bank_address = QLabel('银行地址:')
        self.lbl_balance = QLabel('账户余额:')
        self.lbl_max_month_pay = QLabel('最高月支付额:')
        self.lbl_ac_phone = QLabel('联系电话:')
        self.lbl_regist_date = QLabel('注册日期 (YYYY-MM-DD):')
        self.lbl_co_number = QLabel('公司编号:')

        self.le_ac_number = QLineEdit()
        self.le_bank_name = QLineEdit()
        self.le_bank_address = QLineEdit()
        self.le_balance = QLineEdit()
        self.le_max_month_pay = QLineEdit()
        self.le_ac_phone = QLineEdit()
        self.le_regist_date = QLineEdit()
        self.le_co_number = QLineEdit()

        # 创建按钮
        self.btn_add = QPushButton('添加用户信息')
        self.btn_back = QPushButton('返回上一级')

        # 布局管理
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout(central_widget)

        # 添加布局
        hbox_ac_number = QHBoxLayout()
        hbox_ac_number.addWidget(self.lbl_ac_number)
        hbox_ac_number.addWidget(self.le_ac_number)

        hbox_bank_name = QHBoxLayout()
        hbox_bank_name.addWidget(self.lbl_bank_name)
        hbox_bank_name.addWidget(self.le_bank_name)

        hbox_bank_address = QHBoxLayout()
        hbox_bank_address.addWidget(self.lbl_bank_address)
        hbox_bank_address.addWidget(self.le_bank_address)

        hbox_balance = QHBoxLayout()
        hbox_balance.addWidget(self.lbl_balance)
        hbox_balance.addWidget(self.le_balance)

        hbox_max_month_pay = QHBoxLayout()
        hbox_max_month_pay.addWidget(self.lbl_max_month_pay)
        hbox_max_month_pay.addWidget(self.le_max_month_pay)

        hbox_ac_phone = QHBoxLayout()
        hbox_ac_phone.addWidget(self.lbl_ac_phone)
        hbox_ac_phone.addWidget(self.le_ac_phone)

        hbox_regist_date = QHBoxLayout()
        hbox_regist_date.addWidget(self.lbl_regist_date)
        hbox_regist_date.addWidget(self.le_regist_date)

        hbox_co_number = QHBoxLayout()
        hbox_co_number.addWidget(self.lbl_co_number)
        hbox_co_number.addWidget(self.le_co_number)

        vbox.addLayout(hbox_ac_number)
        vbox.addLayout(hbox_bank_name)
        vbox.addLayout(hbox_bank_address)
        vbox.addLayout(hbox_balance)
        vbox.addLayout(hbox_max_month_pay)
        vbox.addLayout(hbox_ac_phone)
        vbox.addLayout(hbox_regist_date)
        vbox.addLayout(hbox_co_number)
        vbox.addWidget(self.btn_add)
        vbox.addWidget(self.btn_back)

        # 连接信号和槽
        self.btn_add.clicked.connect(self.add_account)
        self.btn_back.clicked.connect(self.go_back)

        self.setWindowTitle('添加用户信息')
        self.show()

    def add_account(self):
        # 获取用户输入
        ac_number = self.le_ac_number.text().strip()
        bank_name = self.le_bank_name.text().strip()
        bank_address = self.le_bank_address.text().strip()
        balance = self.le_balance.text().strip()
        max_month_pay = self.le_max_month_pay.text().strip()
        ac_phone = self.le_ac_phone.text().strip()
        regist_date = self.le_regist_date.text().strip()
        co_number = self.le_co_number.text().strip()

        # 数据验证
        if not all([ac_number, bank_name, ac_phone]):
            QMessageBox.warning(self, '错误', '请填写必要的字段。')
            return

        # 插入数据到数据库
        try:
            with self.db.cursor() as cur:
                sql = "INSERT INTO t_account (ac_number, bank_name, bank_address, balabce, maxMonthpay, ac_phone, regist_date, co_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, (ac_number, bank_name, bank_address, balance, max_month_pay, ac_phone, regist_date, co_number))
                self.db.commit()
                QMessageBox.information(self, '成功', '用户信息已添加。')
                self.clear_fields()
        except pymysql.Error as e:
            QMessageBox.critical(self, '错误', f'添加用户信息失败: {str(e)}')

    def clear_fields(self):
        self.le_ac_number.clear()
        self.le_bank_name.clear()
        self.le_bank_address.clear()
        self.le_balance.clear()
        self.le_max_month_pay.clear()
        self.le_ac_phone.clear()
        self.le_regist_date.clear()
        self.le_co_number.clear()

    def go_back(self):
        # 返回上一级逻辑
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            database='zhanghang',
            charset='utf8'
        )
    except pymysql.Error as e:
        print(f"数据库连接错误: {e}")
        sys.exit(1)

    ex = Ui_MainWindow(db)
    sys.exit(app.exec_())
