# 代码生成时间: 2025-09-19 15:57:04
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                                     QPushButton, QFileDialog, QTextEdit, QLabel, QComboBox, QCheckBox)
from PyQt5.QtCore import Qt
import pandas as pd

class DataCleaningApp(QMainWindow):
    """
    A PyQt5 application for data cleaning and preprocessing.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main window settings
        self.setWindowTitle('Data Cleaning and Preprocessing Tool')
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Add widgets for file selection
        self.file_label = QLabel('Select a CSV file:')
        self.layout.addWidget(self.file_label)
        self.file_button = QPushButton('Browse')
        self.file_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.file_button)
        self.file_path_label = QLabel('No file selected')
        self.layout.addWidget(self.file_path_label)

        # Add widgets for data preview
        self.preview_label = QLabel('Data Preview:')
        self.layout.addWidget(self.preview_label)
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.layout.addWidget(self.preview_text)

        # Add widgets for data cleaning and preprocessing
        self.options_label = QLabel('Choose cleaning options:')
        self.layout.addWidget(self.options_label)
        self.drop_duplicates_checkbox = QCheckBox('Drop Duplicates')
        self.layout.addWidget(self.drop_duplicates_checkbox)
        self.drop_missing_checkbox = QCheckBox('Drop Missing Values')
        self.layout.addWidget(self.drop_missing_checkbox)

        # Add a button to start cleaning process
        self.start_button = QPushButton('Clean Data')
        self.start_button.clicked.connect(self.clean_data)
        self.layout.addWidget(self.start_button)

        # Add a widget to display cleaned data
        self.cleaned_label = QLabel('Cleaned Data Preview:')
        self.layout.addWidget(self.cleaned_label)
        self.cleaned_text = QTextEdit()
        self.cleaned_text.setReadOnly(True)
        self.layout.addWidget(self.cleaned_text)

    def open_file_dialog(self):
        """
        Open a file dialog to select a CSV file.
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                 "", "CSV files (*.csv)", options=options)
        if file_name:
            self.file_path_label.setText(file_name)
            self.file_path = file_name
            self.preview_data()

    def preview_data(self):
        """
        Preview the selected CSV file data.
        """
        try:
            data = pd.read_csv(self.file_path)
            self.preview_text.setText(data.head().to_string())
        except Exception as e:
            self.preview_text.setText(f'Error reading file: {e}')

    def clean_data(self):
        """
        Clean the data based on selected options.
        """
        try:
            data = pd.read_csv(self.file_path)
            if self.drop_duplicates_checkbox.isChecked():
                data = data.drop_duplicates()
            if self.drop_missing_checkbox.isChecked():
                data = data.dropna()
            self.cleaned_text.setText(data.head().to_string())
        except Exception as e:
            self.cleaned_text.setText(f'Error cleaning data: {e}')

# Create the application and run it
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataCleaningApp()
    ex.show()
    sys.exit(app.exec_())