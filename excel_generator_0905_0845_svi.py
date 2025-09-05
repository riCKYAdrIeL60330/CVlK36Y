# 代码生成时间: 2025-09-05 08:45:25
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from openpyxl import Workbook

"""
Excel表格自动生成器
使用Python和PyQt框架创建一个图形界面，允许用户通过点击按钮生成Excel文件。
"""

class ExcelGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始位置
        self.setWindowTitle('Excel表格自动生成器')
        self.setGeometry(100, 100, 300, 200)

        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建按钮，绑定点击事件
        self.button = QPushButton('生成Excel文件', self)
        self.button.clicked.connect(self.generateExcel)
        layout.addWidget(self.button)

        # 设置布局
        self.setLayout(layout)

    def generateExcel(self):
        try:
            # 创建Excel文件
            wb = Workbook()
            # 保存到当前工作目录
            file_path, _ = QFileDialog.getSaveFileName(self, '保存Excel文件', '/', 'Excel 文件 (*.xlsx)')
            if file_path:
                wb.save(file_path)
                QMessageBox.information(self, '成功', 'Excel文件生成成功！')
            else:
                QMessageBox.warning(self, '警告', '未选择文件路径！')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'生成Excel文件时发生错误：{str(e)}')


def main():
    app = QApplication(sys.argv)
    ex = ExcelGenerator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
