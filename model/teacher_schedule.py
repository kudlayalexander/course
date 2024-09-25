class TeacherSchedule:
    def __init__(self, schedule_id, teacher_id, lesson_id, subject_id):
        self.schedule_id = schedule_id
        self.teacher_id = teacher_id
        self.lesson_id = lesson_id
        self.subject_id = subject_id

    def __str__(self):
        return f"TeacherSchedule(schedule_id={self.schedule_id}, teacher_id={self.teacher_id}, lesson_id={self.lesson_id}, subject_id={self.subject_id})"