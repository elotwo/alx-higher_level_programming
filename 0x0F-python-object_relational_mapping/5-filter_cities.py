#!/usr/bin/python3
import sys
import MySQLdb

def list(mysql_username, mysql_password, database_name, state_name):
    db =  MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            database=database_name
            )
    mycursor = db.cursor()
    sql = "SELECT cities.name FROM cities JOIN cities.state_id = states.id WHERE states.name = '%s'"
    mycursor.execute(sql, (state_name,))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    mycursor.close()
    db.close()

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('argument is not complete')
        sys.exit(1)
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]
        list(mysql_username, mysql_password, database_name, state_name)
