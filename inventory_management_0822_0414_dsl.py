# 代码生成时间: 2025-08-22 04:14:31
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

"""
库存管理系统
"""

class InventoryManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('库存管理系统')
        self.setGeometry(100, 100, 600, 400)

        # 创建中心窗口和布局
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        # 创建组件
        self.create_widgets()

    def create_widgets(self):
        # 输入框
        self.item_name = QLineEdit(self)
        self.item_quantity = QLineEdit(self)
        self.item_price = QLineEdit(self)

        # 按钮
        self.add_button = QPushButton('添加库存', self)
        self.add_button.clicked.connect(self.add_inventory)

        # 标签
        self.status_label = QLabel('状态：', self)

        # 表格
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['物品名称', '数量', '价格'])
        self.table.setRowCount(0)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 布局添加组件
        self.layout.addWidget(QLabel('物品名称：', self))
        self.layout.addWidget(self.item_name)
        self.layout.addWidget(QLabel('数量：', self))
        self.layout.addWidget(self.item_quantity)
        self.layout.addWidget(QLabel('价格：', self))
        self.layout.addWidget(self.item_price)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.table)

    def add_inventory(self):
        # 获取输入框内容
        item_name = self.item_name.text()
        item_quantity = self.item_quantity.text()
        item_price = self.item_price.text()

        # 验证输入
        if not item_name or not item_quantity or not item_price:
            QMessageBox.warning(self, '警告', '请填写所有字段')
            return

        try:
            item_quantity = int(item_quantity)
            item_price = float(item_price)
        except ValueError:
            QMessageBox.warning(self, '警告', '数量和价格必须是数字')
            return

        # 添加库存到表格
        self.table.insertRow(0)
        self.table.setItem(0, 0, QTableWidgetItem(item_name))
        self.table.setItem(0, 1, QTableWidgetItem(str(item_quantity)))
        self.table.setItem(0, 2, QTableWidgetItem(str(item_price)))

        # 清空输入框
        self.item_name.clear()
        self.item_quantity.clear()
        self.item_price.clear()

        # 更新状态标签
        self.status_label.setText('状态：添加成功')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    ex = InventoryManagement()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
