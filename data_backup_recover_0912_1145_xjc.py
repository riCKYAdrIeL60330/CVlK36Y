# 代码生成时间: 2025-09-12 11:45:42
 * It uses PyQt for the graphical user interface.
# TODO: 优化性能
 *
 * @author Your Name
 * @version 1.0
 * @date YYYY-MM-DD
 */
# NOTE: 重要实现细节

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt
import shutil
import zipfile


class BackupRestoreApp(QMainWindow):
    def __init__(self):
# 扩展功能模块
        super().__init__()
# 添加错误处理
        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowTitle('Data Backup and Restore')
        self.setGeometry(100, 100, 500, 300)

        # Create the layout and widgets
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Backup button
        self.backup_button = QPushButton('Backup', self)
        self.backup_button.clicked.connect(self.backup_data)
        self.layout.addWidget(self.backup_button)

        # Restore button
        self.restore_button = QPushButton('Restore', self)
        self.restore_button.clicked.connect(self.restore_data)
        self.layout.addWidget(self.restore_button)

    def backup_data(self):
        try:
            # Get the directory to backup
            directory = QFileDialog.getExistingDirectory(self, 'Select Directory to Backup')
            if not directory:
                return

            # Create a zip file for the backup
# 扩展功能模块
            zip_filename = QFileDialog.getSaveFileName(self, 'Save Backup As', '', 'Zip Files (*.zip)')[0]
            if not zip_filename:
                return
# 添加错误处理

            # Backup the directory
# 扩展功能模块
            shutil.make_archive(zip_filename, 'zip', directory)
            print('Backup completed successfully.')

        except Exception as e:
            print(f'An error occurred: {e}')

    def restore_data(self):
        try:
            # Get the zip file to restore from
            zip_filename, _ = QFileDialog.getOpenFileName(self, 'Open Backup File', '', 'Zip Files (*.zip)')
            if not zip_filename:
                return

            # Get the directory to restore to
# 增强安全性
            directory = QFileDialog.getExistingDirectory(self, 'Select Directory to Restore To')
            if not directory:
                return

            # Restore the zip file
            shutil.unpack_archive(zip_filename, directory, 'zip')
# 添加错误处理
            print('Restore completed successfully.')
# NOTE: 重要实现细节

        except Exception as e:
# NOTE: 重要实现细节
            print(f'An error occurred: {e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BackupRestoreApp()
    window.show()
    sys.exit(app.exec_())