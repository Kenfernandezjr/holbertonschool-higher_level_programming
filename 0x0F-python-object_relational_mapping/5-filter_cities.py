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
    mycursor.execute(
        """SELECT cities.name, states.name
        FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name like '{}'
        ORDER BY cities.id ASC""".format(sys.argv[4]))

    '''
    execute sql code
    '''
    myresult = mycursor.fetchall()
    '''
    fetching the results
    '''
    print(", ".join(row[0] for row in myresult))
    '''
    traversal
    '''
