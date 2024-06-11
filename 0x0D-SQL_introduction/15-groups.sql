-- This script is about counting the number of score of the same value
SELECT score, COUNT(*) AS count FROM second_table GROUP BY score;
