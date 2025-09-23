# 代码生成时间: 2025-09-23 14:44:07
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt
import datetime

"""
定时任务调度器程序，使用PyQt5框架实现GUI界面。
"""

class TaskScheduler(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('定时任务调度器')
        self.setGeometry(100, 100, 400, 300)

        # 创建中心窗口和布局
        self.centralWidget = QWidget()
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        # 创建显示当前时间的标签
        self.timeLabel = QLabel('当前时间：' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.layout.addWidget(self.timeLabel)

        # 创建定时任务按钮
        self.taskButton = QPushButton('执行定时任务')
        self.taskButton.clicked.connect(self.executeTask)
        self.layout.addWidget(self.taskButton)

        # 创建定时器，定时更新时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # 每1000毫秒（1秒）触发一次

    def executeTask(self):
        """
        执行定时任务的函数。
        """
        try:
            # 这里添加执行定时任务的代码
            print('执行定时任务...')
        except Exception as e:
            print(f'执行定时任务出错：{e}')

    def updateTime(self):
        """
        定时更新时间的函数。
        """
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.timeLabel.setText('当前时间：' + current_time)

def main():
    app = QApplication(sys.argv)
    scheduler = TaskScheduler()
    scheduler.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()