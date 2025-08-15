# 代码生成时间: 2025-08-15 14:30:26
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import QUrl
import requests

"""
URL Validator using Python and PyQt framework.
This program validates the given URL link for its validity.
"""

class URLValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout
        layout = QVBoxLayout()

        # Input field for URL
        self.urlInput = QLineEdit(self)
        layout.addWidget(self.urlInput)

        # Button to validate URL
        self.validateButton = QPushButton('Validate URL', self)
        self.validateButton.clicked.connect(self.validateURL)
        layout.addWidget(self.validateButton)

        # Label to show validation result
        self.resultLabel = QLabel('Enter URL and click Validate URL', self)
        layout.addWidget(self.resultLabel)

        # Set the layout
        self.setLayout(layout)
        self.setWindowTitle('URL Validator')
        self.resize(400, 200)

    def validateURL(self):
        # Get URL from input field
        url = self.urlInput.text()

        # Check if URL is empty
        if not url:
            self.resultLabel.setText('Please enter a URL')
            return

        # Validate using QUrl
        qurl = QUrl(url)
        if not qurl.isValid():
            self.resultLabel.setText('Invalid URL')
            return

        # Perform a HEAD request to check if the URL is reachable
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code == 200:
                self.resultLabel.setText('Valid and reachable URL')
            else:
                self.resultLabel.setText('URL is not reachable, status code: {}'.format(response.status_code))
        except requests.exceptions.RequestException as e:
            self.resultLabel.setText('Error: {}'.format(str(e)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = URLValidator()
    ex.show()
    sys.exit(app.exec_())