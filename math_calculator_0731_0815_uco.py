# 代码生成时间: 2025-07-31 08:15:14
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

"""
数学计算工具集
"""

class MathCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('数学计算工具集')

        # 创建布局
        layout = QVBoxLayout()

        # 创建输入框
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)

        # 创建标签
        self.label = QLabel('Result:', self)

        # 创建计算按钮
        self.add_button = QPushButton('Add', self)
        self.add_button.clicked.connect(self.add)

        # 将控件添加到布局中
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.add_button)
        layout.addWidget(self.label)

        # 设置布局
        self.setLayout(layout)

    def add(self):
        # 获取输入值
        input1 = self.input1.text()
        input2 = self.input2.text()

        try:
            # 将输入值转换为浮点数
            num1 = float(input1)
            num2 = float(input2)

            # 计算和
            result = num1 + num2

            # 显示结果
            self.label.setText(f'Result: {result}')
        except ValueError:
            # 错误处理
            self.label.setText('Error: Invalid input')

"""
运行程序
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = MathCalculator()
    calculator.show()
    sys.exit(app.exec_())