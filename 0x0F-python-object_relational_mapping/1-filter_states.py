#!/usr/bin/python3
""" scripts lists all states starting from N"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT * FROM states WHERE name
                 LIKE BINARY 'N%' ORDER BY states.id""")
    rows = curs.fetchall()
    for state in rows:
        print(state)
    curs.close()
    db.close()
