-- Drop existing tables if they exist to ensure a clean slate
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Faculties;
DROP TABLE IF EXISTS EducationalPrograms;
DROP TABLE IF EXISTS Weeks;
DROP TABLE IF EXISTS Subjects;
DROP TABLE IF EXISTS Lessons;
DROP TABLE IF EXISTS EducationalProgramSchedule;
DROP TABLE IF EXISTS TeachersSchedule;
DROP TABLE IF EXISTS RetakesSchedule;


CREATE TABLE "Teachers" (
  "TeacherID" SERIAL PRIMARY KEY,
  "TeacherName" TEXT NOT NULL
);

CREATE TABLE "Faculties" (
  "FacultyID" SERIAL PRIMARY KEY,
  "FacultyName" TEXT NOT NULL
);

CREATE TABLE "EducationalPrograms" (
  "EducationalProgramID" SERIAL PRIMARY KEY,
  "EducationalProgramName" TEXT NOT NULL,
  "FacultyID" INTEGER NOT NULL,
  "YearOfAdmission" INTEGER NOT NULL
);

CREATE TABLE "Weeks" (
  "WeekID" SERIAL PRIMARY KEY,
  "WeekNumber" INTEGER NOT NULL,
  "StartDate" DATE NOT NULL,
  "EndDate" DATE NOT NULL
);

CREATE TABLE "Subjects" (
  "SubjectID" SERIAL PRIMARY KEY,
  "SubjectName" TEXT NOT NULL
);

CREATE TABLE "Lessons" (
  "LessonID" SERIAL PRIMARY KEY,
  "WeekID" INTEGER NOT NULL,
  "DayOfWeek" INTEGER NOT NULL,
  "LessonNumber" INTEGER NOT NULL
);

CREATE TABLE "EducationalProgramSchedule" (
  "EducationalProgramScheduleID" SERIAL PRIMARY KEY,
  "EducationalProgramID" INTEGER NOT NULL,
  "LessonID" INTEGER NOT NULL,
  "TeacherID" INTEGER,
  "SubjectID" INTEGER
);

CREATE TABLE "TeacherSchedule" (
  "TeacherScheduleID" SERIAL PRIMARY KEY,
  "TeacherID" INTEGER NOT NULL,
  "LessonID" INTEGER NOT NULL,
  "SubjectID" INTEGER
);

CREATE TABLE "RetakesSchedule" (
  "RetakesScheduleID" SERIAL PRIMARY KEY,
  "LessonID" INTEGER NOT NULL,
  "TeacherID" INTEGER,
  "SubjectID" INTEGER
);

ALTER TABLE "EducationalPrograms" ADD FOREIGN KEY ("FacultyID") REFERENCES "Faculties" ("FacultyID") ON DELETE CASCADE;

ALTER TABLE "EducationalProgramSchedule" ADD FOREIGN KEY ("EducationalProgramID") REFERENCES "EducationalPrograms" ("EducationalProgramID") ON DELETE CASCADE;

ALTER TABLE "EducationalProgramSchedule" ADD FOREIGN KEY ("LessonID") REFERENCES "Lessons" ("LessonID") ON DELETE CASCADE;

ALTER TABLE "EducationalProgramSchedule" ADD FOREIGN KEY ("TeacherID") REFERENCES "Teachers" ("TeacherID");

ALTER TABLE "EducationalProgramSchedule" ADD FOREIGN KEY ("SubjectID") REFERENCES "Subjects" ("SubjectID");

ALTER TABLE "TeacherSchedule" ADD FOREIGN KEY ("TeacherID") REFERENCES "Teachers" ("TeacherID") ON DELETE CASCADE;

ALTER TABLE "TeacherSchedule" ADD FOREIGN KEY ("LessonID") REFERENCES "Lessons" ("LessonID") ON DELETE CASCADE;

ALTER TABLE "TeacherSchedule" ADD FOREIGN KEY ("SubjectID") REFERENCES "Subjects" ("SubjectID");

ALTER TABLE "RetakesSchedule" ADD FOREIGN KEY ("LessonID") REFERENCES "Lessons" ("LessonID") ON DELETE CASCADE;

ALTER TABLE "RetakesSchedule" ADD FOREIGN KEY ("TeacherID") REFERENCES "Teachers" ("TeacherID");

ALTER TABLE "RetakesSchedule" ADD FOREIGN KEY ("SubjectID") REFERENCES "Subjects" ("SubjectID");

ALTER TABLE "Lessons" ADD FOREIGN KEY ("WeekID") REFERENCES "Weeks" ("WeekID");
