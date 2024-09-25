from model.teacher_schedule import TeacherSchedule
from model.database import TeacherScheduleDatabase

class TeacherScheduleController:
    def __init__(self):
        self.teacher_schedule_db = TeacherScheduleDatabase()

    def get_all_schedule_entries(self):
        schedule_data = self.teacher_schedule_db.get_all_schedule_entries()
        return [
            TeacherSchedule(schedule[0], schedule[1], schedule[2], schedule[3])
            for schedule in schedule_data
        ]

    def add_schedule_entry(self, teacher_id, subject_id, lesson_id):
        self.teacher_schedule_db.add_schedule_entry(
            teacher_id, subject_id, lesson_id
        )

    def delete_schedule_entry(self, schedule_id):
        self.teacher_schedule_db.delete_schedule_entry(schedule_id)