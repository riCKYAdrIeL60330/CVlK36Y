# 代码生成时间: 2025-08-21 17:07:02
import os
import shutil
import zipfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox

"""
Data Backup and Recovery application using Python and PyQt5 framework.
This application allows users to create backups of their data and restore them when needed.
"""

class DataBackupRecover(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Data Backup and Recovery'
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create backup button
        self.backup_button = QPushButton('Backup Data', self)
        self.backup_button.clicked.connect(self.backup_data)
        layout.addWidget(self.backup_button)

        # Create restore button
        self.restore_button = QPushButton('Restore Data', self)
        self.restore_button.clicked.connect(self.restore_data)
        layout.addWidget(self.restore_button)

    def backup_data(self):
        try:
            # Get the source directory path from the user
            source_dir = QFileDialog.getExistingDirectory(self, 'Select Source Directory')
            if not source_dir:
                return

            # Get the backup directory path from the user
            backup_dir = QFileDialog.getExistingDirectory(self, 'Select Backup Directory')
            if not backup_dir:
                return

            # Create a zip file for backup
            backup_file = os.path.join(backup_dir, 'backup.zip')
            with zipfile.ZipFile(backup_file, 'w') as zipf:
                for root, dirs, files in os.walk(source_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, source_dir))

            QMessageBox.information(self, 'Backup Completed', 'Data backup successful.')
        except Exception as e:
            QMessageBox.critical(self, 'Backup Error', f'An error occurred: {e}')

    def restore_data(self):
        try:
            # Get the backup file path from the user
            backup_file, _ = QFileDialog.getOpenFileName(self, 'Select Backup File', filter='Zip Files (*.zip)')
            if not backup_file:
                return

            # Get the restore directory path from the user
            restore_dir = QFileDialog.getExistingDirectory(self, 'Select Restore Directory')
            if not restore_dir:
                return

            # Extract the backup file
            with zipfile.ZipFile(backup_file, 'r') as zipf:
                zipf.extractall(restore_dir)

            QMessageBox.information(self, 'Restore Completed', 'Data restore successful.')
        except Exception as e:
            QMessageBox.critical(self, 'Restore Error', f'An error occurred: {e}')

if __name__ == '__main__':
    app = QApplication([])
    window = DataBackupRecover()
    window.show()
    app.exec_()