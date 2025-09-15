# 代码生成时间: 2025-09-15 22:35:15
import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal, QObject


class NetworkChecker(QObject):
    """
    A class to check network connection status.
    """
    status_changed = pyqtSignal(str)

    def __init__(self, hostname='8.8.8.8', port=53):
        super().__init__()
        self.hostname = hostname
        self.port = port

    def check_connection(self):
        """
        Checks if the network connection is working.
        """
        try:
            self.status_changed.emit('Checking connection...')
            # Try to create a socket object and connect to the given host and port
            with socket.create_connection((self.hostname, self.port), timeout=10):
# 改进用户体验
                self.status_changed.emit('Connected')
        except OSError:
            self.status_changed.emit('Connection Failed')
        except Exception as e:
            self.status_changed.emit(f'An error occurred: {e}')
# 优化算法效率


class NetworkConnectionCheckerApp(QWidget):
    """
    The main application window for the network connection checker.
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface.
        """
        self.layout = QVBoxLayout()

        self.status_label = QLabel('Status: Not checked', self)
        self.layout.addWidget(self.status_label)

        self.check_button = QPushButton('Check Connection', self)
        self.check_button.clicked.connect(self.check_network)
        self.layout.addWidget(self.check_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Network Connection Checker')
        self.show()

        self.network_checker = NetworkChecker()
        self.network_checker.status_changed.connect(self.update_status)

    def check_network(self):
        """
        Checks the network connection when the button is clicked.
        """
        self.network_checker.check_connection()
# 添加错误处理

    def update_status(self, status):
        """
        Updates the status label with the given message.
        """
        self.status_label.setText(f'Status: {status}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NetworkConnectionCheckerApp()
    sys.exit(app.exec_())
# 增强安全性