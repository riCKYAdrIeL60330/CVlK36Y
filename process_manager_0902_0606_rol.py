# 代码生成时间: 2025-09-02 06:06:11
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QAbstractItemView
from PyQt5.QtCore import Qt
from subprocess import Popen, PIPE

"""
A simple process manager program using PyQt5 framework.
This program allows the user to view and terminate system processes.
"""

class ProcessManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle('Process Manager')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Process ID', 'Process Name'])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.layout.addWidget(self.table)

        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.refresh_processes)
        self.layout.addWidget(self.refresh_button)

        self.kill_button = QPushButton('Kill Process')
        self.kill_button.clicked.connect(self.kill_process)
        self.layout.addWidget(self.kill_button)

        self.central_widget.setLayout(self.layout)

        self.refresh_processes()

    def refresh_processes(self):
        """Refresh the list of system processes."""
        self.table.setRowCount(0)
        for proc in self.get_system_processes():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(str(proc.pid)))
            self.table.setItem(row_position, 1, QTableWidgetItem(proc.name))

    def get_system_processes(self):
        """Get a list of system processes."""
        processes = []
        try:
            output = Popen(['ps', '-ax'], stdout=PIPE).communicate()[0]
            for line in output.decode('utf-8').splitlines():
                parts = line.split()
                if len(parts) >= 2:
                    processes.append(Process(pid=int(parts[0]), name=parts[1]))
        except Exception as e:
            print(f"Error retrieving processes: {e}")
        return processes

    def kill_process(self):
        """Kill the selected process."""
        selected_items = self.table.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            pid = int(selected_item.text())
            try:
                os.system(f"kill {pid}")
                self.refresh_processes()
            except Exception as e:
                print(f"Error killing process {pid}: {e}")
        else:
            print("No process selected.")

class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProcessManager()
    window.show()
    sys.exit(app.exec_())