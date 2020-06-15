import pymysql
import sys

try:
    conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                         db='test', charset='utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from student where name = %s'
    curs.execute(sql, 'Jihee Kim')
    rows = curs.fetchall()
    print(rows)
except pymysql.MySQLError as e:
    print(e)
    sys.exit()
finally:
    conn.close()
