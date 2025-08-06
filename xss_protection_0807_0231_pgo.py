# 代码生成时间: 2025-08-07 02:31:07
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import re

def escape_html(unsafe):
    """Escape HTML special characters."""
    return (
        unsafe
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("", "&quot;")
        .replace("/", "&#x2F;")
    )

class XssProtectionApp(QWidget):
    """Main application window."""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Set up the user interface."""
        self.setWindowTitle('XSS Attack Protection')
        self.setGeometry(100, 100, 600, 200)

        # Input area
        self.input_label = QLabel("Enter text to sanitize: ", self)
        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText("Type here...")

        # Button to sanitize input
        self.sanitize_button = QPushButton("Sanitize", self)
        self.sanitize_button.clicked.connect(self.sanitize_input)

        # Output area
        self.output_label = QLabel("Sanitized output: ", self)
        self.output_text = QLabel(self)
        self.output_text.setWordWrap(True)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.sanitize_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        self.setLayout(layout)

    def sanitize_input(self):
        """Sanitize the input text to prevent XSS attacks."""
        try:
            input_text = self.input_text.text()
            sanitized_text = escape_html(input_text)
            self.output_text.setText(sanitized_text)
        except Exception as e:
            print(f"Error sanitizing input: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = XssProtectionApp()
    ex.show()
    sys.exit(app.exec_())