# 代码生成时间: 2025-08-03 01:07:00
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt
from cryptography.fernet import Fernet, InvalidToken

"""
密码加密解密工具
"""

class PasswordTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和布局
        self.setWindowTitle('Password Encryption/Decryption Tool')
        self.layout = QVBoxLayout()

        # 输入框
        self.inputText = QLineEdit(self)
        self.inputText.setPlaceholderText('Enter text to encrypt or decrypt')
        self.layout.addWidget(self.inputText)

        # 输出框
        self.outputText = QTextEdit(self)
        self.layout.addWidget(self.outputText)

        # 加密按钮
        self.encryptButton = QPushButton('Encrypt', self)
        self.encryptButton.clicked.connect(self.encrypt)
        self.layout.addWidget(self.encryptButton)

        # 解密按钮
        self.decryptButton = QPushButton('Decrypt', self)
        self.decryptButton.clicked.connect(self.decrypt)
        self.layout.addWidget(self.decryptButton)

        # 布局管理
        self.setLayout(self.layout)

        # 生成密钥
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self):
        # 加密输入文本
        text = self.inputText.text()
        try:
            encrypted_text = self.cipher.encrypt(text.encode())
            self.outputText.setText(encrypted_text.decode())
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Encryption failed: {e}')

    def decrypt(self):
        # 解密输入文本
        text = self.inputText.text()
        try:
            decrypted_text = self.cipher.decrypt(text.encode())
            self.outputText.setText(decrypted_text.decode())
        except InvalidToken:
            QMessageBox.critical(self, 'Error', 'Invalid token, please make sure you are using the correct encrypted text.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Decryption failed: {e}')

    def closeEvent(self, event):
        # 保存密钥到文件以便下次使用
        try:
            with open('key.key', 'wb') as key_file:
                key_file.write(self.key)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save key: {e}')
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = PasswordTool()
    tool.show()
    sys.exit(app.exec_())