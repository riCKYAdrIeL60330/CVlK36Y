# 代码生成时间: 2025-09-04 06:18:11
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QMessageBox, QValidator, QIntValidator

class FormValidator(QWidget):
    """
    A simple PyQt5 form with a validator for integer input.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the layout
        self.layout = QFormLayout()

        # Create the input field and set the validator
        self.inputField = QLineEdit(self)
        self.inputField.setValidator(QIntValidator())

        # Create a button to trigger validation
        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.validateInput)

        # Add widgets to the layout
        self.layout.addRow('Input:', self.inputField)
        self.layout.addRow('', self.submitButton)

        # Set the layout on the widget
        self.setLayout(self.layout)
        self.setWindowTitle('Form Validator')
        self.show()

    def validateInput(self):
        """
        Validate the input from the QLineEdit widget.
        If the input is not an integer, show an error message.
        """
        try:
            # Try to convert the input to an integer
            int(self.inputField.text())
        except ValueError:
            # Show an error message if conversion fails
            QMessageBox.warning(self, 'Validation Error', 'Please enter a valid integer.')
        else:
            # If no exception, input is valid
            QMessageBox.information(self, 'Validation Success', 'Input is a valid integer.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FormValidator()
    sys.exit(app.exec_())