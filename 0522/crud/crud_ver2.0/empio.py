import sys
import pymysql
from emp import Emp
from dept import Dept

# 사원 정보 입력
def inputstring():
    string = input('사원번호 사원명 연봉 부서번호: ')
    return string

# 사용자가 입력한 정보 dictionary 형태로 저장
def string2dic(string):
    info = string.split()
    infodic = {}
    infodic['empno'] = int(info[0])
    infodic['ename'] = info[1]
    infodic['salary'] = int(info[2])
    infodic['deptno'] = int(info[3])
    # Emp instance 생성
    e = Emp(infodic['empno'], infodic['ename'], infodic['salary'], infodic['deptno'])
    return infodic

# 테이블 데이터 입력(a)
def insertData(string):
    infodic = string2dic(string)
    try:
        conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = 'insert into emp (empno, ename, salary, deptno) values(%s, %s, %s, %s);'
        curs.execute(sql, (infodic['empno'], infodic['ename'], infodic['salary'], infodic['deptno']))
        conn.commit()
        print('입력이 완료되었습니다.')
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        conn.close()

# join 테이블 튜플 형태로 저장하기
def jointable2tuple():
    try:
        conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = 'select * from emp natural join dept;'
        curs.execute(sql)
        rows = curs.fetchall()
        return rows
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        conn.close()

# join 테이블 출력하기(s)
def showJointable(rows):
    print(f'사원번호\t\t사원명\t\t연봉\t\t부서번호\t\t부서명')
    for r in rows:
        line = f"{r['empno']}\t\t\t{r['ename']}\t\t{r['salary']}\t\t{r['deptno']}\t\t{r['dname']}"
        print(line)

# 테이블 데이터 수정(u)
def updateData(rows):
    string = input('수정할 사원번호 사원명 연봉 부서번호: ')
    infodic = string2dic(string) # dictionary
    try:
        conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        for r in rows:
            if r['empno'] == infodic['empno']:
                sql = 'update emp set ename = %s, salary = %s, deptno = %s where empno = %s'
                curs.execute(sql, (infodic['ename'], infodic['salary'], infodic['deptno'], infodic['empno']))
                conn.commit()
                print('수정이 완료되었습니다.')
                break
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        conn.close()

# 테이블 데이터 삭제(d)
def deleteData(rows):
    num = int(input('삭제할 사원번호: '))
    try:
        conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        for r in rows:
            if r['empno'] == num:
                sql = 'delete from emp where empno = %s'
                curs.execute(sql, num)
                conn.commit()
                print('삭제가 완료되었습니다.')
                break
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        conn.close()

# 테이블 데이터 검색(f)
def searchData(rows):
    select = input('사원번호(en), 사원명(n), 연봉(s), 부서번호(dn): ')
    try:
        conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        if select == 'en':
            data = input('검색할 사원번호: ')
            # 아래 코드 줄일 수 있는 방법 생각 해보기 #
            for r in rows:
                if r['empno'] == int(data):
                    sql = 'select * from emp natural join dept where empno = %s'
                    curs.execute(sql, data)
                    rows = curs.fetchall()
                    showJointable(rows)
                    break
        elif select == 'n':
            data = input('검색할 사원명: ')
            for r in rows:
                if r['ename'] == data:
                    sql = 'select * from emp natural join dept where ename = %s'
                    curs.execute(sql, data)
                    rows = curs.fetchall()
                    showJointable(rows)
                    break
        elif select == 's':
            data = input('검색할 연봉: ')
            for r in rows:
                if r['salary'] == int(data):
                    sql = 'select * from emp natural join dept where salary = %s'
                    curs.execute(sql, data)
                    rows = curs.fetchall()
                    showJointable(rows)
                    break
        elif select == 'dn':
            data = input('검색할 부서번호: ')
            for r in rows:
                if r['deptno'] == int(data):
                    sql = 'select * from emp natural join dept where deptno = %s'
                    curs.execute(sql, data)
                    rows = curs.fetchall()
                    showJointable(rows)
                    break
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
    finally:
        conn.close()