#!/usr/bin/python3
'''
show created table with states list with n
'''

import MySQLdb
import sys

if __name__ == "__main__":
    '''
    if the main is not being executed
    '''
    mydb = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    '''
    database connection
    '''
    mycursor = mydb.cursor()
    '''
    cursor
    '''
    prime = sys.argv[4]
    '''
    variable for input argument
    '''
    mycursor.execute(
        """SELECT GROUP_CONCAT(DISTINCT cities.name
        ORDER BY cities.id ASC
        SEPARATOR ', ')
        FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name = %s;""", (prime,))

    '''
    execute sql code
    '''
    myresult = mycursor.fetchall()
    '''
    fetching the results
    '''
    for row in myresult:
        print(row[0])

    mydb.close()

    '''
    traversal
    '''
