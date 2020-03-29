#!/usr/bin/python3
'''
show created table using python
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
    sql = "SELECT * FROM states ORDER BY states.id ASC"
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
