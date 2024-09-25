class Faculty:
    def __init__(self, faculty_id, faculty_name):
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name

    def __str__(self):
        return f"Faculty(faculty_id={self.faculty_id}, faculty_name='{self.faculty_name}')"