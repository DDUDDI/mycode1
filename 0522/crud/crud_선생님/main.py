from empio import *

def input_emp():
    data = input('사원정보 -> 사원번호 사원명 급여 부서번호: ')
    info = data.split()
    emp = Emp(int(info[0]), info[1], int(info[2]), int(info[3]))
    return emp

def input_dept():
    data = input('부서정보 -> 부서번호 부서명 위치: ')
    info = data.split()
    dept = Dept(int(info[0]), info[1], info[2])
    return dept

def new_sal():
    data = input('새 급여액 -> 사원번호 새 급여액: ')
    info = data.split()
    emp = Emp(int(info[0]), None, int(info[1]), 0) # 문자는 None, 숫자는 0 for 가독성
    return emp

def input_empno():
    data = input('사원정보 삭제 -> 사원번호: ')
    empno = int(data)
    return empno

def print_list(emplist):
    for e in emplist:
        print(e)

def showMenu():
    menu = input('리스트(s), 추가(a), 변경(u), 검색(f), 삭제(d), 종료(x): ')
    return menu

while True:
    menu = showMenu()
    if menu == 's':
        print_list(get_list())
    elif menu == 'a':
        sm = input('사원정보(e), 부서정보(d): ')
        if sm == 'e':
            insert_emp(input_emp())
        elif sm == 'd':
            insert_dept(input_dept())
    elif menu == 'u':
        update_emp(new_sal())
    elif menu == 'd':
        delete_emp(input_empno())

    elif menu == 'x':
        break

print('프로그램 종료...')
