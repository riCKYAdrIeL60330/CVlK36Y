# 代码生成时间: 2025-09-23 01:24:48
import sys
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt
from PyQt5.QtWidgets import QApplication, QTableView


# 数据模型类
class DataModel(QAbstractTableModel):
    """
    数据模型类，继承自QAbstractTableModel。
    该类负责管理数据，提供数据给视图。
    """
    def __init__(self, data=None, parent=None):
        super(DataModel, self).__init__(parent)
        self._data = data or []  # 初始化数据

    def rowCount(self, parent=QModelIndex()):
        """
        返回行数。
        """
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        """
        返回列数。
        """
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=Qt.DisplayRole):
        """
        返回指定位置的数据。
        """
        if not index.isValid() or not (0 <= index.row() < len(self._data)):
            return None

        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """
        返回表头数据。
        """
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return f"Column {section + 1}"
        else:
            return f"Row {section + 1}"

    def insertRows(self, position, rows, index=QModelIndex()):
        """
        插入行。
        """
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for _ in range(rows):
            self._data.insert(position, [])
        self.endInsertRows()

    def removeRows(self, position, rows, index=QModelIndex()):
        """
        删除行。
        """
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        for _ in range(rows):
            self._data.pop(position)
        self.endRemoveRows()

    def setData(self, index, value, role=Qt.EditRole):
        """
        设置数据。
        """
        if index.isValid() and role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index,
                               Qt.DisplayRole)
            return True
        return False


# 主函数
def main():
    # 创建应用和视图
    app = QApplication(sys.argv)
    view = QTableView()

    # 创建数据模型
    model = DataModel([['Name', 'Age'], ['John', 25], ['Alice', 30]])
    view.setModel(model)

    # 显示视图
    view.show()

    # 运行应用
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
