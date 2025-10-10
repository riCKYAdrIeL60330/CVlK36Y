# 代码生成时间: 2025-10-10 21:49:24
import sys
import psutil
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QProgressBar, QPushButton


class CpuUsageAnalyzer(QMainWindow):
    """
    A PyQt5 application that displays CPU usage as a percentage.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowTitle('CPU Usage Analyzer')
        self.setGeometry(100, 100, 400, 200)

        # Create the layout and central widget
        layout = QVBoxLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        # Create the CPU usage label
        self.cpu_usage_label = QLabel('CPU Usage: 0%')
        layout.addWidget(self.cpu_usage_label)

        # Create the progress bar
        self.cpu_usage_bar = QProgressBar()
        self.cpu_usage_bar.setMaximum(100)
        layout.addWidget(self.cpu_usage_bar)

        # Create the start/stop button
        self.start_stop_button = QPushButton('Start')
        self.start_stop_button.clicked.connect(self.toggle_cpu_usage)
        layout.addWidget(self.start_stop_button)

        # Start the CPU usage thread
        self.cpu_usage_thread = CpuUsageThread()
        self.cpu_usage_thread.update_cpu_usage.connect(self.update_ui)

    def update_ui(self, cpu_usage):
        """
        Update the UI with the new CPU usage percentage.
        """
        self.cpu_usage_label.setText(f'CPU Usage: {cpu_usage}%')
        self.cpu_usage_bar.setValue(cpu_usage)

    def toggle_cpu_usage(self):
        "