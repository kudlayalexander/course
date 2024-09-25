from model.educational_program_schedule import EducationalProgramSchedule
from model.database import EducationalProgramScheduleDatabase

class EducationalProgramScheduleController:
    def __init__(self):
        self.educational_program_schedule_db = EducationalProgramScheduleDatabase()

    def get_all_schedule_entries(self):
        schedule_data = self.educational_program_schedule_db.get_all_schedule_entries()
        return [
            EducationalProgramSchedule(
                schedule[0], schedule[1], schedule[2], schedule[3], schedule[4]
            )
            for schedule in schedule_data
        ]

    def add_schedule_entry(self, program_id, teacher_id, subject_id, lesson_id):
        self.educational_program_schedule_db.add_schedule_entry(
            program_id, teacher_id, subject_id, lesson_id
        )

    def delete_schedule_entry(self, schedule_id):
        self.educational_program_schedule_db.delete_schedule_entry(schedule_id)