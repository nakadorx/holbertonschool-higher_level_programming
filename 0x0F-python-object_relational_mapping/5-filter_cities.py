#!/usr/bin/python3
"""
 con
"""
import MySQLdb
import sys


def mainx():
    """con"""

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %(state_name)s\
                ORDER BY cities.id ASC",
                {'state_name': sys.argv[4]}
                )
    rows = cur.fetchall()
    lst = []
    for row in rows:
        for col in row:
            lst.append(col)
    print(', '.join(lst))
    cur.close()
    db.close()


if __name__ == "__main__":
    mainx()
