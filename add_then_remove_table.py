#!/usr/bin/python
# -*- coding: utf-8 -*-

#this is mostly for testing DB wrapper's functionality
from DBWrapper import DBWrapper

"""
def create_table(table_name, values_tuple):
    return "CREATE TABLE " + table_name + " " str("(id INT PRIMARY KEY, origin VARCHAR(20), cellphone_volume INT, cellphone_status VARCHAR(20))"
}

def insert_into(table_name, values_tuple):
    return
"""


connector       = DBWrapper
connector.db    = 'cellphonedb'
connector.user  = 'jasonlouis'




@connector.decorate
def add_then_remove():
    cur.execute("CREATE TABLE  trial_table (id INT PRIMARY KEY, origin VARCHAR(20), cellphone_volume INT, cellphone_status VARCHAR(20))")
    cur.execute("INSERT INTO trial_table VALUES(1,'machine1', 300    , 'online'  )")
    cur.execute("INSERT INTO trial_table VALUES(2,'machine1', 1400   , 'store'   )")

add_then_remove()




