class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

    def __str__(self):
        return f"Teacher(teacher_id={self.teacher_id}, teacher_name='{self.teacher_name}')"