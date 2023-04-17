#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name)
    
    # Create cursor object to execute queries
    cursor = db.cursor()
    
    # Define query
    query = "SELECT * FROM states"
    
    # Execute query
    cursor.execute(query)
    
    # Retrieve results
    results = cursor.fetchall()
    
    # Display results
    for row in results:
        print(row)

    # Close cursor and database connections
    cursor.close()
    db.close()
