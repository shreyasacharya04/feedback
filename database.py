import sqlite3

connection = sqlite3.connect('feedback.db')
cursor = connection.cursor()

cmd = """
    CREATE TABLE IF NOT EXISTS FEEDBACK (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        usn varchar(10) NOT NULL,
        contact number(10) NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    );
"""

cursor.execute(cmd)
connection.commit()

cmd = """
    INSERT INTO FEEDBACK (fullname, usn, contact, email, message)
    VALUES (?, ?, ?, ?, ?);
"""
'''cursor.execute(cmd, ('Mithul Byndoor', '4MW23AD021', '9108864556',
               'mithul.23ad021@sode-edu.in', 'Great course!'))
connection.commit()'''

cursor.execute(cmd, ('Shreyas Acharya', '4MW23AD047', '9101234567',
               'shreyas.23ad047@sode-edu.in', 'Im a living legend!'))

connection.commit()


f = cursor.execute("SELECT * FROM feedback;").fetchall()
print(f)

connection.close()