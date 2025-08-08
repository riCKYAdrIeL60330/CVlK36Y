# 代码生成时间: 2025-08-08 17:09:54
import os
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import Qt

class DataBackupRestore(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Data Backup and Restore')
        self.setGeometry(100, 100, 400, 200)
        self.initUI()

    def initUI(self):
        # Create and set up the main widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Create a vertical layout and add buttons
        self.layout = QVBoxLayout()
        self.backup_button = QPushButton('Backup Data')
        self.restore_button = QPushButton('Restore Data')
        self.layout.addWidget(self.backup_button)
        self.layout.addWidget(self.restore_button)

        # Set the layout on the main widget
        self.main_widget.setLayout(self.layout)

        # Connect signal and slots
        self.backup_button.clicked.connect(self.backup_data)
        self.restore_button.clicked.connect(self.restore_data)

    def backup_data(self):
        """Back up data to a specified directory."""
        try:
            backup_source = input('Enter the source directory to backup: ')
            backup_destination = input('Enter the destination directory for backup: ')
            shutil.copytree(backup_source, backup_destination)
            QMessageBox.information(self, 'Backup Success', 'Data has been backed up successfully.')
        except FileNotFoundError:
            QMessageBox.warning(self, 'Error', 'Source directory does not exist.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')

    def restore_data(self):
        """Restore data from a specified directory."""
        try:
            restore_source = input('Enter the source directory to restore from: ')
            restore_destination = input('Enter the destination directory for restoration: ')
            shutil.copytree(restore_source, restore_destination)
            QMessageBox.information(self, 'Restore Success', 'Data has been restored successfully.')
        except FileNotFoundError:
            QMessageBox.warning(self, 'Error', 'Source directory does not exist.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')

if __name__ == '__main__':
    app = QApplication([])
    window = DataBackupRestore()
    window.show()
    app.exec_()