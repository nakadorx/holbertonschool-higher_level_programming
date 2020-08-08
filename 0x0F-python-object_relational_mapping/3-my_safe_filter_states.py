#!/usr/bin/python3
"""
cons
"""
import sys
import MySQLdb


if __name__ == '__main__':
	if len(sys.argv) == 5:
		""" fzerfzer """
		con = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
		cur = con.cursor()
		arg = MySQLdb.escape_string(argv[4]).decode()
		cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'\
					ORDER BY id ASC".format(arg))
		query_rows = cur.fetchall()

		for row in query_rows:
			print(row)
		pass
		cur.close()
		con.close()
