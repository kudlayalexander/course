from model.subjects import Subject
from model.database import SubjectsDatabase

class SubjectsController:
    def __init__(self):
        self.subjects_db = SubjectsDatabase()

    def get_all_subjects(self):
        subjects_data = self.subjects_db.get_all_subjects()
        return [Subject(subject[0], subject[1]) for subject in subjects_data]

    def add_subject(self, subject_name):
        self.subjects_db.add_subject(subject_name)

    def delete_subject(self, subject_id):
        self.subjects_db.delete_subject(subject_id)