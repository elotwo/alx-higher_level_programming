#!/usr/bin/python3
"""
this  module is listing states
its take three arguiment mostly mysql_username, mysql_password, database_name
and select where a name in particular is

"""
import sys
import MySQLdb


def list_state(mysql_username, mysql_password, database_name):
    """
    list all state with a spsecific name
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            database=database_name
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage:./2-my_filter_states.py <mysql_username> <database_name>")
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    list_state(mysql_username, mysql_password, database_name)
