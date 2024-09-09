-- This script lists cities and states from the imported database
-- This statement select the name of states and cities in ascending order
SELECT cities.id, cities.name, states.name
FROM cities, states WHERE cities.state_id = states.id ORDER BY cities.id ASC; 
