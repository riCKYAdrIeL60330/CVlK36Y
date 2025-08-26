# 代码生成时间: 2025-08-27 03:31:15
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QThread, pyqtSignal, QTime, QTimer
from PyQt5.QtGui import QFont
import datetime

# 定时任务类
class Task(QThread):
    finished = pyqtSignal()
    def __init__(self, interval, task):
        super().__init__()
        self.interval = interval  # 定时间隔，单位：秒
        self.task = task  # 要执行的任务
        self.is_running = False  # 任务是否正在运行
        self.timer = QTimer(self._run)
        self.timer.timeout.connect(self._run)

    def _run(self):
        # 执行任务
        self.task()
        self.finished.emit()

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.timer.start(self.interval)

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.timer.stop()

    def run(self):
        # QThread运行的函数
        self.start()

# 主窗口类
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('定时任务调度器')
        self.setGeometry(300, 300, 300, 200)

        # 布局
        layout = QVBoxLayout()

        # 显示当前时间的标签
        self.time_label = QLabel('当前时间：', self)
        self.time_label.setFont(QFont('微软雅黑', 12))

        # 开始按钮
        self.start_button = QPushButton('开始', self)
        self.start_button.clicked.connect(self.start_task)

        # 停止按钮
        self.stop_button = QPushButton('停止', self)
        self.stop_button.clicked.connect(self.stop_task)

        # 定时更新时间
        self.update_time()
        update_time = QTimer(self.update_time)
        update_time.start(1000)  # 每1000毫秒更新一次

        # 将控件添加到布局
        layout.addWidget(self.time_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def start_task(self):
        # 创建定时任务
        self.task = Task(5, self.sample_task)
        self.task.finished.connect(self.on_task_finished)
        self.task.start()

    def stop_task(self):
        # 停止定时任务
        if hasattr(self, 'task'):
            self.task.stop()

    def sample_task(self):
        # 示例任务：打印当前时间
        print('Task executed at:', datetime.datetime.now())

    def on_task_finished(self):
        # 任务执行完毕后的回调函数
        print('Task finished.')

    def update_time(self):
        # 更新时间显示
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time_label.setText('当前时间：' + current_time)

# 主函数
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()