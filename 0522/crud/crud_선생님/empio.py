from emp import Emp
from dept import Dept
import sys
import pymysql

def conn_mysql():
    try:
        conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        print('MySQL DB에 접속 성공 !!')
        return conn, curs
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
        return None



def insert_emp(emp):
    (conn, curs) = conn_mysql()
    sql = 'insert into emp values(%s, %s, %s, %s)'
    n = curs.execute(sql, (emp.empno, emp.ename, emp.salary, emp.deptno))
    if n == 1: # 작업에 성공했다면
        print('사원정보 추가 성공!!!')
        conn.commit()
    else:
        print('저장 오류')
    conn.close()

def insert_dept(dept):
    (conn, curs) = conn_mysql()
    sql = 'insert into dept values(%s, %s, %s, %s)'
    n = curs.execute(sql, (dept.deptno, dept.dname, dept.location))
    if n == 1: # 작업에 성공했다면
        print('부서정보 추가 성공!!!')
        conn.commit()
    else:
        print('저장 오류')
    conn.close()

def get_list():
    (conn, curs) = conn_mysql()
    sql = 'select * from emp'
    n = curs.execute(sql)
    tp = curs.fetchall()
    conn.close()
    if tp:
        return [Emp(d['empno'], d['ename'], d['salary'], d['deptno']) for d in tp]
    else:
        return None

def update_emp(emp):
    (conn, curs) = conn_mysql()
    sql = 'update emp set salary = %s where empno = %s'
    n = curs.execute(sql, (emp.salary, emp.empno))
    if n == 1:
        print('사원정보 변경 성공!!!')
        conn.commit()
    else:
        print('변경 오류')
    conn.close()

def delete_emp(empno):
    (conn, curs) = conn_mysql()
    sql = 'delete from emp where empno = %s'
    n = curs.execute(sql, empno)
    if n == 1:
        print('사원정보 삭제 성공!!!')
        conn.commit()
    else:
        print('삭제 오류')
    conn.close()

# Transaction: 다수개의 SQL 명령을 한 작업단위로 묶어서 한번에 실행 or 취소
def delete_dept(deptno): # 단계적 삭제, 두 문장을 하나의 transaction으로 실행
    (conn, curs) = conn_mysql()
    try:
        sql1 = 'delete from emp where deptno = %s' # 자식 테이블
        curs.execute(sql1, deptno)
        sql2 = 'delete from dept where deptno = %s' # 부모 테이블
        curs.execute(sql2, deptno)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()