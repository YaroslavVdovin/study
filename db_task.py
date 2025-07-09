import sqlite3

conn = sqlite3.connect('db_stud.sqlite')

students = [
    (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manchester'),
    (4, 'Kate', 'Brooks', 34, 'Spb')
]

courses = [
    (1, 'python', '21.07.21', '21.08.21'),
    (2, 'java', '13.07.21', '16.08.21')
]

student_courses = [(1, 1),
                   (2, 1),
                   (3, 1),
                   (4, 2)
]
cursor = conn.cursor()

cursor.execute("CREATE TABLE Students (id int, name Varchar(50), surname Varchar(50), age int, city Varchar(50))")

cursor.execute("CREATE TABLE Courses (id int, name Varchar(50), time_start text, time_end text)")

cursor.execute("CREATE TABLE Student_courses (student_id int, course_id int)")

cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", students)

cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", courses)

cursor.executemany("INSERT INTO Student_courses VALUES (?, ?)", student_courses)

conn.commit()

cursor.execute("SELECT * FROM Students WHERE age > 30")

print(cursor.fetchall())

cursor.execute("SELECT id, name, surname, age, city FROM (SELECT * FROM Students INNER JOIN student_courses ON Students.id = Student_courses.student_id INNER JOIN Courses ON Student_courses.course_id = Courses.id AND Courses.name = 'python')")

print(cursor.fetchall())

cursor.execute("SELECT id, name, surname, age, city FROM (SELECT * FROM (SELECT * FROM Students WHERE city = 'Spb') as Students INNER JOIN student_courses ON Students.id = Student_courses.student_id INNER JOIN Courses ON Student_courses.course_id = Courses.id AND Courses.name = 'python')")

print(cursor.fetchall())

conn.close()