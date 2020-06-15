import sys
import pymysql
from emp import Emp
from dept import Dept

def inputstring():
    string = input('사원번호 사원명 연봉 부서번호: ')
    return string

# 사용자가 입력한 string형태의 정보 쪼개서 dictionary로 만들기
def string2dic(string):
    info = string.split()
    infodic = {}
    infodic['empno'] = int(info[0])
    infodic['ename'] = info[1]
    infodic['salary'] = int(info[2])
    infodic['deptno'] = int(info[3])
    return infodic

# 테이블 데이터 입력(a)
def insertData():
    string = inputstring()
    infodic = string2dic(string)
    a = Emp()
    try:
        sql = 'insert into emp (empno, ename, salary, deptno) values(%s, %s, %s, %s);'
        a.curs.execute(sql, (infodic['empno'], infodic['ename'], infodic['salary'], infodic['deptno']))
        a.conn.commit()
        print('입력이 완료되었습니다.')
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        a.conn.close()

# 테이블을 python에서 조회하기 쉬운 튜플 형태로 저장하기
def table2tuple():
    a = Emp()
    b = Dept()
    try:
        sql = 'select * from emp'
        a.curs.execute(sql)
        rows = a.curs.fetchall()
        return rows
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        a.conn.close()
'''
# join 테이블 저장하기
def jointable2tuple():
    a = Emp()
    try:
        sql = 'select * from emp natural join dept;'
        a.curs.execute(sql)
        rows = a.curs.fetchall()
        return(rows)
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        a.conn.close()
'''
# join 테이블 출력하기(s)
def showJointable():
    a = Emp()
    try:
        sql = 'select * from emp natural join dept;'
        a.curs.execute(sql)
        rows = a.curs.fetchall()
        for r in rows:
            print(r)
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        a.conn.close()

# 테이블 데이터 수정(u)
def updateData():
    string = input('수정할 사원번호 사원명 연봉 부서번호: ')
    infodic = string2dic(string) # dictionary
    rows = table2tuple() # tuple
    a = Emp()
    try:
        for r in rows:
            if r['empno'] == infodic['empno']:
                sql = 'update emp set ename = %s, salary = %s, deptno = %s where empno = %s'
                a.curs.execute(sql, (infodic['ename'], infodic['salary'], infodic['deptno'], infodic['empno']))
                a.conn.commit()
                print('수정이 완료되었습니다.')
                break
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        a.conn.close()

# 테이블 데이터 삭제(d)
def deleteData():
    num = int(input('삭제할 사원번호: '))
    rows = table2tuple()
    a = Emp()
    try:
        for r in rows:
            if r['empno'] == num:
                sql = 'delete from emp where empno = %s'
                a.curs.execute(sql, num)
                a.conn.commit()
                print('삭제가 완료되었습니다.')
                break
    except pymysql.MySQLError as e:
        print(e)
        sys.exxit()
    finally:
        a.conn.close()


#### 아래의 sql작성문 부분만 따로 method로 만들어 보기 #####

# 테이블 데이터 검색(f)
def searchData():
    select = input('사원번호(en), 사원명(n), 연봉(s), 부서번호(dn): ')
    rows = table2tuple()
    a = Emp()
    try:
        if select == 'en':
            data = input('검색할 사원번호: ')
            for r in rows:
                if r['empno'] == int(data):
                    sql = 'select * from emp where empno = %s'
                    a.curs.execute(sql, data)
                    res = a.curs.fetchall()
                    print(res)
                    break
        elif select == 'n':
            data = input('검색할 사원명: ')
            for r in rows:
                if r['ename'] == data:
                    sql = 'select * from emp where ename = %s'
                    a.curs.execute(sql, data)
                    res = a.curs.fetchall()
                    print(res)
                    break
        elif select == 's':
            data = input('검색할 연봉: ')
            for r in rows:
                if r['salary'] == int(data):
                    sql = 'select * from emp where salary = %s'
                    a.curs.execute(sql, data)
                    res = a.curs.fetchall()
                    print(res)
                    break
        elif select == 'dn':
            data = input('검색할 부서번호: ')
            for r in rows:
                if r['deptno'] == int(data):
                    sql = 'select * from emp where deptno = %s'
                    a.curs.execute(sql, data)
                    res = a.curs.fetchall()
                    print(res)
                    break
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        a.conn.close()