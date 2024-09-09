-- This script is about creating a table
-- This statement checks if the table exists so as to drop it
DROP TABLE IF EXISTS force_name;
-- This statement is about crating a table 
CREATE TABLE force_name
(
-- This statement is about creating colum id
id INT NOT NULL,
-- This statement is about creating colum name
name VARCHAR(256) NOT NULL
);
