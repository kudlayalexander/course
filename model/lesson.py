class Lesson:
    def __init__(self, lesson_id, week_id, day_of_week, lesson_number):
        self.lesson_id = lesson_id
        self.week_id = week_id
        self.day_of_week = day_of_week
        self.lesson_number = lesson_number

    def __str__(self):
        return f"Lesson(lesson_id={self.lesson_id}, week_id={self.week_id}, day_of_week={self.day_of_week}, lesson_number={self.lesson_number})"