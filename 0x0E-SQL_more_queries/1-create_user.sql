-- This script create and grants all privileges to user user_0d_1
-- This line of code drop user user_0d_1 if its exits
DROP USER IF EXISTS 'user_0d_1'@'localhost';
-- This script craate user  user_0d_1 and password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- This code grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
