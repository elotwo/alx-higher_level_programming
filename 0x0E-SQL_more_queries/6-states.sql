-- This script create databse and uses it 
-- This statesment check if database exists
DROP DATABASE IF EXISTS hbtn_0d_usa;
-- This statements create databse 
CREATE DATABASE hbtn_0d_usa;
-- This statement uses the databsase
USE hbtn_0d_usa;
-- This statement check if the exists so as drop it
DROP TABLE IF EXISTS states;
-- This statement create  table
CREATE TABLE states
(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(256) NOT NULL,
UNIQUE (id)
);
