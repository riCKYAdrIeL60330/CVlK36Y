# 代码生成时间: 2025-08-12 07:18:50
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QSpinBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

"""
# 添加错误处理
图片尺寸批量调整器
"""

class ImageResizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
# 扩展功能模块
        # 设置窗口标题和位置
        self.setWindowTitle('图片尺寸批量调整器')
        self.setGeometry(100, 100, 300, 200)

        # 创建布局
        layout = QVBoxLayout()

        # 添加选择文件夹按钮
        self.btn_select_folder = QPushButton('选择文件夹')
# 扩展功能模块
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)
# 改进用户体验

        # 添加目标尺寸输入框
# 优化算法效率
        self.lbl_target_size = QLabel('目标尺寸 (宽度 x 高度):')
        layout.addWidget(self.lbl_target_size)
        self.spin_width = QSpinBox()
        self.spin_height = QSpinBox()
        layout.addWidget(self.spin_width)
        layout.addWidget(self.spin_height)

        # 添加调整尺寸按钮
        self.btn_resize = QPushButton('调整尺寸')
        self.btn_resize.clicked.connect(self.resize_images)
        layout.addWidget(self.btn_resize)

        # 设置布局
        self.setLayout(layout)

    def select_folder(self):
        # 选择文件夹
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            self.folder_path = folder_path
            print(f'选择的文件夹: {folder_path}')

    def resize_images(self):
        # 读取目标尺寸
        target_width = self.spin_width.value()
        target_height = self.spin_height.value()

        # 检查文件夹路径
# FIXME: 处理边界情况
        if not self.folder_path:
            print('未选择文件夹')
            return

        # 遍历文件夹中的图片文件
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
# TODO: 优化性能
                file_path = os.path.join(self.folder_path, filename)

                try:
                    # 读取图片
                    pixmap = QPixmap(file_path)

                    # 调整图片尺寸
                    resized_pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio)
# NOTE: 重要实现细节

                    # 保存调整后的图片
# 改进用户体验
                    new_file_path = os.path.join(self.folder_path, f'resized_{filename}')
                    resized_pixmap.save(new_file_path)
                    print(f'调整后的图片已保存: {new_file_path}')
                except Exception as e:
                    print(f'调整图片尺寸失败: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    resizer = ImageResizer()
    resizer.show()
    sys.exit(app.exec_())