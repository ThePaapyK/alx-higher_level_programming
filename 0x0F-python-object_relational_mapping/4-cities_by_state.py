#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa
Takes should take 3 arguments: mysql username, mysql password
and database name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM `cities` \
                INNER JOIN `states` \
                ON cities.state_id = states.id \
                ORDER BY cities.`state_id` ASC")
    allcities = cur.fetchall()

    for city in allcities:
        print(city)

    cur.close()
    db.close()
