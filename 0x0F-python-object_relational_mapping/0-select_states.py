#!/usr/bin/python3
"""
connetion
"""
import sys
import MySQLdb


if __name__ == '__main__':
	if len(sys.argv) == 4:
    """con"""
		con = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
		cur = con.cursor()
		cur.execute("SELECT * FROM states ORDER BY id ASC")
		query_rows = cur.fetchall()
		for row in query_rows:
			print(row)
		cur.close()
		conn.close()
