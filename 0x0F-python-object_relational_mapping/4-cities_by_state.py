#!/usr/bin/python3
"""
accepts 3 arguments (mysql username, password and database name)
and lists all cities from that database
"""
import sys
import MySQLdb




if __name__ == '__main__':
    if len(sys.argv) == 4:
    """connects to a given mysql database and lists all 'cities' from it"""
		con = MySQLdb.connect(host="localhost", port=3306,
							user=argv[1], passwd=argv[2], db=argv[3])
		cur = con.cursor()
		cur.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states\
					ON cities.state_id = states.id ORDER BY cities.id ASC")
		query_rows = cur.fetchall()
		for row in query_rows:
			print(row)
		cur.close()
		con.close()

