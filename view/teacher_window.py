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

class TeachersWindow(QWidget):
    update_table_signal = pyqtSignal()

    def __init__(self, teachers_controller):
        super().__init__()
        self.setWindowTitle("Преподаватели")
        self.teachers_controller = teachers_controller

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["ID", "ФИО"])
        self.update_table()

        
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_teacher)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_teacher)

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
        teachers = self.teachers_controller.get_all_teachers()
        self.table.setRowCount(len(teachers))
        for row, teacher in enumerate(teachers):
            self.table.setItem(row, 0, QTableWidgetItem(str(teacher.teacher_id)))
            self.table.setItem(row, 1, QTableWidgetItem(teacher.teacher_name))

    def add_teacher(self):
        self.add_teacher_dialog = AddTeacherDialog(self.teachers_controller)
        self.add_teacher_dialog.finished.connect(self.update_table_signal.emit)
        self.add_teacher_dialog.show()

    def delete_teacher(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                teacher_id = int(self.table.item(row.row(), 0).text())
                self.teachers_controller.delete_teacher(teacher_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

class AddTeacherDialog(QDialog):
    def __init__(self, teachers_controller):
        super().__init__()
        self.setWindowTitle("Добавить преподавателя")
        self.teachers_controller = teachers_controller

        
        fio_input = QLineEdit()

        
        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        
        add_button.clicked.connect(self.add_teacher_to_db)
        cancel_button.clicked.connect(self.close)

        
        layout = QGridLayout()
        layout.addWidget(QLabel("ФИО преподавателя:"), 0, 0)
        layout.addWidget(fio_input, 0, 1)
        layout.addWidget(add_button, 1, 0)
        layout.addWidget(cancel_button, 1, 1)

        self.setLayout(layout)
        self.fio_input = fio_input

    def add_teacher_to_db(self):
        fio = self.fio_input.text()

        
        if not fio:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите ФИО преподавателя.")
            return

        
        self.teachers_controller.add_teacher(fio)
        QMessageBox.information(self, "Успех", "Преподаватель добавлен.")
        self.close()