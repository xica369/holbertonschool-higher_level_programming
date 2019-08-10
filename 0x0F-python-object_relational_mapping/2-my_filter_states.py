#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa that start with N
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    conect = MySQLdb.connect(host="localhost", port=3306,
                             user="{}".format(argv[1]),
                             passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conect.cursor()
    cursor.execute("""SELECT *
    FROM states
    WHERE name = "{}"
    ORDER BY id ASC""".format(argv[4]))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print("{}".format(row))
    cursor.close()
    conect.close()
