# 代码生成时间: 2025-08-10 18:06:48
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
    QVBoxLayout, QFileDialog, QLineEdit, QLabel)
from PyQt5.QtCore import Qt

"""
批量文件重命名工具"""
class BatchFileRenamer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('批量文件重命名工具')
        self.setGeometry(100, 100, 400, 200)

        # 布局
        layout = QVBoxLayout(self)

        # 文件夹选择按钮
        self.folder_btn = QPushButton('选择文件夹')
        self.folder_btn.clicked.connect(self.select_folder)
        layout.addWidget(self.folder_btn)

        # 文件名输入框
        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_input)

        # 重命名按钮
        self.rename_btn = QPushButton('重命名')
        self.rename_btn.clicked.connect(self.rename_files)
        layout.addWidget(self.rename_btn)

        # 状态标签
        self.status_label = QLabel('请选择文件夹', self)
        layout.addWidget(self.status_label)

    def select_folder(self):
        """选择文件夹"""
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            self.status_label.setText(folder_path)
            self.folder_path = folder_path

    def rename_files(self):
        """重命名文件"""
        if not self.name_input.text() or not self.folder_path:
            self.status_label.setText('请先选择文件夹并输入文件名')
            return

        new_name = self.name_input.text()
        old_name = new_name + '_old'

        try:
            for filename in os.listdir(self.folder_path):
                if filename.startswith(old_name):
                    os.rename(os.path.join(self.folder_path, filename),
                              os.path.join(self.folder_path,
                                           f'{new_name}_{os.path.splitext(filename)[1]}'))
            self.status_label.setText('文件重命名成功')
        except Exception as e:
            self.status_label.setText(f'重命名失败: {e}')

if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    # 创建窗口实例
    ex = BatchFileRenamer()
    # 显示窗口
    ex.show()
    # 运行应用程序
    sys.exit(app.exec_())