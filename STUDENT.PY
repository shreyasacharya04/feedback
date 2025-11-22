import sqlite3

connection = sqlite3.connect('STUDENT.db')
cursor = connection.cursor()

cmd = """
    CREATE TABLE IF NOT EXISTS STUDENT(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        usn varchar(10) NOT NULL,
        sem number(10) NOT NULL,
        cgpa number(5) NOT NULL,
        gender TEXT NOT NULL
    );
"""

cursor.execute(cmd)
connection.commit()

cmd = """
    INSERT INTO STUDENT (fullname, usn, sem, cgpa, gender)
    VALUES (?, ?, ?, ?, ?);
"""

cursor.execute(cmd, ('Shreyas Acharya', '4MW23AD047', '5',
               '8', 'Male'))

connection.commit()


f = cursor.execute("SELECT * FROM STUDENT;").fetchall()
print(f)

connection.close()