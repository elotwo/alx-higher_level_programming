#!/usr/bin/env python3
import sys
import MySQLdb
def list_state (mysql_username='root', mysql_password='88888-Fg', database_name='hbtn_0e_0_usa'):
    db = MySQLdb.connect(
            host = "localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            database=database_name
            )
    cursor = db.cursor();
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC");
    myresult = cursor.fetchall()
    for x in myresult:
        print(x);
    cursor.close()
    db.close()
if __name__ == '__main__':
    list_state ('root', '88888-Fg', 'hbtn_0e_0_usa')
     
