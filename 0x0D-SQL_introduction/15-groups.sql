-- return the scores with the matching number
SELECT score , COUNT(*) AS number
FROM second_table
GROUP BY score DESC;
