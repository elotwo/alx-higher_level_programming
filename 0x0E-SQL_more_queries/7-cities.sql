-- This script create a database and table even if they exists
-- Tis statament check if the database exits if yes drop
DROP DATABASE IF EXISTS hbtn_0d_usa;
-- This statement create the database 
CREATE DATABASE hbtn_0d_usa;
-- This statement uses the database created
USE hbtn_0d_usa;
-- This statement check if the table exist, if yes drop
DROP TABLE IF EXISTS cities;
-- this statement create the table cities
CREATE TABLE cities
(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
UNIQUE (id),
FOREIGN KEY (state_id) REFERENCES states(id)
);
