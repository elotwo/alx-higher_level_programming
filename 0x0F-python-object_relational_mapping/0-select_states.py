#!/usr/bin/python3
"""
this module is abuot listing states in the database hbtn_0e_0_usa

"""
import sys
import MySQLdb


def list_state(mysql_username, mysql_password, database_name):
    """
        Lists all states from the specified database, sorted by states.id in ascending order.
        Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        database_name (str): The name of the database to query.
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            database=database_name
            )
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
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
