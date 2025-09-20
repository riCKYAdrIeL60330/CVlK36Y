# 代码生成时间: 2025-09-21 02:03:36
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class ThemeSwitcher(QMainWindow):
    """
    A PyQt5 application that allows users to switch between different themes.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Theme Switcher')
        self.setGeometry(100, 100, 400, 200)
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.theme_combobox = QComboBox()
        self.theme_combobox.addItem('Light Theme', 'light')
        self.theme_combobox.addItem('Dark Theme', 'dark')
        self.theme_combobox.currentIndexChanged.connect(self.change_theme)

        self.change_theme_button = QPushButton('Change Theme')
        self.change_theme_button.clicked.connect(self.change_theme)

        self.layout.addWidget(self.theme_combobox)
        self.layout.addWidget(self.change_theme_button)

    def change_theme(self):
        """
        Change the theme based on the selected index from the combobox.
        """
        theme = self.theme_combobox.currentData()
        if theme == 'dark':
            self.change_to_dark_theme()
        elif theme == 'light':
            self.change_to_light_theme()
        else:
            print(f"Unknown theme: {theme}")

    def change_to_light_theme(self):
        """
        Apply the light theme to the application.
        """
        self.setStyleSheet('QWidget { background-color: #FFFFFF; }')
        self.central_widget.setStyleSheet('QWidget { background-color: #E0E0E0; }')

    def change_to_dark_theme(self):
        """
        Apply the dark theme to the application.
        """
        self.setStyleSheet('QWidget { background-color: #333333; }')
        self.central_widget.setStyleSheet('QWidget { background-color: #505050; }')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ThemeSwitcher()
    window.show()
    sys.exit(app.exec_())