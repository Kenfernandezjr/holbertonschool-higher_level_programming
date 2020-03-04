-- lists all the cities of California that can be found
SELECT id, name FROM cities
WHERE state_id=(
SELECT id, name FROM states
WHERE 'California' )
ORDER BY cities.id ASC;
