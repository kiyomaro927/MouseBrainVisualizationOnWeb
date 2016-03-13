#!/usr/bin/env python
import csv
import sqlite3

conn = sqlite3.connect('cells.db')

csvReader = csv.reader(open('seeds/cells.csv', 'rb'))

sql = u"insert into cells values (?, ?, ?, ?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2], row[3], row[4], row[5]))
    except:
        pass

conn.commit()

conn.close()
