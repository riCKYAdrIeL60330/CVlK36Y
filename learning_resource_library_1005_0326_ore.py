# 代码生成时间: 2025-10-05 03:26:21
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QMessageBox

"""
A PyQt application that serves as a learning resource library.
It allows users to add, view, and manage learning resources."""

class LearningResourceLibrary(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Learning Resource Library')

        layout = QVBoxLayout()

        # Text box for resource title
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText('Enter resource title')
        layout.addWidget(self.title_input)

        # Text box for resource content
        self.content_input = QTextEdit(self)
        layout.addWidget(self.content_input)

        # Add resource button
        self.add_button = QPushButton('Add Resource', self)
        self.add_button.clicked.connect(self.add_resource)
        layout.addWidget(self.add_button)

        # Set the layout
        self.setLayout(layout)

    def add_resource(self):
        """Add a new learning resource to the library."""
        title = self.title_input.text()
        content = self.content_input.toPlainText()

        if not title or not content:
            QMessageBox.warning(self, 'Error', 'Both title and content must be filled.')
            return

        # Here you would add logic to save the resource to a file or a database
        # For demonstration purposes, we'll just print the data
        print(f'Title: {title}
Content: {content}')

        QMessageBox.information(self, 'Success', 'Resource added successfully!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LearningResourceLibrary()
    ex.show()
    sys.exit(app.exec_())