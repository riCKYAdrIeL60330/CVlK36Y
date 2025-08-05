# 代码生成时间: 2025-08-06 03:04:01
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class UserLoginSystem(QWidget):
    """
    用户登录验证系统
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('User Login System')
        self.setGeometry(300, 300, 300, 200)

        # 创建布局
        layout = QVBoxLayout()

        # 创建标签和输入框
        self.username_label = QLabel('Username: ')
        self.username_input = QLineEdit()
        self.password_label = QLabel('Password: ')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # 创建登录按钮
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        # 将组件添加到布局
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        # 设置布局
        self.setLayout(layout)

    def login(self):
        # 获取用户名和密码
        username = self.username_input.text()
        password = self.password_input.text()

        # 简单的用户验证，假设只有用户名为'admin'和密码为'123456'的用户
        if username == 'admin' and password == '123456':
            QMessageBox.information(self, 'Login Success', 'You have successfully logged in.')
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid username or password.')

    def main(self):
        self.show()
        sys.exit(QApplication.instance().exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UserLoginSystem()
    ex.main()