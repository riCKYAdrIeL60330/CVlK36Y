# 代码生成时间: 2025-09-07 02:27:15
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
from PyQt5.QtCore import Qt
from sqlalchemy import create_engine, MetaData, Table

# 数据库迁移工具类
class DatabaseMigrationTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('Database Migration Tool')
        self.setGeometry(100, 100, 800, 600)

        # 创建主布局
        layout = QVBoxLayout()

        # 创建数据库源选择按钮
        self.source_button = QPushButton('Select Source Database')
        self.source_button.clicked.connect(self.select_source_db)
        layout.addWidget(self.source_button)

        # 创建数据库目标选择按钮
        self.target_button = QPushButton('Select Target Database')
        self.target_button.clicked.connect(self.select_target_db)
        layout.addWidget(self.target_button)

        # 创建迁移按钮
        self.migrate_button = QPushButton('Migrate')
        self.migrate_button.clicked.connect(self.migrate_database)
        layout.addWidget(self.migrate_button)

        # 创建状态标签
        self.status_label = QLabel('Ready')
        layout.addWidget(self.status_label)

        # 设置中心小部件和布局
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_source_db(self):
        # 选择源数据库文件
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Source Database', '', 'SQL Files (*.sql)')
        if filename:
            self.source_db = filename
            self.status_label.setText('Source database selected')
        else:
            self.status_label.setText('Source database selection cancelled')

    def select_target_db(self):
        # 选择目标数据库文件
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Target Database', '', 'SQL Files (*.sql)')
        if filename:
            self.target_db = filename
            self.status_label.setText('Target database selected')
        else:
            self.status_label.setText('Target database selection cancelled')

    def migrate_database(self):
        # 执行数据库迁移
        if hasattr(self, 'source_db') and hasattr(self, 'target_db'):
            try:
                # 读取源数据库
                engine = create_engine(f'sqlite:///{self.source_db}')
                metadata = MetaData()
                metadata.reflect(bind=engine)
                tables = metadata.tables

                # 读取目标数据库
                target_engine = create_engine(f'sqlite:///{self.target_db}')
                target_metadata = MetaData()
                target_metadata.reflect(bind=target_engine)
                target_tables = target_metadata.tables

                # 迁移数据
                for table_name in tables:
                    if table_name in target_tables:
                        table = tables[table_name]
                        target_table = target_tables[table_name]
                        rows = engine.execute(table.select()).fetchall()
                        target_engine.execute(target_table.insert(), rows)

                self.status_label.setText('Migration successful')
            except Exception as e:
                self.status_label.setText(f'Migration failed: {e}')
        else:
            self.status_label.setText('Please select both source and target databases')

# 运行应用
def main():
    app = QApplication(sys.argv)
    tool = DatabaseMigrationTool()
    tool.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
