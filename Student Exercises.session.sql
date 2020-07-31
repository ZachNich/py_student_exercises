-- Use the INSERT INTO SQL statement to create...

-- 3 cohorts
-- 5 exercises
-- 3 instructors
-- 7 students (don't put all students in the same cohort)
-- Assign 2 exercises to each student
-- Here's a sample insert statement for an exercise.

-- INSERT INTO Exercise (Name, Language)
-- VALUES ('Kandy Korner', 'JavaScript');
;

CREATE TABLE Exercise (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE,
    Language TEXT NOT NULL
);

CREATE TABLE Cohort (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Slack TEXT NOT NULL UNIQUE,
    CohortId INTEGER NOT NULL,
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Instructor (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    Slack TEXT NOT NULL UNIQUE,
    Specialty TEXT NOT NULL,
    CohortId INTEGER NOT NULL,
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE StudentExercises (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ExerciseId INTEGER NOT NULL,
    StudentId INTEGER NOT NULL,
    FOREIGN KEY(ExerciseId) REFERENCES Exercise(Id),
    FOREIGN KEY(StudentId) REFERENCES Student(Id)
);

INSERT INTO Exercise (Name, Language)
VALUES ('Daily Journal', 'Javascript');
INSERT INTO Exercise (Name, Language)
VALUES ('Frontend Capstone', 'React');
INSERT INTO Exercise (Name, Language)
VALUES ('Car Dealership Challenge', 'Javascript');
INSERT INTO Exercise (Name, Language)
VALUES ('Nutshell', 'Javascript');
INSERT INTO Exercise (Name, Language)
VALUES ('Student Exercises', 'Python');

INSERT INTO Cohort (Name)
VALUES ('Day Cohort 40');
INSERT INTO Cohort (Name)
VALUES ('Day Cohort 38');
INSERT INTO Cohort (Name)
VALUES ('Evening Cohort 19');

INSERT INTO Student (FirstName, LastName, Slack, CohortId)
VALUES ('Zach', 'Nicholson', '@zachattack', 1);
INSERT INTO Student (FirstName, LastName, Slack, CohortId)
VALUES ('Ronnie', 'Lankford', '@m0t0cr0ssg0d', 1);
INSERT INTO Student (FirstName, LastName, Slack, CohortId)
VALUES ('Kaleb', 'Moran', '@ssbmDWAIN', 2);
INSERT INTO Student (FirstName, LastName, Slack, CohortId)
VALUES ('Tanner', 'Brainard', '@bigBRAINbigBUCKS', 2);
INSERT INTO Student (FirstName, LastName, Slack, CohortId)
VALUES ('Daniel', 'Meza', '@MezaAmazeYa', 3);
INSERT INTO Student (FirstName, LastName, Slack, CohortId)
VALUES ('Felipe', 'Moura', '@makeYOUwantMOURA', 3);
INSERT INTO Student (FirstName, LastName, Slack, CohortId)
VALUES ('John', 'Bain', '@BringthepAIN', 3);

INSERT INTO Instructor (FirstName, LastName, Slack, Specialty, CohortId)
VALUES ('Joe', 'Shepherd', '@morningjoe', 'infinite patience', 1);
INSERT INTO Instructor (FirstName, LastName, Slack, Specialty, CohortId)
VALUES ('Bryan', 'Nilsen', '@fathercomedy', 'dd jokes', 2);
INSERT INTO Instructor (FirstName, LastName, Slack, Specialty, CohortId)
VALUES ('Sage', 'Klein', '@fallens0ldier', 'figma', 3);

INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (1, 1);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (2, 1);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (3, 2);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (4, 2);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (5, 3);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (1, 3);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (2, 4);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (3, 4);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (4, 5);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (5, 5);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (1, 6);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (2, 6);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (3, 7);
INSERT INTO StudentExercises (ExerciseId, StudentId)
VALUES (4, 7);

