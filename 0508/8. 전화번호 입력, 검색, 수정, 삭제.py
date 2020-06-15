# 8. 전화번호 '입력' or '검색 or 수정 or 삭제'
# 친구 정보 입력(a), 검색(s) :
# if menu == 'a' :
# 이름, 전화번호 입력 받아서 리스트에 추가
# elif menu == 's' :
# 친구 번호 입력 요청 후, 해당 번호의 친구 정보 출력
# else :
# 입력 실패

nameList = ['김정연', '송하승', '방성환', '정성욱', '손주현']
phoneList = ['010-8960-9185', '010-3194-4875', '010-5097-7678', '010-4361-8876', '010-4123-4608']
# 리스트 생성

indata = input(f'"친구 정보" 입력(a) or 검색(s) or 수정(m) or 삭제(d) : ')
# 입력(a) or 검색(s) or 수정(m) 입력

#--------------------------입력--------------------------#
if indata == ('입력' or 'a') :
    a_name = input('\n이름 : ')
    a_phone = input('번호 : ')
    # 신규 이름, 번호 입력
    nameList.append(a_name)
    phoneList.append(a_phone)
    # List에 신규 이름, 번호 추가
    a_msg = f'\n★ 친구 입력 결과 ★\n이름 : {a_name}\n번호 : {a_phone}'
    print(a_msg)
    print(f'\n친구 목록 :\n{nameList}\n번호 목록 :\n{phoneList}')


#--------------------------검색--------------------------#
elif indata == ('검색' or 's') :
    choice = input('\n친구 번호를 검색하려면 "1" 이름을 검색하려면 "2"를 입력해주세요 :')
    # 번호 or 이름 검색 선택
    if choice == '1' :
        num = input('\n친구 번호를 입력해주세요 : ')
        # 친구 번호 입력
        s_name = nameList[int(num)-1]
        s_phone = phoneList[int(num)-1]
        # List에서 index(친구 번호-1) 위치의 이름, 번호 찾고 변수에 저장
    elif choice == '2' :
        s_name = input('\n검색할 이름을 입력해주세요 : ')
        s_index = nameList.index(s_name)
        s_phone = phoneList[s_index]
    s_msg = f'\n★ 친구 조회 결과 ★\n이름 : {s_name}\n번호 : {s_phone}'
    print(s_msg)


#--------------------------수정--------------------------#
elif indata == ('수정' or 'm') :
    num = input('\n수정할 친구 번호를 입력해주세요 : ')
    res = f'\n★ 기존 정보 ★\n이름 : {nameList[int(num)-1]}\n번호 : {phoneList[int(num)-1]}'
    print(res)
    # 수정할 친구 정보 출력
    m_name = input('\n이름 : ')
    m_phone = input('번호 : ')
    # 수정 이름, 번호 입력
    nameList[int(num)-1] = m_name
    phoneList[int(num)-1] = m_phone
    # List내 element 수정
    m_msg = f'\n ★ {num}번 친구 수정 결과 ★\n이름 : {m_name}\n번호 : {m_phone}'
    #m_msg = f'\n ★ {num}번 친구 수정 결과 ★\n이름 : {nameList[int(num)-1]}\n번호 : {phoneList[int(num)-1]}'
    print(m_msg)


#--------------------------삭제--------------------------#    
elif indata == ('삭제' or 'd') :
    num = input('\n삭제할 친구 번호를 입력해주세요 : ')
    res = f'\n★ 삭제할 정보 ★\n이름 : {nameList[int(num)-1]}\n번호 : {phoneList[int(num)-1]}'
    print(res)
    delete = input(f'\n정말 {nameList[int(num)-1]}의 정보를 삭제 하시겠습니까? (Yes) : ')
    # 삭제 경고문
    if delete == 'Yes' :
        del nameList[int(num)-1]
        del phoneList[int(num)-1]
        print('\n삭제가 완료 되었습니다.')
    else :
        print('\n메뉴 입력 오류 !')     
else :
    print('처리에 실패했습니다.\n입력(a) or 검색(s) or 수정(m) or 삭제(d)을 입력해주세요.')
