# 代码生成时间: 2025-10-01 22:27:02
import sys
from PyQt5.QtWidgets import QApplication, QTreeView, QFileSystemModel, QAbstractItemView
from PyQt5.QtCore import QDir

"""
A PyQt5 example demonstrating the use of QTreeView with a file system model.
This program opens a tree view that displays the contents of a directory.
"""

class TreeViewExample:
    def __init__(self):
        # Create the application and tree view
        self.app = QApplication(sys.argv)
        self.tree_view = QTreeView()
        self.model = QFileSystemModel()
        
        # Set up the model to display the current directory
        self.model.setRootPath(QDir.currentPath())
        self.tree_view.setModel(self.model)
        
        # Hide the column headers and set the view to show the file system's root directory
        self.tree_view.header().setVisible(False)
        self.tree_view.setRootIndex(self.model.index(QDir.currentPath()))
        
        # Set the view to display in a single column, showing file names only
        self.tree_view.setUniformRowHeights(True)
        self.tree_view.setAnimated(False)
        self.tree_view.setIndentation(20)
        self.tree_view.setExpandsOnDoubleClick(False)
        self.tree_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        # Show the tree view
        self.tree_view.show()
        sys.exit(self.app.exec_())

# Run the example
if __name__ == '__main__':
    try:
        TreeViewExample()
    except Exception as e:
        print(f"An error occurred: {e}")
