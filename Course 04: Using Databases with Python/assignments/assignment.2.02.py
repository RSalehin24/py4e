import sqlite3
import os

file_path = os.getcwd() + "/code3/mbox.txt"
file_handle = open(file_path) 

connection = sqlite3.connect('assignment_4_02_01_db.sqlite')
cursor = connection.cursor()

cursor.execute('''
DROP TABLE IF EXISTS Counts            
''')

cursor.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)               
''')

for line in file_handle:
  if not line.startswith("From: "): continue
  email = line.split()[1]
  organization = email.split('@')[1]
  cursor.execute('''
  SELECT * FROM Counts WHERE org=?
  ''', (organization,))
  row = cursor.fetchone()
  if row is None:
    cursor.execute('''
    INSERT INTO Counts (org, count) VALUES (?, 1) 
    ''', (organization,))
  else:
    cursor.execute('''
    UPDATE Counts SET count = count + 1 WHERE org = ? 
    ''', (organization,))

connection.commit()

get_top_ten_organizations = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(get_top_ten_organizations):
  print(str(row[0]), row[1])

cursor.close()
  