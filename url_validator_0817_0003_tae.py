# 代码生成时间: 2025-08-17 00:03:10
import sys
import urllib.request
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtCore import QUrl

"""
URL链接有效性验证程序
"""

class URLValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('URL Validator')
        self.setGeometry(100, 100, 400, 300)

        # 创建布局
        layout = QVBoxLayout()

        # 创建文本框供用户输入URL
        self.urlInput = QTextEdit(self)
        self.urlInput.setPlaceholderText('Enter URL here')
        layout.addWidget(self.urlInput)

        # 创建按钮，点击时验证URL
        self.validateButton = QPushButton('Validate URL', self)
        self.validateButton.clicked.connect(self.validateUrl)
        layout.addWidget(self.validateButton)

        # 设置布局
        self.setLayout(layout)

    def validateUrl(self):
        # 获取用户输入的URL
        urlStr = self.urlInput.toPlainText().strip()

        # 检查URL是否为空
        if not urlStr:
            QMessageBox.warning(self, 'Warning', 'URL cannot be empty.')
            return

        try:
            # 使用QUrl解析URL
            url = QUrl(urlStr)
            # 使用urllib.request.urlopen验证URL是否可达
            response = urllib.request.urlopen(url.toString(QUrl.Encoded))
            # 如果URL有效，显示成功消息
            QMessageBox.information(self, 'Success', 'URL is valid and reachable.')
        except ValueError:
            # URL格式错误
            QMessageBox.warning(self, 'Error', 'Invalid URL format.')
        except urllib.error.URLError as e:
            # URL不可达
            QMessageBox.warning(self, 'Error', f'URL is not reachable. Error: {e.reason}')
        except Exception as e:
            # 其他错误
            QMessageBox.warning(self, 'Error', f'An error occurred: {e}')

def main():
    app = QApplication(sys.argv)
    ex = URLValidator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()