# 代码生成时间: 2025-08-18 12:08:52
import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import pyqtSlot

"""
Network Connection Checker using PyQt
This script creates a simple GUI application that checks the network connection status.
"""

class NetworkChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface"""
        self.layout = QVBoxLayout()
        self.check_button = QPushButton('Check Network Connection')
        self.status_label = QLabel('Network status: Unknown')

        self.layout.addWidget(self.check_button)
        self.layout.addWidget(self.status_label)

        self.check_button.clicked.connect(self.check_connection)
        self.setLayout(self.layout)

    def check_connection(self):
        """Check the network connection status"""
        try:
            socket.create_connection(('8.8.8.8', 53)).close()
            self.status_label.setText('Network status: Connected')
        except OSError:
            self.status_label.setText('Network status: Disconnected')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An unexpected error occurred: {str(e)}')

    @pyqtSlot()
    def on_close(self):
        "