import sqlite3;

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack = handle
        self.cohort = cohort

    def __repr__(self):
        return (f'{self.first_name} {self.last_name} is in {self.cohort}')

class Instructor():

    def __init__(self, first, last, handle, specialty, cohort):
        self.first_name = first
        self.last_name = last
        self.slack = handle
        self.specialty = specialty
        self.cohort = cohort

    def __repr__(self):
        return (f'{self.first_name} {self.last_name} teaches {self.cohort}. Their specialty is {self.specialty}.')

class Cohort():
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return (f'Welcome to {self.name}.')

class Exercise():
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return (f'{self.name} will be written in {self.language}.')
        
class StudentExerciseReports():

    def __init__(self):
        self.db_path = "/home/zach/workspace/python_exercises/py_student_exercises/studentexercises.db"

    def all_students(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.Slack,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def all_instructors(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[4], row[6])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.Slack,
                i.Specialty,
                i.CohortId,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)

    def all_cohorts(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[0])
            cursor = conn.cursor()

            cursor.execute("""
            select c.Name
            from Cohort c
            order by c.Name
            """)

            all_cohorts = cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

    def all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            cursor = conn.cursor()

            cursor.execute("""
            select e.Id,
                e.Name,
                e.Language
            from Exercise e
            order by e.Language
            """)

            all_exercises = cursor.fetchall()

            for ex in all_exercises:
                print(ex)
    
    def js_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            cursor = conn.cursor()

            cursor.execute("""
            select e.Id,
                e.Name,
                e.Language
            from Exercise e
            where e.Language = "Javascript"
            order by e.name
            """)

            js_exercises = cursor.fetchall()

            for ex in js_exercises:
                print(ex)

    def py_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            cursor = conn.cursor()

            cursor.execute("""
            select e.Id,
                e.Name,
                e.Language
            from Exercise e
            where e.Language = "Python"
            order by e.name
            """)

            py_exercises = cursor.fetchall()

            for ex in py_exercises:
                print(ex)

reports = StudentExerciseReports()
reports.all_cohorts()
reports.all_exercises()
reports.js_exercises()
reports.py_exercises()
reports.all_students()
reports.all_instructors()