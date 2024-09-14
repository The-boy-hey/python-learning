import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import pymysql
import 登录页面
# from co_number import 登录页面

# 数据库连接信息
db_config = {
    'host': 'localhost',    # 数据库主机名
    'port': 3306,           # 数据库端口
    'user': 'root',         # 数据库用户名
    'password': 'root',     # 数据库密码
    'database': 'zhanghang',# 数据库名，修改为你的数据库名
    'charset': 'utf8'       # 数据库字符集
}

class MainWindow(QMainWindow):
    def __init__(self, co_number):
        super().__init__()
        self.co_number = co_number
        self.initUI()

    def initUI(self):
        self.setWindowTitle('账户信息')  # 设置窗口标题
        self.setGeometry(200, 200, 800, 600)  # 设置窗口位置和大小

        self.table = QTableWidget()  # 创建表格部件
        self.table.setColumnCount(8)  # 设置表格列数为8
        self.table.setHorizontalHeaderLabels(
            ['ID', '账号', '银行名称', '银行地址', '余额', '最大月付', '电话', '注册日期'])  # 设置表头标签

        self.load_data()  # 加载数据到表格

        vbox = QVBoxLayout()  # 创建垂直布局
        vbox.addWidget(self.table)  # 添加表格部件到布局

        self.setLayout(vbox)  # 设置窗口布局为垂直布局

    def load_data(self):
        try:
            conn = pymysql.connect(**db_config)
            cursor = conn.cursor()

            query = """
                SELECT a_id, ac_number, bank_name, bank_address, balabce, maxMonthpay, ac_phone, regist_date 
                FROM t_account 
                WHERE co_number = %s
            """
            cursor.execute(query, (self.co_number,))
            results = cursor.fetchall()

            self.table.setRowCount(len(results))  # 设置表格行数为查询结果的长度

            for row_index, row_data in enumerate(results):  # 遍历查询结果的行索引和行数据
                for col_index, col_data in enumerate(row_data):  # 遍历行数据的列索引和列数据
                    item = QTableWidgetItem(str(col_data))  # 创建表格项，转换为字符串类型
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # 设置表格项不可编辑
                    self.table.setItem(row_index, col_index, item)  # 设置表格的行列项

            cursor.close()
            conn.close()

        except pymysql.Error as e:
            QMessageBox.critical(self, '数据库错误', f'数据库连接错误: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # co_number = self.co_number  # 替换成要查询的 co_number
    main_window = MainWindow(登录页面.co_number)
    main_window.show()
    sys.exit(app.exec_())
