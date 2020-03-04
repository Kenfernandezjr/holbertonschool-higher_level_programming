-- lists all the cities of California that can be found
SELECT id FROM cities
WHERE id=(
SELECT id FROM states
WHERE 'California' )
ORDER BY cities.id ASC;
