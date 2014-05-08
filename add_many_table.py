#!/usr/bin/python
# -*- coding: utf-8 -*-

#uses INSERT INTO to append to table


import psycopg2
import sys

phones = (
    ( 9, 'machine1',    526, 'online'),
    (10, 'machine1',    571, 'online'),
    (11, 'machine2',    900, 'online'),
    (12, 'machine5',    290, 'online'),
    (13, 'machine13',   350, 'both'),
    (14, 'machine14',   210, 'online'),
    (15, 'machine3',    414, 'online'),
    (16, 'machine15',   216, 'online')
)

con = None

try:
     
    con = psycopg2.connect(database='cellphonedb', user='jasonlouis') 
    cur = con.cursor()

    query = "INSERT INTO cellphonedb (id, origin, cellphone_volume, cellphone_status) VALUES (%s, %s, %s, %s)"
    cur.executemany(query, phones)
    con.commit()


# error handling 
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()