import sqlite3

connection = sqlite3.connect('itstep_DB.sl3', 5)
cur = connection.cursor()
cur.execute("SELECT rowid, name FROM first_table (name) VALUES ('Demasik');")
connection.commit()
connection.close()