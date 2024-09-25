from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QGridLayout,
    QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal

class FacultiesWindow(QWidget):
    update_table_signal = pyqtSignal()

    def __init__(self, faculties_controller):
        super().__init__()
        self.setWindowTitle("Факультеты")
        self.faculties_controller = faculties_controller

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["ID", "Название"])
        self.update_table()

        
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_faculty)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_faculty)

        update_button = QPushButton("Обновить")
        update_button.clicked.connect(self.update_table)

        
        layout = QVBoxLayout()
        layout.addWidget(add_button)
        layout.addWidget(delete_button)
        layout.addWidget(update_button)
        layout.addWidget(self.table)
        self.setLayout(layout)

        
        self.update_table_signal.connect(self.update_table)

    def update_table(self):
        faculties = self.faculties_controller.get_all_faculties()
        self.table.setRowCount(len(faculties))
        for row, faculty in enumerate(faculties):
            self.table.setItem(row, 0, QTableWidgetItem(str(faculty.faculty_id)))
            self.table.setItem(row, 1, QTableWidgetItem(faculty.faculty_name))

    def add_faculty(self):
        self.add_faculty_dialog = AddFacultyDialog(self.faculties_controller)
        self.add_faculty_dialog.finished.connect(self.update_table_signal.emit)
        self.add_faculty_dialog.show()

    def delete_faculty(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                faculty_id = int(self.table.item(row.row(), 0).text())
                self.faculties_controller.delete_faculty(faculty_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

class AddFacultyDialog(QDialog):
    def __init__(self, faculties_controller):
        super().__init__()
        self.setWindowTitle("Добавить факультет")
        self.faculties_controller = faculties_controller

        
        name_input = QLineEdit()

        
        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        
        add_button.clicked.connect(self.add_faculty_to_db)
        cancel_button.clicked.connect(self.close)

        
        layout = QGridLayout()
        layout.addWidget(QLabel("Название факультета:"), 0, 0)
        layout.addWidget(name_input, 0, 1)
        layout.addWidget(add_button, 1, 0)
        layout.addWidget(cancel_button, 1, 1)

        self.setLayout(layout)
        self.name_input = name_input

    def add_faculty_to_db(self):
        name = self.name_input.text()

        
        if not name:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите название факультета.")
            return

        
        self.faculties_controller.add_faculty(name)
        QMessageBox.information(self, "Успех", "Факультет добавлен.")
        self.close()