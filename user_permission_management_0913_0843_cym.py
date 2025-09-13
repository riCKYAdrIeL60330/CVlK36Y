# 代码生成时间: 2025-09-13 08:43:48
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel,
                                QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt

"""
用户权限管理系统
"""

class UserPermissionManager(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和大小
        self.setWindowTitle('用户权限管理系统')
        self.setGeometry(100, 100, 400, 300)

        # 创建布局
        layout = QVBoxLayout()

        # 添加用户名和权限输入框
        self.username_label = QLabel('用户名:')
        self.username_input = QLineEdit()
        self.permission_label = QLabel('权限:')
        self.permission_input = QLineEdit()

        # 添加添加用户按钮
        self.add_user_button = QPushButton('添加用户')
        self.add_user_button.clicked.connect(self.add_user)

        # 添加显示区域
        self.display_area = QTextEdit()

        # 将组件添加到布局
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.permission_label)
        layout.addWidget(self.permission_input)
        layout.addWidget(self.add_user_button)
        layout.addWidget(self.display_area)

        # 设置布局
        self.setLayout(layout)

        # 初始化用户权限字典
        self.user_permissions = {}

    def add_user(self):
        # 获取用户名和权限
        username = self.username_input.text().strip()
        permission = self.permission_input.text().strip()

        # 检查输入是否为空
        if not username or not permission:
            QMessageBox.warning(self, '警告', '用户名和权限不能为空！')
            return

        # 添加用户权限
        try:
            self.user_permissions[username] = permission
            self.display_area.append(f'用户 {username} 添加成功，权限：{permission}')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'添加用户失败：{str(e)}')

"""
主函数
"""
def main():
    app = QApplication(sys.argv)
    window = UserPermissionManager()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()