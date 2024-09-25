import datetime

class Week:
    def __init__(self, week_id, week_number, start_date, end_date):
        self.week_id = week_id
        self.week_number = week_number
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Week(week_id={self.week_id}, week_number={self.week_number}, start_date={self.start_date.strftime('%Y-%m-%d')}, end_date={self.end_date.strftime('%Y-%m-%d')})"