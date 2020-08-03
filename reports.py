import sqlite3;

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/zach/workspace/python_exercises/py_student_exercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
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
                print(f'{student[1]} {student[2]} is in {student[5]}')

reports = StudentExerciseReports()
reports.all_students()