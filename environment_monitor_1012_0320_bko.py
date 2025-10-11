# 代码生成时间: 2025-10-12 03:20:44
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import QTimer

"""
环境监测系统 - 使用Python和PyQt框架创建一个简单的GUI程序，
用于模拟环境数据的监测和显示。
"""

class EnvironmentMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('环境监测系统')
        self.setGeometry(100, 100, 600, 400)

        # 创建中央窗口和布局
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 创建并添加显示环境数据的文本框
        self.data_display = QTextEdit()
        self.data_display.setReadOnly(True)
        layout.addWidget(self.data_display)

        # 创建并添加启动和停止监测的按钮
        self.start_button = QPushButton('启动监测')
        self.start_button.clicked.connect(self.start_monitoring)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('停止监测')
        self.stop_button.clicked.connect(self.stop_monitoring)
        layout.addWidget(self.stop_button)

        # 创建定时器对象
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)

    def start_monitoring(self):
        """
        启动环境数据监测
        """
        try:
            self.timer.start(1000)  # 每1000毫秒更新一次数据
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
        except Exception as e:
            print(f'启动监测时发生错误: {e}')

    def stop_monitoring(self):
        """
        停止环境数据监测
        """
        try:
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
        except Exception as e:
            print(f'停止监测时发生错误: {e}')

    def update_data(self):
        """
        模拟环境数据更新
        """
        # 这里可以添加真实的数据获取逻辑
        data = '温度: 25°C, 湿度: 50%'
        self.data_display.append(f'{data}')

    def closeEvent(self, event):
        """
        关闭窗口事件处理
        """
        self.timer.stop()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    monitor = EnvironmentMonitor()
    monitor.show()
    sys.exit(app.exec_())