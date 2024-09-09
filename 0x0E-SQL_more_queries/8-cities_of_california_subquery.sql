-- This script display name of states and cities
-- This statesments select the name of cities nad states from database
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
