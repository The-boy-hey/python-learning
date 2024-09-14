import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import pymysql

class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用户注册')

        label_username = QLabel('用户名：')
        self.entry_username = QLineEdit()
        label_password = QLabel('密码：')
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)
        button_register = QPushButton('注册')
        button_register.clicked.connect(self.register_user)

        vbox = QVBoxLayout()
        vbox.addWidget(label_username)
        vbox.addWidget(self.entry_username)
        vbox.addWidget(label_password)
        vbox.addWidget(self.entry_password)
        vbox.addWidget(button_register)

        self.setLayout(vbox)

    def register_user(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if not username or not password:
            QMessageBox.critical(self, '错误', '请填写用户名和密码')
            return

        try:
            db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='zhanghang', charset='utf8')
            cursor = db.cursor()

            cursor.execute("INSERT INTO consumer (user_name, user_pwd) VALUES (%s, %s)", (username, password))
            db.commit()

            QMessageBox.information(self, '成功', '注册成功！')

            self.entry_username.clear()
            self.entry_password.clear()

            db.close()

        except pymysql.Error as e:
            QMessageBox.critical(self, '错误', f'注册失败：{e}')
            db.rollback()
            db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationWindow()
    window.show()
    sys.exit(app.exec_())
