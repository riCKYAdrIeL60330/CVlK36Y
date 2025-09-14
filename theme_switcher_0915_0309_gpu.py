# 代码生成时间: 2025-09-15 03:09:15
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QColorDialog
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    """主窗口类，管理主题切换功能。"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化用户界面。"""
        self.setWindowTitle('Theme Switcher')
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.button = QPushButton('Change Theme', self)
        self.button.clicked.connect(self.change_theme)
        self.layout.addWidget(self.button)

        self.light_theme = True
        self.change_theme()

    def change_theme(self):
        """切换主题颜色。"""
        if self.light_theme:
            self.light_theme = False
            color = QColorDialog.getColor(
                QColor('#1c1c1c'), self, 'Select Color', QColorDialog.ShowAlphaChannel)
            if color.isValid():
                self.central_widget.setStyleSheet(f'background-color: {color.name()}')
        else:
            self.light_theme = True
            self.central_widget.setStyleSheet('background-color: white')

def main():
    """程序入口点。"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
