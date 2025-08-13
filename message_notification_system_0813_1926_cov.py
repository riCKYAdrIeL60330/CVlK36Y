# 代码生成时间: 2025-08-13 19:26:48
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, Qt


# 定义一个线程类用于异步显示消息通知
class NotificationThread(QThread):
    # 创建一个信号，用于通知UI线程更新消息
    message_signal = pyqtSignal(str)

    def __init__(self, message):
        super().__init__()
        self.message = message

    def run(self):
        # 在线程中运行，模拟一个延迟
        self.sleep(2)
        # 发送消息信号
        self.message_signal.emit(self.message)


# 主窗口类
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和布局
        self.setWindowTitle('Message Notification System')
        self.layout = QVBoxLayout()

        # 创建一个按钮，用于触发消息通知
        self.button = QPushButton('Show Notification')
        self.button.clicked.connect(self.show_notification)

        # 将按钮添加到布局
        self.layout.addWidget(self.button)

        # 设置主窗口的布局
        self.setLayout(self.layout)

    def show_notification(self):
        # 创建一个线程对象，传入消息
        notification_thread = NotificationThread('Hello, this is a notification!')

        # 连接线程的信号到槽函数，用于接收消息
        notification_thread.message_signal.connect(self.display_message)

        # 启动线程
        notification_thread.start()

    def display_message(self, message):
        # 使用QMessageBox显示消息
        QMessageBox.information(self, 'Notification', message)


# 程序的入口点
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
