# 代码生成时间: 2025-09-21 08:22:01
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget
from openpyxl import Workbook

"""
Excel表格自动生成器
使用PyQt5 GUI和openpyxl库创建Excel文件
"""

class ExcelGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('Excel表格自动生成器')
        self.setGeometry(100, 100, 300, 200)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个按钮，点击后保存Excel文件
        button = QPushButton('保存Excel文件')
        button.clicked.connect(self.save_excel)
        layout.addWidget(button)

        # 设置中心窗口
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def save_excel(self):
        try:
            # 选择保存文件的路径和文件名
            filename, _ = QFileDialog.getSaveFileName(self, '保存Excel文件', 'file.xlsx', 'Excel Files (*.xlsx)')
            if filename:
                # 创建一个Excel工作簿
                wb = Workbook()
                # 添加一个工作表
                ws = wb.active
                # 可以在这里添加更多代码来填充Excel文件
                # 例如，添加标题行
                ws.append(['标题1', '标题2', '标题3'])
                # 保存工作簿
                wb.save(filename)
                print(f'Excel文件已保存到：{filename}')
        except Exception as e:
            print(f'保存Excel文件时发生错误：{e}')


def main():
    app = QApplication(sys.argv)
    ex = ExcelGenerator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
