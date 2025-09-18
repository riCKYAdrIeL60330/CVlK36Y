# 代码生成时间: 2025-09-19 06:45:27
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, 
                                QLineEdit, QLabel)

"""
A simple math calculator using PyQt5 framework.
This calculator provides basic arithmetic operations.
"""

class MathCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layouts
        self.layout = QVBoxLayout()

        # Input fields
        self.num1 = QLineEdit(self)
        self.num2 = QLineEdit(self)

        # Labels
        self.label = QLabel('Enter the numbers:', self)
        self.resultLabel = QLabel('Result:', self)

        # Buttons
        self.addButton = QPushButton('+', self)
        self.subButton = QPushButton('-', self)
        self.mulButton = QPushButton('*', self)
        self.divButton = QPushButton('/', self)

        # Layout configuration
        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.num1)
        inputLayout.addWidget(self.num2)
        self.layout.addLayout(inputLayout)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.resultLabel)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.subButton)
        buttonLayout.addWidget(self.mulButton)
        buttonLayout.addWidget(self.divButton)
        self.layout.addLayout(buttonLayout)

        self.setLayout(self.layout)
        self.setWindowTitle('Math Calculator')
        self.setGeometry(300, 300, 250, 150)
        self.show()

        # Connect signals to slots
        self.addButton.clicked.connect(self.add)
        self.subButton.clicked.connect(self.subtract)
        self.mulButton.clicked.connect(self.multiply)
        self.divButton.clicked.connect(self.divide)

    def add(self):
        try:
            num1 = float(self.num1.text())
            num2 = float(self.num2.text())
            result = num1 + num2
            self.resultLabel.setText(f'Result: {result}')
        except ValueError:
            self.resultLabel.setText('Invalid input')
        except Exception as e:
            self.resultLabel.setText(f'Error: {str(e)}')

    def subtract(self):
        try:
            num1 = float(self.num1.text())
            num2 = float(self.num2.text())
            result = num1 - num2
            self.resultLabel.setText(f'Result: {result}')
        except ValueError:
            self.resultLabel.setText('Invalid input')
        except Exception as e:
            self.resultLabel.setText(f'Error: {str(e)}')

    def multiply(self):
        try:
            num1 = float(self.num1.text())
            num2 = float(self.num2.text())
            result = num1 * num2
            self.resultLabel.setText(f'Result: {result}')
        except ValueError:
            self.resultLabel.setText('Invalid input')
        except Exception as e:
            self.resultLabel.setText(f'Error: {str(e)}')

    def divide(self):
        try:
            num1 = float(self.num1.text())
            num2 = float(self.num2.text())
            if num2 == 0:
                self.resultLabel.setText('Error: Division by zero')
                return
            result = num1 / num2
            self.resultLabel.setText(f'Result: {result}')
        except ValueError:
            self.resultLabel.setText('Invalid input')
        except Exception as e:
            self.resultLabel.setText(f'Error: {str(e)}')

def main():
    app = QApplication(sys.argv)
    calc = MathCalculator()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()