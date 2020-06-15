import sys
import pymysql

class Dept():

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)