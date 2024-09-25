from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTabWidget,
    QMessageBox
)
from view.teacher_window import TeachersWindow
from view.faculty_window import FacultiesWindow
from view.educational_program_window import EducationalProgramsWindow
from view.week_window import WeeksWindow
from view.subject_window import SubjectsWindow
from view.educational_program_schedule_window import EducationalProgramScheduleWindow
from view.teacher_schedule_window import TeacherScheduleWindow
from view.retakes_schedule_window import RetakesScheduleWindow
from controller.teacher_controller import TeachersController
from controller.faculty_controller import FacultiesController
from controller.educational_program_controller import EducationalProgramsController
from controller.weeks_controller import WeeksControllerT
from controller.subject_controller import SubjectsController
from controller.educational_program_schedule_controller import EducationalProgramScheduleController
from controller.teacher_schedule_controller import TeacherScheduleController
from controller.retakes_schedule_controller import RetakesScheduleController

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расписание пересдач")

        # Создание контроллеров
        self.teachers_controller = TeachersController()
        self.faculties_controller = FacultiesController()
        self.educational_programs_controller = EducationalProgramsController()
        self.weeks_controller = WeeksControllerT()
        self.subjects_controller = SubjectsController()
        self.educational_program_schedule_controller = EducationalProgramScheduleController()
        self.teacher_schedule_controller = TeacherScheduleController()
        self.retakes_schedule_controller = RetakesScheduleController()

        # Создание вкладок
        self.tabs = QTabWidget()
        self.tabs.addTab(TeachersWindow(self.teachers_controller), "Преподаватели")
        self.tabs.addTab(FacultiesWindow(self.faculties_controller), "Факультеты")
        self.tabs.addTab(EducationalProgramsWindow(self.educational_programs_controller), "Образовательные программы")
        self.tabs.addTab(WeeksWindow(self.weeks_controller), "Недели")
        self.tabs.addTab(SubjectsWindow(self.subjects_controller), "Предметы")
        self.tabs.addTab(
            EducationalProgramScheduleWindow(
                self.educational_programs_controller,
                self.teachers_controller,
                self.subjects_controller,
                self.weeks_controller,
                self.educational_program_schedule_controller,
            ),
            "Расписание образовательных программ",
        )
        self.tabs.addTab(
            TeacherScheduleWindow(
                self.teachers_controller,
                self.subjects_controller,
                self.weeks_controller,
                self.teacher_schedule_controller,
            ),
            "Расписание преподавателей",
        )
        self.tabs.addTab(
            RetakesScheduleWindow(
                self.teachers_controller,
                self.subjects_controller,
                self.weeks_controller,
                self.retakes_schedule_controller,
            ),
            "Расписание пересдач",
        )

        # Макет для окна
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()