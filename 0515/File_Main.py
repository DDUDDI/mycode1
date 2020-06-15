from memberIO import * # 모든 method import

def showMenu():
    m = input('회원정보 추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x) : ')
    return m

while True:
    menu = showMenu()
    if menu == 'a':
        addMem(inputMem()) # inputMem으로 입력 -> addMem으로 추가
    elif menu == 's':
        printMemList(getList()) # getList로 리스트에 저장 -> printMemList로 출력
    elif menu == 'f':
        searchMem(inputName())
    elif menu == 'u':
        update()
    elif menu == 'd':
        delete()
    elif menu == 'x':
        break
    else:
        print('메뉴 입력 오류')
print('프로그램 종료')