import sys
import pymysql

class Emp():

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
'''
    def showTable(self, conn, curs):
        try:
            curs.execute('select * from emp')
            rows = curs.fetchall()
            for r in rows:
                print(r)
        except pymysql.MySQLError as e:
            print(e)
            sys.exit()
        finally:
            conn.close()
'''