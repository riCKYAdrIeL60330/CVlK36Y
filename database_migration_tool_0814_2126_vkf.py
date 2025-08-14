# 代码生成时间: 2025-08-14 21:26:02
import sys
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from sqlalchemy import create_engine, MetaData, Table, select

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DatabaseMigrationTool(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Database Migration Tool')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.source_button = QPushButton('Select Source Database')
        self.source_button.clicked.connect(self.select_source_database)
        self.layout.addWidget(self.source_button)

        self.target_button = QPushButton('Select Target Database')
        self.target_button.clicked.connect(self.select_target_database)
        self.layout.addWidget(self.target_button)

        self.migrate_button = QPushButton('Migrate')
        self.migrate_button.clicked.connect(self.migrate)
        self.layout.addWidget(self.migrate_button)

    def select_source_database(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Source Database", "", "Database Files (*.*)", options=options)
        if file_name:
            self.source_database = file_name
            logging.info(f'Source database selected: {self.source_database}')

    def select_target_database(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Target Database", "", "Database Files (*.*)", options=options)
        if file_name:
            self.target_database = file_name
            logging.info(f'Target database selected: {self.target_database}')

    def migrate(self):
        if not all([self.source_database, self.target_database]):
            QMessageBox.warning(self, 'Warning', 'Please select both source and target databases')
            return

        try:
            engine_source = create_engine(f'sqlite:///{self.source_database}')
            engine_target = create_engine(f'sqlite:///{self.target_database}')
            metadata = MetaData()
            metadata.reflect(bind=engine_source)
            for table_name in metadata.tables:
                table = Table(table_name, metadata, autoload_with=engine_source)
                s = select(table)
                result = engine_source.execute(s)
                for row in result:
                    engine_target.execute(table.insert().values(row))
            QMessageBox.information(self, 'Success', 'Migration completed successfully')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            logging.error(f'Migration failed: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = DatabaseMigrationTool()
    tool.show()
    sys.exit(app.exec_())