# 代码生成时间: 2025-09-02 17:36:39
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal


# JSON数据格式转换器
class JsonConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('JSON Converter')
        self.setGeometry(100, 100, 600, 400)

        # 创建布局
        layout = QVBoxLayout()

        # 创建输入和输出文本框
        self.inputTextEdit = QPlainTextEdit(self)
        self.outputTextEdit = QPlainTextEdit(self)
        self.outputTextEdit.setReadOnly(True)

        # 创建按钮
        self.convertButton = QPushButton('Convert', self)
        self.convertButton.clicked.connect(self.convertJson)

        # 将控件添加到布局
        layout.addWidget(self.inputTextEdit)
        layout.addWidget(self.outputTextEdit)
        layout.addWidget(self.convertButton)

        # 设置布局
        self.setLayout(layout)

    def convertJson(self):
        try:
            # 读取输入文本框中的内容
            input_text = self.inputTextEdit.toPlainText()
            # 尝试将文本转换为JSON对象
            json_obj = json.loads(input_text)
            # 将JSON对象转换回字符串
            output_text = json.dumps(json_obj, indent=4)
            # 将转换后的结果显示在输出文本框中
            self.outputTextEdit.setPlainText(output_text)
        except json.JSONDecodeError as e:
            # 显示错误信息
            QMessageBox.critical(self, 'Error', f'Invalid JSON: {e.msg}')


# 主函数
def main():
    app = QApplication(sys.argv)
    converter = JsonConverter()
    converter.show()
    sys.exit(app.exec_())


# 程序入口
if __name__ == '__main__':
    main()