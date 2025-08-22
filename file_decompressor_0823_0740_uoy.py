# 代码生成时间: 2025-08-23 07:40:46
import sys
import zipfile
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

"""
文件解压工具使用PyQt5界面和zipfile库实现解压功能。
该工具允许用户选择需要解压的zip文件，并将其解压到指定目录。
"""

class FileDecompressor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('文件解压工具')
# 增强安全性
        self.setGeometry(100, 100, 300, 100)

        # 创建按钮和布局
        self.btn_open = QPushButton('选择文件', self)
# 增强安全性
        self.btn_open.clicked.connect(self.openFileDialog)
# NOTE: 重要实现细节
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.btn_open)
        self.setLayout(self.layout)

    def openFileDialog(self):
        # 打开文件对话框，选择需要解压的文件
        options = QFileDialog.Options()
# TODO: 优化性能
        fileName, _ = QFileDialog.getOpenFileName(self, "选择ZIP文件", "", "ZIP Files (*.zip)", options=options)

        if fileName:
            try:
# NOTE: 重要实现细节
                self.decompressFile(fileName)
                QMessageBox.information(self, '解压成功', '文件解压成功！')
            except Exception as e:
                QMessageBox.critical(self, '解压失败', f'文件解压失败: {str(e)}')

    def decompressFile(self, filePath):
# 改进用户体验
        # 解压文件到指定目录
        with zipfile.ZipFile(filePath, 'r') as zip_ref:
            extract_path = QFileDialog.getExistingDirectory(self, '选择解压目录', options=QFileDialog.ShowDirsOnly)
# FIXME: 处理边界情况
            if extract_path:
                zip_ref.extractall(extract_path)
            else:
                raise ValueError('未选择解压目录')

if __name__ == '__main__':
    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 创建文件解压工具窗口实例
# 改进用户体验
    decompressor = FileDecompressor()
    decompressor.show()

    # 运行应用程序，直到所有窗口关闭
    sys.exit(app.exec_())