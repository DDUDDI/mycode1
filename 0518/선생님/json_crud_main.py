from json_io import *

def print_mem(dic):
    print(dic['num'], ' ', dic['name'], ' ', dic['phone'])

def showList(memList):
    for d in memList:
        print_mem(d)

while True:
    menu = input('회원정보 추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ')
    if menu == 'a':
        add(line2dic(input('번호 이름 전화: ')))
    elif menu == 'f':
        print_mem(find_name(input('이름: ')))
    elif menu == 's':
        showList(dic_from_json())
    elif menu == 'u':
        info = input('수정할 이름 새 전화: ').split()
        update(info[0], info[1])
    elif menu == 'd':
        info = input('삭제할 이름: ')
        delete(info)
    elif menu == 'x':
        break
print('프로그램 종료')
