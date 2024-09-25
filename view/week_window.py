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
    QMessageBox,
    QDateEdit
)
from PyQt5.QtCore import Qt, pyqtSignal

class WeeksWindow(QWidget):
    update_table_signal = pyqtSignal()

    def __init__(self, weeks_controller):
        super().__init__()
        self.setWindowTitle("Недели")
        self.weeks_controller = weeks_controller

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Номер недели", "Дата начала", "Дата окончания"])
        self.update_table()

        
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_week)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_week)

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
        weeks = self.weeks_controller.get_all_weeks()
        self.table.setRowCount(len(weeks))
        for row, week in enumerate(weeks):
            self.table.setItem(row, 0, QTableWidgetItem(str(week.week_id)))
            self.table.setItem(row, 1, QTableWidgetItem(str(week.week_number)))
            self.table.setItem(row, 2, QTableWidgetItem(week.start_date.strftime("%Y-%m-%d")))
            self.table.setItem(row, 3, QTableWidgetItem(week.end_date.strftime("%Y-%m-%d")))

    def add_week(self):
        self.add_week_dialog = AddWeekDialog(self.weeks_controller)
        self.add_week_dialog.finished.connect(self.update_table_signal.emit)
        self.add_week_dialog.show()

    def delete_week(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            for row in selected_rows:
                week_id = int(self.table.item(row.row(), 0).text())
                self.weeks_controller.delete_week(week_id)
            self.update_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

class AddWeekDialog(QDialog):
    def __init__(self, weeks_controller):
        super().__init__()
        self.setWindowTitle("Добавить неделю")
        self.weeks_controller = weeks_controller

        
        week_number_input = QLineEdit()

        
        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        
        add_button.clicked.connect(self.add_week_to_db)
        cancel_button.clicked.connect(self.close)

        
        layout = QGridLayout()
        layout.addWidget(QLabel("Номер недели:"), 0, 0)
        layout.addWidget(week_number_input, 0, 1)
        layout.addWidget(add_button, 1, 0)
        layout.addWidget(cancel_button, 1, 1)

        self.setLayout(layout)
        self.week_number_input = week_number_input

    def add_week_to_db(self):
        week_number_str = self.week_number_input.text()

        
        if not week_number_str:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите номер недели.")
            return

        
        try:
            week_number = int(week_number_str)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите числовое значение для номера недели.")
            return

        
        existing_weeks = self.weeks_controller.get_all_weeks()
        if any(week.week_number == week_number for week in existing_weeks):
            QMessageBox.warning(self, "Ошибка", "Неделя с таким номером уже существует.")
            return

        
        self.weeks_controller.add_week(week_number)
        QMessageBox.information(self, "Успех", "Неделя добавлена.")
        self.close()