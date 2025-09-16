# 代码生成时间: 2025-09-16 18:10:06
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import Qt

"""
A simple PyQt application that converts JSON data between different formats.
"""

class JsonConverter(QWidget):
    """
    A PyQt widget for converting JSON data.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface.
        """
        self.setWindowTitle('JSON Converter')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.json_input = QTextEdit()
        self.json_input.setPlaceholderText('Paste your JSON data here.')
        layout.addWidget(self.json_input)

        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_json)
        layout.addWidget(self.convert_button)

        self.json_output = QTextEdit()
        self.json_output.setPlaceholderText('Converted JSON data will appear here.')
        layout.addWidget(self.json_output)

        self.setLayout(layout)

    def convert_json(self):
        """
        Convert the JSON data from input to output.
        """
        try:
            json_data = self.json_input.toPlainText()
            if not json_data:
                raise ValueError('No JSON data provided.')

            # Attempt to parse the JSON data
            json_data = json.loads(json_data)

            # Convert the JSON data back to a string with indentation
            self.json_output.setText(json.dumps(json_data, indent=4))

        except json.JSONDecodeError as e:
            self.json_output.setText(f'Error: {e}')
        except Exception as e:
            self.json_output.setText(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = JsonConverter()
    converter.show()
    sys.exit(app.exec_())