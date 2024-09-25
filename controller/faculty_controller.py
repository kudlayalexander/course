from model.faculty import Faculty
from model.database import FacultiesDatabase

class FacultiesController:
    def __init__(self):
        self.faculties_db = FacultiesDatabase()

    def get_all_faculties(self):
        faculties_data = self.faculties_db.get_all_faculties()
        return [Faculty(faculty[0], faculty[1]) for faculty in faculties_data]

    def add_faculty(self, faculty_name):
        self.faculties_db.add_faculty(faculty_name)

    def delete_faculty(self, faculty_id):
        self.faculties_db.delete_faculty(faculty_id)