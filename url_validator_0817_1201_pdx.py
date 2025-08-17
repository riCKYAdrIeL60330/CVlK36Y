# 代码生成时间: 2025-08-17 12:01:49
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from urllib.parse import urlparse

"""
URL Validator application using PyQt5 framework.
This application allows the user to input a URL and checks its validity.
"""

class URLValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create layout
        layout = QVBoxLayout()

        # URL input field
        self.urlInput = QLineEdit(self)
        self.urlInput.setPlaceholderText('Enter URL here')
        layout.addWidget(self.urlInput)

        # Check button
        self.checkButton = QPushButton('Check URL', self)
        self.checkButton.clicked.connect(self.checkURL)
        layout.addWidget(self.checkButton)

        # Result label
        self.resultLabel = QLabel(self)
        layout.addWidget(self.resultLabel)

        # Set layout to widget
        self.setLayout(layout)
        self.setWindowTitle('URL Validator')
        self.setGeometry(300, 300, 300, 150)

    def checkURL(self):
        url = self.urlInput.text()
        try:
            # Parse the URL and check its scheme
            result = urlparse(url)
            if not result.scheme or not result.netloc:
                raise ValueError('Invalid URL format')

            # Try to send a GET request to the URL
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code == 200:
                self.resultLabel.setText('URL is valid.')
                self.resultLabel.setStyleSheet('color: green;')
            else:
                self.resultLabel.setText(f'URL is invalid. Status code: {response.status_code}')
                self.resultLabel.setStyleSheet('color: red;')
        except requests.RequestException as e:
            QMessageBox.critical(self, 'Error', f'Failed to check URL: {e}')
            self.resultLabel.setText('Failed to check URL.')
            self.resultLabel.setStyleSheet('color: red;')
        except ValueError as e:
            QMessageBox.critical(self, 'Error', f'Invalid URL: {e}')
            self.resultLabel.setText('Invalid URL.')
            self.resultLabel.setStyleSheet('color: red;')

# Main function to run the application
def main():
    app = QApplication(sys.argv)
    ex = URLValidator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()