# 导入所需的模块
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, pyqtSlot
import sqlite3

# 数据库连接
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()


# 输入界面窗口类
class InputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('输入企业编号')
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel('请输入企业编号：', self)
        self.input_box = QLineEdit(self)
        self.submit_button = QPushButton('确认', self)

        self.submit_button.clicked.connect(self.on_submit_clicked)

        layout.addWidget(self.label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    @pyqtSlot()
    def on_submit_clicked(self):
        company_id = self.input_box.text()
        # 跳转到显示企业信息界面
        self.display_window = DisplayWindow(company_id)
        self.display_window.show()
        self.close()


# 显示企业信息界面窗口类
class DisplayWindow(QWidget):
    def __init__(self, company_id):
        super().__init__()
        self.setWindowTitle('企业信息')
        self.resize(400, 200)

        layout = QVBoxLayout()

        # 查询数据库，获取企业信息
        query = "SELECT * FROM companies WHERE id = ?"
        cursor.execute(query, (company_id,))
        company_info = cursor.fetchone()  # 假设返回一个元组

        if company_info:
            # 显示企业信息
            name_label = QLabel(f'企业名称： {company_info[1]}', self)
            address_label = QLabel(f'地址： {company_info[2]}', self)
            contact_label = QLabel(f'联系方式： {company_info[3]}', self)

            layout.addWidget(name_label)
            layout.addWidget(address_label)
            layout.addWidget(contact_label)
        else:
            not_found_label = QLabel('未找到该企业信息', self)
            layout.addWidget(not_found_label)

        self.setLayout(layout)


# 主程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建输入企业编号的界面
    input_window = InputWindow()
    input_window.show()

    sys.exit(app.exec_())
