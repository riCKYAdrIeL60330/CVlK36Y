# 代码生成时间: 2025-09-21 17:15:39
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QTextEdit
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
import random

"""
Interactive Chart Generator
=========================

This script is a PyQt5 application that generates interactive charts based on user input.

Features:
- User can select chart type (line chart) and input data.
- Chart updates interactively as user inputs data.
"""

class InteractiveChartGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Interactive Chart Generator')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Layout for the main window
        mainLayout = QVBoxLayout()
        self.centralWidget.setLayout(mainLayout)

        # Add a label for the chart type selection
        chartTypeLabel = QLabel('Chart Type:')
        mainLayout.addWidget(chartTypeLabel)

        # Combo box for chart type selection
        self.chartTypeComboBox = QComboBox()
        self.chartTypeComboBox.addItems(['Line Chart'])  # Add more chart types as needed
        mainLayout.addWidget(self.chartTypeComboBox)

        # Add a label for the data input
        dataInputLabel = QLabel('Enter Data Points:')
        mainLayout.addWidget(dataInputLabel)

        # Text edit for data input
        self.dataInputTextEdit = QTextEdit()
        mainLayout.addWidget(self.dataInputTextEdit)

        # Add a button to generate the chart
        self.generateChartButton = QPushButton('Generate Chart')
        self.generateChartButton.clicked.connect(self.generateChart)
        mainLayout.addWidget(self.generateChartButton)

        # Add a layout for the chart view
        self.chartLayout = QHBoxLayout()
        mainLayout.addLayout(self.chartLayout)

    def generateChart(self):
        # Clear the current chart
        self.chartLayout.removeWidget(self.chartView)
        self.chartView.deleteLater()

        # Get the selected chart type
        chartType = self.chartTypeComboBox.currentText()

        # Parse the data points from the text edit
        try:
            dataPoints = self.dataInputTextEdit.toPlainText().split(',')
            dataPoints = [float(point) for point in dataPoints]
        except ValueError:
            self.showError('Invalid data points. Please enter comma-separated numbers.')
            return

        # Create a new chart based on the selected type
        if chartType == 'Line Chart':
            self.createLineChart(dataPoints)

    def createLineChart(self, dataPoints):
        # Create a line series
        series = QLineSeries()
        for i, point in enumerate(dataPoints):
            series.append(i, point)

        # Create a chart and add the series
        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()

        # Set up the axes
        axisX = QCategoryAxis()
        axisX.append(QCategoryAxis.Category(i) for i in range(len(dataPoints)))
        chart.setAxisX(axisX, series)

        axisY = QValueAxis()
        chart.setAxisY(axisY, series)

        # Create a chart view and add it to the layout
        self.chartView = QChartView(chart)
        self.chartLayout.addWidget(self.chartView)

    def showError(self, message):
        # Show an error message to the user
        print(f'Error: {message}')

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InteractiveChartGenerator()
    window.show()
    sys.exit(app.exec_())