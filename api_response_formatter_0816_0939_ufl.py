# 代码生成时间: 2025-08-16 09:39:22
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox

"""
API响应格式化工具
使用Python和PyQt框架创建一个GUI应用程序，
用于格式化JSON API响应。
"""

class ApiResponseFormatter(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('API Response Formatter')
        self.resize(400, 300)

        # 创建布局
        layout = QVBoxLayout()

        # 创建文本编辑框，用于显示和编辑API响应
        self.text_edit = QTextEdit()
        self.text_edit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        # 创建按钮，用于格式化API响应
        self.format_button = QPushButton('Format Response')
        self.format_button.clicked.connect(self.format_response)

        # 将组件添加到布局
        layout.addWidget(self.text_edit)
        layout.addWidget(self.format_button)

        # 设置窗口的布局
        self.setLayout(layout)

    def format_response(self):
        # 从文本编辑框获取API响应文本
        api_response = self.text_edit.toPlainText()

        # 尝试解析和格式化JSON响应
        try:
            # 将文本转换为JSON对象
            json_response = json.loads(api_response)
            # 美化JSON格式
            formatted_response = json.dumps(json_response, indent=4)
            # 显示格式化后的响应
            self.text_edit.setText(formatted_response)
        except json.JSONDecodeError as e:
            # 显示错误消息
            QMessageBox.critical(self, 'Error', f'Invalid JSON: {e}')
        except Exception as e:
            # 显示一般错误消息
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')


def main():
    app = QApplication(sys.argv)
    formatter = ApiResponseFormatter()
    formatter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()