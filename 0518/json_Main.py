from jsonIO import *

def print_mem(dic):
    print(dic['num'], ' ', dic['name'], ' ', dic['phone'])
def showList(memList):
    for m in memList:
        print(m)

while True:
    menu = input('회원정보 추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x): ')
    if menu == 'a':
        info = input('번호 이름 전화: ')
        add(line2dic(info))
    elif menu == 's':
        showList(list_from_json())
    elif menu == 'f':
        info = input('검색할 이름: ')
        findname(info)
    elif menu == 'u':
        info = input('수정할 이름 번호: ').split()
        update(info[0], info[1])
    elif menu == 'd':
        info = input('삭제할 이름: ')
        delete(info)
    elif menu == 'x':
        break
print('프로그램 종료')

