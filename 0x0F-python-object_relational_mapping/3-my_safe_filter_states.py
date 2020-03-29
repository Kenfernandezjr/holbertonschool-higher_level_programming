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
    platform = sys.argv[4]
    '''
    sql variable
    '''
    mycursor.execute("""SELECT * FROM states WHERE BINARY name = %s ORDER BY
    states.id ASC""", (platform,))
    '''
    execute sql code
    '''
    myresult = mycursor.fetchall()
    '''
    fetching the results
    '''
    for x in myresult:
        print(x)

    mydb.close()

    '''
    traversal
    '''
