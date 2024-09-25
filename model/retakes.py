class Retake:
    def __init__(self, retake_id, lesson_id, teacher_id, subject_id):
        self.retake_id = retake_id
        self.lesson_id = lesson_id
        self.teacher_id = teacher_id
        self.subject_id = subject_id

    def __str__(self):
        return f"Retake(retake_id={self.retake_id}, lesson_id={self.lesson_id}, teacher_id={self.teacher_id}, subject_id={self.subject_id})"