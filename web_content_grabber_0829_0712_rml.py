# 代码生成时间: 2025-08-29 07:12:44
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import requests
from PyQt5.QtCore import pyqtSignal


class WebContentGrabber(QMainWindow):
    """
    网页内容抓取工具的主窗口类。
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        初始化用户界面。
        """
        self.setWindowTitle('Web Content Grabber')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel('Enter URL:')
        self.layout.addWidget(self.label)

        self.url_input = QTextEdit()
        self.layout.addWidget(self.url_input)

        self.go_button = QPushButton('Go')
        self.go_button.clicked.connect(self.on_go_button_clicked)
        self.layout.addWidget(self.go_button)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

    def on_go_button_clicked(self):
        """
        处理'Go'按钮的点击事件。
        """
        url = self.url_input.toPlainText()
        if not url.startswith('http'):
            url = 'http://' + url
        self.web_view.setUrl(QUrl(url))
        self.web_view.loadFinished.connect(self.on_page_loaded)

    def on_page_loaded(self, result):
        "