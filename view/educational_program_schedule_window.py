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

class EducationalProgramScheduleWindow(QWidget):
    update_table_signal = pyqtSignal()

    def __init__(
        self,
        educational_programs_controller,
        teachers_controller,
        subjects_controller,
        weeks_controller,
        educational_program_schedule_controller,
    ):
        super().__init__()
        self.setWindowTitle("Расписание образовательных программ")
        self.educational_programs_controller = educational_programs_controller
        self.teachers_controller = teachers_controller
        self.subjects_controller = subjects_controller
        self.weeks_controller = weeks_controller
        self.educational_program_schedule_controller = educational_program_schedule_controller

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Образовательная программа", "Преподаватель", "Предмет", "Занятие"]
        )
        self.update_table()

        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_schedule_entry)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_schedule_entry)

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
        schedule_entries = (
            self.educational_program_schedule_controller.get_all_schedule_entries()
        )
        self.table.setRowCount(len(schedule_entries))
        for row, entry in enumerate(schedule_entries):
            self.table.setItem(
                row,
                0,
                QTableWidgetItem(str(entry.schedule_id)),
            )
            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    get_educational_program_name(
                        entry.program_id, self.educational_programs_controller
                    )
                ),
            )
            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    get_teacher_name(entry.teacher_id, self.teachers_controller)
                ),
            )
            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    get_subject_name(entry.subject_id, self.subjects_controller)
                ),
            )
            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    get_lesson_info(entry.lesson_id, self.weeks_controller)
                ),
            )

    def add_schedule_entry(self):
        self.add_schedule_entry_dialog = AddScheduleEntryDialog(
            self.educational_programs_controller,
            self.teachers_controller,
            self.subjects_controller,
            self.weeks_controller,
            self.educational_program_schedule_controller,
        )
        self.add_schedule_entry_dialog.finished.connect(self.update_table_signal.emit)
        self.add_schedule_entry_dialog.show()

    def delete_schedule_entry(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                schedule_id = int(self.table.item(row.row(), 0).text())
                self.educational_program_schedule_controller.delete_schedule_entry(
                    schedule_id
                )
            self.update_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

def get_educational_program_name(program_id, educational_programs_controller):
    programs = educational_programs_controller.get_all_educational_programs()
    for program in programs:
        if program.program_id == program_id:
            return program.program_name
    return "Неизвестная образовательная программа"

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

class AddScheduleEntryDialog(QDialog):
    def __init__(
        self,
        educational_programs_controller,
        teachers_controller,
        subjects_controller,
        weeks_controller,
        educational_program_schedule_controller,
    ):
        super().__init__()
        self.setWindowTitle("Добавить запись в расписание")
        self.educational_programs_controller = educational_programs_controller
        self.teachers_controller = teachers_controller
        self.subjects_controller = subjects_controller
        self.weeks_controller = weeks_controller
        self.educational_program_schedule_controller = (
            educational_program_schedule_controller
        )

        program_combo = QComboBox()
        program_combo.addItems(
            [
                program.program_name
                for program in self.educational_programs_controller.get_all_educational_programs()
            ]
        )

        teacher_combo = QComboBox()
        teacher_combo.addItems(
            [
                teacher.teacher_name
                for teacher in self.teachers_controller.get_all_teachers()
            ]
        )

        subject_combo = QComboBox()
        subject_combo.addItems(
            [
                subject.subject_name
                for subject in self.subjects_controller.get_all_subjects()
            ]
        )

        lesson_combo = QComboBox()
        lesson_combo.addItems(
            [
                f"Неделя {lesson.week_number}, День {lesson.day_of_week}, Занятие {lesson.lesson_number}"
                for lesson in self.weeks_controller.get_all_lessons()
            ]
        )

        # Кнопки "Добавить" и "Отмена"
        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        # Обработчики событий
        add_button.clicked.connect(self.add_schedule_entry_to_db)
        cancel_button.clicked.connect(self.close)

        # Макет для элементов диалогового окна
        layout = QGridLayout()
        layout.addWidget(QLabel("Образовательная программа:"), 0, 0)
        layout.addWidget(program_combo, 0, 1)
        layout.addWidget(QLabel("Преподаватель:"), 1, 0)
        layout.addWidget(teacher_combo, 1, 1)
        layout.addWidget(QLabel("Предмет:"), 2, 0)
        layout.addWidget(subject_combo, 2, 1)
        layout.addWidget(QLabel("Занятие:"), 3, 0)
        layout.addWidget(lesson_combo, 3, 1)
        layout.addWidget(add_button, 4, 0)
        layout.addWidget(cancel_button, 4, 1)

        self.setLayout(layout)
        self.program_combo = program_combo
        self.teacher_combo = teacher_combo
        self.subject_combo = subject_combo
        self.lesson_combo = lesson_combo

    def add_schedule_entry_to_db(self):
        program_id = (
            self.educational_programs_controller.get_all_educational_programs()[
                self.program_combo.currentIndex()
            ].program_id
        )
        teacher_id = (
            self.teachers_controller.get_all_teachers()[
                self.teacher_combo.currentIndex()
            ].teacher_id
        )
        subject_id = (
            self.subjects_controller.get_all_subjects()[
                self.subject_combo.currentIndex()
            ].subject_id
        )
        lesson_id = (
            self.weeks_controller.get_all_lessons()[
                self.lesson_combo.currentIndex()
            ].lesson_id
        )

        # Проверка ввода
        if not all([program_id, teacher_id, subject_id, lesson_id]):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите все поля.")
            return

        # Добавление записи в расписание в базу данных
        self.educational_program_schedule_controller.add_schedule_entry(
            program_id, teacher_id, subject_id, lesson_id
        )
        QMessageBox.information(self, "Успех", "Запись в расписание добавлена.")
        self.close()