# 代码生成时间: 2025-09-07 23:02:32
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox

"""
API响应格式化工具 - 将API响应的JSON字符串格式化为易读的JSON对象。
"""

class ApiResponseFormatter(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle('API响应格式化工具')

        # 创建布局
        self.layout = QVBoxLayout()

        # 创建文本编辑框，用于输入API响应
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        # 创建按钮，用于格式化JSON
        self.format_button = QPushButton('格式化JSON')
        self.format_button.clicked.connect(self.format_json)
        self.layout.addWidget(self.format_button)

        # 设置布局
        self.setLayout(self.layout)

    def format_json(self):
        # 读取文本编辑框中的文本
        json_string = self.text_edit.toPlainText()

        # 尝试解析JSON
        try:
            data = json.loads(json_string)
            # 格式化JSON并显示
            formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
            self.text_edit.setText(formatted_json)
        except json.JSONDecodeError as e:
            # 显示错误信息
            QMessageBox.critical(self, '错误', '无效的JSON格式：' + str(e))

# PyQt5 GUI应用程序入口点
def main():
    app = QApplication(sys.argv)
    formatter = ApiResponseFormatter()
    formatter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()