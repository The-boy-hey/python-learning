
import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import ui_uart_tools

class myMainWindow(qw.QMainWindow, ui_uart_tools.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.settings = None
        self.setupUi(self)

        # 初始化窗口
        self.statusbar.showMessage("status:ok")

        #加载配置文件
        self.settings=qc.QSettings("config.ini",qc.QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")

        self.config_uart_baud=self.settings.value("SETUP/UART_BAUD",type=int)
        print("uart baud(int) is %d"%self.config_uart_baud)

        # 初始化界面
        self.radioButton_recv_ascii.setChecked(True)
        self.radioButton_send_ascii.setChecked(True)
        self.spinBox.setRange(100, 30 * 1000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setWrapping(True)
        self.spinBox.setValue(1000)

        self.comboBox_baud.setCurrentText(str(self.config_uart_baud))


        #绑定信号与槽
        self.comboBox_baud.currentIndexChanged.connect(self.comboBox_baud_cb)
        self.btn_send.clicked.connect(self.btn_send_cb)
        self.action_start.triggered.connect(self.action_start_cb)
        self.action_pause.triggered.connect(self.action_pause_cb)
        self.action_stop.triggered.connect(self.action_stop_cb)
        self.action_clean.triggered.connect(self.action_clean_cb)
        self.radioButton_recv_ascii.toggled.connect(self.radioButton_recv_ascii_cb)
        self.radioButton_send_ascii.toggled.connect(self.radioButton_send_ascii_cb)
        self.radioButton_recv_hex.toggled.connect(self.radioButton_recv_hex_cb)
        self.radioButton_send_hex.toggled.connect(self.radioButton_send_hex_cb)
        self.checkBox_auto_line.toggled.connect(self.checkBox_auto_line_cb)
        self.checkBox_show_send.toggled.connect(self.checkBox_show_send_cb)
        self.checkBox_show_time.toggled.connect(self.checkBox_show_time_cb)
        self.checkBox_repeat_send.toggled.connect(self.checkBox_repeat_send_cb)
        self.spinBox.valueChanged.connect(self.spinBox_value_cb)

    def comboBox_baud_cb(self):
        content = self.comboBox_baud.currentText()
        print("combox's value is ",content)
        text="您当前选中了%s"%content
        qw.QMessageBox.information(self,"提示",text,qw.QMessageBox.Cancel | qw.QMessageBox.Ok)

    def btn_send_cb(self):
        print("your clicked btn_sand")
        # text=self.textEdit_get.toPlainText()
        # print("text is ",text)
        # #加载到combox的下拉选项
        # self.comboBox_uart.addItem(text)
        #测试QSettings写入

        uart_baud=self.comboBox_baud.currentText()
        print("current uart baud is ",uart_baud)
        self.settings.setValue("SETUP/UART_BAUD",uart_baud)


    def action_start_cb(self):
        print("your clicked action_start")


    def action_pause_cb(self):
        print("your clicked action_pause")


    def action_stop_cb(self):
        print("your clicked action_stop")


    def action_clean_cb(self):
        print("your clicked action_clean")



    def radioButton_recv_ascii_cb(self):
        print("your selected radioButton_recv_ascii")


    def radioButton_send_ascii_cb(self):
        print("your selected radioButton_send_ascii")


    def radioButton_recv_hex_cb(self):
        print("your selected radioButton_recv_hex")


    def radioButton_send_hex_cb(self):
        print("your selected radioButton_send_hex")


    def checkBox_auto_line_cb(self):
        print("your selected checkBox_auto_line")
        res_auto_line=self.checkBox_auto_line.isChecked()
        print("auto_line is ",res_auto_line)
        res_show_send=self.checkBox_show_send.isChecked()
        print("show_send is ",res_show_send)
        res_show_time=self.checkBox_show_time.isChecked()
        print("res_show_time is",res_show_time)
        res_repeat_sand=self.checkBox_repeat_send.isChecked()
        print("res_repeat_sand is ",res_repeat_sand)


    def checkBox_show_send_cb(self):
        print("your selected checkBox_show_send")


    def checkBox_show_time_cb(self):
        print("your selected checkBox_show_time")



    def checkBox_repeat_send_cb(self):
        print("your selected checkBox_repeat")


    def spinBox_value_cb(self):
        value=self.spinBox.value()
        print("spinBox's current value is",value)





if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w=myMainWindow()
    w.show()
    sys.exit(app.exec_())
