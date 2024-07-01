#!/usr/bin/python3
import sys
import MySQLdb


def list_state(mysql_username, mysql_password, database_name):
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            database=database_name
            )
    cursor = db.cursor()
    cursor.execute(f"SELECT id, name FROM cities ORDER BY id ASC")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./2-my_filter_states.py <mysql_username> .... <state_name_searched>")
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    list_state(mysql_username, mysql_password, database_name)
