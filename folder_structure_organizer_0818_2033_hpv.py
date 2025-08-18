# 代码生成时间: 2025-08-18 20:33:25
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtCore import pyqtSlot

"""
Folder Structure Organizer

This program allows the user to select a directory and then
organizes its contents into subfolders based on file extensions.
"""

class FolderStructureOrganizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a vertical layout
        self.layout = QVBoxLayout()

        # Add a button to select a directory
        self.selectFolderButton = QPushButton('Select Folder')
        self.selectFolderButton.clicked.connect(self.selectFolder)
        self.layout.addWidget(self.selectFolderButton)

        # Add a button to organize folder
        self.organizeButton = QPushButton('Organize Folder')
        self.organizeButton.clicked.connect(self.organizeFolder)
        self.layout.addWidget(self.organizeButton)

        # Set the layout for the main window
        self.setLayout(self.layout)
        self.setWindowTitle('Folder Structure Organizer')
        self.show()

    @pyqtSlot()
    def selectFolder(self):
        # Open a file dialog to select a directory
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            self.directory = directory
            print(f'Selected directory: {self.directory}')

    @pyqtSlot()
    def organizeFolder(self):
        # Check if a directory is selected
        if not hasattr(self, 'directory'):
            print('Please select a directory first.')
            return

        # Create a dictionary to store file extensions and their corresponding files
        fileDict = {}
        for item in os.listdir(self.directory):
            file, ext = os.path.splitext(item)
            if ext:
                if ext not in fileDict:
                    fileDict[ext] = []
                fileDict[ext].append(item)

        # Create subfolders and move files
        for ext, files in fileDict.items():
            folderPath = os.path.join(self.directory, ext[1:])  # Remove the dot from the extension
            os.makedirs(folderPath, exist_ok=True)
            for file in files:
                try:
                    shutil.move(os.path.join(self.directory, file), folderPath)
                except Exception as e:
                    print(f'Error moving file {file}: {e}')

        print('Folder organization complete.')

if __name__ == '__main__':
    app = QApplication([])
    organizer = FolderStructureOrganizer()
    app.exec_()