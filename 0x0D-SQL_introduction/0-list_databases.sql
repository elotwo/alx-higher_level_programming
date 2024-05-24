#!/bin/bash

# Variables
MYSQL_USER = "Emma"
MYSQL_PASSWORD ="88888"
MYSQL_HOST = "localhost"

# Connect to MySQL and list databases
mysql -u $MYSQL_USER -p $MYSQL_PASSWORD -h$MYSQL_HOST -e "SHOW DATABASES;"

