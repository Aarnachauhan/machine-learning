import sqlite3

connection=sqlite3.connect('example.db')
connection
o/p
<sqlite3.Connection at 0x2443895db70>

  //example.db file will be created on it own
---------------------------------------------------
  #create a table
cursor.execute(
    '''
create table if not exists employees(
     id Integer Primary Key,
     name Text Not Null,
     age Integer,
     department Text
)
'''
)

connection.commit()
----------------------------------------------
#select
cursor.execute(
    '''
Select * from employees
'''
)
o/p
<sqlite3.Cursor at 0x24438c5f440>
  we are getting something
-----------------------------------------------
#insert data in sqlite3
cursor.execute('''
Insert into employees(name,age,department) values ('aarna',21,'cse')
''')
connection.commit()
--------------------------------------------------
query the data
cursor.execute('''
Insert into employees(name,age,department) values ('haritha',21,'cse')
''')
cursor.execute('''
Insert into employees(name,age,department) values ('shreya',21,'cse')
''')
connection.commit()
----------------------------------------------------------------
cursor.execute('select * from employees')
rows=cursor.fetchall()
for row in rows:
    print(row)

o/p
(1, 'aarna', 21, 'cse')
(2, 'aarna', 21, 'cse')
(3, 'haritha', 21, 'cse')
(4, 'shreya', 21, 'cse')

---------------------------------------------------------------
#update
cursor.execute('''
Update employees
               set age=20 where name='aarna'
               

''')
connection.commit()

cursor.execute('select * from employees')
rows=cursor.fetchall()
for row in rows:
    print(row)

o/p-
(1, 'aarna', 20, 'cse')
(2, 'aarna', 20, 'cse')
(3, 'haritha', 21, 'cse')
(4, 'shreya', 21, 'cse')

------------------------------------------------------------
#delete
cursor.execute('''
Delete from employees
               where name='shreya'

''')
connection.commit()
cursor.execute('select * from employees')
rows=cursor.fetchall()
for row in rows:
    print(row)
o/p
(1, 'aarna', 20, 'cse')
(2, 'aarna', 20, 'cse')
(3, 'haritha', 21, 'cse')

-------------------------------------------------------
bulk insertion - executemany
