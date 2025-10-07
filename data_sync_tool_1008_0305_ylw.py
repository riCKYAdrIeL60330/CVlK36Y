# 代码生成时间: 2025-10-08 03:05:27
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

"""
Data Synchronization Tool using Python and PyQt framework.
This tool allows users to select two directories to sync data between them.
"""

class DataSyncTool(QWidget):
# 扩展功能模块
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window title and size
# 添加错误处理
        self.setWindowTitle('Data Synchronization Tool')
        self.resize(400, 200)

        # Create layout
        layout = QVBoxLayout()

        # Create buttons
# 优化算法效率
        self.source_button = QPushButton('Select Source Directory')
        self.source_button.clicked.connect(self.select_source_dir)
        layout.addWidget(self.source_button)

        self.target_button = QPushButton('Select Target Directory')
# TODO: 优化性能
        self.target_button.clicked.connect(self.select_target_dir)
# 改进用户体验
        layout.addWidget(self.target_button)
# NOTE: 重要实现细节

        self.sync_button = QPushButton('Sync Data')
        self.sync_button.clicked.connect(self.sync_data)
        self.sync_button.setEnabled(False)
# 添加错误处理
        layout.addWidget(self.sync_button)

        # Set layout
        self.setLayout(layout)

    def select_source_dir(self):
        # Open file dialog to select source directory
        directory = QFileDialog.getExistingDirectory(self, 'Select Source Directory')
        if directory:
            self.source_button.setText(directory)
            self.source_dir = directory
            self.sync_button.setEnabled(True)

    def select_target_dir(self):
        # Open file dialog to select target directory
        directory = QFileDialog.getExistingDirectory(self, 'Select Target Directory')
# 添加错误处理
        if directory:
# 改进用户体验
            self.target_button.setText(directory)
# 扩展功能模块
            self.target_dir = directory
            self.sync_button.setEnabled(True)

    def sync_data(self):
        # Check if both source and target directories are selected
# 增强安全性
        if not self.source_dir or not self.target_dir:
            QMessageBox.warning(self, 'Error', 'Please select both source and target directories.')
            return

        try:
            # Sync data from source to target directory
            self.sync(self.source_dir, self.target_dir)
# 改进用户体验
            QMessageBox.information(self, 'Success', 'Data synchronization completed successfully.')
        except Exception as e:
            # Handle any errors that occur during synchronization
            QMessageBox.warning(self, 'Error', f'An error occurred: {str(e)}')

    def sync(self, source_dir, target_dir):
# FIXME: 处理边界情况
        # Synchronize data from source directory to target directory
        for root, dirs, files in os.walk(source_dir):
            relative_path = os.path.relpath(root, source_dir)
            target_path = os.path.join(target_dir, relative_path)
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            for file in files:
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(target_path, file)
                if not os.path.exists(target_file_path):
                    # Copy file from source to target directory
                    self.copy_file(source_file_path, target_file_path)
                else:
                    # Update file if it's modified in source directory
                    if os.path.getmtime(source_file_path) > os.path.getmtime(target_file_path):
                        self.copy_file(source_file_path, target_file_path)

    def copy_file(self, source_file_path, target_file_path):
        # Copy file from source to target
        try:
            with open(source_file_path, 'rb') as source_file:
                with open(target_file_path, 'wb') as target_file:
                    target_file.write(source_file.read())
        except Exception as e:
# 优化算法效率
            # Handle any errors that occur during file copy
            print(f'Error copying file {source_file_path} to {target_file_path}: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
# 优化算法效率
    ex = DataSyncTool()
    ex.show()
    sys.exit(app.exec_())