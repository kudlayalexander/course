import psycopg2
import datetime

class FacultiesDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_faculties(self):
        self.cursor.execute("SELECT * FROM Faculties")
        return self.cursor.fetchall()

    def add_faculty(self, faculty_name):
        self.cursor.execute("INSERT INTO Faculties (FacultyName) VALUES (%s)", (faculty_name,))
        self.conn.commit()

    def update_faculty(self, faculty_id, faculty_name):
        self.cursor.execute("UPDATE Faculties SET FacultyName=%s WHERE FacultyID=%s", (faculty_name, faculty_id))
        self.conn.commit()

    def delete_faculty(self, faculty_id):
        self.cursor.execute("DELETE FROM Faculties WHERE FacultyID=%s", (faculty_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class TeachersDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_teachers(self):
        self.cursor.execute("SELECT * FROM Teachers")
        return self.cursor.fetchall()

    def add_teacher(self, teacher_name):
        self.cursor.execute("INSERT INTO Teachers (TeacherName) VALUES (%s)", (teacher_name,))
        self.conn.commit()

    def update_teacher(self, teacher_id, teacher_name):
        self.cursor.execute("UPDATE Teachers SET TeacherName=%s WHERE TeacherID=%s", (teacher_name, teacher_id))
        self.conn.commit()

    def delete_teacher(self, teacher_id):
        self.cursor.execute("DELETE FROM Teachers WHERE TeacherID=%s", (teacher_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
    

class EducationalProgramsDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_educational_programs(self):
        self.cursor.execute("SELECT * FROM EducationalPrograms")
        return self.cursor.fetchall()

    def add_educational_program(self, educational_program_name, faculty_id, year):
        self.cursor.execute(
            "INSERT INTO EducationalPrograms (EducationalProgramName, FacultyID, YearOfAdmission) VALUES (%s, %s, %s)",
            (educational_program_name, faculty_id, year),
        )
        self.conn.commit()

    def update_educational_program(self, educational_program_id, educational_program_name, faculty_id, year):
        self.cursor.execute(
            "UPDATE EducationalPrograms SET EducationalProgramName=%s, FacultyID=%s, YearOfAdmission=%s WHERE EducationalProgramID=%s",
            (educational_program_name, faculty_id, year, educational_program_id),
        )
        self.conn.commit()

    def delete_educational_program(self, educational_program_id):
        self.cursor.execute("DELETE FROM EducationalPrograms WHERE EducationalProgramID=%s", (educational_program_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


import psycopg2
import datetime

class WeeksDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_weeks(self):
        self.cursor.execute("SELECT * FROM Weeks")
        return self.cursor.fetchall()

    def add_week(self, week_number):
        first_day = datetime.date.today()
        start_date = first_day + datetime.timedelta(days=(week_number - 1) * 7)
        end_date = start_date + datetime.timedelta(days=6)

        self.cursor.execute(
            "INSERT INTO Weeks (WeekNumber, StartDate, EndDate) VALUES (%s, %s, %s)",
            (week_number, start_date, end_date),
        )
        self.conn.commit()

    def update_week(self, week_id, week_number):
        first_day = datetime.date.today()
        start_date = first_day + datetime.timedelta(days=(week_number - 1) * 7)
        end_date = start_date + datetime.timedelta(days=6)

        self.cursor.execute(
            "UPDATE Weeks SET WeekNumber=%s, StartDate=%s, EndDate=%s WHERE WeekID=%s",
            (week_number, start_date, end_date, week_id),
        )
        self.conn.commit()

    def delete_week(self, week_id):
        self.cursor.execute("DELETE FROM Weeks WHERE WeekID=%s", (week_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class SubjectsDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_subjects(self):
        self.cursor.execute("SELECT * FROM Subjects")
        return self.cursor.fetchall()

    def add_subject(self, subject_name):
        self.cursor.execute("INSERT INTO Subjects (SubjectName) VALUES (%s)", (subject_name,))
        self.conn.commit()

    def update_subject(self, subject_id, subject_name):
        self.cursor.execute("UPDATE Subjects SET SubjectName=%s WHERE SubjectID=%s", (subject_name, subject_id))
        self.conn.commit()

    def delete_subject(self, subject_id):
        self.cursor.execute("DELETE FROM Subjects WHERE SubjectID=%s", (subject_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class RetakesDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_retakes(self):
        self.cursor.execute("SELECT * FROM RetakesSchedule")
        return self.cursor.fetchall()

    def add_retake(self, lesson_id, teacher_id, subject_id):
        self.cursor.execute(
            "INSERT INTO RetakesSchedule (LessonID, TeacherID, SubjectID) VALUES (%s, %s, %s)",
            (lesson_id, teacher_id, subject_id),
        )
        self.conn.commit()

    def update_retake(self, retake_id, lesson_id, teacher_id, subject_id):
        self.cursor.execute(
            "UPDATE RetakesSchedule SET LessonID=%s, TeacherID=%s, SubjectID=%s WHERE RetakesScheduleID=%s",
            (lesson_id, teacher_id, subject_id, retake_id),
        )
        self.conn.commit()

    def delete_retake(self, retake_id):
        self.cursor.execute("DELETE FROM RetakesSchedule WHERE RetakesScheduleID=%s", (retake_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class EducationalProgramScheduleDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_schedule_entries(self):
        self.cursor.execute("SELECT * FROM EducationalProgramSchedule")
        return self.cursor.fetchall()

    def add_schedule_entry(self, program_id, teacher_id, subject_id, lesson_id):
        self.cursor.execute(
            "INSERT INTO EducationalProgramSchedule (EducationalProgramID, TeacherID, SubjectID, LessonID) VALUES (%s, %s, %s, %s)",
            (program_id, teacher_id, subject_id, lesson_id),
        )
        self.conn.commit()

    def update_schedule_entry(self, schedule_id, program_id, teacher_id, subject_id, lesson_id):
        self.cursor.execute(
            "UPDATE EducationalProgramSchedule SET EducationalProgramID=%s, TeacherID=%s, SubjectID=%s, LessonID=%s WHERE EducationalProgramScheduleID=%s",
            (program_id, teacher_id, subject_id, lesson_id, schedule_id),
        )
        self.conn.commit()

    def delete_schedule_entry(self, schedule_id):
        self.cursor.execute("DELETE FROM EducationalProgramSchedule WHERE EducationalProgramScheduleID=%s", (schedule_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class TeacherScheduleDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_schedule_entries(self):
        self.cursor.execute("SELECT * FROM TeacherSchedule")
        return self.cursor.fetchall()

    def add_schedule_entry(self, teacher_id, subject_id, lesson_id):
        self.cursor.execute(
            "INSERT INTO TeacherSchedule (TeacherID, SubjectID, LessonID) VALUES (%s, %s, %s)",
            (teacher_id, subject_id, lesson_id),
        )
        self.conn.commit()

    def update_schedule_entry(self, schedule_id, teacher_id, subject_id, lesson_id):
        self.cursor.execute(
            "UPDATE TeacherSchedule SET TeacherID=%s, SubjectID=%s, LessonID=%s WHERE TeacherScheduleID=%s",
            (teacher_id, subject_id, lesson_id, schedule_id),
        )
        self.conn.commit()

    def delete_schedule_entry(self, schedule_id):
        self.cursor.execute("DELETE FROM TeacherSchedule WHERE TeacherScheduleID=%s", (schedule_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class RetakesScheduleDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_schedule_entries(self):
        self.cursor.execute("SELECT * FROM RetakesSchedule")
        return self.cursor.fetchall()

    def add_schedule_entry(self, teacher_id, subject_id, lesson_id):
        self.cursor.execute(
            "INSERT INTO RetakesSchedule (TeacherID, SubjectID, LessonID) VALUES (%s, %s, %s)",
            (teacher_id, subject_id, lesson_id),
        )
        self.conn.commit()

    def update_schedule_entry(self, schedule_id, teacher_id, subject_id, lesson_id):
        self.cursor.execute(
            "UPDATE RetakesSchedule SET TeacherID=%s, SubjectID=%s, LessonID=%s WHERE RetakesScheduleID=%s",
            (teacher_id, subject_id, lesson_id, schedule_id),
        )
        self.conn.commit()

    def delete_schedule_entry(self, schedule_id):
        self.cursor.execute("DELETE FROM RetakesSchedule WHERE RetakesScheduleID=%s", (schedule_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class LessonsDatabase:
    def __init__(self, db_name="kursdb", db_user="kursuser", db_password="postgres", db_host="localhost", db_port="5432"):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self.cursor = self.conn.cursor()

    def get_all_lessons(self):
        self.cursor.execute("SELECT * FROM Lessons")
        return self.cursor.fetchall()

    def add_lesson(self, week_id, day_of_week, lesson_number):
        self.cursor.execute(
            "INSERT INTO Lessons (WeekID, DayOfWeek, LessonNumber) VALUES (%s, %s, %s)",
            (week_id, day_of_week, lesson_number),
        )
        self.conn.commit()

    def update_lesson(self, lesson_id, week_id, day_of_week, lesson_number):
        self.cursor.execute(
            "UPDATE Lessons SET WeekID=%s, DayOfWeek=%s, LessonNumber=%s WHERE LessonID=%s",
            (week_id, day_of_week, lesson_number, lesson_id),
        )
        self.conn.commit()

    def delete_lesson(self, lesson_id):
        self.cursor.execute("DELETE FROM Lessons WHERE LessonID=%s", (lesson_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()