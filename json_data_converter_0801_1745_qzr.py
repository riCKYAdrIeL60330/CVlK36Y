# 代码生成时间: 2025-08-01 17:45:08
import json
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt

"""
A PyQt5 application that converts JSON data from one format to another.

This program allows users to enter or paste JSON data into a text area, then converts it to
the desired format by clicking a button. It handles errors gracefully and provides
user feedback.
"""

class JsonDataConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('JSON Data Converter')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.source_text_edit = QTextEdit(self)
        self.source_text_edit.setPlaceholderText('Paste your JSON data here')
        layout.addWidget(self.source_text_edit)

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert_json)
        layout.addWidget(self.convert_button)

        self.result_text_edit = QTextEdit(self)
        self.result_text_edit.setReadOnly(True)
        layout.addWidget(self.result_text_edit)

        self.setLayout(layout)

    def convert_json(self):
        try:
            # Get JSON data from the source text edit
            json_data = self.source_text_edit.toPlainText()
            # Load JSON data
            data = json.loads(json_data)
            # Convert the data back to JSON string with indentation for better readability
            formatted_json = json.dumps(data, indent=4)
            # Display the formatted JSON in the result text edit
            self.result_text_edit.setText(formatted_json)
        except json.JSONDecodeError as e:
            # Handle JSON decoding errors
            self.result_text_edit.setText(f'Error parsing JSON: {e}')

def main():
    app = QApplication(sys.argv)
    converter = JsonDataConverter()
    converter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()