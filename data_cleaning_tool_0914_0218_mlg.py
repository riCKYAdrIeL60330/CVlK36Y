# 代码生成时间: 2025-09-14 02:18:50
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLabel, QComboBox, QCheckBox, QLineEdit
from PyQt5.QtCore import Qt

"""
Data Cleaning and Preprocessing Tool using Python and PyQt framework.
This tool provides a simple GUI for users to load a dataset, perform basic data cleaning and preprocessing operations.
"""

class DataCleaningTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Cleaning and Preprocessing Tool')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout()

        # Load Data
        self.load_data_label = QLabel('Load Data:')
        layout.addWidget(self.load_data_label, 0, 0)

        self.load_data_button = QPushButton('Load Data')
        self.load_data_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_data_button, 0, 1)

        # Data Operations
        self.operations_label = QLabel('Data Operations:')
        layout.addWidget(self.operations_label, 1, 0)

        self.drop_duplicates_checkbox = QCheckBox('Drop Duplicates')
        layout.addWidget(self.drop_duplicates_checkbox, 2, 0)

        self.remove_missing_values_checkbox = QCheckBox('Remove Missing Values')
        layout.addWidget(self.remove_missing_values_checkbox, 2, 1)

        self.rename_columns_combobox = QComboBox()
        self.rename_columns_combobox.addItems(['No Change', 'Auto'])
        layout.addWidget(self.rename_columns_combobox, 3, 0)

        self.process_button = QPushButton('Process Data')
        self.process_button.clicked.connect(self.process_data)
        layout.addWidget(self.process_button, 4, 0)

        self.output_label = QLabel('')
        layout.addWidget(self.output_label, 5, 0, 1, 2)

        central_widget.setLayout(layout)

    def load_data(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                 "", "All Files (*);;CSV Files (*.csv)", options=options)
        if file_name:
            try:
                self.data = pd.read_csv(file_name)
                self.output_label.setText('Data loaded successfully.')
            except Exception as e:
                self.output_label.setText(f'Error loading data: {e}')
        else:
            self.output_label.setText('No file selected.')

    def process_data(self):
        try:
            if self.drop_duplicates_checkbox.isChecked():
                self.data.drop_duplicates(inplace=True)
            if self.remove_missing_values_checkbox.isChecked():
                self.data.dropna(inplace=True)
            if self.rename_columns_combobox.currentText() == 'Auto':
                self.data.columns = [f'Column_{i}' for i in range(len(self.data.columns))]
            self.output_label.setText('Data processed successfully.')
        except Exception as e:
            self.output_label.setText(f'Error processing data: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataCleaningTool()
    ex.show()
    sys.exit(app.exec_())