# 代码生成时间: 2025-09-17 08:24:03
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
# 扩展功能模块
import os

"""
A simple document converter using PyQt5.
This program allows the user to select a document and convert it to a different format.
Currently, it only supports converting from .txt to .md and vice versa.
"""

class DocumentConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Document Converter')
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Select a document to convert:', self)
        layout.addWidget(self.label)

        self.browse_button = QPushButton('Browse', self)
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        self.status_label = QLabel('Ready', self)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def browse_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Document', '', 'All Files (*);;Text Files (*.txt)', options=options)
        if file_name:
            self.convert_document(file_name)
        else:
            self.status_label.setText('No file selected.')
# NOTE: 重要实现细节

    def convert_document(self, file_name):
        try:
            file_extension = os.path.splitext(file_name)[1]
            if file_extension == '.txt':
                self.convert_to_md(file_name)
            elif file_extension == '.md':
# 扩展功能模块
                self.convert_to_txt(file_name)
            else:
                raise ValueError('Unsupported file format.')
        except Exception as e:
            self.status_label.setText(str(e))

    def convert_to_md(self, file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        md_file_name = file_name.replace('.txt', '.md')
        with open(md_file_name, 'w') as file:
            file.write(content)
        self.status_label.setText(f'Converted to {md_file_name}')

    def convert_to_txt(self, file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        txt_file_name = file_name.replace('.md', '.txt')
        with open(txt_file_name, 'w') as file:
# 扩展功能模块
            file.write(content)
        self.status_label.setText(f'Converted to {txt_file_name}')
# 优化算法效率

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = DocumentConverter()
    converter.show()
    sys.exit(app.exec_())