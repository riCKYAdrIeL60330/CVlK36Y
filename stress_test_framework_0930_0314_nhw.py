# 代码生成时间: 2025-09-30 03:14:30
import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox, QLabel, QTextEdit
from PyQt5.QtCore import pyqtSignal, QObject
import requests
import time

# 定义一个信号，用于更新UI
class UpdateUISignal(QObject):
    updated = pyqtSignal(str)

class StressTestFramework(QWidget):
    '''
    压力测试框架主窗口
    '''
    def __init__(self):
        super().__init__()
        self.initUI()
        self.running = False
        self.update_signal = UpdateUISignal()
        self.update_signal.updated.connect(self.update_output)

    def initUI(self):
        '''
        初始化UI组件
        '''
        self.setWindowTitle('压力测试框架')
        layout = QVBoxLayout()

        self.url_input = QTextEdit()
        self.url_input.setPlaceholderText('请输入要测试的URL')
        layout.addWidget(self.url_input)

        self.thread_count = QSpinBox()
        self.thread_count.setRange(1, 1000)
        self.thread_count.setValue(10)
        layout.addWidget(self.thread_count)

        self.start_button = QPushButton('开始测试')
        self.start_button.clicked.connect(self.start_test)
        layout.addWidget(self.start_button)

        self.output_label = QLabel('输出将显示在这里')
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def start_test(self):
        '''
        开始压力测试
        '''
        if not self.running:
            self.running = True
            self.start_button.setEnabled(False)
            self.output_label.setText('正在测试...')
            thread_count = self.thread_count.value()
            urls = self.url_input.toPlainText().split('
')

            threads = []
            for _ in range(thread_count):
                t = threading.Thread(target=self.threaded_request, args=(urls,))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

            self.running = False
            self.start_button.setEnabled(True)
            self.output_label.setText('测试完成')
        else:
            self.output_label.setText('测试已在进行中')

    def threaded_request(self, urls):
        '''
        在单独线程中执行请求
        '''
        while self.running:
            for url in urls:
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        self.update_signal.updated.emit(f'{url} 成功返回')
                    else:
                        self.update_signal.updated.emit(f'{url} 返回状态码 {response.status_code}')
                except requests.exceptions.RequestException as e:
                    self.update_signal.updated.emit(f'{url} 错误: {e}')
                time.sleep(0.1)

    def update_output(self, message):
        '''
        更新UI输出
        '''
        self.output_label.setText(message)

# 检查是否是主线程
if __name__ == '__main__':
    app = QApplication(sys.argv)
    test_frame = StressTestFramework()
    test_frame.show()
    sys.exit(app.exec_())