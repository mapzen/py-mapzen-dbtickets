# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import sys
import random
import mysql.connector

# https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/

class dbtickets:

    def __init__(self, *hosts):

        conns = []

        for cfg in hosts:
            conn = self.connect(**cfg)
            conns.append(conn)

        self.conns = conns

    def connect(self, **cfg):

        conn = mysql.connector.connect(**cfg)
        return conn

    def connection(self):

        if len(self.conns) > 1:
            random.shuffle(self.conns)

        return self.conns[0]

    def generate_id(self):

        conn = self.connection()
        curs = conn.cursor()

        sql = "REPLACE INTO Tickets64 (stub) VALUES (%s)"
        params = ('a',)

        try:
            curs.execute(sql, params)
            conn.commit()
        except Exception, e:
            conn.rollback()
            logging.error(e)
            raise Exception, e

        try:
            sql = "SELECT LAST_INSERT_ID()"
            curs.execute(sql)
            
            row = curs.fetchone()
        except Exception, e:
            logging.error(e)
            raise Exception, e

        return row[0]

if __name__ == '__main__':

    cfgs = [
        {'user':'dbtickets', 'password':'PASSWORD', 'host':'HOST', 'database':'dbtickets'}
    ]

    t = dbtickets(*cfgs)
    print t.generate_id()
