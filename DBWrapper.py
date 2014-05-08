#!/usr/bin/python
# -*- coding: utf-8 -*-

#error handling
import psycopg2
import sys,traceback

"""


"""



#wrapper should have all the components necessary for connecting
#to a database given a 
class DBWrapper():
    """docstring for DBWrapper

    DBWrapper is used thusly:



    connector = DBWrapper
    connector.db    = 'fubberDB'
    connector.user  = 'user1'
    @connector
    def some_psycopg2_commands(con, cur):
    foobar_tuple = ((1, 'baaar'), (2, 'foooo'))
    query = "INSERT INTO foo (id, bar) VALUES (%s, %s)"





    the previous block of code would insert the values of 'foobar_tuple' into
    the 'fubberDB' database on table 'foo'. 
    Note: in the 'some_psycopg2_commands' function there is no need to create
    a connection. The wrapper executes connection (psycopg2., commision (con.commit), """
    def __init__(self):
        super(DBWrapper, self).__init__()
        self.db     = ''
        self.user   = ''
        # no password should be stored here due to scope-vulnerability
        
        #initialize the DB wrapper with a db and username
    

    def decorate(self, function):
        def connect_and_commit(*args, **kwargs):

            con = None

            try:
                con = psycopg2.connect(database=self.db, user=self.user)
                cur = con.cursor()

                #call the function
                function(con, cur, *args, **kwargs)
                con.commit()

            except psycopg2.DatabaseError, e:

                # should an exception occur during the try, any changes to the DB
                # are rolled back.
                if con:
                    con.rollback()
                # error is logged to console, and python is exited.
                print 'Error %s' % e
                sys.exit(1)
                
                
            finally:
                
                #close connection to db if necessary
                #(might remove .close() later if presistent connection is necessary)
                print "executed {} successfully...".format( function.__name__ )
                if con:
                    con.close()
                    print "connection to {} closed successfully...".format( self.db )
        return connect_and_commit


if __name__ == "__main__":
    DBWrapper()
