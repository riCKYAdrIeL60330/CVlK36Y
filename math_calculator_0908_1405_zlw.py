# 代码生成时间: 2025-09-08 14:05:47
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
from PyQt5.QtCore import Qt


# 定义数学计算类
class MathCalculator:
    def __init__(self):
        self.current_value = 0

    def add(self, num):
        """加法运算"""
        self.current_value += num
        return self.current_value

    def subtract(self, num):
        """减法运算"""
        self.current_value -= num
        return self.current_value

    def multiply(self, num):
        """乘法运算"""
        self.current_value *= num
        return self.current_value

    def divide(self, num):
        """除法运算"""
        if num == 0:
            raise ValueError('Cannot divide by zero')
        self.current_value /= num
        return self.current_value


# 定义主窗口类
class MathCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculator = MathCalculator()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Math Calculator')
        
        self.input_label = QLabel('Input:', self)
        self.input_field = QLineEdit(self)
        self.result_label = QLabel('Result: 0', self)

        self.add_button = QPushButton('Add', self)
        self.subtract_button = QPushButton('Subtract', self)
        self.multiply_button = QPushButton('Multiply', self)
        self.divide_button = QPushButton('Divide', self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.result_label)
        layout.addWidget(self.add_button)
        layout.addWidget(self.subtract_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.divide_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.add_button.clicked.connect(self.handle_add)
        self.subtract_button.clicked.connect(self.handle_subtract)
        self.multiply_button.clicked.connect(self.handle_multiply)
        self.divide_button.clicked.connect(self.handle_divide)

    def handle_add(self):
        try:
            num = float(self.input_field.text())
            result = self.calculator.add(num)
            self.result_label.setText(f'Result: {result}')
        except ValueError:
            self.result_label.setText('Invalid input')

    def handle_subtract(self):
        try:
            num = float(self.input_field.text())
            result = self.calculator.subtract(num)
            self.result_label.setText(f'Result: {result}')
        except ValueError:
            self.result_label.setText('Invalid input')

    def handle_multiply(self):
        try:
            num = float(self.input_field.text())
            result = self.calculator.multiply(num)
            self.result_label.setText(f'Result: {result}')
        except ValueError:
            self.result_label.setText('Invalid input')

    def handle_divide(self):
        try:
            num = float(self.input_field.text())
            result = self.calculator.divide(num)
            self.result_label.setText(f'Result: {result}')
        except ValueError:
            self.result_label.setText('Invalid input')
        except ZeroDivisionError:
            self.result_label.setText('Cannot divide by zero')


# 运行程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MathCalculatorApp()
    window.show()
    sys.exit(app.exec_())