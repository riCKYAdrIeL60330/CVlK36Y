# 代码生成时间: 2025-08-04 19:34:59
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

"""
Math Calculator - A simple PyQt5 application to perform basic mathematical operations.
"""

class MathCalculator(QWidget):
    """
    A GUI application for performing basic mathematical operations using PyQt5.
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle('Math Calculator')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.expression_input = QLineEdit(self)
        self.result_label = QLabel('Result: ', self)

        layout.addWidget(self.expression_input)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.show()

        # Connect the button click to the evaluate_expression method
        self.expression_input.returnPressed.connect(self.evaluate_expression)

    def evaluate_expression(self):
        """Evaluate the mathematical expression entered by the user."""
        expression = self.expression_input.text()
        try:
            # Use eval() to calculate the expression
            # Note: eval() can be dangerous if used with untrusted input.
            # Here it is used for simplicity and because the input is controlled.
            result = eval(expression)
            self.result_label.setText(f'Result: {result}')
        except (SyntaxError, NameError, Exception):
            # Handle any errors that occur during evaluation
            self.result_label.setText('Error in expression')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = MathCalculator()
    sys.exit(app.exec_())