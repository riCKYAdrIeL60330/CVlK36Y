# 代码生成时间: 2025-08-19 16:05:47
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PyQt5.QtCore import Qt

"""
A simple PyQt application to generate random test data.
This application will create a window with a button to generate
random test data and display it in a text area.
"""

class TestDataGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window title and size
        self.setWindowTitle('Test Data Generator')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a text area to display the generated test data
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        # Create a button to generate test data
        self.generate_button = QPushButton('Generate Test Data')
        self.generate_button.clicked.connect(self.generateTestData)
        layout.addWidget(self.generate_button)

    def generateTestData(self):
        try:
            # Clear the text area before generating new data
            self.text_area.clear()

            # Generate a random string of test data
            test_data = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(100))

            # Append the generated test data to the text area
            self.text_area.append(test_data)
        except Exception as e:
            # Handle any exceptions that occur during test data generation
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    app = QApplication([])
    window = TestDataGenerator()
    window.show()
    app.exec_()