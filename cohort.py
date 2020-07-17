class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()
    
    def addStudents(self, *students):
        for student in students:
            self.students.append(student)
            student.cohort = self.name

    def addInstructors(self, *instructors):
        for instructor in instructors:
            self.instructors.append(instructor)
            instructor.cohort = self.name
    
    def __str__(self):
        string = f"Welcome to {self.name}! Led by"
        for instructor in self.instructors:
            if len(self.instructors) == 1:
                string += f" {instructor.first_name} {instructor.last_name}. \n"
            elif len(self.instructors) == 2:
                if self.instructors[-1] == instructor:
                    string += f" and {instructor.first_name} {instructor.last_name}. \n"
                else:
                    string += f" {instructor.first_name} {instructor.last_name}"
            else:
                if self.instructors[-1] == instructor:
                    string += f" and {instructor.first_name} {instructor.last_name}. \n"
                else:
                    string += f" {instructor.first_name} {instructor.last_name},"
        string += f"Say hello to your fellow classmates: \n"
        for student in self.students:
            string += f"* {student.first_name} {student.last_name} \n"
        return string