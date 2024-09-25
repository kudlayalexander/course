from model.educational_program import EducationalProgram
from model.database import EducationalProgramsDatabase

class EducationalProgramsController:
    def __init__(self):
        self.educational_programs_db = EducationalProgramsDatabase()

    def get_all_educational_programs(self):
        programs_data = self.educational_programs_db.get_all_educational_programs()
        return [
            EducationalProgram(program[0], program[1], program[2], program[3])
            for program in programs_data
        ]

    def add_educational_program(self, program_name, faculty_id, year):
        self.educational_programs_db.add_educational_program(program_name, faculty_id, year)

    def delete_educational_program(self, program_id):
        self.educational_programs_db.delete_educational_program(program_id)