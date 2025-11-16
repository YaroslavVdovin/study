import sqlite3

con = sqlite3.connect("database_test.sqlite")
cursor = con.cursor()

cursor.execute("SELECT student_id, course_id FROM StudentCourses;")
print(cursor.fetchall())