#!/usr/bin/python3
"""
conenction
"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) == 4:
    """connects """
        con = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
        cur = con.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        pass
        cur.close()
        con.close()

