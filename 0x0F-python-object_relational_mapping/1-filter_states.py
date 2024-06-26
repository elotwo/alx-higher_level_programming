#!/usr/bin/env python3
import sys
import MySQLdb
def list_state (mysql_username, mysql_password, database_name):
    db = MySQLdb.connect(
            host = "localhost",
            port=3306,
            user = "root",
            password = "88888-Fg",
            database = "hbtn_0e_0_usa"
            )
    cursor = db.cursor();
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC");
    myresult = cursor.fetchall()
    for x in myresult:
        print(x);
    cursor.close()
    db.close()
if __name__ == '__main__':
    list_state ('mysql_username', 'mysql_password', 'database_name')
     
