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
    sql = ("""SELECT * FROM states WHERE BINARY name='{}' ORDER BY states.id
    ASC""".format(sys.argv[4]))
    '''
    sql variable
    '''
    mycursor.execute(sql)
    '''
    execute sql code
    '''
    myresult = mycursor.fetchall()
    '''
    fetching the results
    '''
    for x in myresult:
        print(x)

    '''
    traversal
    '''
