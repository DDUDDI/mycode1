import sys
import pymysql

class Dept():

    def __init__(self, deptno, dname, location):
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        self.deptno = deptno
        self.dname = dname
        self.location = location