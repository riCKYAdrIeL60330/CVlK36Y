# 代码生成时间: 2025-09-10 00:15:52
import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel

"""
哈希值计算工具，使用Python和PyQt框架创建。
"""

class HashCalculator(QWidget):
    """
    哈希值计算工具的主窗口类。
    """
    def __init__(self):
        super().__init__()
        self.title = '哈希值计算工具'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        """
        初始化用户界面。
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel('输入文本:', self)
        layout.addWidget(self.label)

        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)

        self.hashLabel = QLabel('哈希值:', self)
        layout.addWidget(self.hashLabel)

        self.result = QTextEdit(self)
        self.result.setReadOnly(True)
        layout.addWidget(self.result)

        self.button = QPushButton('计算哈希值', self)
        self.button.clicked.connect(self.calculateHash)
        layout.addWidget(self.button)

    def calculateHash(self):
        """
        计算输入文本的哈希值并显示结果。
        """
        text = self.textEdit.toPlainText()
        try:
            hash_value = hashlib.sha256(text.encode()).hexdigest()
            self.result.setText(hash_value)
        except Exception as e:
            self.result.setText(f'计算哈希值时出错: {e}')

def main():
    """
    程序的主入口点。
    """
    app = QApplication(sys.argv)
    ex = HashCalculator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()