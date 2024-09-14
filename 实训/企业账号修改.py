import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import pymysql

class CorporateModifyApp(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化数据库连接
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='zhanghang', charset='utf8')
        self.cursor = self.db.cursor()

        self.initUI()

    def initUI(self):
        # 创建标签和文本框用于每个字段
        self.lbl_id = QLabel('ID:')
        self.lbl_name = QLabel('公司名称:')
        self.lbl_major_work = QLabel('主营业务:')
        self.lbl_regist_address = QLabel('注册地址:')
        self.lbl_regist_date = QLabel('注册日期 (YYYY-MM-DD):')
        self.lbl_regist_money = QLabel('注册资本:')
        self.lbl_co_number = QLabel('公司编号:')

        self.le_id = QLineEdit()
        self.le_name = QLineEdit()
        self.le_major_work = QLineEdit()
        self.le_regist_address = QLineEdit()
        self.le_regist_date = QLineEdit()
        self.le_regist_money = QLineEdit()
        self.le_co_number = QLineEdit()

        # 创建按钮
        self.btn_load = QPushButton('加载数据')
        self.btn_update = QPushButton('更新数据')

        # 布局管理
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        hbox7 = QHBoxLayout()

        hbox1.addWidget(self.lbl_id)
        hbox1.addWidget(self.le_id)
        hbox1.addWidget(self.btn_load)

        hbox2.addWidget(self.lbl_name)
        hbox2.addWidget(self.le_name)

        hbox3.addWidget(self.lbl_major_work)
        hbox3.addWidget(self.le_major_work)

        hbox4.addWidget(self.lbl_regist_address)
        hbox4.addWidget(self.le_regist_address)

        hbox5.addWidget(self.lbl_regist_date)
        hbox5.addWidget(self.le_regist_date)

        hbox6.addWidget(self.lbl_regist_money)
        hbox6.addWidget(self.le_regist_money)

        hbox7.addWidget(self.lbl_co_number)
        hbox7.addWidget(self.le_co_number)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)
        vbox.addWidget(self.btn_update)

        self.setLayout(vbox)

        # 连接信号和槽
        self.btn_load.clicked.connect(self.load_data)
        self.btn_update.clicked.connect(self.update_data)

        self.setWindowTitle('修改企业信息')
        self.show()

    def load_data(self):
        co_id = self.le_id.text().strip()
        if co_id.isdigit():
            sql = "SELECT co_name, major_work, regist_address, regist_date, regist_money, co_number FROM t_corporate WHERE co_id = %s"
            self.cursor.execute(sql, (co_id,))
            result = self.cursor.fetchone()
            if result:
                self.le_name.setText(result[0])
                self.le_major_work.setText(result[1])
                self.le_regist_address.setText(result[2])
                self.le_regist_date.setText(result[3].strftime('%Y-%m-%d') if result[3] else '')
                self.le_regist_money.setText(str(result[4]) if result[4] else '')
                self.le_co_number.setText(result[5])
            else:
                QMessageBox.warning(self, '错误', '未找到该公司ID的信息。')
        else:
            QMessageBox.warning(self, '错误', '请输入有效的公司ID。')

    def update_data(self):
        co_id = self.le_id.text().strip()
        co_name = self.le_name.text().strip()
        major_work = self.le_major_work.text().strip()
        regist_address = self.le_regist_address.text().strip()
        regist_date = self.le_regist_date.text().strip()
        regist_money = self.le_regist_money.text().strip()
        co_number = self.le_co_number.text().strip()

        if co_id.isdigit():
            sql = "UPDATE t_corporate SET co_name = %s, major_work = %s, regist_address = %s, regist_date = %s, regist_money = %s, co_number = %s WHERE co_id = %s"
            try:
                self.cursor.execute(sql, (co_name, major_work, regist_address, regist_date, regist_money, co_number, co_id))
                self.db.commit()
                QMessageBox.information(self, '成功', '企业信息已更新。')
            except Exception as e:
                self.db.rollback()
                QMessageBox.warning(self, '错误', f'更新数据失败：{str(e)}')
        else:
            QMessageBox.warning(self, '错误', '请先加载一个有效的公司ID。')

    def closeEvent(self, event):
        self.db.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CorporateModifyApp()
    sys.exit(app.exec_())
