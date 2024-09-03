-- This script create both user and database
-- this statement check if a user user_0d_2 so as to drop user
DROP USER IF EXISTS 'user_0d_2'@'localhost';
-- This statement create the user user_0d_2
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- This statement grant all privileges to the user user_0d_2
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
-- This stetement check if this database exists so as to drop them
DROP DATABASE IF EXISTS hbtn_0d_2;
-- This statement create a database hbtn_0d_2
CREATE DATABASE hbtn_0d_2;
-- This grant the privilege of select to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
