# 代码生成时间: 2025-08-26 07:14:20
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QComboBox, QListWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

"""购物车程序实现了基本的购物车功能。"""

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """添加商品到购物车。"""
        self.items.append(item)
        return True

    def remove_item(self, item):
        """从购物车中移除商品。"""
        try:
            self.items.remove(item)
            return True
        except ValueError:
            return False

    def clear_cart(self):
        """清空购物车。"""
        self.items = []

    def get_cart_items(self):
        """获取购物车中的商品列表。"""
        return self.items

class ShoppingCartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cart = ShoppingCart()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('购物车')
        self.setGeometry(100, 100, 400, 300)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        self.item_combo = QComboBox()
        self.item_combo.addItems(['商品A', '商品B', '商品C'])
        layout.addWidget(self.item_combo)

        self.add_button = QPushButton('添加商品')
        self.add_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton('移除商品')
        self.remove_button.clicked.connect(self.remove_item)
        layout.addWidget(self.remove_button)

        self.clear_button = QPushButton('清空购物车')
        self.clear_button.clicked.connect(self.clear_cart)
        layout.addWidget(self.clear_button)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.central_widget.setLayout(layout)

    def add_item(self):
        item = self.item_combo.currentText()
        if self.cart.add_item(item):
            self.update_list_widget()
        else:
            QMessageBox.warning(self, '错误', '添加商品失败。')

    def remove_item(self):
        item = self.item_combo.currentText()
        if self.cart.remove_item(item):
            self.update_list_widget()
        else:
            QMessageBox.warning(self, '错误', '商品不存在。')

    def clear_cart(self):
        self.cart.clear_cart()
        self.update_list_widget()

    def update_list_widget(self):
        """更新列表显示。"""
        self.list_widget.clear()
        for item in self.cart.get_cart_items():
            self.list_widget.addItem(item)

def main():
    app = QApplication(sys.argv)
    window = ShoppingCartWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()