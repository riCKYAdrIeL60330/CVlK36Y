# 代码生成时间: 2025-09-09 19:04:28
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
import psutil
"""
进程管理器程序，使用PyQt5图形界面。
"""

class ProcessManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('Process Manager')
        self.setGeometry(100, 100, 600, 400)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 创建表格用于显示进程信息
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['PID', 'Process Name', 'CPU Usage', 'Memory Usage'])
        self.table.setRowCount(0)
        layout.addWidget(self.table)
        
        # 创建按钮用于刷新进程列表
        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.refreshProcesses)
        layout.addWidget(self.refresh_button)
        
        # 创建按钮用于结束选中的进程
        self.terminate_button = QPushButton('Terminate')
        self.terminate_button.clicked.connect(self.terminateProcess)
        layout.addWidget(self.terminate_button)
        
    def refreshProcesses(self):
        """刷新进程列表"""
        self.table.setRowCount(0)
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            pid, name, cpu, memory = proc.info
            self.table.insertRow(self.table.rowCount())
            self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(str(pid)))
            self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(name))
            self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(f'{cpu}%'))
            self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(f'{memory}%'))
    
    def terminateProcess(self):
        """结束选中的进程"""
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, 'Warning', 'Please select a process to terminate.')
            return
        pid = int(self.table.item(row, 0).text())
        try:
            os.kill(pid, 9)  # SIGKILL
            self.refreshProcesses()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to terminate process: {str(e)}')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    manager = ProcessManager()
    manager.show()
    sys.exit(app.exec_())