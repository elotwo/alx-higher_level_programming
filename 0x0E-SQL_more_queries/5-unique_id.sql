-- This script create table
-- This statement checks if a table exists so as to drop them
DROP TABLE IF EXISTS unique_id;
-- This statement create a teble
CREATE TABLE unique_id
(
-- This statement set a colum id with a defualt value
id INT default 1,
-- This statement set a colum name
name VARCHAR(256),
UNIQUE (id)
);
