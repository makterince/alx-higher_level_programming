#!/usr/bin/python3
""" gets user input"""
import MySQLdb
import sys


mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                     passwd=mysql_password, db=database_name)

cursor = db.cursor()
query = "SELECT * FROM states WHERE name = '{}'
ORDER BY id ASC".format(state_name)
cursor.execute(query)
rows = cursor.fetchall()
if rows:
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))
    else:
        print("No results found.")

    cursor.close()
    db.close()
