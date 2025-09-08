# 代码生成时间: 2025-09-09 03:19:22
import sys
import base64
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

"""
密码加密解密工具
"""
class PasswordTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口基本属性
# FIXME: 处理边界情况
        self.setWindowTitle('Password Encryption Decryption Tool')
        self.setGeometry(100, 100, 400, 200)

        # 创建布局
# NOTE: 重要实现细节
        layout = QVBoxLayout()

        # 创建输入框
        self.input_edit = QLineEdit()
        self.input_edit.setPlaceholderText('Enter password')
        layout.addWidget(self.input_edit)

        # 创建显示框
        self.output_edit = QLineEdit()
        self.output_edit.setPlaceholderText('Encrypted/Decrypted password')
        self.output_edit.setReadOnly(True)
        layout.addWidget(self.output_edit)

        # 创建加密按钮
        self.encrypt_btn = QPushButton('Encrypt')
        self.encrypt_btn.clicked.connect(self.encrypt)
        layout.addWidget(self.encrypt_btn)

        # 创建解密按钮
        self.decrypt_btn = QPushButton('Decrypt')
        self.decrypt_btn.clicked.connect(self.decrypt)
        layout.addWidget(self.decrypt_btn)

        # 设置布局
        self.setLayout(layout)

    def encrypt(self):
        try:
# 优化算法效率
            # 获取输入框内容
            password = self.input_edit.text()

            # 检查密码是否为空
            if not password:
                raise ValueError('Password cannot be empty')

            # 加密密码
            encrypted_password = self.encrypt_password(password)
            self.output_edit.setText(encrypted_password)
        except Exception as e:
            self.output_edit.setText(str(e))

    def decrypt(self):
        try:
            # 获取输入框内容
# 改进用户体验
            encrypted_password = self.output_edit.text()

            # 检查加密密码是否为空
# 改进用户体验
            if not encrypted_password:
                raise ValueError('Encrypted password cannot be empty')

            # 解密密码
            decrypted_password = self.decrypt_password(encrypted_password)
# 添加错误处理
            self.output_edit.setText(decrypted_password)
        except Exception as e:
# 增强安全性
            self.output_edit.setText(str(e))

    def encrypt_password(self, password):
        # 使用MD5算法加密密码
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        return base64.b64encode(md5.digest()).decode('utf-8')

    def decrypt_password(self, encrypted_password):
# 增强安全性
        # 检查加密密码是否有效
        try:
            # 使用Base64解码加密密码
            base64_bytes = encoded_password.encode('utf-8')
            base64_password = base64.b64decode(base64_bytes)
            # 使用MD5算法解密密码
            md5 = hashlib.md5()
            md5.update(base64_password)
            return md5.hexdigest()
        except Exception as e:
            raise ValueError('Invalid encrypted password')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = PasswordTool()
    tool.show()
    sys.exit(app.exec_())
# 扩展功能模块