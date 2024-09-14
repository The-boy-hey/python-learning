import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QAction,QMenuBar
import pymysql
import detail_mg_ac

class CorporateModifyApp(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化数据库连接
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='financial_system', charset='utf8')
        self.cursor = self.db.cursor()

        self.initUI()


    def initUI(self):
        # 创建标签和文本框用于每个字段
        self.lbl_a_id = QLabel('ID:')
        self.lbl_ac_number = QLabel('用户名称:')
        self.lbl_bank_name = QLabel('开户行:')
        self.lbl_bank_address = QLabel('开户行地址:')
        self.lbl_balabce = QLabel('余额:')
        self.lbl_maxMonthpay = QLabel('每月最大支出:')
        self.lbl_ac_phone = QLabel('绑定电话:')
        self.lbl_regist_date = QLabel('注册日期 (YYYY-MM-DD):')
        self.lbl_co_number = QLabel('公司账号:')

        self.le_a_id = QLineEdit()
        self.le_ac_number = QLineEdit()
        self.le_bank_name = QLineEdit()
        self.le_bank_address = QLineEdit()
        self.le_balabce = QLineEdit()
        self.le_maxMonthpay = QLineEdit()
        self.le_ac_phone = QLineEdit()
        self.le_regist_date = QLineEdit()
        self.le_co_number = QLineEdit()


        # 创建按钮
        self.btn_load = QPushButton('加载数据')
        self.btn_delete = QPushButton('删除数据')
        self.btn_back = QPushButton('返回账户列表')

        # 布局管理
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        hbox7 = QHBoxLayout()
        hbox8 = QHBoxLayout()
        hbox9 = QHBoxLayout()

        hbox1.addWidget(self.lbl_a_id)
        hbox1.addWidget(self.le_a_id)
        hbox1.addWidget(self.btn_load)

        hbox2.addWidget(self.lbl_ac_number)
        hbox2.addWidget(self.le_ac_number)

        hbox3.addWidget(self.lbl_bank_name)
        hbox3.addWidget(self.le_bank_name)

        hbox4.addWidget(self.lbl_bank_address)
        hbox4.addWidget(self.le_bank_address)

        hbox5.addWidget(self.lbl_balabce)
        hbox5.addWidget(self.le_balabce)

        hbox6.addWidget(self.lbl_maxMonthpay)
        hbox6.addWidget(self.le_maxMonthpay)

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
        vbox.addWidget(self.btn_delete)
        vbox.addWidget(self.btn_back)

        self.setLayout(vbox)

        # 连接信号和槽
        self.btn_load.clicked.connect(self.load_data)
        self.btn_delete.clicked.connect(self.delete_data)
        self.btn_back.clicked.connect(self.back_to_acdetail)


        self.setWindowTitle('删除账户信息')
        self.show()

    def load_data(self):
        a_id = self.le_a_id.text().strip()
        if a_id.isdigit():
            sql = "SELECT ac_number, bank_name, bank_address, balabce, maxMonthpay, ac_phone, regist_date, co_number FROM t_account WHERE a_id = %s"
            try:
                self.cursor.execute(sql, (a_id,))
                result = self.cursor.fetchone()
                if result:
                    self.le_ac_number.setText(result[0])
                    self.le_bank_name.setText(result[1])
                    self.le_bank_address.setText(result[2])
                    self.le_balabce.setText(str(result[3]))  # 假设balabce是数字类型
                    self.le_maxMonthpay.setText(str(result[4]))  # 假设maxMonthmoney也是数字类型
                    self.le_ac_phone.setText(result[5])
                    self.le_regist_date.setText(result[6].strftime('%Y-%m-%d') if result[6] is not None else '')
                    self.le_co_number.setText(result[7])
                else:
                    QMessageBox.warning(self, '错误', '未找到该用户ID的信息。')
            except (pymysql.MySQLError, Exception) as e:
                QMessageBox.critical(self, '数据库错误', f'数据库查询失败: {e}')
        else:
            QMessageBox.warning(self, '错误', '请输入有效的用户ID。')
    def delete_data(self):
        a_id = self.le_a_id.text().strip()

        if a_id.isdigit():
            sql = "delete from t_account  where a_id = %s"
            try:
                self.cursor.execute(sql, (a_id,))
                self.db.commit()
                QMessageBox.information(self, '成功', '用户信息已删除。')
            except Exception as e:
                self.db.rollback()
                QMessageBox.warning(self, '错误', f'删除数据失败：{str(e)}')
        else:
            QMessageBox.warning(self, '错误', '请先加载一个有效的用户ID。')


    def back_to_acdetail(self):
        self.hide()  # 主界面的隐藏
        self.gtc = detail_mg_ac.Ui_MainWindow()
        #注册界面打开
        self.gtc.show()


    def closeEvent(self, event):
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CorporateModifyApp()
    sys.exit(app.exec_())