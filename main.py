from student import Student
from exercise import Exercise
from instructor import Instructor
from cohort import Cohort

daily_journal = Exercise("Daily Journal", "Javascript")
frontend_capstone = Exercise("Frontend Capstone", "React")
car_dealership = Exercise("Car Dealership Challenge", "Javascript")
nutshell = Exercise("Nutshell", "Javascript")

c40 = Cohort("Day Cohort 40")
c19 = Cohort("Evening Cohort 19")
c38 = Cohort("Day Cohort 38")

zach = Student("Zach", "Nicholson", "@zachattack")
ronnie = Student("Ronnie", "Lankford", "@m0t0cr0ssg0d")
kaleb = Student("Kaleb", "Moran", "@ssbmDWAIN")
tanner = Student("Tanner", "Brainard", "@bigBRAINbigBUCKS")

joe = Instructor("Joe", "Shepherd", "@morningjoe", "Infinite patience")
bryan = Instructor("Bryan", "Nielsen", "@fathercomedy", "Dad jokes")
sage = Instructor("Sage", "Klein", "@fallensoldierRIP", "Humor & Figma?")

c40.addStudents(zach, kaleb)
c38.addStudents(ronnie, tanner)
c19.addStudents(zach, ronnie, kaleb, tanner)

c40.addInstructors(joe, bryan, sage)
c38.addInstructors(joe, bryan)
c19.addInstructors(sage)

joe.assignExercise(zach, car_dealership)
bryan.assignExercise(kaleb, car_dealership)
sage.assignExercise(ronnie, frontend_capstone)
joe.assignExercise(zach, nutshell)
joe.assignExercise(tanner, nutshell)
joe.assignExercise(ronnie, nutshell)
joe.assignExercise(kaleb, nutshell)
bryan.assignExercise(tanner, daily_journal)
sage.assignExercise(tanner, frontend_capstone)
sage.assignExercise(ronnie, daily_journal)

print(zach, kaleb, ronnie, tanner)
print(c40, c38, c19)