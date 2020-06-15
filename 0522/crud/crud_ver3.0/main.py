# python과 mysql을 이용한 crud 연습문제
# 테이블: emp, dept
# emp(empno, ename, salary, deptno)
# dept(deptno, dname, location)
# 클래스: Emp, Dept
# 모듈: emp.py, dept.py, empio.py, main.py
# 프로그램이 시작되면 아래와 같은 메뉴가 표시된다.
# 리스트(s), 추가(a), 변경(u), 검색(f), 삭제(d), 종료(x)

from empio import *

def showMenu():
    menu = input('리스트(s), 추가(a), 변경(u), 검색(f), 삭제(d), 종료(x): ')
    return menu

while True:
    menu = showMenu()
    if menu == 'a':
        insertData(inputstring())

    elif menu == 's':
        showJointable(jointable2tuple())

    elif menu == 'u':
        updateData(jointable2tuple())

    elif menu =='f':
        select = input('사원번호(en), 사원명(n), 연봉(s), 부서번호(dn): ')
        if select == 'en':
            searchEnum(jointable2tuple())
        elif select == 'n':
            searchEname(jointable2tuple())
        elif select == 's':
            searchSalary(jointable2tuple())
        elif select == 'dn':
            searchDeptno(jointable2tuple())
        else:
            print('검색할 내용 오류')
    elif menu == 'd':
        deleteData(jointable2tuple())

    elif menu =='x':
        break

    else:
        print('프로그램 종료..')

