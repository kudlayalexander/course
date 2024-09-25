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
    QComboBox,
    QDialog,
    QGridLayout,
    QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal

class LessonsWindowT(QWidget):
    update_table_signal = pyqtSignal()

    def __init__(self, weeks_controller, lessons_controller):
        super().__init__()
        self.setWindowTitle("Занятия")
        self.weeks_controller = weeks_controller
        self.lessons_controller = lessons_controller

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Неделя", "День недели", "Номер занятия"])
        self.update_table()

        
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_lesson)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_lesson)

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
        lessons = self.lessons_controller.get_all_lessons()
        self.table.setRowCount(len(lessons))
        for row, lesson in enumerate(lessons):
            self.table.setItem(row, 0, QTableWidgetItem(str(lesson.lesson_id)))
            self.table.setItem(row, 1, QTableWidgetItem(str(lesson.week_id)))
            self.table.setItem(row, 2, QTableWidgetItem(str(lesson.day_of_week)))
            self.table.setItem(row, 3, QTableWidgetItem(str(lesson.lesson_number)))

    def add_lesson(self):
        self.add_lesson_dialog = AddLessonDialog(self.weeks_controller, self.lessons_controller)
        self.add_lesson_dialog.finished.connect(self.update_table_signal.emit)
        self.add_lesson_dialog.show()

    def delete_lesson(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                lesson_id = int(self.table.item(row.row(), 0).text())
                self.lessons_controller.delete_lesson(lesson_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

class AddLessonDialog(QDialog):
    def __init__(self, weeks_controller, lessons_controller):
        super().__init__()
        self.setWindowTitle("Добавить занятие")
        self.weeks_controller = weeks_controller
        self.lessons_controller = lessons_controller

        
        week_combo = QComboBox()
        week_combo.addItems([str(week.week_id) for week in self.weeks_controller.get_all_weeks()])

        
        day_input = QLineEdit()

        
        lesson_number_input = QLineEdit()

        
        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        
        add_button.clicked.connect(self.add_lesson_to_db)
        cancel_button.clicked.connect(self.close)

        
        layout = QGridLayout()
        layout.addWidget(QLabel("Неделя:"), 0, 0)
        layout.addWidget(week_combo, 0, 1)
        layout.addWidget(QLabel("День недели:"), 1, 0)
        layout.addWidget(day_input, 1, 1)
        layout.addWidget(QLabel("Номер занятия:"), 2, 0)
        layout.addWidget(lesson_number_input, 2, 1)
        layout.addWidget(add_button, 3, 0)
        layout.addWidget(cancel_button, 3, 1)

        self.setLayout(layout)
        self.week_combo = week_combo
        self.day_input = day_input
        self.lesson_number_input = lesson_number_input

    def add_lesson_to_db(self):
        week_id = int(self.week_combo.currentText())
        day_of_week = self.day_input.text()
        lesson_number = int(self.lesson_number_input.text())

        
        if not all([week_id, day_of_week, lesson_number]):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        
        self.lessons_controller.add_lesson(week_id, day_of_week, lesson_number)
        QMessageBox.information(self, "Успех", "Занятие добавлено.")
        self.close()