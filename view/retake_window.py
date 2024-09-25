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

class RetakesWindow(QWidget):
    update_table_signal = pyqtSignal()

    def __init__(self, teachers_controller, subjects_controller, weeks_controller, retakes_controller):
        super().__init__()
        self.setWindowTitle("Пересдачи")
        self.teachers_controller = teachers_controller
        self.subjects_controller = subjects_controller
        self.weeks_controller = weeks_controller
        self.retakes_controller = retakes_controller

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Преподаватель", "Предмет", "Занятие"])
        self.update_table()

        
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_retake)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_retake)

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
        retakes = self.retakes_controller.get_all_retakes()
        self.table.setRowCount(len(retakes))
        for row, retake in enumerate(retakes):
            self.table.setItem(row, 0, QTableWidgetItem(str(retake.retake_id)))
            self.table.setItem(row, 1, QTableWidgetItem(get_teacher_name(retake.teacher_id, self.teachers_controller)))
            self.table.setItem(row, 2, QTableWidgetItem(get_subject_name(retake.subject_id, self.subjects_controller)))
            self.table.setItem(row, 3, QTableWidgetItem(get_lesson_info(retake.lesson_id, self.weeks_controller)))

    def add_retake(self):
        self.add_retake_dialog = AddRetakeDialog(
            self.teachers_controller, self.subjects_controller, self.weeks_controller, self.retakes_controller
        )
        self.add_retake_dialog.finished.connect(self.update_table_signal.emit)
        self.add_retake_dialog.show()

    def delete_retake(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                retake_id = int(self.table.item(row.row(), 0).text())
                self.retakes_controller.delete_retake(retake_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

def get_teacher_name(teacher_id, teachers_controller):
    teachers = teachers_controller.get_all_teachers()
    for teacher in teachers:
        if teacher.teacher_id == teacher_id:
            return teacher.teacher_name
    return "Неизвестный преподаватель"

def get_subject_name(subject_id, subjects_controller):
    subjects = subjects_controller.get_all_subjects()
    for subject in subjects:
        if subject.subject_id == subject_id:
            return subject.subject_name
    return "Неизвестный предмет"

def get_lesson_info(lesson_id, weeks_controller):
    lessons = weeks_controller.get_all_lessons()
    for lesson in lessons:
        if lesson.lesson_id == lesson_id:
            return f"Неделя {lesson.week_number}, День {lesson.day_of_week}, Занятие {lesson.lesson_number}"
    return "Неизвестное занятие"

class AddRetakeDialog(QDialog):
    def __init__(self, teachers_controller, subjects_controller, weeks_controller, retakes_controller):
        super().__init__()
        self.setWindowTitle("Добавить пересдачу")
        self.teachers_controller = teachers_controller
        self.subjects_controller = subjects_controller
        self.weeks_controller = weeks_controller
        self.retakes_controller = retakes_controller

        
        teacher_combo = QComboBox()
        teacher_combo.addItems([teacher.teacher_name for teacher in self.teachers_controller.get_all_teachers()])

        
        subject_combo = QComboBox()
        subject_combo.addItems([subject.subject_name for subject in self.subjects_controller.get_all_subjects()])

        
        lesson_combo = QComboBox()
        lesson_combo.addItems([f"Неделя {lesson.week_number}, День {lesson.day_of_week}, Занятие {lesson.lesson_number}" for lesson in self.weeks_controller.get_all_lessons()])

        
        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        
        add_button.clicked.connect(self.add_retake_to_db)
        cancel_button.clicked.connect(self.close)

        
        layout = QGridLayout()
        layout.addWidget(QLabel("Преподаватель:"), 0, 0)
        layout.addWidget(teacher_combo, 0, 1)
        layout.addWidget(QLabel("Предмет:"), 1, 0)
        layout.addWidget(subject_combo, 1, 1)
        layout.addWidget(QLabel("Занятие:"), 2, 0)
        layout.addWidget(lesson_combo, 2, 1)
        layout.addWidget(add_button, 3, 0)
        layout.addWidget(cancel_button, 3, 1)

        self.setLayout(layout)
        self.teacher_combo = teacher_combo
        self.subject_combo = subject_combo
        self.lesson_combo = lesson_combo

    def add_retake_to_db(self):
        teacher_id = self.teachers_controller.get_all_teachers()[self.teacher_combo.currentIndex()].teacher_id
        subject_id = self.subjects_controller.get_all_subjects()[self.subject_combo.currentIndex()].subject_id
        lesson_id = self.weeks_controller.get_all_lessons()[self.lesson_combo.currentIndex()].lesson_id

        
        if not all([teacher_id, subject_id, lesson_id]):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите все поля.")
            return

        
        self.retakes_controller.add_retake(lesson_id, teacher_id, subject_id)
        QMessageBox.information(self, "Успех", "Пересдача добавлена.")
        self.close()