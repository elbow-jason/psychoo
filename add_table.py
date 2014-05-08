#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:
     
    con = psycopg2.connect(database='cellphonedb', user='jasonlouis')    
    
    cur = con.cursor()
  
    cur.execute("CREATE TABLE cellphones(id INT PRIMARY KEY, origin VARCHAR(20), cellphone_volume INT, cellphone_status VARCHAR(20))")
    cur.execute("INSERT INTO cellphones VALUES(1,'machine1', 300    , 'online'  )")
    cur.execute("INSERT INTO cellphones VALUES(2,'machine1', 1400   , 'store'   )")
    cur.execute("INSERT INTO cellphones VALUES(3,'machine2', 301    , 'both'    )")
    cur.execute("INSERT INTO cellphones VALUES(4,'machine3', 340    , 'online'  )")
    cur.execute("INSERT INTO cellphones VALUES(5,'machine4', 350    , 'both'    )")
    cur.execute("INSERT INTO cellphones VALUES(6,'machine5', 210    , 'store'   )")
    cur.execute("INSERT INTO cellphones VALUES(7,'machine1', 414    , 'both'    )")
    cur.execute("INSERT INTO cellphones VALUES(8,'machine3', 216    , 'both'    )")
    con.commit()

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()