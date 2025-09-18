# 代码生成时间: 2025-09-18 21:38:01
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
import random
"""
随机数生成器程序，使用PyQt5框架构建图形用户界面。
用户可以通过输入最小值和最大值来生成一个随机数。
"""

class RandomNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('Random Number Generator')
        
        # 创建布局
        layout = QVBoxLayout()
        
        # 创建输入框，用于输入最小值
        self.minValueInput = QLineEdit()
        self.minValueInput.setPlaceholderText('Enter Min Value')
        layout.addWidget(self.minValueInput)
        
        # 创建输入框，用于输入最大值
        self.maxValueInput = QLineEdit()
        self.maxValueInput.setPlaceholderText('Enter Max Value')
        layout.addWidget(self.maxValueInput)
        
        # 创建按钮，点击生成随机数
        self.generateButton = QPushButton('Generate')
        self.generateButton.clicked.connect(self.generate_random)
        layout.addWidget(self.generateButton)
        
        # 创建标签，用于显示生成的随机数
        self.resultLabel = QLabel('Result: ')
        layout.addWidget(self.resultLabel)
        
        # 设置布局
        self.setLayout(layout)
        
        # 设置窗口大小
        self.resize(300, 120)
        
    def generate_random(self):
        try:
            # 获取用户输入的最小值和最大值
            min_value = int(self.minValueInput.text())
            max_value = int(self.maxValueInput.text())
            
            # 检查输入值是否有效
            if min_value >= max_value:
                raise ValueError('Min value must be less than max value.')
            
            # 生成随机数
            result = random.randint(min_value, max_value)
            
            # 显示结果
            self.resultLabel.setText(f'Result: {result}')
        except ValueError as e:
            # 错误处理
            self.resultLabel.setText(f'Error: {e}')
        except Exception as e:
            # 其他异常处理
            self.resultLabel.setText(f'An unexpected error occurred: {e}')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    rng = RandomNumberGenerator()
    rng.show()
    sys.exit(app.exec_())