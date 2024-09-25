class EducationalProgramSchedule:
    def __init__(self, schedule_id, program_id, lesson_id, teacher_id, subject_id):
        self.schedule_id = schedule_id
        self.program_id = program_id
        self.lesson_id = lesson_id
        self.teacher_id = teacher_id
        self.subject_id = subject_id

    def __str__(self):
        return f"EducationalProgramSchedule(schedule_id={self.schedule_id}, program_id={self.program_id}, lesson_id={self.lesson_id}, teacher_id={self.teacher_id}, subject_id={self.subject_id})"