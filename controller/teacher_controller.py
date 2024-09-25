from model.teacher import Teacher
from model.database import TeachersDatabase

class TeachersController:
    def __init__(self):
        self.teachers_db = TeachersDatabase()

    def get_all_teachers(self):
        teachers_data = self.teachers_db.get_all_teachers()
        return [Teacher(teacher[0], teacher[1]) for teacher in teachers_data]

    def add_teacher(self, teacher_name):
        self.teachers_db.add_teacher(teacher_name)

    def delete_teacher(self, teacher_id):
        self.teachers_db.delete_teacher(teacher_id)