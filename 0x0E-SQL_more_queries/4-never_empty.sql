-- This script create table
-- This statement checks if a table exists so as to drop them
DROP TABLE IF EXISTS id_not_null;
-- This statement create a teble
CREATE TABLE id_not_null
(
-- This statement set a colum id with a defualt value
id INT default 1,
-- This statement set a colum name
name VARCHAR(256)
);
