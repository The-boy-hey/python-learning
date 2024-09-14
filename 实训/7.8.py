import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QDateEdit
from PyQt5.QtCore import Qt, QDate

class AddCorporateInfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('添加企业信息')
        self.setGeometry(100, 100, 600, 400)

        # 创建各个组件
        lbl_name = QLabel('公司名称:')
        self.txt_name = QLineEdit()

        lbl_major_work = QLabel('主要业务:')
        self.txt_major_work = QLineEdit()

        lbl_regist_address = QLabel('注册地址:')
        self.txt_regist_address = QLineEdit()

        lbl_regist_date = QLabel('注册日期:')
        self.date_regist_date = QDateEdit()
        self.date_regist_date.setDate(QDate.currentDate())

        lbl_regist_money = QLabel('注册资金:')
        self.txt_regist_money = QLineEdit()

        lbl_co_number = QLabel('公司编号:')
        self.txt_co_number = QLineEdit()

        btn_submit = QPushButton('添加企业信息')
        btn_submit.clicked.connect(self.submit_corporate_info)

        # 创建布局
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        form_layout.addRow(lbl_name, self.txt_name)
        form_layout.addRow(lbl_major_work, self.txt_major_work)
        form_layout.addRow(lbl_regist_address, self.txt_regist_address)
        form_layout.addRow(lbl_regist_date, self.date_regist_date)
        form_layout.addRow(lbl_regist_money, self.txt_regist_money)
        form_layout.addRow(lbl_co_number, self.txt_co_number)

        layout.addLayout(form_layout)
        layout.addWidget(btn_submit)

        self.setLayout(layout)

    def submit_corporate_info(self):
        co_name = self.txt_name.text()
        major_work = self.txt_major_work.text()
        regist_address = self.txt_regist_address.text()
        regist_date = self.date_regist_date.date().toString(Qt.ISODate)
        regist_money = self.txt_regist_money.text()
        co_number = self.txt_co_number.text()

        # 在这里添加将数据提交到数据库的代码
        print(f'提交企业信息：{co_name}, {major_work}, {regist_address}, {regist_date}, {regist_money}, {co_number}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddCorporateInfoWindow()
    window.show()
    sys.exit(app.exec_())
