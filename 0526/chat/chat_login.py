import pymysql


def conn_mysql():
    try:
        conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        print('MySQL DB 접속 성공 !!!')
        return conn, curs
    except pymysql.MySQLError as e:
        print(e)
        return None


def authenticate(uid, pwd):
    (conn, curs) = conn_mysql()
    sql = 'select * from login where uid=%s and pwd=%s'
    curs.execute(sql, (uid, pwd))
    rows = curs.fetchall()
    conn.close()
    if len(rows) != 0:
        return True
    else:
        return False