# python과 mysql을 이용한 crud 연습문제
# 테이블: emp, dept
# emp(empno, ename, salary, deptno)
# dept(deptno, dname, location)
# 클래스: Emp, Dept
# 모듈: emp.py, dept.py, empio.py, main.py
# 프로그램이 시작되면 아래와 같은 메뉴가 표시된다.
# 리스트(s), 추가(a), 변경(u), 검색(f), 삭제(d), 종료(x)

import pymysql
import sys

try:
    conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                         db='test', charset='utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    #### 테이블 생성 ####
    sql = 'create table dept(deptno decimal primary key, dname varchar(20), location varchar(20))'
    curs.execute(sql)


    rows = curs.fetchall()
    print(rows)
except pymysql.MySQLError as e:
    print(e)
    sys.exit()
finally:
    conn.close()