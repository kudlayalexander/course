from model.lesson import Lesson
from model.database import LessonsDatabase

class LessonsController:
    def __init__(self):
        self.lessons_db = LessonsDatabase()

    def get_all_lessons(self):
        lessons_data = self.lessons_db.get_all_lessons()
        return [Lesson(lesson[0], lesson[1], lesson[2], lesson[3]) for lesson in lessons_data]

    def add_lesson(self, week_id, day_of_week, lesson_number):
        self.lessons_db.add_lesson(week_id, day_of_week, lesson_number)

    def delete_lesson(self, lesson_id):
        self.lessons_db.delete_lesson(lesson_id)