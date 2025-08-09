# 代码生成时间: 2025-08-09 13:49:53
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QComboBox, QLabel, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt

"""
    Folder Structure Organizer
# 增强安全性
    This program allows users to select a directory, specify a new folder structure,
    and then organize the files in that directory according to the given structure.
# FIXME: 处理边界情况
"""

class FolderStructureOrganizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Folder Structure Organizer')
        self.setGeometry(100, 100, 400, 300)
# 扩展功能模块

        # Layout for the interface
        grid_layout = QGridLayout()

        # Directory selection
        self.dir_label = QLabel('Select Directory: ')
        self.dir_edit = QLineEdit()
# 改进用户体验
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.browse_directory)
        grid_layout.addWidget(self.dir_label, 0, 0)
        grid_layout.addWidget(self.dir_edit, 0, 1)
        grid_layout.addWidget(self.browse_button, 0, 2)

        # Folder structure specification
        self.structure_label = QLabel('Folder Structure: ')
# NOTE: 重要实现细节
        self.structure_edit = QLineEdit()
        grid_layout.addWidget(self.structure_label, 1, 0)
        grid_layout.addWidget(self.structure_edit, 1, 1)

        # Start organizing button
# 添加错误处理
        self.organize_button = QPushButton('Organize')
        self.organize_button.clicked.connect(self.organize_folder)
        grid_layout.addWidget(self.organize_button, 2, 1)

        # Layout setup
        self.setLayout(grid_layout)

    def browse_directory(self):
        # Open file dialog to select directory
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.dir_edit.setText(directory)

    def organize_folder(self):
        # Get the selected directory and folder structure
        directory = self.dir_edit.text()
        structure = self.structure_edit.text()

        # Check if directory is valid
        if not os.path.isdir(directory):
            print("Error: The specified directory is not valid.")
            return
# NOTE: 重要实现细节

        # Organize files according to the structure
        try:
# FIXME: 处理边界情况
            # Create folders based on the structure
            for folder in structure.split('/'):
                folder_path = os.path.join(directory, folder)
                os.makedirs(folder_path, exist_ok=True)

            # Move files into the new structure
            for file in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, file)):
                    shutil.move(os.path.join(directory, file), os.path.join(directory, structure, file))

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication([])
    organizer = FolderStructureOrganizer()
    organizer.show()
    app.exec_()