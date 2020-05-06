''' Страница упражнения - 255 '''

# 1
import csv
import sqlite3

import redis as redis
import sqlalchemy as sqlalchemy

test1 = 'This is a test of the emergency text system'

with open('chapter_8/test.txt', 'wt') as wfile:
    wfile.write(test1)

# 2
with open('chapter_8/test.txt', 'rt') as rfile:
    test2 = rfile.read()

print(test1 == test2)

# 3
# books.csv

# 4
print()
with open('chapter_8/books.csv', 'rt') as rfile:
    books = csv.DictReader(rfile)

    for book in books:
        print(book)

# 5
# books1.csv

# 6
conn = sqlite3.connect('chapter_8/books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
    (title VARCHAR(255),
     author VARCHAR(255),
     year INT)''')

# 7
ins = 'INSERT INTO books VALUES(?, ?, ?)'
with open('chapter_8/books1.csv', 'rt') as rfile:
    books = csv.DictReader(rfile)

    for book in books:
        curs.execute(ins, (book['title'], book['author'], book['year']))

# 8
print()
curs.execute('SELECT title FROM books ORDER BY title')
for title in curs.fetchall():
    print(title[0])

# 9
print()
curs.execute('SELECT * FROM books ORDER BY year')
for book in curs.fetchall():
    print(book)

curs.close()
conn.close()

# 10
print()
conn = sqlalchemy.create_engine('sqlite:///chapter_8/books.db')
rows = conn.execute('SELECT title FROM books ORDER BY title')

for title in rows:
    print(title[0])

# 11
print()
conn = redis.Redis()
conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
conn.hgetall('test')

# 12
conn.hset('test', 'count', 25)
conn.hget('test', 'count')

