# 代码生成时间: 2025-10-03 03:53:21
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox

"""
A simple PyQt application to handle return and exchange of products.
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the title and size of the window
        self.setWindowTitle('Return and Exchange Handling System')
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a button to initiate return/exchange process
        process_button = QPushButton('Process Return/Exchange')
        process_button.clicked.connect(self.handle_process)
        layout.addWidget(process_button)

    def handle_process(self):
        # Placeholder for the actual return/exchange logic
        try:
            # For demonstration, we'll just show a message box
            QMessageBox.information(self, 'Return/Exchange Process',
                              'Please provide product details and reason for return/exchange.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')

    def closeEvent(self, event):
        # Handle closing of the application
        reply = QMessageBox.question(self, 'Message',
                                  'Are you sure to quit?',
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())