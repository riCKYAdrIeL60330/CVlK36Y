# 代码生成时间: 2025-09-05 18:12:52
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel
from PyQt5.QtCore import QProcess


class ProcessManager(QWidget):
    """进程管理器界面"""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化用户界面"""
        self.setWindowTitle('Process Manager')
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()

        self.label = QLabel('Running Processes:', self)
        layout.addWidget(self.label)

        self.process_list = QListWidget(self)
        layout.addWidget(self.process_list)

        self.start_button = QPushButton('Start New Process', self)
        self.start_button.clicked.connect(self.start_process)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Stop Selected Process', self)
        self.stop_button.clicked.connect(self.stop_process)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def start_process(self):
        """启动新进程"""
        process = QProcess(self)
        process.start('python', ['--version'])  # 示例：启动Python并显示版本
        self.process_list.addItem(process.program())

    def stop_process(self):
        """停止选中的进程"""
        selected_item = self.process_list.currentItem()
        if selected_item:
            process_name = selected_item.text()
            for proc in subprocess.process_iter():
                if process_name in proc.cmdline():
                    try:
                        proc.terminate()
                        proc.wait()
                        self.process_list.takeItem(self.process_list.row(selected_item))
                    except:
                        print(f'Error terminating process: {process_name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ProcessManager()
    main_window.show()
    sys.exit(app.exec_())