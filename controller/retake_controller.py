from model.retakes import Retake
from model.database import RetakesDatabase

class RetakesController:
    def __init__(self):
        self.retakes_db = RetakesDatabase()

    def get_all_retakes(self):
        retakes_data = self.retakes_db.get_all_retakes()
        return [
            Retake(retake[0], retake[1], retake[2], retake[3])
            for retake in retakes_data
        ]

    def add_retake(self, lesson_id, teacher_id, subject_id):
        self.retakes_db.add_retake(lesson_id, teacher_id, subject_id)

    def delete_retake(self, retake_id):
        self.retakes_db.delete_retake(retake_id)