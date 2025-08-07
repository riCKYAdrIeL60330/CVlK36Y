# 代码生成时间: 2025-08-07 18:41:08
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot

"""
API响应格式化工具

该程序使用Python和PyQt框架创建一个GUI应用程序，
用于格式化API响应。用户可以粘贴JSON响应，并将其格式化为
更易读的格式。
"""

class ApiResponseFormatter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化用户界面"""
        self.setWindowTitle('API响应格式化工具')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.rawText = QTextEdit(self)
        self.rawText.setPlaceholderText('粘贴API响应...')
        self.layout.addWidget(self.rawText)

        self.formattedText = QTextEdit(self)
        self.formattedText.setReadOnly(True)
        self.layout.addWidget(self.formattedText)

        self.formatButton = QPushButton('格式化', self)
        self.formatButton.clicked.connect(self.formatResponse)
        self.layout.addWidget(self.formatButton)

        self.setLayout(self.layout)

    @pyqtSlot()
    def formatResponse(self):
        """格式化API响应"""
        raw_response = self.rawText.toPlainText()
        try:
            data = json.loads(raw_response)
            formatted_response = json.dumps(data, indent=4, ensure_ascii=False)
            self.formattedText.setText(formatted_response)
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, '错误', f'无效的JSON格式: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ApiResponseFormatter()
    ex.show()
    sys.exit(app.exec_())
