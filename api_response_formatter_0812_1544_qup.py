# 代码生成时间: 2025-08-12 15:44:16
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox


class ApiResponseFormatter(QWidget):
    """
    A PyQt5 GUI application to format API responses into JSON.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        self.layout = QVBoxLayout()
        self.response_text_edit = QTextEdit(self)
        self.response_text_edit.setPlaceholderText('Paste your API response here...')
        self.format_button = QPushButton('Format', self)
        self.format_button.clicked.connect(self.format_response)
        self.layout.addWidget(self.response_text_edit)
        self.layout.addWidget(self.format_button)
        self.setLayout(self.layout)
        self.setWindowTitle('API Response Formatter')
        self.show()

    def format_response(self):
        """Attempt to format the pasted API response as JSON."""
        try:
            response_data = self.response_text_edit.toPlainText()
            # Remove any trailing whitespace or newlines
            response_data = response_data.strip()
            # Try to parse the response as JSON and format it
            formatted_data = json.dumps(json.loads(response_data), indent=4)
            # Display the formatted JSON in a message box
            QMessageBox.information(self, 'Formatted JSON', formatted_data)
        except json.JSONDecodeError as e:
            # Handle JSON decoding errors
            QMessageBox.critical(self, 'Error', 'Invalid JSON response: ' + str(e))


if __name__ == '__main__':
    app = QApplication([])
    formatter = ApiResponseFormatter()
    app.exec_()