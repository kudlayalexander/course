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

class EducationalProgramsWindow(QWidget):
    update_table_signal = pyqtSignal()

    def __init__(self, faculties_controller, educational_programs_controller):
        super().__init__()
        self.setWindowTitle("Образовательные программы")
        self.faculties_controller = faculties_controller
        self.educational_programs_controller = educational_programs_controller

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Название", "Факультет", "Год поступления"])
        self.update_table()

        
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_educational_program)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_educational_program)

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
        programs = self.educational_programs_controller.get_all_educational_programs()
        self.table.setRowCount(len(programs))
        for row, program in enumerate(programs):
            self.table.setItem(row, 0, QTableWidgetItem(str(program.program_id)))
            self.table.setItem(row, 1, QTableWidgetItem(program.program_name))
            self.table.setItem(row, 2, QTableWidgetItem(get_faculty_name(program.faculty_id, self.faculties_controller)))
            self.table.setItem(row, 3, QTableWidgetItem(str(program.year_of_admission)))

    def add_educational_program(self):
        self.add_educational_program_dialog = AddEducationalProgramDialog(
            self.faculties_controller, self.educational_programs_controller
        )
        self.add_educational_program_dialog.finished.connect(self.update_table_signal.emit)
        self.add_educational_program_dialog.show()

    def delete_educational_program(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                program_id = int(self.table.item(row.row(), 0).text())
                self.educational_programs_controller.delete_educational_program(program_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

def get_faculty_name(faculty_id, faculties_controller):
    faculties = faculties_controller.get_all_faculties()
    for faculty in faculties:
        if faculty.faculty_id == faculty_id:
            return faculty.faculty_name
    return "Неизвестный факультет"

class AddEducationalProgramDialog(QDialog):
    def __init__(self, faculties_controller, educational_programs_controller):
        super().__init__()
        self.setWindowTitle("Добавить образовательную программу")
        self.faculties_controller = faculties_controller
        self.educational_programs_controller = educational_programs_controller

        
        name_input = QLineEdit()

        
        faculty_combo = QComboBox()
        faculty_combo.addItems([faculty.faculty_name for faculty in self.faculties_controller.get_all_faculties()])

        
        year_input = QLineEdit()

        
        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        
        add_button.clicked.connect(self.add_educational_program_to_db)
        cancel_button.clicked.connect(self.close)

        
        layout = QGridLayout()
        layout.addWidget(QLabel("Название образовательной программы:"), 0, 0)
        layout.addWidget(name_input, 0, 1)
        layout.addWidget(QLabel("Факультет:"), 1, 0)
        layout.addWidget(faculty_combo, 1, 1)
        layout.addWidget(QLabel("Год поступления:"), 2, 0)
        layout.addWidget(year_input, 2, 1)
        layout.addWidget(add_button, 3, 0)
        layout.addWidget(cancel_button, 3, 1)

        self.setLayout(layout)
        self.name_input = name_input
        self.faculty_combo = faculty_combo
        self.year_input = year_input

    def add_educational_program_to_db(self):
        name = self.name_input.text()
        faculty_id = self.faculties_controller.get_all_faculties()[self.faculty_combo.currentIndex()].faculty_id
        year = int(self.year_input.text())

        
        if not all([name, faculty_id, year]):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        
        self.educational_programs_controller.add_educational_program(name, faculty_id, year)
        QMessageBox.information(self, "Успех", "Образовательная программа добавлена.")
        self.close()