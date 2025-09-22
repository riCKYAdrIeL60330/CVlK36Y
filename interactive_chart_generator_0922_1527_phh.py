# 代码生成时间: 2025-09-22 15:27:11
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter

"""
An interactive chart generator using PyQt framework.
This program allows users to create line charts interactively
with the ability to add or remove data points.
"""

class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.series = QLineSeries()
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Interactive Line Chart")
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.chart_view)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.load_button)

        self.add_button = QPushButton("Add Data Point", self)
        self.add_button.clicked.connect(self.add_data_point)

        self.remove_button = QPushButton("Remove Data Point", self)
        self.remove_button.clicked.connect(self.remove_data_point)

        self.save_button = QPushButton("Save Chart", self)
        self.save_button.clicked.connect(self.save_chart)

        self.load_button = QPushButton("Load Chart", self)
        self.load_button.clicked.connect(self.load_chart)

        self.data_x = 0
        self.data_y = 0

    def add_data_point(self):
        """Add a new data point to the chart."""
        self.data_x += 1
        self.data_y = float(input("Enter y value: "))
        self.series.append(self.data_x, self.data_y)

    def remove_data_point(self):
        """Remove the last data point from the chart."""
        if self.series.count() > 0:
            self.series.remove(self.series.at(self.series.count() - 1))
        else:
            print("No data points to remove.")

    def save_chart(self):
        """Save the current chart as an image file."""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Chart", "", "PNG Files (*.png)", options=options)
        if file_name:
            self.chart.save(file_name)

    def load_chart(self):
        """Load a chart from an image file."""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load Chart", "", "PNG Files (*.png)", options=options)
        if file_name:
            self.chart.load(file_name)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive Chart Generator")
        self.resize(800, 600)
        self.chart_widget = ChartWidget(self)
        self.setCentralWidget(self.chart_widget)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                             "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()