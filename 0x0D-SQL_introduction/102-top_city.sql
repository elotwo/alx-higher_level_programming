USE hbtn_0c_0;
SELECT city, month, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
