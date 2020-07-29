""" import sqlite3 it's a built in database in python
"""
import sqlite3 as sl

# creating a connection object of database

con = sl.connect('sample-database-testing.db')

# let's create a table for experiment

with con:
    con.execute("""
CREATE TABLE EMP (
eid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT,
salary INTEGER);

""")

# let's make some entry to EMP table

sql = 'INSERT INTO EMP (eid, name, salary) values (?, ?, ?)'

sample_data = [
    (1, 'Ishu', 10000),
    (2, 'Jai', 42000),
    (3, 'Marilyn', 25222)
    ]

# use executemany for inserting multiple records to table at once
with con:
    con.executemany(sql,sample_data)
    
    
    
 # let's make some entry to EMP table without primary key as it's autoincrement 

sql = 'INSERT INTO EMP (name, salary) values (?, ?)'

sample_data = [
    ('Ishu', 10000),
    ('Jai', 42000),
    ('Marilyn', 25222)
    ]

with con:
    con.executemany(sql,sample_data)
# select data from database and print them in output

sql = 'SELECT * FROM EMP WHERE eid >5'
with con:
    data = con.execute(sql)

for row in data:
    print(row)
    
