import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
import pymysql


class CorporateInfoEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_data()

    def initUI(self):
        self.setWindowTitle('企业信息编辑器')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # 假设的UI元素
        self.label_name = QLabel('企业名称:')
        self.line_name = QLineEdit()

        # 添加布局
        layout.addWidget(self.label_name)
        layout.addWidget(self.line_name)

        # 假设的提交按钮
        self.button_submit = QPushButton('提交')
        self.button_submit.clicked.connect(self.on_submit)
        layout.addWidget(self.button_submit)

        self.setLayout(layout)

    def load_data(self):
        # 连接到MySQL数据库
        db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'zhanghang',
            'charset': 'utf8mb4',  # 使用utf8mb4以支持更广泛的Unicode字符
            'cursorclass': pymysql.cursors.DictCursor
        }
        connection = pymysql.connect(**db_config)

        try:
            with connection.cursor() as cursor:
                # 假设我们加载第一条记录
                sql = "SELECT * FROM corporate LIMIT 1"
                cursor.execute(sql)
                row = cursor.fetchone()
                if row:
                    self.line_name.setText(row['co_name'])
                    # 设置其他UI元素的值...

        finally:
            connection.close()

    def on_submit(self):
        # 这里实现提交逻辑
        # 注意：在这个简单的例子中，我们没有实现实际的提交逻辑
        # 你可以在这里添加代码来更新数据库或进行其他操作
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CorporateInfoEditor()
    ex.show()
    sys.exit(app.exec_())