import sys
import pymysql
import qdarkstyle
from PyQt5 import QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowTitle("账户删除界面")
        self.setGeometry(100, 100, 500, 250)

        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            database='zhanghang',
            charset='utf8'
        )

        self.init_ui()

        self.delete_button.clicked.connect(self.delete_account)
        self.back_button.clicked.connect(self.go_back)

    def init_ui(self):
        self.label_ac_number = QtWidgets.QLabel("账户号码:", self)
        self.label_ac_number.setGeometry(30, 30, 100, 30)

        self.ac_number_input = QtWidgets.QLineEdit(self)
        self.ac_number_input.setGeometry(150, 30, 300, 30)

        self.label_co_number = QtWidgets.QLabel("公司编号:", self)
        self.label_co_number.setGeometry(30, 80, 100, 30)

        self.co_number_input = QtWidgets.QLineEdit(self)
        self.co_number_input.setGeometry(150, 80, 300, 30)

        self.delete_button = QtWidgets.QPushButton("删除账户", self)
        self.delete_button.setGeometry(100, 130, 100, 30)

        self.back_button = QtWidgets.QPushButton("返回上一级", self)
        self.back_button.setGeometry(300, 130, 100, 30)

    def delete_account(self):
        ac_number = self.ac_number_input.text()
        co_number = self.co_number_input.text()

        if not ac_number or not co_number:
            QtWidgets.QMessageBox.warning(self, "警告", "请填写账户号码和公司编号")
            return

        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM t_account WHERE ac_number = %s AND co_number = %s", (ac_number, co_number))
            if cursor.rowcount > 0:
                self.db.commit()
                QtWidgets.QMessageBox.information(self, "信息", "账户删除成功")
                self.ac_number_input.clear()
                self.co_number_input.clear()
            else:
                QtWidgets.QMessageBox.warning(self, "信息", "未找到匹配的账户")
                self.ac_number_input.clear()
                self.co_number_input.clear()
        except Exception as e:
            self.db.rollback()
            QtWidgets.QMessageBox.critical(self, "错误", f"删除失败: {e}")
        finally:
            cursor.close()

    def go_back(self):
        # 关闭当前窗口或实现其他返回逻辑
        self.close()

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window.show()
    sys.exit(app.exec_())
