# 代码生成时间: 2025-09-19 21:14:29
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt

"""
Memory Usage Analyzer using Python and PyQt framework.
This program displays the current memory usage of the system.
"""

class MemoryUsageAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('Memory Usage Analyzer')
        self.setGeometry(100, 100, 400, 200)

        # Create a central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Create a label to display memory usage
        self.memory_usage_label = QLabel('Memory Usage: 0%', self)
        self.memory_usage_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.memory_usage_label)

        # Start the memory usage analysis loop
        self.analyze_memory_usage()

    def analyze_memory_usage(self):
        """Analyze memory usage in an infinite loop."""
        try:
            while True:
                # Get the memory usage percentage
                memory_usage = psutil.virtual_memory().percent

                # Update the label with the memory usage
                self.memory_usage_label.setText(f'Memory Usage: {memory_usage}%')

                # Update every 1 second
                self. QTimer.singleShot(1000, self.analyze_memory_usage)
        except Exception as e:
            print(f'Error analyzing memory usage: {e}')

if __name__ == '__main__':
    app = QApplication([])
    window = MemoryUsageAnalyzer()
    window.show()
    app.exec_()