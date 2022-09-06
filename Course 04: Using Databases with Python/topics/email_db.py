import sqlite3
import os

connection = sqlite3.connect("emaildb.sqlite")
cursor = connection.cursor()

cursor.execute('''
DROP TABLE IF EXISTS COUNTS
''')
cursor.execute('''
CREATE TABLE COUNTS (email TEXT, count INTEGER)
''')

file_name = input("Enter file name: ")
file_path = os.getcwd() + "/code3/" + 'mbox.txt'
file_handle = open(file_path)

for line in file_handle :
  if not line.startswith("From: ") : continue
  substring = line.split()
  email = substring[1]
  cursor.execute('SELECT count FROM COUNTS WHERE email = ?', (email,))
  row = cursor.fetchone()
  if row is None  :
    cursor.execute('''
    INSERT INTO COUNTS (email, count) VALUES (?, 1)               
    ''', (email,))
  else :
    cursor.execute('''
    UPDATE COUNTS SET count = count + 1 WHERE email = ?                     
    ''', (email,))
    
  connection.commit()

sql_get_top_ten_emails = "SELECT email, count FROM COUNTS ORDER BY count DESC LIMIT 10"

for row in cursor.execute(sql_get_top_ten_emails) :
  print(str(row[0]), row[1])

cursor.close()
  