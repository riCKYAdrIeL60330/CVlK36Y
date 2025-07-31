# 代码生成时间: 2025-08-01 03:06:13
import sys
import zipfile
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt

class FileUncompressor(QWidget):
    """
    A PyQt5 application for unzipping files.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface.
        """
        self.setWindowTitle('File Uncompressor')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel('Select a zip file to uncompress:', self)
        self.layout.addWidget(self.label)

        self.button = QPushButton('Browse', self)
        self.button.clicked.connect(self.get_file)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def get_file(self):
        """
        Open a file dialog to select a zip file.
        """
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Zip Files (*.zip)', options=options)
        if fileName:
            try:
                self.unzip_file(fileName)
            except zipfile.BadZipFile:
                QMessageBox.critical(self, 'Error', 'Selected file is not a valid zip file.')
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))
        else:
            QMessageBox.warning(self, 'Warning', 'No file selected.')

    def unzip_file(self, file_path):
        """
        Unzip the selected file to the current working directory.
        """
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
            QMessageBox.information(self, 'Success', 'File uncompressed successfully.')

def main():
    """
    Run the PyQt5 application.
    """
    app = QApplication(sys.argv)
    window = FileUncompressor()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()