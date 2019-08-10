#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa that start with N
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    conect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[1][0] == "N":
            print(row)
    cursor.close()
    conect.close()
