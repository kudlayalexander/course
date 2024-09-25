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
from controller.subject_controller import SubjectsController

class SubjectsWindow(QWidget):
    update_table_signal = pyqtSignal()

    def __init__(self, subjects_controller):
        super().__init__()
        self.setWindowTitle("Предметы")
        self.subjects_controller: SubjectsController = subjects_controller

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["ID", "Название"])
        self.update_table()

        
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_subject)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_subject)

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
        subjects = self.subjects_controller.get_all_subjects()
        self.table.setRowCount(len(subjects))
        for row, subject in enumerate(subjects):
            self.table.setItem(row, 0, QTableWidgetItem(str(subject.subject_id)))
            self.table.setItem(row, 1, QTableWidgetItem(subject.subject_name))

    def add_subject(self):
        self.add_subject_dialog = AddSubjectDialog(self.subjects_controller)
        self.add_subject_dialog.finished.connect(self.update_table_signal.emit)
        self.add_subject_dialog.show()

    def delete_subject(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                subject_id = int(self.table.item(row.row(), 0).text())
                self.subjects_controller.delete_subject(subject_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

class AddSubjectDialog(QDialog):
    def __init__(self, subjects_controller):
        super().__init__()
        self.setWindowTitle("Добавить предмет")
        self.subjects_controller = subjects_controller

        
        name_input = QLineEdit()

        
        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        
        add_button.clicked.connect(self.add_subject_to_db)
        cancel_button.clicked.connect(self.close)

        
        layout = QGridLayout()
        layout.addWidget(QLabel("Название предмета:"), 0, 0)
        layout.addWidget(name_input, 0, 1)
        layout.addWidget(add_button, 1, 0)
        layout.addWidget(cancel_button, 1, 1)

        self.setLayout(layout)
        self.name_input = name_input

    def add_subject_to_db(self):
        name = self.name_input.text()

        
        if not name:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите название предмета.")
            return

        
        self.subjects_controller.add_subject(name)
        QMessageBox.information(self, "Успех", "Предмет добавлен.")
        self.close()