from NSSPerson import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack):
        super().__init__(first_name, last_name, slack)
        self.exercises = list()

    def __str__(self):
        string = f"{self.first_name} {self.last_name} AKA {self.slack} is currently working on: \n"
        for exercise in self.exercises:
            string += f"* {exercise.name} ({exercise.language}) \n"
        return string