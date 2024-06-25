#!/usr/bin/env python3
import sys
import MySQLdb
db = MySQLdb.connect(
        host = "localhost",
        user = "root",
        password = "88888-Fg",
        database = "hbtn_0e_0_usa"
        )
cursor = db.cursor();
cursor.execute("SELECT id, name FROM states ORDER BY id ASC");
myresult = cursor.fetchall()
for x in myresult:
    print(x);
     
