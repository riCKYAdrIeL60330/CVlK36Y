# 代码生成时间: 2025-09-04 20:12:01
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import datetime

class NotificationSystem(QMainWindow):
    """消息通知系统主窗口类"""
    def __init__(self, parent=None):
        super(NotificationSystem, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('消息通知系统')

        # 创建主布局
        self.layout = QVBoxLayout()

        # 创建显示消息的标签
        self.messageLabel = QLabel()
        self.layout.addWidget(self.messageLabel)

        # 创建发送消息的按钮
        self.sendButton = QPushButton('发送消息')
        self.sendButton.clicked.connect(self.sendMessage)
        self.layout.addWidget(self.sendButton)

        # 设置中央组件
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        # 设置窗口初始大小
        self.resize(300, 200)

    def sendMessage(self):
        # 获取当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 模拟消息内容
        message = f'消息发送时间：{current_time}'
        # 显示消息
        self.messageLabel.setText(message)
        # 弹出消息框提示
        QMessageBox.information(self, '消息通知', message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    notification_system = NotificationSystem()
    notification_system.show()
    sys.exit(app.exec_())