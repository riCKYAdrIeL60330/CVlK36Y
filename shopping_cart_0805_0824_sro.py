# 代码生成时间: 2025-08-05 08:24:28
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QComboBox, QListWidget
from PyQt5.QtCore import Qt

"""
A simple shopping cart application using PyQt5.
This program allows the user to select items from a list and add them to a shopping cart.
"""

class ShoppingCart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create a label for the items list
        self.item_label = QLabel('Available Items:')
        self.layout.addWidget(self.item_label)

        # Create a list widget to display available items
        self.items_list = QListWidget()
        self.layout.addWidget(self.items_list)
        self.items_list.addItems(['Apple', 'Banana', 'Orange', 'Milk', 'Bread'])

        # Create a label for the cart
        self.cart_label = QLabel('Shopping Cart:')
        self.layout.addWidget(self.cart_label)

        # Create a list widget to display the shopping cart items
        self.cart_list = QListWidget()
        self.layout.addWidget(self.cart_list)

        # Create a button to add items to the cart
        self.add_button = QPushButton('Add to Cart')
        self.add_button.clicked.connect(self.addToCart)
        self.layout.addWidget(self.add_button)

        # Set the window title and size
        self.setWindowTitle('Shopping Cart')
        self.setGeometry(300, 300, 300, 200)

    def addToCart(self):
        # Get the current item selected in the items list
        current_item = self.items_list.currentItem()
        if current_item is not None:
            # Add the item to the cart list
            self.cart_list.addItem(current_item.text())
            # Clear the selection in the items list
            self.items_list.setCurrentRow(-1)
        else:
            # Show an error message if no item is selected
            print('Please select an item to add to the cart.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cart = ShoppingCart()
    cart.show()
    sys.exit(app.exec_())