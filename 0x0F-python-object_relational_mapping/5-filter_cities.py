#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Takes should take 4 arguments: mysql username, mysql password,
database name and state name
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

    print(", ".join(city[1] for city in allcities if city[2] == sys.argv[4]))

    cur.close()
    db.close()
