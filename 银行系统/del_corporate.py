import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QAction,QMenuBar
import pymysql
import detail_mg_ac
import detail_mg_co


class CorporateModifyApp(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化数据库连接
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='financial_system', charset='utf8')
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
        self.lbl_co_number = QLabel('公司账号:')
        self.lbl_legalman = QLabel('法人')

        self.le_id = QLineEdit()
        self.le_name = QLineEdit()
        self.le_major_work = QLineEdit()
        self.le_regist_address = QLineEdit()
        self.le_regist_date = QLineEdit()
        self.le_regist_money = QLineEdit()
        self.le_co_number = QLineEdit()
        self.le_legalman = QLineEdit()


        # 创建按钮
        self.btn_load = QPushButton('加载数据')
        self.btn_delete_co = QPushButton('删除数据')
        self.btn_back = QPushButton('返回查看企业信息')

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

        hbox8.addWidget(self.lbl_legalman)
        hbox8.addWidget(self.le_legalman)


        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)
        vbox.addLayout(hbox8)
        vbox.addWidget(self.btn_load)
        vbox.addWidget(self.btn_delete_co)
        vbox.addWidget(self.btn_back)
        self.setLayout(vbox)

        # 连接信号和槽
        self.btn_load.clicked.connect(self.load_data)
        self.btn_delete_co.clicked.connect(self.delete_data)
        self.btn_back.clicked.connect(self.back_to_codetail)


        self.setWindowTitle('删除账户信息')
        self.show()

    def load_data(self):
        co_id = self.le_id.text().strip()
        if co_id.isdigit():
            sql = "SELECT co_name, major_work, regist_address, regist_date, regist_money, co_number,legalman FROM t_corporate WHERE co_id = %s"
            self.cursor.execute(sql, (co_id,))
            result = self.cursor.fetchone()
            if result:
                self.le_name.setText(result[0])
                self.le_major_work.setText(result[1])
                self.le_regist_address.setText(result[2])
                self.le_regist_date.setText(result[3].strftime('%Y-%m-%d') if result[3] is not None else '')
                self.le_regist_money.setText(str(result[4]) if result[4] else '')
                self.le_co_number.setText(result[5])
                self.le_legalman.setText(result[6])
            else:
                QMessageBox.warning(self, '错误', '未找到该公司ID的信息。')
        else:
            QMessageBox.warning(self, '错误', '请输入有效的公司ID。')

    def delete_data(self):
        a_id = self.le_a_id.text().strip()

        if a_id.isdigit():
            sql = "delete from t_coporate  where a_id = %s"
            try:
                self.cursor.execute(sql, (a_id,))
                self.db.commit()
                QMessageBox.information(self, '成功', '用户信息已删除。')
            except Exception as e:
                self.db.rollback()
                QMessageBox.warning(self, '错误', f'删除数据失败：{str(e)}')
        else:
            QMessageBox.warning(self, '错误', '请先加载一个有效的用户ID。')


    def back_to_codetail(self):
        self.hide()  # 主界面的隐藏
        self.gtc = detail_mg_co.Ui_MainWindow()
        #注册界面打开
        self.gtc.show()


    def closeEvent(self, event):
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CorporateModifyApp()
    sys.exit(app.exec_())