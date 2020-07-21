from NSSPerson import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack, specialty):
        super().__init__(first_name, last_name, slack)
        self.specialty = specialty

    def assignExercise(self, student, exercise):
        student.exercises.append(exercise)