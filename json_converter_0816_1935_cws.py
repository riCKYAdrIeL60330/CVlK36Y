# 代码生成时间: 2025-08-16 19:35:45
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import Qt

"""JSON数据格式转换器

该程序使用Python和PyQt框架创建一个GUI应用，用于将JSON数据进行格式化和反格式化。
用户可以通过界面输入JSON数据，然后转换为格式化或反格式化的JSON字符串。
"""

class JsonConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('JSON Data Formatter')
        self.setGeometry(100, 100, 600, 400)

        # 创建布局
        layout = QVBoxLayout()

        # 创建文本编辑器
        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText('Paste your JSON data here...')
        layout.addWidget(self.textEdit)

        # 创建按钮
        self.formatButton = QPushButton('Format JSON', self)
        self.formatButton.clicked.connect(self.formatJson)
        layout.addWidget(self.formatButton)

        self.unformatButton = QPushButton('Unformat JSON', self)
        self.unformatButton.clicked.connect(self.unformatJson)
        layout.addWidget(self.unformatButton)

        # 添加布局到窗口
        self.setLayout(layout)

    def formatJson(self):
        """格式化JSON数据"""
        json_data = self.textEdit.toPlainText()
        try:
            formatted_json = json.dumps(json.loads(json_data), indent=4)
            self.textEdit.setText(formatted_json)
        except json.JSONDecodeError as e:
            self.textEdit.setText(f'Error: {e}')

    def unformatJson(self):
        """反格式化JSON数据"""
        json_data = self.textEdit.toPlainText()
        try:
            unformatted_json = json.dumps(json.loads(json_data))
            self.textEdit.setText(unformatted_json)
        except json.JSONDecodeError as e:
            self.textEdit.setText(f'Error: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = JsonConverter()
    converter.show()
    sys.exit(app.exec_())