import sqlite3

conn = sqlite3.connect('softhealth.db')
cursor = conn.cursor()
cursor.execute('''
                SELECT * FROM login
                ''')
result = cursor.fetchall()
print(result)
conn.close()
