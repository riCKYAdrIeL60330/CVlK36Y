# 代码生成时间: 2025-08-23 22:41:01
#!/usr/bin/env python

"""
Inventory Management System using Python and PyQt framework.
This program allows users to manage inventory with the following features:
- Add new items
- Update existing items
- Delete items
- View current inventory
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QFormLayout, QLineEdit, QLabel, QMessageBox, QListWidget)

class InventoryManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Inventory Management System')
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        # Form layout for item details
        self.form_layout = QFormLayout()
        self.item_name = QLineEdit()
        self.item_quantity = QLineEdit()
        self.form_layout.addRow('Item Name:', self.item_name)
        self.form_layout.addRow('Quantity:', self.item_quantity)

        # List to display inventory items
        self.inventory_list = QListWidget()

        # Buttons for adding, updating, and deleting items
        self.add_button = QPushButton('Add Item')
        self.add_button.clicked.connect(self.add_item)
        self.update_button = QPushButton('Update Item')
        self.update_button.clicked.connect(self.update_item)
        self.delete_button = QPushButton('Delete Item')
        self.delete_button.clicked.connect(self.delete_item)

        # Layout setup
        layout.addLayout(self.form_layout)
        layout.addWidget(self.inventory_list)
        layout.addWidget(self.add_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.inventory = {}

    def add_item(self):
        """Add a new item to the inventory."""
        item_name = self.item_name.text()
        quantity = self.item_quantity.text()
        if item_name and quantity.isdigit():
            if item_name in self.inventory:
                QMessageBox.warning(self, 'Warning', 'Item already exists.')
            else:
                self.inventory[item_name] = int(quantity)
                self.inventory_list.addItem(item_name)
                self.item_name.clear()
                self.item_quantity.clear()
        else:
            QMessageBox.critical(self, 'Error', 'Invalid input.')

    def update_item(self):
        """Update an existing item in the inventory."""
        item_name = self.item_name.text()
        quantity = self.item_quantity.text()
        if item_name and quantity.isdigit():
            if item_name in self.inventory:
                self.inventory[item_name] = int(quantity)
                self.inventory_list.addItem(item_name)
            else:
                QMessageBox.warning(self, 'Warning', 'Item does not exist.')
            self.item_name.clear()
            self.item_quantity.clear()
        else:
            QMessageBox.critical(self, 'Error', 'Invalid input.')

    def delete_item(self):
        """Delete an item from the inventory."""
        current_item = self.inventory_list.currentItem()
        if current_item:
            item_name = current_item.text()
            if item_name in self.inventory:
                del self.inventory[item_name]
                self.inventory_list.takeItem(self.inventory_list.row(current_item))
            else:
                QMessageBox.warning(self, 'Warning', 'Item does not exist.')
        else:
            QMessageBox.warning(self, 'Warning', 'No item selected.')

    def show_inventory(self):
        """Display the current inventory."""
        inventory_str = ''
        for item, quantity in self.inventory.items():
            inventory_str += f'{item}: {quantity}
'
        QMessageBox.information(self, 'Inventory', inventory_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InventoryManagement()
    ex.show()
    sys.exit(app.exec_())