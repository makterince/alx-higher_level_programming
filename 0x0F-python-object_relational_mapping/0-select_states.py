#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    
    curs = db.cursor()
    
    query = "SELECT * FROM states"
    
    curs.execute(query)
    
    results = curs.fetchall()
    
    for row in results:
        print(row)

    curs.close()
    db.close()
