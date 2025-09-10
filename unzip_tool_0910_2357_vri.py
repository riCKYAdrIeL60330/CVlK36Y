# 代码生成时间: 2025-09-10 23:57:03
import sys
import zipfile
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtCore import pyqtSignal, Qt


class UnzipTool(QWidget):
    # Signal for updating the progress bar
    progressUpdate = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Setup the user interface
        self.setWindowTitle('Unzip Tool')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Click the button to choose a zip file to extract.', self)
        layout.addWidget(self.label)

        self.button = QPushButton('Select Zip File', self)
        self.button.clicked.connect(self.selectZipFile)
        layout.addWidget(self.button)

        self.progressBar = QProgressBar(self)
        layout.addWidget(self.progressBar)

        self.setLayout(layout)

    def selectZipFile(self):
        # Open a file dialog to select a zip file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                 "Zip Files (*.zip)", options=options)
        if fileName:
            self.extractZipFile(fileName)

    def extractZipFile(self, zipFilePath):
        # Extract the zip file
        try:
            self.label.setText('Extracting file...')
            self.progressBar.setValue(0)
            with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
                zip_ref.extractall('extracted_files')
                self.label.setText('Extraction complete!')
            self.progressBar.setValue(100)
        except zipfile.BadZipFile:
            self.label.setText('Error: The file is not a zip file or it is corrupted.')
        except FileNotFoundError:
            self.label.setText('Error: The file does not exist.')
        except Exception as e:
            self.label.setText(f'An error occurred: {e}')

    def closeEvent(self, event):
        # Handle the close event
        self.label.setText('')
        event.accept()


app = QApplication(sys.argv)
ex = UnzipTool()
ex.show()
sys.exit(app.exec_())