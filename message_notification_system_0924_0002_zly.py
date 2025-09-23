# 代码生成时间: 2025-09-24 00:02:22
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import QTimer

"""
消息通知系统，使用Python和PyQt5框架实现。
"""

class MessageNotificationSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('消息通知系统')
        self.setGeometry(100, 100, 300, 200)  # 设置窗口位置和大小
        self.initUI()

    def initUI(self):
        # 创建中心窗口部件
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # 创建布局
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        # 创建标签显示消息
        self.messageLabel = QLabel('无消息')
        self.layout.addWidget(self.messageLabel)

        # 创建按钮显示通知
        self.notifyButton = QPushButton('显示通知')
        self.notifyButton.clicked.connect(self.showNotification)
        self.layout.addWidget(self.notifyButton)

        # 创建定时器，用于定时更新消息
        self.timer = QTimer(self.updateMessage)
        self.timer.start(1000)  # 每1秒更新一次

    def updateMessage(self):
        """
        随机生成一条消息并显示在标签上。
        """
        messages = ['消息1', '消息2', '消息3', '无消息']
        self.messageLabel.setText(messages[0])
        if self.messageLabel.text() != '无消息':
            self.showMessage()

    def showNotification(self):
        """
        显示通知消息。
        """
        QMessageBox.information(self, '通知', '您有新的消息！')

    def showMessage(self):
        """
        显示消息。
        """
        QMessageBox.information(self, '消息', self.messageLabel.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MessageNotificationSystem()
    window.show()
    sys.exit(app.exec_())