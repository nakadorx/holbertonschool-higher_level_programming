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
    cur.execute("SELECT *\
                FROM states\
                WHERE name = %(searched_name)s\
                ORDER BY id ASC",
                {'searched_name': sys.argv[4]}
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    mainx()
