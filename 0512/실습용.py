# 6. 회원정보 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)

Dic = {}

while True:
    func = input(f'"회원 정보" 확인(s) or 입력(a) or 검색(f) or 수정(u) or 삭제(d) or 종료(x) : ')

    # 확인 기능
    if func == 's':
        print('\t*****정보 목록*****')
        for name, phone in Dic.items():  # Dic.items(): (key, value) Tuple로 출력
            print('\t', name, ':', phone)

    # 입력 기능
    elif func == 'a':
        name, phone = input('\t이름, 번호 : ').split()
        Dic[name] = phone

    # 검색 기능
    elif func == 'f':
        name = input('\t검색할 이름 : ')
        print('\t*****검색 결과*****')
        phone = Dic.get(name, '검색 실패') # 해당하는 value가 없으면 메세지 출력
        print('\t', name, ':', phone)

    # 수정 기능
    elif func == 'u':
        name = input('\t수정할 이름 : ')
        if name not in Dic.keys():  # name이 keys에 없으면 메세지 출력
            print(f'\t{name}은(는) 없는 이름입니다')
            continue  # loop 처음부터 다시
        else:
            phone = input('\t새 번호 : ')
            Dic[name] = phone
            print(f'\t{name}의 번호가 변경되었습니다')

    # 삭제 기능
    elif func == 'd':
        name = input('\t삭제할 이름 : ')
        if name not in Dic.keys(): # namedl keys에 없으면 메세지 출력
            print(f'\t{name}은(는) 없는 이름입니다')

        else:
            msg = input('\t정말 삭제하시겠습니까?(Yes/No) : ')
            if msg == 'Yes':
                del Dic[name]
                print(f'\t{name}의 번호가 삭제되었습니다')

    # 종료 기능
    elif func == 'x':
        print('\t프로그램을 종료합니다')
        break # loop 종료
    else :
        print('\t입력 오류')




