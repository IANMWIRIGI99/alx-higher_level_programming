-- Import in hbtn_0c_0 database the temperatures table dump
-- This script displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT city, AVG(value) AS avg_temp FROM temperatures 
GROUP BY city ORDER BY avg_temp DESC;
