import sys
import pymysql
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QInputDialog, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class CorporateInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('企业信息展示')
        self.setGeometry(100, 100, 800, 600)

        # 设置背景颜色为黑色
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)

        # 创建菜单栏
        menubar = self.menuBar()

        # 添加菜单项
        queryMenu = menubar.addMenu('查询企业账号信息')
        exitAction = QAction('退出', self)
        exitAction.triggered.connect(self.close)

        # 添加查询功能
        self.queryByIdAction = QAction('按ID查询', self)
        self.queryByIdAction.triggered.connect(self.queryById)
        queryMenu.addAction(self.queryByIdAction)

        self.queryByNameAction = QAction('按公司名称查询', self)
        self.queryByNameAction.triggered.connect(self.queryByName)
        queryMenu.addAction(self.queryByNameAction)

        self.queryByNumberAction = QAction('按账号查询', self)
        self.queryByNumberAction.triggered.connect(self.queryByNumber)
        queryMenu.addAction(self.queryByNumberAction)

        menubar.addAction(exitAction)

        # 查询结果显示区域
        self.resultTable = QTableWidget()
        self.resultTable.setColumnCount(7)
        self.resultTable.setHorizontalHeaderLabels(['ID', '公司名称', '主要业务', '注册地址', '注册日期', '注册资金', '公司账号'])

        # 设置主布局
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.resultTable)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def executeQuery(self, query, params):
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', database='zhanghang', charset='utf8')
        cursor = db.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        db.close()
        return results

    def queryById(self):
        query, ok = self.getQueryInput('按ID查询', '请输入公司ID:')
        if ok and query:
            sql = "SELECT * FROM t_corporate WHERE co_id = %s"
            results = self.executeQuery(sql, (query,))
            self.displayResults(results)

    def queryByName(self):
        query, ok = self.getQueryInput('按公司名称查询', '请输入公司名称:')
        if ok and query:
            sql = "SELECT * FROM t_corporate WHERE co_name LIKE %s"
            results = self.executeQuery(sql, ('%' + query + '%',))
            self.displayResults(results)

    def queryByNumber(self):
        query, ok = self.getQueryInput('按账号查询', '请输入公司账号:')
        if ok and query:
            sql = "SELECT * FROM t_corporate WHERE co_number = %s"
            results = self.executeQuery(sql, (query,))
            self.displayResults(results)

    def getQueryInput(self, title, label):
        query, ok = QInputDialog.getText(self, title, label)
        return query, ok

    def displayResults(self, results):
        self.resultTable.setRowCount(len(results))
        for rowIndex, row in enumerate(results):
            for colIndex, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                if rowIndex % 2 == 0:
                    item.setBackground(QColor(220, 220, 220))  # 浅灰色
                else:
                    item.setBackground(QColor(255, 255, 255))  # 白色
                self.resultTable.setItem(rowIndex, colIndex, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CorporateInfoApp()
    ex.show()
    sys.exit(app.exec_())
