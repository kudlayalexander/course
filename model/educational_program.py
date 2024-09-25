class EducationalProgram:
    def __init__(self, program_id, program_name, faculty_id, year_of_admission):
        self.program_id = program_id
        self.program_name = program_name
        self.faculty_id = faculty_id
        self.year_of_admission = year_of_admission

    def __str__(self):
        return f"EducationalProgram(program_id={self.program_id}, program_name='{self.program_name}', faculty_id={self.faculty_id}, year_of_admission={self.year_of_admission})"