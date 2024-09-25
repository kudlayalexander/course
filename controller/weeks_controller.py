from model.week import Week
from model.database import WeeksDatabase

class WeeksControllerT:
    def __init__(self):
        self.weeks_db = WeeksDatabase()

    def get_all_weeks(self):
        weeks_data = self.weeks_db.get_all_weeks()
        return [
            Week(week[0], week[1], week[2], week[3])
            for week in weeks_data
        ]

    def add_week(self, week_number):
        self.weeks_db.add_week(week_number)

    def delete_week(self, week_id):
        self.weeks_db.delete_week(week_id)