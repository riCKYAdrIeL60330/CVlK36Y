# 代码生成时间: 2025-08-26 15:11:50
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import Qt

"""
API响应格式化工具

该工具允许用户输入原始API响应，然后格式化为JSON格式。
"""

class ApiResponseFormatter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题
        self.setWindowTitle('API响应格式化工具')

        # 创建布局
        layout = QVBoxLayout()

        # 创建标签提示输入原始响应
        self.raw_response_label = QLabel('请输入原始API响应：')
        layout.addWidget(self.raw_response_label)

        # 创建文本框用于输入原始响应
        self.raw_response_text = QTextEdit()
        self.raw_response_text.setPlaceholderText('在此输入原始API响应')
        layout.addWidget(self.raw_response_text)

        # 创建按钮用于格式化响应
        self.format_button = QPushButton('格式化')
        self.format_button.clicked.connect(self.format_response)
        layout.addWidget(self.format_button)

        # 创建标签显示格式化后的结果
        self.formatted_response_label = QLabel('格式化后的JSON：')
        layout.addWidget(self.formatted_response_label)

        # 创建文本框用于显示格式化后的结果
        self.formatted_response_text = QTextEdit()
        self.formatted_response_text.setReadOnly(True)
        layout.addWidget(self.formatted_response_text)

        # 设置布局
        self.setLayout(layout)

    def format_response(self):
        # 获取用户输入的原始响应
        raw_response = self.raw_response_text.toPlainText()

        try:
            # 尝试将原始响应转换为字典
            data = json.loads(raw_response)

            # 将字典转换为格式化的JSON字符串
            formatted_response = json.dumps(data, indent=4, ensure_ascii=False)

            # 显示格式化后的结果
            self.formatted_response_text.setText(formatted_response)

        except json.JSONDecodeError as e:
            # 捕获JSON解析错误
            self.formatted_response_text.setText(f'解析错误：{e}')

# 运行程序
if __name__ == '__main__':
    app = QApplication([])
    formatter = ApiResponseFormatter()
    formatter.show()
    app.exec_()