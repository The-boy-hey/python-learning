import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
import pymysql

class 添加企业信息窗口(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('添加企业信息')
        self.setGeometry(200, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.co_name_label = QLabel('公司名称:')
        self.co_name_edit = QLineEdit()
        self.layout.addWidget(self.co_name_label)
        self.layout.addWidget(self.co_name_edit)

        self.major_work_label = QLabel('主营业务:')
        self.major_work_edit = QLineEdit()
        self.layout.addWidget(self.major_work_label)
        self.layout.addWidget(self.major_work_edit)

        self.regist_address_label = QLabel('注册地址:')
        self.regist_address_edit = QLineEdit()
        self.layout.addWidget(self.regist_address_label)
        self.layout.addWidget(self.regist_address_edit)

        self.regist_date_label = QLabel('注册日期:')
        self.regist_date_edit = QLineEdit()
        self.layout.addWidget(self.regist_date_label)
        self.layout.addWidget(self.regist_date_edit)

        self.regist_money_label = QLabel('注册资本:')
        self.regist_money_edit = QLineEdit()
        self.layout.addWidget(self.regist_money_label)
        self.layout.addWidget(self.regist_money_edit)

        self.co_number_label = QLabel('统一社会信用代码:')
        self.co_number_edit = QLineEdit()
        self.layout.addWidget(self.co_number_label)
        self.layout.addWidget(self.co_number_edit)

        self.add_button = QPushButton('添加企业信息')
        self.add_button.clicked.connect(self.add_corporate_info)
        self.layout.addWidget(self.add_button)

        self.central_widget.setLayout(self.layout)

    def add_corporate_info(self):
        co_name = self.co_name_edit.text().strip()
        major_work = self.major_work_edit.text().strip()
        regist_address = self.regist_address_edit.text().strip()
        regist_date = self.regist_date_edit.text().strip()
        regist_money = self.regist_money_edit.text().strip()
        co_number = self.co_number_edit.text().strip()

        # 验证必填字段
        if not co_name or not major_work:
            QMessageBox.warning(self, '验证错误', '公司名称和主营业务为必填字段。')
            return

        # 连接数据库并插入数据
        try:
            db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='zhanghang', charset='utf8')
            cursor = db.cursor()

            # 插入数据到t_corporate表
            sql = "INSERT INTO t_corporate (co_name, major_work, regist_address, regist_date, regist_money, co_number) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (co_name, major_work, regist_address, regist_date, regist_money, co_number))
            db.commit()

            QMessageBox.information(self, '成功', '企业信息添加成功。')
            self.clear_fields()

        except Exception as e:
            QMessageBox.critical(self, '错误', f'添加企业信息时出错: {str(e)}')

        finally:
            if 'db' in locals() and db.open():
                db.close()

    def clear_fields(self):
        self.co_name_edit.clear()
        self.major_work_edit.clear()
        self.regist_address_edit.clear()
        self.regist_date_edit.clear()
        self.regist_money_edit.clear()
        self.co_number_edit.clear()

def main():
    app = QApplication(sys.argv)
    window = 添加企业信息窗口()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

